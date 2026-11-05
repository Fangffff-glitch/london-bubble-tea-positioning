"""Rebuild descriptive charts from the published AI-coded pilot CSV.
Chart code generated with Codex assistance. This script does not classify text.
Run: python3 build_charts.py (requires matplotlib and numpy).
"""
from pathlib import Path
import csv,json
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=Path(__file__).resolve().parent
rows=list(csv.DictReader((p/'review_coding_public.csv').open(encoding='utf-8')))
assert len(rows)==60 and len({r['google_review_id'] for r in rows})==60
valid=[r for r in rows if r['included']=='true']
brands=['T4','Milksha','Truedan']
places=['T4 · Liverpool Street','Milksha · Shaftesbury Ave','Truedan · Russell Square']
labels=['positive','mixed','neutral','negative']
colors={'positive':'#157F78','mixed':'#DC9A33','neutral':'#9AA4B2','negative':'#BE4B59'}
themes=['Taste and product experience','Staff and service','Ingredients and authenticity','Price and value','Speed and waiting','Convenience and setting','Promotions and capacity']
ns=[sum(r['brand']==b for r in valid) for b in brands]
assert ns==[18,17,18]
for r in valid:
 assert r['sentiment'] in labels
 assert set(json.loads(r['theme_polarity'])).issubset(themes)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'figure.facecolor':'#FAFAF7','axes.facecolor':'#FAFAF7','text.color':'#172B3A','axes.labelcolor':'#172B3A','xtick.color':'#51616D','ytick.color':'#172B3A'})
footer='Google Maps · collected 5 Nov 2026 · newest-first convenience pilot\nAI-coded; author human review pending. Store-specific, not representative brand rankings.'
def save(fig,name):
 fig.savefig(p/name,dpi=170,facecolor=fig.get_facecolor());plt.close(fig)
fig,ax=plt.subplots(figsize=(11,5.2));fig.subplots_adjust(left=.27,right=.96,top=.76,bottom=.25)
left=np.zeros(3)
for lab in labels:
 counts=np.array([sum(r['brand']==b and r['sentiment']==lab for r in valid) for b in brands]);vals=counts/np.array(ns)*100
 ax.barh(range(3),vals,left=left,color=colors[lab],height=.53,label=lab.title())
 for i,(v,c,l) in enumerate(zip(vals,counts,left)):
  if c:ax.text(l+v/2,i,f'{c}\n{v:.1f}%',ha='center',va='center',color='white' if lab in ('positive','negative') else '#172B3A',fontsize=10,fontweight='bold')
 left+=vals
ax.set_yticks(range(3),[f'{place}\ntext n = {n}' for place,n in zip(places,ns)]);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xticks([0,25,50,75,100],['0%','25%','50%','75%','100%']);ax.tick_params(length=0)
fig.text(.04,.94,'How do the sampled reviews feel?',fontsize=21,fontweight='bold')
fig.text(.04,.88,'Text sentiment, not star-rating buckets · 53 included reviews from 60 candidates',fontsize=11)
ax.legend(ncol=4,loc='upper center',bbox_to_anchor=(.48,-.16),frameon=False)
fig.text(.04,.045,footer,fontsize=9,color='#51616D');save(fig,'sentiment_distribution.png')
counts=np.array([[sum(r['brand']==b and t in json.loads(r['theme_polarity']) for r in valid) for b in brands] for t in themes]);pct=counts/np.array(ns)*100
fig,ax=plt.subplots(figsize=(11,7));fig.subplots_adjust(left=.34,right=.96,top=.78,bottom=.2)
ax.imshow(pct,cmap='YlGnBu',vmin=0,vmax=100,aspect='auto')
for i in range(len(themes)):
 for j in range(3):ax.text(j,i,f'{counts[i,j]}/{ns[j]} · {pct[i,j]:.0f}%',ha='center',va='center',color='white' if pct[i,j]>55 else '#172B3A',fontsize=12,fontweight='bold')
ax.set_yticks(range(len(themes)),themes);ax.set_xticks(range(3),brands);ax.xaxis.tick_top();ax.tick_params(length=0,pad=10)
fig.text(.04,.94,'What do customers choose to mention?',fontsize=21,fontweight='bold')
fig.text(.04,.88,'Share of included text reviews mentioning each theme · multiple themes per review',fontsize=11)
fig.text(.04,.11,'Counts are shown in every cell. Darker colour = higher share. Zero means absent in this sample, not unimportant.',fontsize=9)
fig.text(.04,.035,footer,fontsize=9,color='#51616D');save(fig,'theme_prevalence.png')
fig,ax=plt.subplots(figsize=(11,7));fig.subplots_adjust(left=.34,right=.96,top=.78,bottom=.25)
left=np.zeros(len(themes));polcounts={}
for lab in labels:
 vals=np.array([sum(json.loads(r['theme_polarity']).get(t)==lab for r in valid) for t in themes]);polcounts[lab]=vals.tolist()
 ax.barh(range(len(themes)),vals,left=left,height=.58,color=colors[lab],label=lab.title())
 for i,(v,l) in enumerate(zip(vals,left)):
  if v:ax.text(l+v/2,i,str(v),ha='center',va='center',fontsize=10,fontweight='bold',color='white' if lab in ('positive','negative') else '#172B3A')
 left+=vals
ax.set_yticks(range(len(themes)),themes);ax.invert_yaxis();ax.set_xlabel('Number of reviews mentioning the theme (all three stores pooled)');ax.tick_params(length=0)
ax.legend(ncol=4,loc='upper center',bbox_to_anchor=(.4,-.2),frameon=False)
fig.text(.04,.94,'Where does praise coexist with friction?',fontsize=21,fontweight='bold')
fig.text(.04,.88,'Theme-level sentiment · one polarity per mentioned theme per review',fontsize=11)
fig.text(.04,.04,footer+'\nPooling describes this pilot only; differences in store mix affect these totals.',fontsize=9,color='#51616D');save(fig,'theme_sentiment.png')
summary={b:{'included':ns[i],**{lab:sum(r['brand']==b and r['sentiment']==lab for r in valid) for lab in labels}} for i,b in enumerate(brands)}
(p/'summary_counts.json').write_text(json.dumps({'stores':summary,'theme_order':themes,'theme_counts_by_store':counts.tolist(),'pooled_theme_polarity':polcounts},indent=2)+'\n')
print(json.dumps(summary,indent=2));print('Validated totals and generated three charts.')
