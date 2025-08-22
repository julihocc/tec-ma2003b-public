import os
import runpy


def test_coding_software_runs():
    path = os.path.join(os.path.dirname(__file__), 'coding_software_practice.py')
    runpy.run_path(path, run_name='__main__')
