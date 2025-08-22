import os
import runpy


def test_costs_priors_runs():
    path = os.path.join(os.path.dirname(__file__), 'costs_priors_practice.py')
    runpy.run_path(path, run_name='__main__')
