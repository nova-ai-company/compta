import glob,re,sys
def num(x):
    x=x.strip().replace('*','').replace(' ','').replace(' ','').replace('€','')
    if not x: return 0.0
    if not re.fullmatch(r'-?\d+(,\d+)?',x): return None
    return float(x.replace(',','.'))
bad=0;n=0
for f in sorted(glob.glob(sys.argv[1]+'/modules/*/corriges/*.md')):
    lines=open(f).read().splitlines()
    i=0
    while i<len(lines):
        l=lines[i]
        if l.startswith('|') and re.search(r'\|\s*Débit\s*\|\s*Crédit\s*\|\s*$',l):
            hdr=[c.strip() for c in l.strip('|').split('|')]
            di,ci=len(hdr)-2,len(hdr)-1
            D=C=0.0; tot=None; j=i+2; ok=True
            while j<len(lines) and lines[j].startswith('|'):
                cells=[c for c in lines[j].strip().strip('|').split('|')]
                if len(cells)!=len(hdr): j+=1; continue
                d,c=num(cells[di]),num(cells[ci])
                if 'total' in lines[j].lower() and not cells[0].strip():
                    tot=(d,c); j+=1; continue
                if d is None or c is None: ok=False
                else: D+=d;C+=c
                j+=1
            n+=1
            if ok and (abs(D-C)>0.011 or (tot and tot[0] is not None and (abs(tot[0]-D)>0.011 or abs((tot[1] or 0)-C)>0.011))):
                bad+=1; print(f.split('modules/')[1], 'ligne',i+1,'D=%.2f C=%.2f tot=%s'%(D,C,tot))
            i=j
        else: i+=1
print(n,'tables,',bad,'anomalies')
