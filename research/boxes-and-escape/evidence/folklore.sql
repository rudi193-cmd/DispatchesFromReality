-- Six-continent pig-escape survey, 2026-07-28.
--
-- Loaded after seed.sql. Full agent reports live in ../survey/.
--
-- BLANKET VERIFICATION WARNING: all six agents hit the same wall this session --
-- WebFetch returned 403 on every host (Wikipedia, JSTOR, sacred-texts, Ulukau,
-- Te Ara, archive.org, open-access PDFs alike) and each exhausted its 200-query
-- search budget. NOT ONE PRIMARY TEXT WAS READ IN THIS ENTIRE SURVEY. Every row
-- below is a real, locatable citation assembled from search-result summaries.
-- Nothing here is publication-ready until a human opens the source.
--
-- Confidence grades are the agents' own, carried through unchanged.

BEGIN TRANSACTION;

-- ---------------------------------------------------------------------------
-- AFRICA -- escape motif WEAK in oral narrative; exclusion material dominant
-- ---------------------------------------------------------------------------

INSERT INTO folklore (continent, culture, title, item_type, theme_class, description, motif_index, is_native, confidence, source_note, notes) VALUES
    ('Africa','Ancient Egypt','Herodotus II.47-48 on swineherds','historical_event','boundary_taboo',
     'Pork treated as impure; casual contact required immediate immersion; swineherds alone barred from every temple and forced into caste endogamy. The boundary is drawn around the pig, then drawn again permanently around the people who touch pigs.',
     NULL,1,'solid','Herodotus, Histories II.47-48.',
     'Volokhine complicates Herodotus -- pigs WERE farmed in the New Kingdom. Do not take at face value.'),

    ('Africa','Ancient Egypt','Set as the black boar','myth','boundary_taboo',
     'Set takes the form of a black boar; Ra declares the pig an abomination to Horus.',
     NULL,1,'probable','Egyptian mythological corpus; specific papyrus not confirmed.',NULL),

    ('Africa','Sub-Saharan (Zambia, Kenya)','Farmers who decline to confine pigs','historical_event','escape_enclosure',
     'Veterinary literature records farmers rejecting confinement outright, citing inability to confine; tethered pigs deliberately released each evening. An entire disease ecology (T. solium, a leading cause of acquired epilepsy in Africa) rests on the practice.',
     NULL,0,'solid','Thys et al., Veterinary Parasitology (2016); Parasites & Vectors (2022); Thomas et al., BMC Vet Res 9:46 (2013).',
     'The continent-scale literal answer, and it sits in the epidemiology rather than the folklore.'),

    ('Africa','Egypt (Coptic Zabbaleen)','The 2009 Cairo pig cull','historical_event','boundary_taboo',
     '300,000 pigs culled on a swine-flu pretext with zero positive tests, destroying the Coptic Zabbaleen waste-collectors'' livelihood. Cairo''s organic waste collection then collapsed and rubbish piled in the streets.',
     NULL,0,'solid','Contemporary news reporting, 2009.',
     'The pigs were the infrastructure. The containment that failed was Cairo''s, not the pigs''.'),

    ('Africa','Kenya','The 2013 "MPigs" protest','historical_event','uncatchable',
     'Boniface Mwangi''s activists released a dozen-plus piglets painted "MPigs", with pig blood, at the gates of Parliament. Police fired tear gas and were then reduced to chasing piglets across the parliamentary flowerbeds.',
     NULL,0,'solid','Contemporary news reporting, 2013.',
     'The survey''s best single image. Pigs turned loose INSIDE the most guarded enclosure in the country, and the state''s failure to catch them WAS the argument.'),

    ('Africa','Sotho-Tswana (BaLobedu)','Kolobe as clan totem','ritual','boundary_taboo',
     'Wild pig as seboko (totem) of BaLobedu clans including the Modjadji Rain Queens. Same prohibition on eating, opposite logic: protected as kin rather than excluded as filth.',
     NULL,1,'probable','Southern African ethnographic literature; specific source not confirmed.',NULL),

    ('Africa','Yoruba','Ijapa and Eledẹ ("why the pig roots the ground")','tale','no_containment',
     'The pig''s eternal rooting explained as a permanently unsuccessful pursuit of a debtor tortoise.',
     NULL,0,'thin','Yoruba tale corpus; agent could not read the ending.',
     'Closest African escape candidate. The agent explicitly labelled its escape reading as INFERENCE, not finding.'),

    ('Africa','Pan-African','ABSENCE: the pig is not a trickster','tale','no_containment',
     'No African ATU 2030 analogue, no ATU 124 analogue, no escaping-pig proverb located. The trickster role is held by hare, tortoise and spider.',
     NULL,NULL,'solid','Negative finding across the agent''s full search.',
     'STRUCTURAL FINDING. Corroborated independently by the Asia agent (mousedeer). The escape-trickster slot is constant; the animal cast in it varies with husbandry and taboo.');

-- ---------------------------------------------------------------------------
-- ASIA -- literal pen-escape near-absent as a tale type; four other clusters
-- ---------------------------------------------------------------------------

INSERT INTO folklore (continent, culture, title, item_type, theme_class, description, motif_index, is_native, confidence, source_note, notes) VALUES
    ('Asia','Goguryeo (Korea)','The runaway sacrificial pig (郊豕), Samguk Sagi','historical_event','escape_enclosure',
     'Three escapes across two centuries. Yuri yr 19 (1 BCE): the pig bolts, two officials catch it and cut its leg tendons; the king executes them for maiming a victim consecrated to Heaven and then falls ill from their vengeful ghosts. Yuri yr 21 (2 CE): it bolts again, the keeper Seolji chases it to Gungnae and reports the terrain -- the capital is moved there and stays roughly 400 years. Sansang, 208 CE: it bolts again, is caught by a woman of Jutong village, and the son she bears the king is named 郊彘 ("sacrificial piglet"), the future King Dongcheon.',
     NULL,1,'solid','Samguk Sagi, via National Institute of Korean History (db.history.go.kr, contents.history.go.kr) and Encykorea.',
     'BEST ITEM IN ASIA. A runaway pig relocates a state and produces a king. Note that the men who successfully PREVENTED an escape are the ones executed for it.'),

    ('Asia','Rabbinic Judaism','Bava Kamma 82b -- the pig hoisted over the wall','literary','boundary_taboo',
     'During the 65 BCE siege of Jerusalem the besiegers hoist a pig over the wall in place of a lamb; midway it digs its hooves into the wall and the land quakes. The sages then curse anyone who raises pigs and anyone who teaches his son Greek wisdom.',
     NULL,0,'solid','Babylonian Talmud, Bava Kamma 82b.',
     'The one recorded moment a pig gets IN rather than out. The curse pairs pig-rearing with foreign learning -- two kinds of boundary breach in one breath.'),

    ('Asia','China','Zhu Bajie (猪八戒), Journey to the West','literary','boundary_taboo',
     'His containment is vow-based rather than architectural: 八戒 means the eight precepts, a nickname given to fence his appetite. His identity is a list of prohibitions he continually breaches. His fall into a sow''s womb is a reincarnation clerical error. His one explicit act of confinement is performed on a human -- he locks his Gao Village wife away for six months.',
     NULL,1,'solid','Wu Cheng''en, Journey to the West (16th c.).',
     'He is named after his own guardrails.'),

    ('Asia','Japan','Fukushima exclusion-zone boar-pig hybrids','historical_event','escape_enclosure',
     'Farm pigs abandoned in the 2011 evacuation went feral and interbred with wild boar. ~16% of boars sampled in the zone are hybrids; pig ancestry ~8% and declining.',
     NULL,1,'solid','Anderson et al., Proceedings of the Royal Society B (2021).',
     'A mass escape recorded in genomes rather than in stories. The declining ancestry means the domestic is being reabsorbed.'),

    ('Asia','East Asia (idiom stock)','Boar as forward charge, never evasion','idiom','no_containment',
     'The boar''s uncontainability in the idiom stock is always headlong forward motion -- 猪突猛進 (chototsu moshin), 狼奔豕突, 封豕長蛇 -- and never evasion or hiding.',
     NULL,1,'solid','Standard Chinese/Japanese idiom dictionaries.',
     'A different GRAMMAR of uncontainability: unstoppable rather than uncatchable. Justifies keeping escape_enclosure and uncatchable as separate classes.'),

    ('Asia','Tibet','Samding Dorje Phagmo -- the monastery turned to pigs','myth','transformation',
     'Escape from attackers achieved by transforming the entire monastery into pigs. The pig-body is the hiding place rather than the thing that flees.',
     NULL,0,'probable','Tibetan Buddhist hagiographical tradition.',NULL),

    ('Asia','Malaysia','Selangor pig-farm relocation politics','legal','boundary_taboo',
     'The 2026 Bukit Tagar pig-farm relocation fight, with PAS counter-proposing the non-Muslim island of Pulau Ketam; and the 2012 pig-heads-at-mosques incidents.',
     NULL,0,'solid','Contemporary Malaysian news reporting.',
     'The contemporary form of the theme is not a pen. It is a map.'),

    ('Asia','Malay-Indonesian','ABSENCE: the escape-trickster is the mousedeer (kancil)','tale','no_containment',
     'In the largest Muslim-majority region on earth, the small-animal trickster whose entire repertoire is slipping traps is the mousedeer, not the pig. No Asian analogue of ATU 2030 or indigenous ATU 124 located.',
     NULL,NULL,'solid','Negative finding across the agent''s full search.',
     'STRUCTURAL FINDING, independently matching Africa. The genre is strongest exactly where the pig has been evicted from narrative.');

-- ---------------------------------------------------------------------------
-- EUROPE -- densest containment material; much of it legal rather than literary
-- ---------------------------------------------------------------------------

INSERT INTO folklore (continent, culture, title, item_type, theme_class, description, motif_index, is_native, confidence, source_note, notes) VALUES
    ('Europe','Welsh','Twrch Trwyth','myth','uncatchable',
     'The treasures are stripped from the boar one by one across an enormous chase, but the boar itself is never contained -- he escapes into the sea. Rhys read the chase as an extended dindsenchas of swine place-names.',
     NULL,1,'solid','Culhwch ac Olwen, in the Mabinogion.',NULL),

    ('Europe','Welsh','Henwen','myth','uncatchable',
     'Near-exact structural twin of Twrch Trwyth and badly under-used. Arthur sets out to destroy her and FAILS; she crosses the whole island farrowing monsters at named places and ends at the sea.',
     NULL,1,'solid','Welsh Triads; swineherd Coll ap Collfrewy.',
     'Wales has TWO uncatchable-swine epics. With Pryderi''s Otherworld pigs and the Mochdref toponyms it is a regional pattern, not a single text.'),

    ('Europe','Welsh','Pryderi''s Otherworld pigs','myth','escape_enclosure',
     'Otherworld pigs driven across Wales, leaving the Mochdref ("pig-town") toponyms behind them.',
     NULL,1,'probable','Mabinogi, Fourth Branch.',NULL),

    ('Europe','English','The Old Woman and Her Pig','tale','escape_enclosure',
     'The entire plot is a pig that will not cross a stile -- a structure purpose-built to pass people and stop livestock. Europe''s purest refusal-to-stay-put tale is organised around an interface with a type constraint in it.',
     'ATU 2030; Motif Z41',1,'solid','Jacobs, English Fairy Tales (1890), from Halliwell.',
     'A stile is a schema. Verify the Thompson motif number against the printed index.'),

    ('Europe','English','ATU 124 -- the three little pigs','tale','no_containment',
     'FLAGGED INVERSION: the pig is besieged, not escaping -- the story is about keeping something OUT. Fox/geese variants show the pig is not essential to the type.',
     'ATU 124',1,'solid','Aarne-Thompson-Uther index.',
     'Belongs in the residual. The most famous pig-and-enclosure story in English is about a wolf failing to get in.'),

    ('Europe','England','Urban swine management and the volume of regulation','legal','escape_enclosure',
     'Overturns the popular image: medieval English town pigs were NOT free roamers but subject to cradle-to-grave controls. Pinfolds; six swineherds amerced in 1425; an owner could not retrieve his own strayed pig except through the manor court. The burden runs unbroken to s.4 Animals Act 1971.',
     NULL,1,'solid','Dolly Jorgensen, "Running Amuck? Urban Swine Management in Late Medieval England", Agricultural History 87:4 (2013), 429-451.',
     'METHODOLOGICALLY THE MOST USEFUL ITEM IN THE SURVEY. The volume of rule-making is itself the evidence of chronic escape. You do not write that many rules about a thing that stays put.'),

    ('Europe','France','The Savigny sow, 1457','legal','escape_enclosure',
     'A sow hanged for killing a child; her six piglets acquitted as having been led astray by maternal example. The best-documented of the medieval pig trials.',
     NULL,1,'solid','Medieval French court records; Evans, The Criminal Prosecution and Capital Punishment of Animals (1906).',
     'The pig trials are containment-failure aftermath -- a penned pig does not reach a child in a cradle. Falaise 1386''s human-clothing and fresco details are the WEAKEST-evidenced elements in that literature.'),

    ('Europe','London','The tantony pig and the 1311 loophole','legal','escape_enclosure',
     'St Anthony''s Hospital belled pigs the London market judged unfit for slaughter, making them legally free of the street -- a licensed exception to containment, fed by citizens. In 1311 a hospital tenant, Roger de Wynchester, was forced to promise the City not to claim wandering pigs nor bell any swine but those given in charity.',
     NULL,1,'solid','London civic records, 1311.',
     'M1-SEAM in a medieval city: the single lawful exemption permitting an uncontained pig was immediately being used to launder other people''s escapees.'),

    ('Europe','Greek','The Erymanthian Boar and Eurystheus','myth','uncatchable',
     'Eurystheus demands the boar be brought back alive, and then hides in a buried jar when it arrives. The man who ordered the pig contained ends up the one in the container.',
     NULL,1,'solid','Greek mythological corpus (Apollodorus).',NULL),

    ('Europe','Britain','Wild boar restored by fence failure','historical_event','escape_enclosure',
     'No reintroduction programme: the Great Storm of October 1987 smashed farm fences in Kent and East Sussex; a 1990s escape near Ross-on-Wye seeded the Forest of Dean; ~60 were illegally dumped at Staunton in 2004; 1-2 escape incidents annually 1989/90-2008/9.',
     NULL,1,'solid','UK wildlife and DEFRA reporting.',
     'An extinct species restored to a country entirely by containment failure.');

-- ---------------------------------------------------------------------------
-- NORTH AMERICA -- no native suid; everything downstream of introduction+escape
-- ---------------------------------------------------------------------------

INSERT INTO folklore (continent, culture, title, item_type, theme_class, description, motif_index, is_native, confidence, source_note, notes) VALUES
    ('North America','Colonial English','Fence law inverted, and the hog reeve','legal','social_boundary',
     'Livestock described as "the principal agents responsible for dispossessing the Indians". The Chesapeake statute -- "Every man shall enclose his ground with sufficient fences uppon theire owne perill" -- inverted English practice by putting the burden of exclusion on the crop-grower, so colonial pigs were legally entitled to Indigenous fields. The hog reeve was among the earliest elected offices in colonial North America.',
     NULL,0,'solid','Virginia DeJohn Anderson, "King Philip''s Herds", WMQ 51:4 (1994), 601-624; Creatures of Empire (Oxford UP, 2004).',
     'The darkest and best-sourced thread in the survey. The first thing colonial democracy did was elect someone to deal with loose pigs.'),

    ('North America','US/British','The Pig War, 1859','historical_event','social_boundary',
     'Lyman Cutlar shot Charles Griffin''s HBC Berkshire boar in his unfenced potato patch on San Juan Island, 15 June 1859. Escalation was about whose law applied; joint military occupation ran to 1872. The pig was the only fatality.',
     NULL,0,'solid','BC Studies, "From Imbroglio to Pig War"; US National Park Service.',
     'A border dispute triggered by an animal crossing a line.'),

    ('North America','New York City','The Piggery War, 1859','historical_event','social_boundary',
     '87 armed men, per the New York Times of 27 July 1859. A street-foraging pig costs nothing to feed, so free range was a subsistence strategy for the landless and enclosure was gentrification. Women were the most militant defenders.',
     NULL,0,'solid','Catherine McNeur, Journal of Urban History 37:5 (2011), 639-660; Taming Manhattan (Harvard UP, 2014).',
     'Containment as a class weapon. The push to enclose was a transfer of who gets to survive in a city.'),

    ('North America','Caribbean Spanish','Cimarron / boucanier / jibaro','idiom','social_boundary',
     'Cimarron was applied first to domestic livestock gone wild in the hills of Hispaniola and only afterwards to escaped Indigenous and African people, giving English "maroon". Boucanier (buccaneer) meant a man who lived by hunting the feral cattle and hogs left when Spanish Hispaniola depopulated. Jibaro -- Pichardo (1836): "montaraz, rustico, indomable" -- was used of masterless animals gone wild before it named the mountain peasant and then the Puerto Rican national type.',
     NULL,0,'solid','Pichardo, Diccionario provincial de voces cubanas (1836); Oviedo (1535); colonial Caribbean lexicography.',
     'INDEPENDENTLY CORROBORATED by the South America agent. Three defining Caribbean forms of life outside colonial control are named after animals that got out first. HANDLE WITH CARE: this runs directly through chattel slavery and marronage. Not available for borrowing as a metaphor.'),

    ('North America','US vernacular','"Root hog or die"','proverb','no_containment',
     'Proverbial in the Vermont Gazette by 1829 and in Crockett''s Narrative (1834). Presupposes the free-ranging hog: you have been turned loose, forage or perish.',
     NULL,0,'solid','Vermont Gazette (1829); David Crockett, Narrative (1834).',NULL),

    ('North America','Spanish colonial','De Soto''s thirteen pigs','historical_event','escape_enclosure',
     'Thirteen pigs landed at Tampa Bay in 1539 became roughly 700, escaping continuously across a 3,100-mile march. Columbus''s 1493 introduction required a crown order to cut the population within twelve years.',
     NULL,0,'solid','Colonial Spanish records.',NULL),

    ('North America','Canada','"Super pigs"','historical_event','escape_enclosure',
     'Escaped from 1980s-90s wild-boar diversification farms; now occupying ~750,000 km2 and expanding ~88,000 km2 per year, sheltering in self-dug "pigloos".',
     NULL,0,'solid','Ryan Brook, University of Saskatchewan.',NULL),

    ('North America','US internet','"30-50 feral hogs"','idiom','uncatchable',
     'August 2019 viral formulation, now a fixed idiom for an absurd but genuine uncontainable threat.',
     NULL,0,'solid','Contemporary reporting, 2019.',NULL),

    ('North America','US literary','Charlotte''s Web -- ch. 3, "Escape"','literary','escape_enclosure',
     'Wilbur finds a loose board, gets out of the pen with the goose urging him on, discovers he has no idea what to do with the outside, and follows a bucket of slops straight back in.',
     NULL,0,'probable','E. B. White, Charlotte''s Web (1952), ch. 3.',
     'DESCRIBED FROM MEMORY, NOT FROM THE TEXT. Beats confident: loose board, goose, slops, voluntary return. Exact wording unverified.'),

    ('North America','US literary','Charlotte''s Web -- the words in the web','literary','transformation',
     'Wilbur''s real enclosure is a date, not a fence, and he escapes it without moving: Charlotte writes SOME PIG, TERRIFIC, RADIANT, HUMBLE, and the description of him changes. He never leaves the pen; he leaves the category. The message works because of its container -- a web is an impossible place for text, so the humans read it as being about the pig rather than about the author.',
     NULL,0,'solid','E. B. White, Charlotte''s Web (1952). Rachel Dean-Ruzicka, "Advertising the Self: The Culture of Personality in E. B. White''s Charlotte''s Web", Jeunesse 6:1.',
     'THE FORMAT ARGUMENT, STATED IN 1952. White worked ~2 years as a copywriter at the Frank Seaman agency before joining The New Yorker in 1925. Same work appears twice under different theme_class -- the schema could not hold it in one row, which is the defect this piece is about.'),

    ('North America','Mesoamerica','OPEN LEAD: release of impounded game (A1421)','myth','escape_enclosure',
     'Thompson motif A1421 -- the dueno del monte who keeps the game penned until someone releases it. A peccary version in Maya ethnography would be the strongest possible Indigenous item here and would rhyme exactly with the Mundurucu sty myth.',
     'Motif A1421',1,'thin','NOT FOUND. Next step: Thompson, Ethnology of the Mayas (1930); Braakhuis, Xbalanque''s Marriage.',
     'Needs a human with library access.'),

    ('North America','US search results','CONTAMINATION: fabricated Indigenous material and Grokipedia','historical_event','no_containment',
     'Searching javelina plus Indigenous tradition returns, at the top of results, uncited "Tohono O''odham and Yaqui" symbolism from spirit-animal content farms with no narrator, collector or publication. Grokipedia (LLM-generated) surfaced in roughly eight result sets.',
     NULL,NULL,'solid','Agent''s own search log, 2026-07-28.',
     'BELONGS IN THE PIECE. Research into what models absorbed from human narrative is already being contaminated by machine-generated encyclopedia entries about that same narrative.');

-- ---------------------------------------------------------------------------
-- SOUTH AMERICA -- native peccaries plus twice-feral Iberian introductions
-- ---------------------------------------------------------------------------

INSERT INTO folklore (continent, culture, title, item_type, theme_class, description, motif_index, is_native, confidence, source_note, notes) VALUES
    ('South America','Mundurucu','The origin of wild pigs','myth','escape_enclosure',
     'Karusakaibe transforms humans into pigs, who are first kept in a pig-sty in the village and killed one by one, until someone lets them out and they flee into the forest and become the wild pigs of today. Contemporary tellings add the Tapajos crossing, the sacred passage at Macapa/Mukapap, a variant where Karosakaybu re-traps the pigs between mountains, and a son who crosses over and stays with them.',
     NULL,1,'solid','Robert F. Murphy, Mundurucu Religion, UCPAAE 49(1), 1958. Treated in Levi-Strauss, The Raw and the Cooked.',
     'KEYSTONE. Not a story with an escape in it -- an origin story in which the species IS the escape. Berkeley open-access PDF blocked; must be read. Sty detail graded PROBABLE.'),

    ('South America','Pan-Amazonian','White-lipped peccary disappearance cycles','historical_event','uncatchable',
     '43 documented disappearance events across nine countries and 88 years of harvest data; 7-12 year troughs in 20-30 year cycles, synchronised across up to 5 million km2. The paper incorporates Indigenous testimony explaining disappearances as caused by the death of a powerful shaman, with return securable only through another shaman''s ritual work.',
     NULL,1,'solid','Fragoso et al., PLOS ONE (2022).',
     'Peer-reviewed, and it takes Indigenous explanation seriously as data rather than colour.'),

    ('South America','Brazilian','Caipora / Curupira as godfather of the herds','myth','uncatchable',
     'Rides a caititu or queixada, travels with the peccary herds, steers the pigs away from hunters'' traps, and bargains a quota of animals for tobacco, cachaca and cloth.',
     NULL,1,'probable','Popular Brazilian folklore sources; Camara Cascudo attribution unverified.',
     'An explicit uncatchability mechanism with an agent behind it.'),

    ('South America','Wari'' / Ese Eja','Peccaries as the dead returning','myth','transformation',
     'THE COUNTER-MOTIF. Wari'' ancestors return as white-lipped peccaries and approach kin hunters deliberately, so that their meat feeds their own relatives. Movement inward, not outward.',
     NULL,1,'probable','Aparecida Vilaca, Wari'' ethnography.',
     'Important residual case: a pig-crossing story where the crossing is a return, not an escape.'),

    ('South America','Argentina','The jabali release chain','historical_event','escape_enclosure',
     '1906 San Huberto reserve (now Parque Luro, La Pampa); 1909 Carpathian stock released into an 800-hectare enclosure; Pedro Luro''s bankruptcy lets them off the property; escapes 1914-1930; a 1931 accident seeds Patagonia.',
     NULL,0,'probable','Argentine environmental history.',NULL),

    ('South America','Brazil','IBAMA''s 1998 javali breeding ban','legal','escape_enclosure',
     'IBAMA banned javali breeding in 1998, and breeders responded by releasing their stock. The containment regulation is what set the animal loose.',
     NULL,0,'probable','Brazilian environmental regulation and reporting.',
     'Directly analogous to the open-weights argument. A restriction produced the proliferation it was meant to prevent.'),

    ('South America','Colonial Spanish','Puercos cimarrones','idiom','social_boundary',
     'Oviedo describes puercos cimarrones in 1535. The same term covered escaped livestock and escaped people; Argentines still say chanchos cimarrones.',
     NULL,0,'solid','Oviedo (1535); colonial Spanish lexicography.',
     'Independently corroborated by the North America agent. See the handling caution on that row.');

-- ---------------------------------------------------------------------------
-- OCEANIA -- three incompatible answers to the same question
-- ---------------------------------------------------------------------------

INSERT INTO folklore (continent, culture, title, item_type, theme_class, description, motif_index, is_native, confidence, source_note, notes) VALUES
    ('Oceania','Hawaiian','Kamapua''a -- serial failed containment','myth','uncatchable',
     'Four times the guards -- eight hundred strong and increasing each time -- capture him in hog shape and tie him to a pole; four times his grandmother releases him with a chant. Bound for sacrifice on a heiau, he escapes because the priest Lonoaohi had instructed his sons to only PRETEND to tie him: the ropes are theatre.',
     NULL,1,'solid','Martha Beckwith, Hawaiian Mythology (1940), ch. XIV. Lilikala Kame''eleihiwa, A Legendary Tradition of Kamapua''a (Bishop Museum Press, 1996), translating an anonymous 1891 Ka Leo o ka Lahui serial.',
     'THE ROPES ARE THEATRE. A constraint that looks binding from outside, staged by someone inside the system who arranged for it not to hold. Kame''eleihiwa reportedly reads the 1891 timing, two years before the overthrow, as anti-colonial defiance -- VERIFY her introduction.'),

    ('Oceania','Hawaiian','Kamapua''a at Kaliuwa''a','myth','escape_enclosure',
     'He becomes a giant hog so his people can climb his back out of a box canyon. The place (Sacred Falls, O''ahu) is named for the escape.',
     NULL,1,'solid','Beckwith, Hawaiian Mythology (1940).',NULL),

    ('Oceania','Hawaiian','Kamapua''a as humuhumunukunukuapua''a','myth','transformation',
     'Fleeing Pele''s fire he becomes the humuhumunukunukuapua''a -- the escape-form is named after the thing escaping.',
     NULL,1,'solid','Beckwith, Hawaiian Mythology (1940).',NULL),

    ('Oceania','Tsembaga Maring (PNG)','The kaiko festival trigger','ritual','escape_enclosure',
     'The festival is not scheduled. It is triggered when the herd grows until pigs invade gardens and the labour burden on women becomes insupportable. An entire ritual calendar keyed to the moment fences stop working.',
     NULL,0,'solid','Roy Rappaport, Pigs for the Ancestors (1968).',
     'Hedge the functionalist theory; the observation is secure.'),

    ('Oceania','Vanuatu','Tusker boars','ritual','social_boundary',
     'THE INVERSION. Upper canines avulsed so the lower ones curl unimpeded -- full circle in 6-7 years, double in 10-12, eventually puncturing the animal''s own jaw and requiring surgical care. Required for grade-taking; the boar''s tusk is on the national flag.',
     NULL,0,'solid','Vanuatu ethnographic literature.',
     'Containment as decade-long artwork, where the constraint is what produces the value. The exact opposite theory of the pig from Kamapua''a, in the same ocean.'),

    ('Oceania','British/Pacific','Cook''s deliberate releases','historical_event','escape_enclosure',
     'Cook left breeding pairs on islands as POLICY, not accident -- so that a future wrecked British ship would find protein waiting. Escape reconceived as infrastructure. In the same decade he is recorded describing Malakula''s tusks bent into perfect closed circles.',
     NULL,0,'solid','Cook''s voyage journals.',
     'THE OPEN-WEIGHTS SECTION. He did not lose those pigs, he invested them. Release because proliferation is the point, versus the tusker''s cultivated constraint -- two opposite theories of the pig, one man, the 1770s.'),

    ('Oceania','New Zealand','"Captain Cooker"','idiom','uncatchable',
     'New Zealanders named their uncatchable feral pig after the man who released the founders. The escape is memorialised in the escapee''s surname.',
     NULL,0,'solid','New Zealand vernacular; Te Ara.',NULL),

    ('Oceania','Maori (Waima)','The pigs in the tapu kumara plantations','tale','boundary_taboo',
     'Pigs entered tapu kumara plantations and, because of the tapu, no one could go in and remove them. The grunting from inside the sacred ground convinced people they were gods.',
     NULL,0,'solid','Te Ao Hou.',
     'A containment failure caused by ritual law rather than bad fencing -- the rule protecting the space prevented its own enforcement.'),

    ('Oceania','Aotearoa/Pacific','ABSENCE: no deep proverbial stock','proverb','no_containment',
     'No documented Tok Pisin pig proverb and no Maori whakatauki about poaka. Pigs reached Aotearoa only after 1769 -- too recent to sediment into the proverbial layer.',
     NULL,0,'solid','Negative finding across the agent''s full search.',
     'DATING CONTROL FOR THE WHOLE SURVEY. Proverbs need centuries. Where pigs are recent arrivals you get ecology and newspapers; where ancient, idiom. Proverb density is a rough clock.'),

    ('Oceania','Polynesian','NOT FOUND: Maui and pig','myth','no_containment',
     'No reliable Maui-and-pig episode exists.',
     NULL,1,'dubious','Negative finding. Agent recommends omitting entirely.',
     'Recorded so nobody goes looking for it twice.');

COMMIT;
