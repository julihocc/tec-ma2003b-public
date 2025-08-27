#!/usr/bin/env python3
"""
fetch_invest.py

Minimal script to download a public EuStockMarkets CSV and save it as
`invest.csv` in the same folder. Very small and explicit: no extra
dependencies, uses urllib from the standard library.

Usage:
    python fetch_invest.py

"""
import os
import sys
from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/EuStockMarkets.csv"


def main():
    dst = os.path.join(os.path.dirname(__file__), "invest.csv")
    try:
        with urlopen(URL) as r:
            data = r.read()
    except Exception as e:
        print("Download failed:", e, file=sys.stderr)
        return 2

    try:
        with open(dst, "wb") as f:
            f.write(data)
    except Exception as e:
        print("Write failed:", e, file=sys.stderr)
        return 3

    print("Saved:", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
