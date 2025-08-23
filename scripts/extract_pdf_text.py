from pathlib import Path
from pdfminer.high_level import extract_text

src = Path("backup/ma2003b/Beamers/MA2003B_DrJonathanMontalvo_20250821.pdf")
out = Path("build/ma2003b/beamers")
out.mkdir(parents=True, exist_ok=True)
if not src.exists():
    raise SystemExit(f"Source PDF not found: {src}")
text = extract_text(str(src))
with open(out / (src.stem + ".txt"), "w", encoding="utf-8") as f:
    f.write(text)
print(f"Extracted text to: {out / (src.stem + '.txt')}")
