import os
import runpy


def test_discrimination_two_populations_runs():
    path = os.path.join(os.path.dirname(__file__), 'discrimination_two_populations_practice.py')
    # should run without raising
    runpy.run_path(path, run_name='__main__')
