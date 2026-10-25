import os
from pathlib import Path
CIK = "1803498"
# SEC requires a real contact in the User-Agent: export SEC_USER_AGENT="Your Name you@email.com"
HEADERS = {"User-Agent": os.environ.get("SEC_USER_AGENT", "Your Name your.email@example.com")}
ROOT = Path(__file__).parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "out"
for p in (RAW, OUT):
    p.mkdir(parents=True, exist_ok=True)
FIRST_PORTFOLIO_QUARTER = "2021-03-31"   # fund commenced operations Jan 2021; earlier filings are pre-launch (verify)
