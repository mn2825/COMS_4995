import sys
from pylint import lint
import pytest

def test_lint():
    THRESHOLD = 4
    if len(sys.argv) < 2:
        raise ArgumentError("Fix input args")
    run = lint.Run([sys.argv[2]], do_exit=False)
    score = run.linter.stats['global_note']

    if score < THRESHOLD:
        pytest.fail("{}".format("Pylint score below threshold."))
