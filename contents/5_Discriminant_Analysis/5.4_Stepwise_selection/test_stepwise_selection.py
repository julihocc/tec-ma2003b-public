import os
import runpy


def test_stepwise_selection_runs():
    path = os.path.join(os.path.dirname(__file__), 'stepwise_selection_practice.py')
    runpy.run_path(path, run_name='__main__')
