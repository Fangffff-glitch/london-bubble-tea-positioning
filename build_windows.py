"""Rebuild inclusion flags, window CSVs and summary_counts.json from the public archive.
Dates are approximate relative-display-age proxies, not verified exact windows.
Run before build_charts.py. No sentiment labels or topic flags are changed.
"""
import csv,json,re,shutil
from pathlib import Path
from collections import Counter
P=Path(__file__).parent
keys=['t4','milksha','truedan']
names={'t4':'T4 · Liverpool Street','milksha':'Milksha · Shaftesbury Ave','truedan':'Truedan · Russell Square'}
themes=list(json.loads((P/'theme_dictionary.json').read_text()))
rows=list(csv.DictReader((P/'review_coding_public.csv').open()))
for r in rows:
 age=r['displayed_age'].removeprefix('Edited ')
 recent=bool(re.fullmatch(r'(a|an|\d+) (hour|day|week|month)s? ago',age))
 one=age=='a year ago'
 assert recent or re.fullmatch(r'(a|\d+) years? ago',age),age
 historic=r['record_id']=='MILKSHA-0331'
 r.update({'edited_date_flag':str(int(r['displayed_age'].startswith('Edited '))),
  'known_historical_experience':str(int(historic)),
  'main_2y_proxy':str(int((recent or one) and not historic)),
  'comparison_1y_proxy':str(int(recent and not historic)),
  'window_reason':'explicit_2021_experience' if historic else ('relative_age_under_one_year' if recent else 'relative_age_one_year' if one else 'relative_age_two_years_or_older')})
with (P/'review_coding_public.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def summarise(rr):
 result={}
 for k in keys:
  v=[r for r in rr if r['store']==k];t=[r for r in v if r['has_text']=='1']
  result[k]={'records':len(v),'text_reviews':len(t),'rating_only':len(v)-len(t),
   'sentiment':dict(Counter(r['sentiment'] for r in t)),
   'stars':dict(sorted(Counter(r['stars'] for r in v).items())),
   'themes':{theme:sum(int(r[theme]) for r in t) for theme in themes},
   'edited_text_reviews':sum(int(r['edited_date_flag']) for r in t),
   'nonpositive_with_5_stars':sum(r['stars']=='5' and r['sentiment']!='positive' for r in t)}
 return result
S={'snapshot_date':'2026-11-05','revision_date':'2026-11-06',
 'intended_main_period':'2024-11-05 to 2026-11-05 (approximate; not verified exact dates)',
 'intended_comparison_period':'2025-11-05 to 2026-11-05 (approximate; not verified exact dates)',
 'main_2y_proxy':summarise([r for r in rows if r['main_2y_proxy']=='1']),
 'comparison_1y_proxy':summarise([r for r in rows if r['comparison_1y_proxy']=='1']),
 'main_without_edited':summarise([r for r in rows if r['main_2y_proxy']=='1' and r['edited_date_flag']=='0']),
 'all_history_archive':summarise(rows)}
(P/'summary_counts.json').write_text(json.dumps(S,indent=2))
for filename,field in [('reviews_main_2y.csv','main_2y_proxy'),('reviews_comparison_1y.csv','comparison_1y_proxy')]:
 with (P/filename).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(r for r in rows if r[field]=='1')
