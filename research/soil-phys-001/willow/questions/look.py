import json, re, sys, collections
sys.path.insert(0, __import__("os").environ["WILLOW"]); import kernel
Q=[l.rstrip("\n").split("\t",1) for l in open("questions.tsv",encoding="utf-8")]
K=[json.loads(l) for l in open("kernel.jsonl",encoding="utf-8")]
def src(w): return re.sub(r"(\.(pdf|html|txt|part2))+$","",w.rsplit(":",1)[0].split("/")[-1])
def holds_all(q,text):
    want=set(kernel.words(q))-kernel.FUNCTION; t=kernel.forms(kernel.words(text))
    return bool(want) and all(kernel.holds(w,t) for w in want)
want=sys.argv[1:]
for (n,q),k in zip(Q,K):
    if not n.startswith("pair:"): continue
    pair,lang=n[5:].rsplit("|",1)
    if pair not in want and "|".join(pair.split("|")[::-1]) not in want: continue
    for x in k.get("served",[])[:10]:
        if holds_all(q,x["text"]):
            print(f"[{pair} {lang}] {x['where']} | {' '.join(x['text'].split())[:240]}"); break
