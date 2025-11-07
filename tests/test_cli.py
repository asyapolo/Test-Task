from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from main import main


def test_main_average_rating(tmp_path, capsys):
    csv_content = """name,brand,price,rating
iphone,apple,100,4.0
iphone2,apple,200,5.0
galaxy,samsung,300,3.0
"""
    file_path = tmp_path / "products.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    argv = ["--files", str(file_path), "--report", "average-rating"]
    exit_code = main(argv)

    assert exit_code == 0

    captured = capsys.readouterr()
    out = captured.out

    assert "apple" in out
    assert "4.5" in out          # средний рейтинг apple
    assert "samsung" in out
    assert "|  2 | samsung |      3" in out  # строка с samsung и рейтингом 3
