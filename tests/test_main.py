import pytest
from .. import main
import json


def test_generate_report():
    src = "./tests/test_input.txt"
    expected_output = {
        "invalid_logs": [
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:15 -78C",
            "2023-01-02 01:10"
        ],
        "invalid_logs_percentage": "30.0",
        "report_duration": 120,
        "temperature": {
            "max": "115.3",
            "min": "90.0",
            "average": "102.4"
        },
        "longest_overheating_time": 40,
        "overheating_periods_number": 2,
        "problems": {
            "high_EM_interference_level": True,
            "high_risk_of_engine_damage_due_to_temperature": True
        }
    }

    assert main.generate_report(src) == expected_output


def test_generate_report_empty():
    src = "./tests/test_input_empty.txt"
    expected_output = {
        "invalid_logs": [],
        "invalid_logs_percentage": "100.0",
        "report_duration": 0,
        "temperature": {
            "max": None,
            "min": None,
            "average": None
        },
        "longest_overheating_time": 0,
        "overheating_periods_number": 0,
        "problems": {
            "high_EM_interference_level": False,
            "high_risk_of_engine_damage_due_to_temperature": False
        }
    }

    assert main.generate_report(src) == expected_output


def test_generate_report_single():
    src = "./tests/test_input_single.txt"
    expected_output = {
        "invalid_logs": [],
        "invalid_logs_percentage": "0.0",
        "report_duration": 0,
        "temperature": {
            "max": '90C',
            "min": '90C',
            "average": '90C'
        },
        "longest_overheating_time": 0,
        "overheating_periods_number": 0,
        "problems": {
            "high_EM_interference_level": False,
            "high_risk_of_engine_damage_due_to_temperature": False
        }
    }

    assert main.generate_report(src) == expected_output
