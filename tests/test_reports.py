from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from mane_reports import average_rating_report


def test_average_rating_report_basic():
    rows = [
        {"name": "p1", "brand": "apple", "price": "100", "rating": "4.0"},
        {"name": "p2", "brand": "apple", "price": "200", "rating": "5.0"},
        {"name": "p3", "brand": "samsung", "price": "300", "rating": "3.0"},
    ]

    headers, table = average_rating_report(rows)

    assert headers == ["brand", "rating"]
    assert table[0][0] == "apple"
    assert table[0][1] == 4.5
    assert table[1][0] == "samsung"
    assert table[1][1] == 3.0
