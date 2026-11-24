set -e
cd "$(dirname "$0")"
.venv/bin/jupyter nbconvert --to notebook --execute --inplace AMS-553-Simulation-and-Modeling/data.ipynb
.venv/bin/python AMS-553-Simulation-and-Modeling/FraudProb.py
.venv/bin/jupyter nbconvert --to notebook --execute --inplace AMS-553-Simulation-and-Modeling/queue_plots.ipynb
