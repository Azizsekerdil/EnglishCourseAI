import os
import tempfile
from pathlib import Path

TEST_HOME = Path(tempfile.mkdtemp(prefix="eca-tests-"))
os.environ["ECA_HOME"] = str(TEST_HOME)
