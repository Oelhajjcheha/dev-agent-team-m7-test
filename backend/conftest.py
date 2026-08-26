import os
import sys

# Ensure the repository root (the parent of this backend/ directory) is on
# sys.path so that `import backend` / `from backend.app import ...` works
# regardless of the current working directory pytest is invoked from.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
