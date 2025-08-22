import os
import runpy


def test_basic_discrimination_runs():
    path = os.path.join(os.path.dirname(__file__), "basic_discrimination_practice.py")
    runpy.run_path(path, run_name="__main__")
