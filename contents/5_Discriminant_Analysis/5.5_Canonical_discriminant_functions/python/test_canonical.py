import os
import runpy


def test_canonical_runs():
    path = os.path.join(os.path.dirname(__file__), "canonical_practice.py")
    runpy.run_path(path, run_name="__main__")
