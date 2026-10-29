"""Validate resumable state and evidence claims without network or mutations."""
import json,sys
from pathlib import Path
ALLOWED={"pending","source_captured","mockup_saved","implemented","verified","published","baseline_published","retained_external","blocked"}
def validate(s):
 e=[]
 if s.get("project_id")!="appgprj_6ae10560a9dc8191be01ad534c0d49dd":e.append("wrong/missing project identity")
 pages=s.get("pages",[]);ids=[p.get("id") for p in pages]
 if len(set(ids))!=len(ids):e.append("duplicate page IDs")
 for p in pages:
  status=p.get("status");label=p.get("id")
  if status not in ALLOWED:e.append(f"{label}: invalid stage")
  if status=="published":
   for k in ["source_url","demo_path","current_screenshot","proposed_mockup","annotation_board","after_screenshot","verification","commit_sha","version_id","deployment_id","deployed_url"]:
    if not p.get(k):e.append(f"{label}: published without {k}")
   if p.get("deployment_status")!="succeeded":e.append(f"{label}: deployment not succeeded")
  if status=="retained_external" and not p.get("reason"):e.append(f"{label}: missing retention reason")
  if status=="blocked" and not p.get("blocker"):e.append(f"{label}: missing blocker")
 if s.get("run_status")=="complete":
  if any(p.get("status") not in {"published","retained_external"} for p in pages):e.append("cannot claim complete with unfinished/gallery-pending pages")
  if not s.get("sitemap_reconciled"):e.append("cannot claim complete before sitemap reconciliation")
 return e
if __name__=="__main__":
 s=json.loads(Path(sys.argv[1]).read_text());e=validate(s)
 if e:print("\\n".join(e));sys.exit(1)
 print(f"PASS: {len(s['pages'])} page records; completion claims have required evidence.")
