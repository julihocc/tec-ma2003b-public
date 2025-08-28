#!/usr/bin/env python3
"""
fetch_kuiper.py

Minimal script to download a public Kuiper CSV and save it as `kuiper.csv`
in the same folder. Minimal dependencies: uses urllib from the standard
library (same pattern as `fetch_invest.py`).

Usage:
    python fetch_kuiper.py

Note: replace the `URL` constant below with your canonical CSV location if
you host the file elsewhere.
"""
import os
import sys
from urllib.request import urlopen

# MPCORB source (bulk orbit file)
MPCORB_URL = "https://minorplanetcenter.net/iau/MPCORB/MPCORB.DAT.gz"


def main():
    import gzip
    import io

    dst = os.path.join(os.path.dirname(__file__), "kuiper.csv")

    try:
        with urlopen(MPCORB_URL, timeout=120) as r:
            gz = r.read()
    except Exception as e:
        print("Failed to download MPCORB:", e, file=sys.stderr)
        return 2

    try:
        raw = gzip.decompress(gz).decode("utf-8", errors="ignore")
    except Exception as e:
        print("Failed to decompress MPCORB:", e, file=sys.stderr)
        return 3

    rows = []
    for line in raw.splitlines():
        line = line.rstrip()
        if not line:
            continue
        parts = line.split()
        # Typical data lines begin with a numeric designation (e.g., '00001' or '2003VB12')
        if len(parts) < 11:
            continue
        # Heuristic: first token starts with digit
        if not parts[0][0].isdigit():
            continue
        try:
            des = parts[0]
            H = parts[1]
            i = parts[7]
            e = parts[8]
            a = parts[10]
            a_f = float(a)
        except Exception:
            continue
        if a_f >= 30.0:
            rows.append({"designation": des, "a": a, "e": e, "i": i, "H": H})

    if not rows:
        print(
            "No Kuiper-like objects found in MPCORB extract; check download/parse.",
            file=sys.stderr,
        )
        return 4

    # Write CSV
    try:
        import pandas as pd

        df = pd.DataFrame(rows)
        df.to_csv(dst, index=False)
    except Exception:
        try:
            with open(dst, "w", encoding="utf-8") as f:
                f.write("designation,a,e,i,H\n")
                for r in rows:
                    f.write(f"{r['designation']},{r['a']},{r['e']},{r['i']},{r['H']}\n")
        except Exception as e:
            print("Failed to write CSV:", e, file=sys.stderr)
            return 5

    print("Saved:", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
