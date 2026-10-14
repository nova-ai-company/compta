import os,re,glob,sys
root=sys.argv[1]
mods=sorted(glob.glob(os.path.join(root,'modules','M*')))
out=["# Index des exercices","","> Généré automatiquement. Cliquez sur l'énoncé, faites l'exercice, **puis seulement** ouvrez le corrigé.",""]
total=0; missing=[]
for m in mods:
    name=os.path.basename(m)
    cours=os.path.join(m,'cours.md')
    t=re.sub(r'^M\d\d\s*[—:-]\s*','',open(cours).readline().lstrip('# ').strip()) if os.path.exists(cours) else name
    out+=[f"## {name[:3]} — {t}","",f"📘 [Cours]({os.path.relpath(cours,root)})","","| N° | Exercice | Client | Difficulté | Énoncé | Corrigé |","|---|---|---|---|---|---|"]
    for f in sorted(glob.glob(os.path.join(m,'exercices','*.md'))):
        txt=open(f).read()
        first=txt.splitlines()[0].lstrip('# ').strip()
        num=os.path.basename(f).split('_')[0]
        title=re.sub(r'^E\d\d-\d\d\s*[—-]\s*','',first)
        cl=re.search(r'\*\*Clients?\s*:\*\*\s*([^|\n]+)',txt); cl=cl.group(1).strip() if cl else ''
        di=re.search(r'\*\*Difficulté\s*:\*\*\s*([★☆]+)',txt); di=di.group(1) if di else ''
        cands=glob.glob(os.path.join(m,'corriges',num+'*.md'))
        if not cands: missing.append(num)
        cor=' · '.join(f"[{os.path.basename(c).replace('.md','').replace(num+'_','').replace('corrige','corrigé')}]({os.path.relpath(c,root)})" for c in sorted(cands))
        out.append(f"| {num} | {title} | {cl} | {di} | [énoncé]({os.path.relpath(f,root)}) | {cor} |")
        total+=1
    out.append("")
out.insert(4,f"**{total} exercices** répartis en {len(mods)} modules.\n")
open(os.path.join(root,'02_INDEX_DES_EXERCICES.md'),'w').write("\n".join(out))
print(total,'exercices; corrigés manquants:',missing)
