import json, re, sys, collections
sys.path.insert(0, __import__("os").environ["WILLOW"]); import kernel
Q=[l.rstrip("\n").split("\t",1) for l in open("questions.tsv",encoding="utf-8")]
K=[json.loads(l) for l in open("kernel.jsonl",encoding="utf-8")]
B=[json.loads(l) for l in open("bm25.jsonl",encoding="utf-8")]
def src(w): return re.sub(r"(\.(pdf|html|txt|part2))+$","",w.rsplit(":",1)[0].split("/")[-1])
def holds_all(q,text):
    want=set(kernel.words(q))-kernel.FUNCTION; t=kernel.forms(kernel.words(text))
    return bool(want) and all(kernel.holds(w,t) for w in want)
meet=collections.defaultdict(lambda: collections.defaultdict(list))  # pair -> src -> [(lang, where, text)]
for (n,q),k,b in zip(Q,K,B):
    if not n.startswith("pair:"): continue
    pair,lang=n[5:].rsplit("|",1)
    for x in k.get("served",[])+b.get("served",[]):
        if holds_all(q,x["text"]):
            meet[pair][src(x["where"])].append((lang,x["where"],x["text"]))
pairs=sorted({n[5:].rsplit("|",1)[0] for n,_ in Q if n.startswith("pair:")})
never=[p for p in pairs if not meet[p]]
one=[(p,list(meet[p])[0]) for p in pairs if len(meet[p])==1]
print(len(pairs),"pairs;",len(never),"meet nowhere;",len(one),"meet in one source only")
json.dump({"never":never,"one":one},open("pairs_out.json","w"),ensure_ascii=False,indent=0)
cnt=collections.Counter(s for p,s in one); print("single-source meetings by source:",cnt.most_common(15))
# concept "degree": how many other concepts each meets
deg=collections.Counter()
for p in pairs:
    if meet[p]:
        a,b=p.split("|"); deg[a]+=1; deg[b]+=1
names=sorted({x for p in pairs for x in p.split("|")})
print("\nconcepts meeting the fewest others:", sorted(((deg[x],x) for x in names))[:15])
print("concepts meeting the most:", sorted(((deg[x],x) for x in names),reverse=True)[:10])
# language-only meetings: pairs that meet only in German or only in French
lang_only=collections.defaultdict(list)
for p in pairs:
    langs={l for s in meet[p].values() for l,*_ in s}
    if langs and "en" not in langs: lang_only["/".join(sorted(langs))].append(p)
print("\npairs that meet only outside English:",{k:len(v) for k,v in lang_only.items()})
json.dump(lang_only,open("lang_only.json","w"),ensure_ascii=False,indent=0)
# the focal concepts' meetings
for c in ["zero","nothing","empty","void","container","boundary","origin","unit","one","distinction"]:
    m=sorted([(p, sorted(meet[p])) for p in pairs if c in p.split("|") and meet[p]], key=lambda x: len(x[1]))
    print(f"\n## {c}: meets {len(m)} of {len(names)-1}; never meets:", sorted(p.replace(c,'').strip('|') for p in pairs if c in p.split('|') and not meet[p])[:40])
