"""Reproduce mention flags from locally held raw JSON; no sentiment model.
Usage: python3 code_themes.py /path/to/raw_directory > theme_flags.csv
Raw files: t4_raw_private.json, milksha_raw_private.json, truedan_raw_private.json
"""
import csv,json,re,sys
from pathlib import Path
patterns=json.loads((Path(__file__).parent/'theme_dictionary.json').read_text())
writer=csv.DictWriter(sys.stdout,fieldnames=['record_id','google_review_id']+list(patterns));writer.writeheader()
for key in ['t4','milksha','truedan']:
 records=json.loads((Path(sys.argv[1])/f'{key}_raw_private.json').read_text())
 for i,r in enumerate(records,1):
  text=r['text'].strip()
  speed_text=re.sub(r"\b(can.?t|cannot) wait (for my next visit|to (try|visit|return|go|spend|drink))",'',text,flags=re.I)
  flags={theme:int(bool(text and re.search(pattern,speed_text if theme=='speed_waiting' else text,re.I))) for theme,pattern in patterns.items()}
  writer.writerow({'record_id':f'{key.upper()}-{i:04}','google_review_id':r['id'],**flags})
