import re


# -------------------- Dataset Metadata --------------------
dataset_metadata = {
    "file_name_pattern": "/**/conn.log.labeled",
    "file_header": (
        "ts uid id.orig_h id.orig_p id.resp_h id.resp_p "
        "proto service duration orig_bytes resp_bytes conn_state "
        "local_orig local_resp missed_bytes history orig_pkts "
        "orig_ip_bytes resp_pkts resp_ip_bytes tunnel_parents "
        "label detailed-label\n"
    ),
    "all_columns": [
        "ts", "uid", "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p",
        "proto", "service", "duration", "orig_bytes", "resp_bytes",
        "conn_state", "local_orig", "local_resp", "missed_bytes",
        "history", "orig_pkts", "orig_ip_bytes", "resp_pkts",
        "resp_ip_bytes", "tunnel_parents", "label", "detailed-label"
    ],
    "numeric_columns": [
        "duration", "orig_bytes", "resp_bytes", "missed_bytes",
        "local_orig", "local_resp", "orig_pkts", "orig_ip_bytes",
        "resp_pkts", "resp_ip_bytes"
    ],
}


# -------------------- Data Cleaning Rules --------------------
data_cleanup = {
    "target_column": "detailed-label",
    "drop_columns": ["ts", "uid", "label"],
    "missing_value_replacements": {
        "-": 0
    },
    "class_labels": {
        0: "Benign",
        1: "Attack",
        2: "CommandAndControl",
        3: "DDoS",
        4: "Malware",
        5: "PortScan"
    },
    "categorical_encodings": {
        "proto": {"icmp": 0, "tcp": 1, "udp": 2},
        "conn_state": {
            "S0": 0, "S1": 1, "SF": 2, "REJ": 3,
            "RSTO": 4, "RSTR": 5, "OTH": 6
        },
        "service": {
            "-": 0, "dns": 1, "http": 2, "ssh": 3,
            "ssl": 4, "dhcp": 5
        }
    }
}


# -------------------- Feature Sets (RENAMED & SIMPLIFIED) --------------------
feature_sets = {
    "basic_net_features": {
        "description": "Basic network-level traffic features",
        "features": [
            "id.orig_p", "id.resp_p", "proto", "service",
            "duration", "orig_bytes", "resp_bytes",
            "conn_state", "orig_pkts", "resp_pkts",
            "detailed-label"
        ]
    },

    "statistical_features": {
        "description": "Extended statistical traffic features",
        "features": [
            "id.orig_h", "id.orig_p", "id.resp_h", "id.resp_p",
            "proto", "service", "duration",
            "orig_bytes", "resp_bytes", "missed_bytes",
            "orig_pkts", "orig_ip_bytes",
            "resp_pkts", "resp_ip_bytes",
            "detailed-label"
        ]
    }
}


# -------------------- Dataset Configuration --------------------
datasets = {
    "scenario_1": [
        "Benign.csv",
        "DDoS.csv"
    ],
    "scenario_2": [
        "Benign.csv",
        "Malware.csv",
        "PortScan.csv"
    ]
}


# -------------------- Sampling Utility --------------------
def get_data_sample(dataset_name: str, rows_per_dataset_file: int = 100_000):
    """
    Returns configuration for sampling a subset of the dataset
    """
    return {
        "name": dataset_name,
        "files": datasets.get(dataset_name, []),
        "rows_per_file": rows_per_dataset_file,
        "output_file": f"{dataset_name}_sample.csv",
        "clean_file": f"{dataset_name}_clean.csv"
    }


# -------------------- File Helpers --------------------
def get_train_file_path(base_path: str) -> str:
    return f"{base_path}_train.csv"


def get_test_file_path(base_path: str) -> str:
    return f"{base_path}_test.csv"


# -------------------- Text Formatting --------------------
def format_line(line: str, separator: str = ",") -> str:
    line = _replace_whitespace(line, separator)
    return line.rstrip(separator) + "\n"


def _replace_whitespace(text: str, replace_with: str = ",") -> str:
    return re.sub(r"\s+", replace_with, text)


# -------------------- Label Decoding --------------------
def decode_label(label_id: int) -> str:
    return data_cleanup["class_labels"].get(label_id, "Unknown")
