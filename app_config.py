import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories (kept relative for portability)
DATA_DIR = os.path.join(BASE_DIR, "data")

iot23_scenarios_dir = os.path.join(DATA_DIR, "scenarios")
iot23_attacks_dir = os.path.join(DATA_DIR, "attacks")
iot23_data_dir = os.path.join(DATA_DIR, "processed")
iot23_experiments_dir = os.path.join(BASE_DIR, "experiments")
