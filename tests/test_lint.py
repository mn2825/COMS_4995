import sys
from pylint import lint
import pytest

def test_lint():
    threshold = 5
    if len(sys.argv) < 2:
        raise ArgumentError("Fix input args")
    run = lint.Run(['--disable=C0103,W0621,C0200,R0912,R0915',sys.argv[2]], do_exit=False)
    score = run.linter.stats['global_note']
    print("SCORE: ", score)
    if score < threshold:
        pytest.fail("{}".format("Pylint score below threshold."))
