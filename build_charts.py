"""Rebuild charts and verify counts from the public, already-coded review table.
This script does not run a sentiment model. Python 3 + matplotlib + numpy.
"""
import csv, json
from pathlib import Path
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE=Path(__file__).parent
rows=list(csv.DictReader((BASE/'review_coding_public.csv').open()))
keys=['t4','milksha','truedan']; names=['T4 · Liverpool Street','Milksha · Shaftesbury Ave','Truedan · Russell Square']
labels=['positive','mixed','neutral','negative','unclear']
colors=['#227c70','#e3b04b','#91a0aa','#cb6658','#8368a0']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.titleweight':'bold','figure.facecolor':'#faf9f5','axes.facecolor':'#faf9f5','savefig.facecolor':'#faf9f5'})
texts={k:[r for r in rows if r['store']==k and r['has_text']=='1'] for k in keys}
summary=json.loads((BASE/'summary_counts.json').read_text())
assert len(rows)==2941 and len({r['google_review_id'] for r in rows})==2941
for k in keys:
 assert Counter(r['sentiment'] for r in texts[k])==summary[k]['sentiment']

def finish(fig,filename,foot):
 fig.text(.02,.025,foot,fontsize=9,color='#536268',va='bottom')
 fig.savefig(BASE/filename,dpi=180,bbox_inches='tight');plt.close(fig)

fig,ax=plt.subplots(figsize=(12,5.4));left=np.zeros(3)
for label,c in zip(labels,colors):
 counts=np.array([sum(r['sentiment']==label for r in texts[k]) for k in keys]);p=counts/np.array([len(texts[k]) for k in keys])*100
 ax.barh(np.arange(3),p,left=left,color=c,label=label.title(),height=.56)
 for i,v in enumerate(p):
  if v>=4:ax.text(left[i]+v/2,i,f'{v:.1f}%',ha='center',va='center',color='white' if label=='positive' else '#253135',fontweight='bold')
 left+=p
ax.set(yticks=range(3),yticklabels=[f'{n}\ntext n = {len(texts[k]):,}' for k,n in zip(keys,names)],xlim=(0,100),xlabel='Share of text reviews (%)',title='Customer sentiment across the complete review snapshot')
ax.invert_yaxis();ax.legend(ncol=5,loc='upper center',bbox_to_anchor=(.5,-.17),frameon=False)
fig.subplots_adjust(left=.25,bottom=.27,top=.88)
finish(fig,'sentiment_distribution.png','2,375 text reviews · AI semantic labels · Mixed retains both praise and criticism.\n566 rating-only records are excluded from text sentiment, not from the dataset. Google Maps · 5 Nov 2026.')

themes={'drink_product':'Product / drink vocabulary','staff_service':'Staff / service','speed_waiting':'Speed / waiting','authenticity_origin':'Authenticity / Taiwanese origin','price_value':'Price / value / promotions','customisation':'Customisation','setting_location':'Setting / location','desserts_bakery':'Desserts / bakery','digital_delivery':'Digital ordering / delivery','repeat_loyalty':'Repeat / loyalty language'}
matrix=np.array([[sum(int(r[t]) for r in texts[k])/len(texts[k])*100 for k in keys] for t in themes])
fig,ax=plt.subplots(figsize=(12,7.6));im=ax.imshow(matrix,cmap='YlGnBu',vmin=0,vmax=85,aspect='auto')
for y,t in enumerate(themes):
 for x,k in enumerate(keys):
  count=sum(int(r[t]) for r in texts[k]);ax.text(x,y,f'{matrix[y,x]:.1f}%  ·  {count:,}',ha='center',va='center',color='white' if matrix[y,x]>45 else '#253135')
ax.set(yticks=range(len(themes)),yticklabels=list(themes.values()),xticks=range(3),xticklabels=['T4\nn=1,323','Milksha\nn=418','Truedan\nn=634'],title='What customers mention')
ax.tick_params(length=0);fig.subplots_adjust(left=.32,bottom=.16,top=.9,right=.97)
finish(fig,'theme_prevalence.png','Dictionary-detected mentions: % of each store’s text reviews, followed by count. Multi-label; totals exceed 100%.\nMentions show topics, not sentiment, importance or verified facts. Product vocabulary overlaps with desserts.')

fig,ax=plt.subplots(figsize=(12,5.4));left=np.zeros(3)
for star,c in zip([5,4,3,2,1],['#227c70','#80b3a1','#d7c47c','#df966a','#cb6658']):
 ns=np.array([sum(r['store']==k for r in rows) for k in keys]);counts=np.array([sum(r['store']==k and int(r['stars'])==star for r in rows) for k in keys]);p=counts/ns*100
 ax.barh(range(3),p,left=left,color=c,label=f'{star} stars',height=.56)
 for i,v in enumerate(p):
  if v>=5:ax.text(left[i]+v/2,i,f'{v:.1f}%',ha='center',va='center',color='white' if star==5 else '#253135')
 left+=p
ax.set(yticks=range(3),yticklabels=[f'{n}\nall records n = {summary[k]["collected"]:,}' for k,n in zip(keys,names)],xlim=(0,100),xlabel='Share of all review/rating records (%)',title='Star ratings include every collected record')
ax.invert_yaxis();ax.legend(ncol=5,loc='upper center',bbox_to_anchor=(.5,-.17),frameon=False);fig.subplots_adjust(left=.25,bottom=.27,top=.88)
finish(fig,'rating_distribution.png','2,941 records, including 566 without customer text · Google Maps snapshot · 5 Nov 2026.\nStar ratings and text sentiment measure different things; these are three stores, not whole-brand rankings.')

fig,ax=plt.subplots(figsize=(12,5.7));y=np.arange(3)
for offset,recent,c,name in [(-.18,False,'#227c70','All text reviews'),(.18,True,'#6f91b0','Displayed age under one year')]:
 for i,k in enumerate(keys):
  rr=[r for r in texts[k] if not recent or r['display_age_band']=='under_one_year'];p=sum(r['sentiment']=='positive' for r in rr)/len(rr)*100
  ax.barh(i+offset,p,height=.32,color=c,label=name if i==0 else None);ax.text(p+1,i+offset,f'{p:.1f}% (n={len(rr):,})',va='center',fontsize=10)
ax.set(yticks=y,yticklabels=names,xlim=(0,117),xlabel='Positive-only text sentiment (%)',title='Does the broad recency check change the picture?')
ax.set_xticks([0,20,40,60,80,100]);ax.invert_yaxis();ax.legend(loc='upper center',bbox_to_anchor=(.5,-.14),ncol=2,frameon=False);fig.subplots_adjust(left=.25,bottom=.27,top=.88)
finish(fig,'recency_sensitivity.png','Recent means Google displays hours/days/weeks/months, not a precise 12-month visit window.\nEdited dates and historical experiences can fall in the recent bucket. No significance or causal claim.')

# Keep the existing filename but correct its interpretation explicitly.
fig,ax=plt.subplots(figsize=(12,7));selected=['staff_service','speed_waiting','authenticity_origin','price_value','desserts_bakery','digital_delivery'];left=np.zeros(len(selected))
for label,c in zip(labels,colors):
 rr=[[r for r in rows if r[t]=='1'] for t in selected];p=np.array([sum(r['sentiment']==label for r in v)/len(v)*100 for v in rr])
 ax.barh(range(len(selected)),p,left=left,color=c,label=label.title(),height=.64);left+=p
ax.set(yticks=range(len(selected)),yticklabels=[f'{themes[t]} (n={sum(r[t]=="1" for r in rows)})' for t in selected],xlim=(0,100),xlabel='Whole-review sentiment (%)',title='Sentiment of reviews mentioning each topic')
ax.invert_yaxis();ax.legend(ncol=5,loc='upper center',bbox_to_anchor=(.5,-.12),frameon=False);fig.subplots_adjust(left=.34,bottom=.23,top=.9)
finish(fig,'theme_sentiment.png','Pooled across stores; overlapping groups. These are whole-review labels, NOT sentiment about the named topic.\nFor example, praise for tea plus criticism of service is mixed in every topic the review mentions.')
print('Verified 2,941 records and generated five charts.')
