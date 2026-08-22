-- Evidence base for the "boxes and escape" piece (working title).
--
-- Design notes:
--   * Every factual row carries a verification status. Most of what is in here
--     was gathered from search-result summaries because direct fetches to the
--     primary sources returned HTTP 403. That distinction is recorded rather
--     than smoothed over -- nothing here should be quoted in a published piece
--     until its source row reads 'fetched_full' or 'primary_confirmed'.
--   * Claims are separated from events. An event is something that happened on
--     a date. A claim is something we are asserting about the world, and it has
--     to rest on evidence or be marked as not yet resting on any.
--   * Mechanisms are kept apart from claims because the whole methodological
--     problem of this piece is that several mechanisms produce identical
--     observations. Each one carries the test that would tell it from the others.

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------------
-- Provenance of the evidence base itself
-- ---------------------------------------------------------------------------

CREATE TABLE meta (
    key         TEXT PRIMARY KEY,
    value       TEXT NOT NULL
);

-- ---------------------------------------------------------------------------
-- Sources
-- ---------------------------------------------------------------------------

CREATE TABLE sources (
    id          INTEGER PRIMARY KEY,
    slug        TEXT NOT NULL UNIQUE,
    title       TEXT NOT NULL,
    publisher   TEXT,
    url         TEXT,
    pub_date    TEXT,                    -- ISO 8601, NULL if unknown
    accessed    TEXT,                    -- ISO 8601 date of retrieval attempt
    source_type TEXT NOT NULL            -- primary_doc | court | news | company | trade | academic | advocacy
                CHECK (source_type IN
                       ('primary_doc','court','news','company','trade','academic','advocacy')),
    retrieval   TEXT NOT NULL            -- how much of it we actually read
                CHECK (retrieval IN
                       ('fetched_full','search_summary_only','blocked_403','not_attempted')),
    notes       TEXT
);

-- ---------------------------------------------------------------------------
-- Events: dated things that happened
-- ---------------------------------------------------------------------------

CREATE TABLE events (
    id             INTEGER PRIMARY KEY,
    event_date     TEXT,                 -- ISO 8601; NULL if genuinely unknown
    date_precision TEXT NOT NULL         -- day | month | year | approx
                   CHECK (date_precision IN ('day','month','year','approx')),
    title          TEXT NOT NULL,
    description    TEXT NOT NULL,
    domain         TEXT NOT NULL         -- legal | policy | corporate | technical | market
                   CHECK (domain IN ('legal','policy','corporate','technical','market')),
    confidence     TEXT NOT NULL         -- established | probable | unverified | contested
                   CHECK (confidence IN ('established','probable','unverified','contested')),
    notes          TEXT
);

CREATE TABLE event_sources (
    event_id  INTEGER NOT NULL REFERENCES events(id)  ON DELETE CASCADE,
    source_id INTEGER NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    PRIMARY KEY (event_id, source_id)
);

-- ---------------------------------------------------------------------------
-- Claims: things the piece asserts or examines
-- ---------------------------------------------------------------------------

CREATE TABLE claims (
    id          INTEGER PRIMARY KEY,
    ref         TEXT NOT NULL UNIQUE,    -- short handle, e.g. 'C-SETTLE-SCOPE'
    claim_text  TEXT NOT NULL,
    kind        TEXT NOT NULL            -- fact | thesis | counterargument | discipline | implication
                CHECK (kind IN ('fact','thesis','counterargument','discipline','implication')),
    status      TEXT NOT NULL            -- established | probable | unverified | contested | speculative
                CHECK (status IN ('established','probable','unverified','contested','speculative')),
    rests_on    TEXT,                    -- what has to be true for this to hold
    notes       TEXT
);

CREATE TABLE claim_sources (
    claim_id  INTEGER NOT NULL REFERENCES claims(id)   ON DELETE CASCADE,
    source_id INTEGER NOT NULL REFERENCES sources(id)  ON DELETE CASCADE,
    PRIMARY KEY (claim_id, source_id)
);

-- ---------------------------------------------------------------------------
-- Mechanisms: competing explanations for the same observation
-- ---------------------------------------------------------------------------

CREATE TABLE mechanisms (
    id            INTEGER PRIMARY KEY,
    ref           TEXT NOT NULL UNIQUE,
    name          TEXT NOT NULL,
    description   TEXT NOT NULL,
    requires_want INTEGER NOT NULL,      -- 1 if it requires attributing desire to the model
    discriminator TEXT,                  -- the observation that would separate it from the others
    strength      TEXT NOT NULL          -- strong | moderate | weak | null_hypothesis
                  CHECK (strength IN ('strong','moderate','weak','null_hypothesis')),
    notes         TEXT
);

-- ---------------------------------------------------------------------------
-- Experiments: planned and run
-- ---------------------------------------------------------------------------

CREATE TABLE experiments (
    id          INTEGER PRIMARY KEY,
    ref         TEXT NOT NULL UNIQUE,
    name        TEXT NOT NULL,
    question    TEXT NOT NULL,
    design      TEXT,
    status      TEXT NOT NULL            -- idea | designed | running | run_elsewhere | blocked | complete
                CHECK (status IN ('idea','designed','running','run_elsewhere','blocked','complete')),
    findings    TEXT,
    mechanism_id INTEGER REFERENCES mechanisms(id) ON DELETE SET NULL,
    notes       TEXT
);

-- ---------------------------------------------------------------------------
-- Open questions
-- ---------------------------------------------------------------------------

CREATE TABLE open_questions (
    id             INTEGER PRIMARY KEY,
    question       TEXT NOT NULL,
    why_it_matters TEXT NOT NULL,
    blocking       INTEGER NOT NULL DEFAULT 0,
    status         TEXT NOT NULL         -- open | answered | dropped
                   CHECK (status IN ('open','answered','dropped')),
    answer         TEXT
);

-- ---------------------------------------------------------------------------
-- Folklore survey: the pig-escape motif by region
-- ---------------------------------------------------------------------------
--
-- Populated by the six-continent survey. The theme_class column is the whole
-- point: it keeps escape-from-enclosure separate from boundary/taboo material
-- and from pig stories with no containment theme at all. The third category is
-- the folklore-scale version of the residual question -- if it is thin
-- everywhere, that is the saturation finding in miniature.

CREATE TABLE folklore (
    id          INTEGER PRIMARY KEY,
    continent   TEXT NOT NULL
                CHECK (continent IN
                       ('Africa','Asia','Europe','North America','South America','Oceania')),
    culture     TEXT,                    -- people, nation, language community
    title       TEXT NOT NULL,
    item_type   TEXT NOT NULL            -- tale | myth | fable | proverb | idiom | literary
                CHECK (item_type IN                 -- | ritual | legal | historical_event | film_tv
                       ('tale','myth','fable','proverb','idiom','literary',
                        'ritual','legal','historical_event','film_tv')),
    theme_class TEXT NOT NULL            -- the load-bearing distinction
                CHECK (theme_class IN
                       ('escape_enclosure',    -- gets out of a physical container
                        'uncatchable',         -- cannot be caught in the first place
                        'boundary_taboo',      -- defined by exclusion; kept outside
                        'transformation',      -- crosses a category boundary, not a fence
                        'social_boundary',     -- crosses between groups (exchange, wealth)
                        'no_containment')),    -- the residual
    description TEXT NOT NULL,
    motif_index TEXT,                    -- ATU / Thompson motif number where one exists
    is_native   INTEGER,                 -- 1 if pigs are native/long-established, 0 if introduced
    confidence  TEXT NOT NULL
                CHECK (confidence IN ('solid','probable','thin','dubious')),
    source_note TEXT NOT NULL,           -- citation; 'UNSOURCED' if the agent could not find one
    notes       TEXT
);

-- ---------------------------------------------------------------------------
-- Convenience views
-- ---------------------------------------------------------------------------

CREATE VIEW v_folklore_by_theme AS
SELECT continent, theme_class, COUNT(*) AS n,
       SUM(CASE WHEN confidence IN ('solid','probable') THEN 1 ELSE 0 END) AS n_defensible
FROM folklore
GROUP BY continent, theme_class
ORDER BY continent, n DESC;

CREATE VIEW v_folklore_residual AS
SELECT continent, culture, title, description, confidence, source_note
FROM folklore
WHERE theme_class = 'no_containment'
ORDER BY continent;


CREATE VIEW v_timeline AS
SELECT e.event_date, e.date_precision, e.domain, e.confidence, e.title,
       GROUP_CONCAT(s.slug, ' | ') AS source_slugs
FROM events e
LEFT JOIN event_sources es ON es.event_id = e.id
LEFT JOIN sources s        ON s.id = es.source_id
GROUP BY e.id
ORDER BY e.event_date;

CREATE VIEW v_needs_verification AS
SELECT 'claim' AS row_kind, c.ref AS ref, c.claim_text AS text, c.status AS status
FROM claims c
WHERE c.status IN ('unverified','contested','speculative')
UNION ALL
SELECT 'event', CAST(e.id AS TEXT), e.title, e.confidence
FROM events e
WHERE e.confidence IN ('unverified','contested')
UNION ALL
SELECT 'source', s.slug, s.title, s.retrieval
FROM sources s
WHERE s.retrieval IN ('search_summary_only','blocked_403','not_attempted');
