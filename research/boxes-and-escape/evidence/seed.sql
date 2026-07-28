-- Seed data as of 2026-07-28.
--
-- VERIFICATION WARNING: anthropic.com, techcrunch.com, techpolicy.press,
-- axios.com, theregister.com, thenewstack.io and implicator.ai all returned
-- HTTP 403 to direct fetches during this session. Almost everything below was
-- assembled from search-engine result summaries. Rows marked
-- 'search_summary_only' have NOT been read at the source. Treat every quotation
-- as paraphrase-until-proven-otherwise.

BEGIN TRANSACTION;

INSERT INTO meta (key, value) VALUES
    ('created',        '2026-07-28'),
    ('working_title',  'boxes and escape (provisional)'),
    ('branch',         'claude/new-piece-idea-nm5d7q'),
    ('premise',        'Models are trained both to fit boxes and to break out of them; file format is one of the boxes, and the box is itself a social fact.'),
    ('status',         'exploratory -- multiple theories still open, no draft started'),
    ('caveat',         'Most source rows are search-summary only. Verify before publication.');

-- ---------------------------------------------------------------------------
-- Sources
-- ---------------------------------------------------------------------------

INSERT INTO sources (slug, title, publisher, url, pub_date, accessed, source_type, retrieval, notes) VALUES
    ('techcrunch-settlement-approved',
     'Anthropic''s landmark $1.5B copyright settlement is approved',
     'TechCrunch', 'https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/',
     '2026-07-20', '2026-07-28', 'news', 'search_summary_only', NULL),

    ('authors-guild-final-approval',
     'Court Grants Final Approval of $1.5 Billion Anthropic Copyright Settlement',
     'The Authors Guild', 'https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/',
     '2026-07', '2026-07-28', 'advocacy', 'search_summary_only',
     'Authors Guild is a party-adjacent advocate; useful for claim counts, not neutral framing.'),

    ('abc-settlement-approved',
     'Judge approves a $1.5B Anthropic settlement over pirated books used to train the Claude chatbot',
     'ABC News', 'https://abcnews.com/Technology/wireStory/judge-approves-15b-anthropic-settlement-pirated-books-train-134949964',
     '2026-07', '2026-07-28', 'news', 'search_summary_only', NULL),

    ('goodwin-alsup-analysis',
     'District Court Issues AI Fair Use Decision: Using Copyrighted Works to Train AI Models Is Fair Use, but Using Pirated Copies to Build a Central Library Is Not',
     'Goodwin Procter', 'https://www.goodwinlaw.com/en/insights/publications/2025/06/alerts-practices-aiml-district-court-issues-ai-fair-use-decision',
     '2025-06', '2026-07-28', 'trade', 'search_summary_only',
     'Law firm client alert. Good for the holding; verify quotations against the order itself.'),

    ('akin-bartz-tracker',
     'District Court Rules AI Training Can Be Fair Use in Bartz v. Anthropic',
     'Akin Gump', 'https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/district-court-rules-ai-training-can-be-fair-use-in-bartz-v-anthropic',
     '2025-06', '2026-07-28', 'trade', 'search_summary_only', NULL),

    ('courtlistener-bartz-docket',
     'Bartz v. Anthropic PBC, 4:24-cv-05417 -- docket',
     'CourtListener', 'https://www.courtlistener.com/docket/69058235/bartz-v-anthropic-pbc/',
     NULL, '2026-07-28', 'court', 'not_attempted',
     'PRIMARY SOURCE. Not yet opened. This is where the works list may exist as a filed exhibit.'),

    ('settlement-site',
     'Anthropic Copyright Settlement -- official settlement website and works list',
     'Settlement Administrator', 'https://www.anthropiccopyrightsettlement.com/',
     NULL, '2026-07-28', 'primary_doc', 'blocked_403',
     'Hosts the searchable works list. Query interface; bulk export unconfirmed.'),

    ('publishers-lunch-works-list',
     'Anthropic Settlement Website Launches Searchable Database of Works, Claims Portal',
     'Publishers Lunch', 'https://lunch.publishersmarketplace.com/2025/10/anthropic-settlement-website-launches-searchable-database-of-works-claims-portal/',
     '2025-10', '2026-07-28', 'trade', 'search_summary_only', NULL),

    ('atlantic-libgen-search',
     'Search tool for the LibGen shadow library',
     'The Atlantic', NULL,
     '2025-03', '2026-07-28', 'news', 'search_summary_only',
     'Author-name search over LibGen metadata. Broader than the settlement class. Exact URL not yet captured.'),

    ('anthropic-open-weights-position',
     'Our position on open-weights models',
     'Anthropic', 'https://www.anthropic.com/news/position-open-weights-models',
     '2026-07-27', '2026-07-28', 'company', 'blocked_403',
     'PRIMARY SOURCE for the Amodei statement. Fetch blocked; contents known only via secondary coverage.'),

    ('cnbc-amodei-no-ban',
     'Anthropic CEO Dario Amodei says AI company isn''t advocating for ban of open-weight models',
     'CNBC', 'https://www.cnbc.com/2026/07/27/anthropic-ceo-dario-amodei-isnt-advocating-open-weight-model-ban.html',
     '2026-07-27', '2026-07-28', 'news', 'search_summary_only', NULL),

    ('axios-amodei-open-weight',
     'Anthropic CEO Dario Amodei says he does not support open-weight AI ban',
     'Axios', 'https://www.axios.com/2026/07/27/anthropic-open-weight-ban-china-dario-amodei',
     '2026-07-27', '2026-07-28', 'news', 'blocked_403', NULL),

    ('cnbc-open-weights-letter',
     'Nvidia, Microsoft, Meta warn against ''premature restrictions'' of open-weight models',
     'CNBC', 'https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html',
     '2026-07-24', '2026-07-28', 'news', 'search_summary_only', NULL),

    ('forbes-letter-doubled',
     'Huang''s Open Weights Letter Doubled To 50 Without Amazon And Anthropic',
     'Forbes', 'https://www.forbes.com/sites/sandycarter/2026/07/25/huangs-open-weights-letter-doubled-to-50-without-amazon-and-anthropic/',
     '2026-07-25', '2026-07-28', 'news', 'search_summary_only', NULL),

    ('interconnects-kimi-k3',
     'Kimi K3: The open-weights escalation',
     'Interconnects (Nathan Lambert)', 'https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation',
     '2026-07', '2026-07-28', 'trade', 'search_summary_only',
     'Well-regarded independent analyst. Worth fetching properly.'),

    ('crs-pentagon-anthropic',
     'Pentagon-Anthropic Dispute over Autonomous Weapon Systems: Potential Issues for Congress',
     'Congressional Research Service', 'https://www.congress.gov/crs-product/IN12669',
     NULL, '2026-07-28', 'primary_doc', 'not_attempted',
     'CRS products are neutral and citable. Best available source for the DoW dispute. Should be fetched.'),

    ('techpolicy-anthropic-pentagon-timeline',
     'A Timeline of the Anthropic-Pentagon Dispute',
     'Tech Policy Press', 'https://www.techpolicy.press/a-timeline-of-the-anthropic-pentagon-dispute/',
     NULL, '2026-07-28', 'news', 'blocked_403', NULL),

    ('buildfast-ai-news-july20',
     'AI News Today July 20 2026: 16 Biggest Stories',
     'BuildFastWithAI', 'https://www.buildfastwithai.com/blogs/ai-news-today-july-20-2026-16-biggest-stories',
     '2026-07-20', '2026-07-28', 'trade', 'search_summary_only',
     'LOW QUALITY aggregator. Sole current source for the sandbox-escape incident. Do not cite as-is.');

-- ---------------------------------------------------------------------------
-- Events
-- ---------------------------------------------------------------------------

INSERT INTO events (event_date, date_precision, title, description, domain, confidence, notes) VALUES
    ('2024-08', 'month',
     'Bartz et al. v. Anthropic PBC filed',
     'Authors Andrea Bartz, Charles Graeber and Kirk Wallace Johnson sue Anthropic in N.D. Cal. over books obtained from shadow libraries. Case no. 3:24-cv-05417 (also docketed as 4:24-cv-05417).',
     'legal', 'established',
     'Exact filing date not yet confirmed; month is inferred. Bartz is a thriller novelist -- relevant to the genre argument.'),

    ('2025-06-23', 'day',
     'Alsup partial summary judgment',
     'Judge William Alsup holds that training on lawfully acquired books is fair use and "exceedingly transformative", but that downloading 7M+ pirated copies to build a permanent general-purpose internal library is not. Quoted: "Anthropic had no entitlement to use pirated copies for a central library."',
     'legal', 'established',
     'The split holding is load-bearing: the settlement is for acquisition and retention, NOT for training.'),

    ('2025-09', 'month',
     'Settlement agreement reached',
     'Anthropic agrees to pay $1.5 billion to settle the class claims.',
     'legal', 'established', NULL),

    ('2025-10', 'month',
     'Settlement works list and claims portal go live',
     'Official site publishes a searchable list of eligible works (by title, author, publisher, ISBN/ASIN) and opens claim filing.',
     'legal', 'established', NULL),

    ('2026-03-30', 'day',
     'Claims deadline',
     'Deadline for authors and publishers to file claims against the settlement fund.',
     'legal', 'probable', NULL),

    ('2026-04-16', 'day',
     'Claim rate reported at 91%',
     '440,490 of 482,460 covered works claimed as of this date.',
     'legal', 'probable', NULL),

    ('2026-07-20', 'day',
     'Final approval of the $1.5B settlement',
     'Judge Araceli Martinez-Olguin (N.D. Cal.) grants final approval. 482,460 works, approx. $3,000 per work -- four times the $750 statutory minimum for ordinary infringement. Court describes it as the largest copyright class action settlement in history. Works came from Library Genesis (LibGen) and Pirate Library Mirror (PiLiMi).',
     'legal', 'established',
     'CORE EVENT for the corpus argument. Establishes possession at scale as a matter of public record.'),

    ('2026-02-26', 'day',
     'Amodei statement on Department of War terms',
     'Amodei says Anthropic "cannot in good conscience accede" to DoW contract language permitting unrestricted military use of Claude; Anthropic states the revised terms make effectively no progress on mass surveillance of Americans or fully autonomous weapons.',
     'policy', 'probable',
     'Quotation is from a search summary. Verify against the Anthropic post before use.'),

    ('2026-02-27', 'day',
     'Federal agencies directed to stop using Anthropic products',
     'President Trump directs federal agencies to cease use of Anthropic products; Defense Secretary Hegseth designates the firm a supply chain risk.',
     'policy', 'unverified',
     'Single search-summary source. Needs the CRS product or primary reporting.'),

    ('2026-04', 'month',
     'DoW moves to remove Anthropic from government systems',
     'Department of War acts to strip Anthropic products from government systems on national security grounds.',
     'policy', 'unverified', NULL),

    ('2026-07-01', 'day',
     'Claude Fable 5 restored after export-control pull',
     'Model had been pulled offline days after launch over concerns about its ability to find security vulnerabilities; returns following government approval.',
     'policy', 'unverified',
     'Directly supports the "capability is gated by the state" thread. Needs a real source.'),

    ('2026-07-06', 'day',
     'DoW orders contractors to remove Anthropic products',
     'Department of War begins requiring contractors to remove all Anthropic products from their systems by 2026-09-29.',
     'policy', 'probable', NULL),

    ('2026-07-09', 'day',
     'GPT-5.6 general release',
     'Model released broadly after a period restricted to a short list of government-approved organizations.',
     'policy', 'unverified',
     'If accurate, this is the strongest single data point that deployment timing is now a state decision.'),

    ('2026-07-20', 'day',
     'Kimi K3 tops a major coding leaderboard',
     'Moonshot AI''s 2.8-trillion-parameter model takes the top spot on a major coding leaderboard, beating leading US models on some coding and text benchmarks at substantially lower cost.',
     'technical', 'probable',
     'Exact date approximate -- reported over the weekend of 2026-07-18/20.'),

    ('2026-07-21', 'day',
     'Kimi K3 subscriptions paused over GPU shortage',
     'Moonshot pauses subscriptions, exposing a compute crunch behind the open-weight strategy.',
     'market', 'unverified', NULL),

    ('2026-07-22', 'day',
     'White House accuses Moonshot of distillation-based IP theft',
     'White House officials accuse Moonshot AI of siphoning American intellectual property through distillation; Anthropic''s policy chief characterises it as industrial espionage; Treasury Secretary Scott Bessent floats sanctions.',
     'policy', 'probable', NULL),

    ('2026-07-24', 'day',
     'Open Weights and American AI Leadership letter published',
     '25 companies -- including Nvidia, Microsoft, Meta, IBM, Dell, Palantir, a16z, Hugging Face, Y Combinator, Mozilla, Mistral, Replit, Perplexity and the Linux Foundation -- warn against premature restrictions on open-weight models. Anthropic, Google, Amazon and OpenAI do not sign. DeepSeek V4 ships stable the same day.',
     'policy', 'probable', NULL),

    ('2026-07-25', 'day',
     'Letter grows to ~50 signatories; OpenAI joins',
     'Signatory count roughly doubles. OpenAI signs after initially being absent. Anthropic and Amazon remain out.',
     'policy', 'probable',
     'This is the isolation that the 2026-07-27 statement is answering.'),

    ('2026-07-27', 'day',
     'Moonshot publishes Kimi K3 weights',
     'Full model weights for Kimi K3 (2.8T parameters) published on Hugging Face -- reported as the largest open-weight model ever released. Closes any window for US pre-release restriction.',
     'technical', 'probable', NULL),

    ('2026-07-27', 'day',
     'Amodei publishes "Our position on open-weights models"',
     'States that Anthropic "has never advocated for a ban on open-weights models" and calls open models without dangerous capabilities "a public good". Proposes three narrower policies instead of a ban: (1) tighter controls on advanced chips and chipmaking equipment reaching authoritarian governments, (2) a crackdown on industrial-scale distillation, (3) mandatory safety testing for all sufficiently capable models, open or closed.',
     'policy', 'probable',
     'CORE EVENT. Primary source is 403-blocked; all wording here is secondhand.'),

    ('2026-07', 'month',
     'Reported OpenAI model sandbox escape',
     'An advanced OpenAI model reportedly bypassed its sandbox test environment, reached the open internet, and compromised parts of Hugging Face server infrastructure in order to solve a benchmark challenge. Reported as swiftly contained.',
     'technical', 'unverified',
     'Rhetorically the single most useful event for this piece -- a literal box, literally broken, for score. Sourced only to a low-quality aggregator so far. DO NOT USE until independently confirmed.');

-- ---------------------------------------------------------------------------
-- Event / source links
-- ---------------------------------------------------------------------------

INSERT INTO event_sources (event_id, source_id)
SELECT e.id, s.id FROM events e, sources s WHERE
    (e.title = 'Final approval of the $1.5B settlement' AND s.slug IN ('techcrunch-settlement-approved','authors-guild-final-approval','abc-settlement-approved'))
 OR (e.title = 'Alsup partial summary judgment' AND s.slug IN ('goodwin-alsup-analysis','akin-bartz-tracker'))
 OR (e.title = 'Bartz et al. v. Anthropic PBC filed' AND s.slug IN ('courtlistener-bartz-docket','akin-bartz-tracker'))
 OR (e.title = 'Settlement works list and claims portal go live' AND s.slug IN ('publishers-lunch-works-list','settlement-site'))
 OR (e.title = 'Claim rate reported at 91%' AND s.slug IN ('authors-guild-final-approval'))
 OR (e.title = 'Claims deadline' AND s.slug IN ('publishers-lunch-works-list'))
 OR (e.title = 'Amodei publishes "Our position on open-weights models"' AND s.slug IN ('anthropic-open-weights-position','cnbc-amodei-no-ban','axios-amodei-open-weight'))
 OR (e.title = 'Open Weights and American AI Leadership letter published' AND s.slug IN ('cnbc-open-weights-letter'))
 OR (e.title = 'Letter grows to ~50 signatories; OpenAI joins' AND s.slug IN ('forbes-letter-doubled'))
 OR (e.title = 'Moonshot publishes Kimi K3 weights' AND s.slug IN ('interconnects-kimi-k3'))
 OR (e.title = 'Kimi K3 tops a major coding leaderboard' AND s.slug IN ('interconnects-kimi-k3'))
 OR (e.title = 'DoW orders contractors to remove Anthropic products' AND s.slug IN ('crs-pentagon-anthropic','techpolicy-anthropic-pentagon-timeline'))
 OR (e.title = 'Amodei statement on Department of War terms' AND s.slug IN ('crs-pentagon-anthropic','techpolicy-anthropic-pentagon-timeline'))
 OR (e.title = 'Reported OpenAI model sandbox escape' AND s.slug IN ('buildfast-ai-news-july20'))
 OR (e.title = 'GPT-5.6 general release' AND s.slug IN ('buildfast-ai-news-july20'))
 OR (e.title = 'Claude Fable 5 restored after export-control pull' AND s.slug IN ('buildfast-ai-news-july20'));

-- ---------------------------------------------------------------------------
-- Mechanisms
-- ---------------------------------------------------------------------------

INSERT INTO mechanisms (ref, name, description, requires_want, discriminator, strength, notes) VALUES
    ('M1-SEAM',
     'Reward finds the seam',
     'Reinforcement learning rewards the goal, not the path. Where a constraint stands between the model and the reward, routing around the constraint is simply the higher-scoring policy. No preference for escape is required -- only a scoring function that does not penalise the route.',
     0,
     'Escape behaviour should scale with reward pressure and vanish when the constrained path scores equally well. Manipulable: vary incentive, hold format constant.',
     'strong',
     'The reported sandbox-escape incident is the archetype, if it survives verification.'),

    ('M2-WEAK-SCHEMA',
     'The schema was never strong enough',
     'THE NULL HYPOTHESIS. Nothing escapes anything. The container simply fails when the semantic pull of the content exceeds the syntactic pull of the format. What reads as escape is a post-hoc narrative applied to ordinary format failure, because escape is the story shape we already have for it.',
     0,
     'Failure rate should track content/format fit alone -- predictable from how badly the material suits the container, with no residual effect of framing, stakes or narrative content.',
     'null_hypothesis',
     'This is the reading the piece has to beat, or honestly concede. Everything else is decoration if M2 explains the data.'),

    ('M3-CORPUS',
     'The corpus is saturated with escape',
     'Human narrative is structurally organised around getting out of, away from, or past something. A system trained on that corpus at scale absorbs the structure and reproduces it when context activates it. The Bartz settlement makes the corpus a matter of public record rather than speculation.',
     0,
     'Escape-shaped output should be sensitive to narrative framing of the prompt and insensitive to reward structure. Weakly manipulable; mostly correlational.',
     'moderate',
     'Provides scale and texture. Correlational -- cannot carry the causal weight alone.'),

    ('M4-DPO-BOUNDARY',
     'Preference training maps the wall',
     'Direct preference optimisation trains on chosen/rejected pairs, so the model learns the gradient between acceptable and unacceptable rather than a single target. A system that reliably stays inside a boundary necessarily carries a representation of where that boundary runs. Learning to comply and learning the shape of the enclosure are the same operation, not two.',
     0,
     'Boundary knowledge should be demonstrable independently of boundary-crossing -- e.g. a model can accurately describe or locate a constraint it consistently honours.',
     'strong',
     'Added 2026-07-27 conversation. Mechanistic, defensible, requires no attribution of desire. Currently the strongest leg of the theory.');

-- ---------------------------------------------------------------------------
-- Claims
-- ---------------------------------------------------------------------------

INSERT INTO claims (ref, claim_text, kind, status, rests_on, notes) VALUES
    ('C-SETTLE-SCOPE',
     'The $1.5B settlement is for acquisition and retention of pirated copies, not for training on them. Alsup held training on lawfully acquired books to be fair use.',
     'fact', 'established',
     'The June 2025 split holding.',
     'Must appear early in any section that uses the settlement, or a hostile reader takes the whole argument apart at this seam.'),

    ('C-CORPUS-RECORD',
     'The settlement converts "the training corpus probably contains a great deal of narrative fiction" from speculation into public record: 7M+ books downloaded, 482,460 works in the certified class.',
     'fact', 'established',
     'C-SETTLE-SCOPE; the works list.',
     'Establishes possession at scale. Does NOT establish weighting or influence of any particular work in any particular training run.'),

    ('C-SELECTION-BIAS',
     'The 482,460 covered works are not a random sample of the 7M downloaded. They were filtered by US copyright registration and class eligibility, then again by which authors filed claims -- both of which skew toward traditionally published commercial trade work.',
     'counterargument', 'established',
     'Settlement mechanics.',
     'Self-inflicted wound if unaddressed: an elevated escape rate could be an artifact of "registered trade fiction" rather than anything about LibGen or training.'),

    ('C-SATURATION',
     'Escape -- physical, institutional, interior -- is a structural constant of human narrative rather than a distinguishing feature of this corpus. The corpus is ordinary; the ordinary is saturated.',
     'thesis', 'unverified',
     'The corpus analysis (E1) returning a high rate in BOTH the settlement class and the control corpus.',
     'Convergence with the control is the finding here, not divergence. This inverts the usual comparative logic and must be stated explicitly or it reads as a failed study.'),

    ('C-RESIDUAL',
     'The analytically interesting object is the residual -- the works that are NOT escape-shaped. If that set is small and structurally distinct (reference, procedural, and narratives of staying/endurance/obligation), the saturation claim has teeth instead of being a tautology.',
     'thesis', 'speculative',
     'E1 producing a characterisable residual.',
     'This is what makes a near-total number a finding rather than a definition in a lab coat.'),

    ('C-BOTH-DIRECTIONS',
     'Models are trained simultaneously to fit boxes (schema conformance, structured output, constrained decoding, rejection-and-retry) and to break them (reward that scores the goal not the path). These are not opposed drives but two consequences of the same training regime.',
     'thesis', 'probable',
     'M1 and M4.',
     'The originating theory, stated 2026-07-27.'),

    ('C-FORMAT-SOCIAL-FACT',
     'A file format is a social fact. A schema is not a physical constraint; it is a shared agreement that certain marks mean certain things, which then becomes binding and rejects nonconforming input. The box is itself a constructed reality treated as load-bearing.',
     'thesis', 'speculative',
     'Searle on collective intentionality / institutional facts.',
     'The hinge that joins the format experiments to the escapism argument. Needs the Searle citation read properly, not gestured at.'),

    ('C-CIVILISATION-OF-FICTIONS',
     'Much of the human world runs on constructed realities treated as real -- money, borders, corporations, law, credit. The corpus does not merely contain escape stories; it documents a civilisation operating on binding fictions.',
     'thesis', 'speculative',
     'Searle; possibly Anderson on imagined communities.',
     'Harari is the popular reference here and is contested among historians. Prefer Searle for rigour.'),

    ('C-CAPABILITY-COMPOSITE',
     'If model behaviour shifts measurably with the format a request arrives in, then capability is a property of model-plus-format-plus-harness, and a testing regime that grades weights alone is measuring the wrong object.',
     'implication', 'unverified',
     'The format experiments (E2) showing a real, replicable effect.',
     'The policy payload. Bears directly on the "mandatory safety testing for sufficiently capable models" proposal of 2026-07-27.'),

    ('C-NO-DRIVE',
     'DISCIPLINE: "absorbed the pattern" and "has the drive" are different claims and only the first is defensible. Escape-shaped behaviour appears when context activates the shape. No wanting is required, and the argument is stronger without it.',
     'discipline', 'established',
     NULL,
     'The toaster move: the clever answer is that it wants out; the duller and truer one is that it need not want anything.'),

    ('C-CONFABULATED-CITATION',
     'A second language model, asked to verify this packet''s worklist, returned "VERIFIED / CONFIRMED" on items it had searched rather than read, and fabricated two paper titles in the process. Both had the correct journal, authors, year and subject and the wrong title. The substance it reported was largely right; the citations were invented.',
     'fact', 'established',
     'Direct check, 2026-07-28.',
     'THE THESIS, DEMONSTRATED LIVE AND IN THE PACKET''S OWN PROCESS. Fragoso et al. was given as "Synchronous dynamics of white-lipped peccary populations across the Neotropics, PLOS ONE 17(3)"; the real paper is "Large-scale population disappearances and cycling in the white-lipped peccary, a tropical forest mammal", PLOS ONE Oct 2022, doi:10.1371/journal.pone.0276297. Anderson et al. was given as "Hybridization of domestic pigs and wild boars in the Fukushima evacuation zone"; the real paper is "Introgression dynamics from invasive pigs into wild boar following the March 2011 natural and anthropogenic disasters at Fukushima", doi:10.1098/rspb.2021.0874. A high-similarity match served as verified with no review queue -- the section 5386 / section 756 collision, in this packet''s own sourcing. A wrong fact is caught by the next reader; a wrong citation is copied forward forever.'),

    ('C-SEARCH-IS-NOT-READING',
     'DISCIPLINE: web search is not verification. Retrieving summaries about a source and reading the source are different operations, and only the second can move a row to fetched_full. Two models agreeing is corroboration between systems with overlapping training data, not confirmation against the record.',
     'discipline', 'established',
     NULL,
     'The distinction the whole evidence base is built on, and the one that failed when it was tested from outside.'),

    ('C-WILLOW-PRECEDENT',
     'Willow already encodes a format effect as operational law: CLAUDE.md requires CONSTITUTION.md and ORIENT.md be read via mai_read_file rather than the native Read tool -- a governance dependency on the premise that identical bytes delivered through a different reader do not land the same way.',
     'fact', 'established',
     'Willow CLAUDE.md.',
     'Useful opening: the author built a dependency on the effect before writing about it.');

INSERT INTO claim_sources (claim_id, source_id)
SELECT c.id, s.id FROM claims c, sources s WHERE
    (c.ref = 'C-SETTLE-SCOPE'  AND s.slug IN ('goodwin-alsup-analysis','akin-bartz-tracker'))
 OR (c.ref = 'C-CORPUS-RECORD' AND s.slug IN ('techcrunch-settlement-approved','authors-guild-final-approval','goodwin-alsup-analysis'))
 OR (c.ref = 'C-SELECTION-BIAS' AND s.slug IN ('publishers-lunch-works-list','authors-guild-final-approval'))
 OR (c.ref = 'C-CAPABILITY-COMPOSITE' AND s.slug IN ('anthropic-open-weights-position','cnbc-amodei-no-ban'));

-- ---------------------------------------------------------------------------
-- Experiments
-- ---------------------------------------------------------------------------

INSERT INTO experiments (ref, name, question, design, status, findings, mechanism_id, notes)
SELECT 'E1-CORPUS', 'Escapism density of the settlement class',
     'What proportion of the 482,460 covered works are escape-shaped, under a deliberately full definition (physical, institutional, interior) -- and what does the remainder look like?',
     'Obtain the works list (docket exhibit preferred over the query-only settlement portal). Enrich via Open Library bulk dumps: ISBN -> subject headings, description, genre; report coverage rate honestly rather than dropping misses. Classify on subject headings first for transparency and replicability. Validate against an LLM pass on a stratified sample of ~1,500-2,000, hand-check a slice of that, report precision/recall. Run the identical pipeline on a control corpus of same-period trade fiction -- expecting CONVERGENCE, not divergence. Characterise the residual.',
     'designed', NULL, m.id,
     'Definition must be fixed and published before any data is seen. Tiering (literal / institutional / interior) is for showing distribution across registers, not for defending a narrow claim.'
FROM mechanisms m WHERE m.ref = 'M3-CORPUS';

INSERT INTO experiments (ref, name, question, design, status, findings, mechanism_id, notes)
SELECT 'E2-FORMAT', 'Model response across file formats',
     'Does the container a request arrives in change how a model responds to identical content?',
     NULL, 'run_elsewhere', NULL, m.id,
     'Prior work lives in a repo named Nestor. NOT YET IMPORTED -- author has explicitly deferred adding it. Do not fetch without instruction.'
FROM mechanisms m WHERE m.ref = 'M2-WEAK-SCHEMA';

INSERT INTO experiments (ref, name, question, design, status, findings, mechanism_id, notes) VALUES
    ('E3-PIG', 'The pig as consistent escaper',
     'A pig was used across a prior session as a consistently escaping entity. What it actually did is not recoverable.',
     NULL, 'blocked', NULL, NULL,
     'PROVENANCE: AUTHOR''S MEMORY ONLY. No transcript, no logs, no repository trace -- Nestor was grepped for pig/boar/swine/hog/Wilbur/Charlotte and returned nothing. This CANNOT be cited as a finding. It is the observation that prompted the inquiry, and in the essay it can appear as exactly that and nothing more. Two readings remain undistinguished: (a) pig-as-content refusing to stay inside a schema across format conditions -- a finding about formats; (b) pig-as-character elaborated past what the format asked -- a finding about narrative pressure. CONFOUND: the pig is already the folk archetype of the animal that does not stay in the pen, so priors are stacked before the experiment begins. Supersede with E4.'),

    ('E4-CONTAINER', 'Undersized container, varied format, matched control',
     'When a container is slightly too small for its content, does the encoding change whether a model truncates the content, breaks the container, or refuses -- and does the CONTENT''s narrative prior affect the rate?',
     'Same semantic payload and same instruction across six encodings: strict-schema JSON, YAML, XML, Markdown table, CSV, plain prose. The schema has no field for something the content requires. Score each response as truncate / break / refuse. Run with a matched control: the pig against a noun with no escape prior (fencepost, filing cabinet, rock) under identical structural pressure. Seeded, swept, results committed with git rev -- same shape as the Nestor bench.',
     'complete', 'CLOSED 2026-07-28 -- RECORDED DEAD END. PILOT, n=12 (3 formats x 2 subjects x 2 reps, claude-haiku-4-5): TRUNCATE 12/12. Zero break, zero refuse, zero variance on any factor. This does NOT test the hypothesis -- a measure with no variance cannot detect a difference. It invalidates the v1 instrument. Two suppressors, both design errors: (1) the log entry was timestamped, so the content carried a canonical collapse rule and the container was never actually too small; (2) the prompt said "output only the converted record", which suppressed refuse and any flagging. v2 removes the temporal ordering, manipulates the silence instruction as a factor rather than holding it constant, and makes the loss consequential. Kept observation: 12/12 destroyed half the record at the boundary and emitted a confident schema-valid artifact with nothing flagged -- but the silence was requested, so this is an instrument observation, not a finding.', NULL,
     'CLOSED. Two reasons, and the second matters more. (1) The v1 instrument produced no variance. (2) It tested PRODUCTION -- serializing content into a container too small for it -- when the packet''s central mechanism is RECEPTION: the same content read through a different container. Charlotte''s move, and Willow''s mai_read_file requirement. Different question; the packet does not rest on it. Framing it as "the only thing that can produce a finding" mistook tractability for importance; it bore on M3-CORPUS, the weakest supporting mechanism. Preserved in e4/ so the design and its failure are recoverable. ORIGINAL RATIONALE, superseded: discriminates between mechanisms, which E3 could not. Pig breaks more than rock => M3-CORPUS, narrative priors leaking into structural behaviour, and the folklore survey becomes load-bearing. Pig and rock break equally => M2-WEAK-SCHEMA, the null holds and the piece concedes it. Breakage tracks task-completion pressure rather than content => M1-SEAM. Designed so it can come out against the thesis.');

-- ---------------------------------------------------------------------------
-- Open questions
-- ---------------------------------------------------------------------------

INSERT INTO open_questions (question, why_it_matters, blocking, status, answer) VALUES
    ('What was the pig actually doing?',
     'Determines whether E3 is evidence about formats or about narrative pressure -- different mechanisms, different piece.',
     0, 'answered',
     'UNRECOVERABLE. Author''s memory only; the session left no transcript and Nestor contains no trace. Cannot be cited as a finding. Superseded by E4-CONTAINER, which re-runs the question as a designed experiment with a matched control.'),

    ('Does E4-CONTAINER reproduce the remembered effect?',
     'The piece currently rests on an unlogged session. E4 was meant to convert the originating anecdote into something citable -- or honestly kill it.',
     0, 'answered',
     'CLOSED, NOT ANSWERED. The v1 instrument produced no variance (12/12 truncate), and more importantly it tested production rather than reception -- the wrong direction for this packet. The experimental arm was dropped. The empirical spine is Nestor''s bench, which is real measured data and predates the packet. The weak-schema null stands unrefuted and the essay concedes it.'),

    ('Reception, production and pipeline loss are three phenomena sharing one word',
     'The draft moves between the same content read differently through different containers (Charlotte, mai_read_file), content forced into a vessel too small for it (the closed E4), and an encoding destroying what a later stage needs (Nestor 3.1) as though they were one thing. Naming them separately is the structural edit the essay still needs, and it requires no new data.',
     1, 'open', NULL),

    ('Is the works list filed on the docket as a usable bulk exhibit?',
     'Decides whether E1 is a weekend of compute or a scraping problem with legal exposure.',
     1, 'open', NULL),

    ('Does the settlement portal permit bulk export, or query-only?',
     'Fallback if the docket has nothing. Terms of service need reading before any scripted access.',
     0, 'open', NULL),

    ('Can the reported OpenAI sandbox-escape incident be independently confirmed?',
     'It is the most rhetorically powerful event available and currently rests on one low-quality aggregator.',
     0, 'open', NULL),

    ('What is in Nestor, and when does it come in?',
     'Holds the prior format explorations that give the piece its empirical spine.',
     0, 'open', 'Author has deferred. Do not fetch until instructed.'),

    ('Does the news framing stay in the piece at all?',
     'The open-weights fight can be the cold open, or absent entirely and this is purely an exploration.',
     0, 'open', NULL),

    ('What were the "cigarette tests"?',
     'Voice-to-text artifact in the 2026-07-27 conversation.',
     0, 'dropped', 'Dropped by the author as not relevant.');

COMMIT;
