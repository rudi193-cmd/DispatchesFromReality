import json, re, sys, collections
sys.path.insert(0, __import__("os").environ["WILLOW"]); import kernel
Q=[l.rstrip("\n").split("\t",1) for l in open("questions.tsv",encoding="utf-8")]
K=[json.loads(l) for l in open("kernel.jsonl",encoding="utf-8")]
B=[json.loads(l) for l in open("bm25.jsonl",encoding="utf-8")]
assert len(Q)==len(K)==len(B)
def src(where): return re.sub(r"(\.(pdf|html|txt|part2))+$","",where.rsplit(":",1)[0].split("/")[-1])
def year(s):
    m=re.search(r"(1[6-9]\d\d|20\d\d)",s); return int(m.group(1)) if m else None
def holds_all(q,text):
    want=set(kernel.words(q))-kernel.FUNCTION; t=kernel.forms(kernel.words(text))
    return all(kernel.holds(w,t) for w in want)
R={}
# 1 hubs and dark sources
rank1=collections.Counter(); top3src=collections.Counter(); answered=0
for (n,q),k in zip(Q,K):
    s=k.get("served",[])
    if s: answered+=1; rank1[(s[0]["where"],s[0]["text"][:120])]+=1
    for x in s[:3]: top3src[src(x["where"])]+=1
allsrc={src(x["where"]) for k in K for x in k.get("served",[])}
print("answered",answered,"of",len(Q))
print("\n## passages served first most often")
for (w,t),c in rank1.most_common(12): print(f"{c:5}  {w}  {' '.join(t.split())[:100]}")
print("\n## sources by how often in a top 3 (fewest)")
for s,c in sorted(top3src.items(), key=lambda x:x[1])[:12]: print(f"{c:6}  {s}")
# 2 own questions answered by another source
print("\n## the papers' own questions, first answer from ANOTHER source holding all the question's content words")
rows=[]
for (n,q),k in zip(Q,K):
    if not n.startswith("own:"): continue
    asker=n.split(":",1)[1]
    for x in k.get("served",[]):
        if src(x["where"]).split("-open")[0].split("-english")[0]!=asker.split("-open")[0].split("-english")[0] and holds_all(q,x["text"]) and not x["echo"]:
            rows.append((asker,q,src(x["where"]),x["where"],x["text"])); break
print(len(rows),"of",sum(n.startswith("own:") for n,_ in Q),"own questions")
json.dump(rows,open("own_answered.json","w"),ensure_ascii=False,indent=0)
