import pathlib, re, json
ROOTS = ["core","builder","freelance","tasks","storage","reports","dashboard","sim","security","utils"]
def find_targets():
    targets=[]
    for root in ROOTS:
        for p in pathlib.Path(root).rglob("*.py"):
            txt=p.read_text(errors="ignore")
            if not txt.strip() or len(txt)<30 or re.search(r"TODO|pass\s+#\s*stub|#\s*🚧",txt):
                targets.append(str(p))
    return targets
if __name__=="__main__":
    print(json.dumps(find_targets(), indent=2))
