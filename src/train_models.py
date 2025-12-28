import os
import warnings

import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier

from app_config import attacks_data_dir, processed_data_dir, results_dir
from src.helpers.log_helper import add_logger
from src.helpers.process_helper import run_end_to_end_process
from src.iot23 import get_data_sample, dataset_metadata, feature_sets


# -------------------- Logging --------------------
add_logger(file_name="training.log")


# -------------------- Warning Handling --------------------
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)
warnings.filterwarnings("ignore", category=sklearn.exceptions.ConvergenceWarning)


# -------------------- Directory Setup --------------------
os.makedirs(results_dir, exist_ok=True)

raw_data_dir = attacks_data_dir
processed_dir = processed_data_dir


# -------------------- Dataset Metadata --------------------
file_header = dataset_metadata["file_header"]


# -------------------- Training Data Configuration --------------------
training_samples = [
    get_data_sample(
        dataset_name="scenario_1",
        rows_per_dataset_file=1_000_000
    ),
    get_data_sample(
        dataset_name="scenario_2",
        rows_per_dataset_file=1_000_000
    ),
]


# -------------------- Feature Configuration --------------------
selected_features = [
    feature_sets["basic_net_features"],
    feature_sets["statistical_features"],
]


# -------------------- Model Pipelines --------------------
training_algorithms = {
    "decision_tree": Pipeline([
        ("scaler", StandardScaler()),
        ("model", DecisionTreeClassifier(random_state=42))
    ]),

    "naive_bayes": Pipeline([
        ("scaler", StandardScaler()),
        ("model", GaussianNB())
    ]),

    "logistic_regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),

    "random_forest": Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        ))
    ]),

    "linear_svm": Pipeline([
        ("scaler", MinMaxScaler()),
        ("model", LinearSVC(max_iter=5000))
    ]),
}


# -------------------- Training Execution --------------------
run_end_to_end_process(
    raw_data_dir=raw_data_dir,
    processed_data_dir=processed_dir,
    results_dir=results_dir,
    training_samples=training_samples,
    selected_features=selected_features,
    models=training_algorithms,
    final_report_name="model_comparison_results.xlsx"
)
