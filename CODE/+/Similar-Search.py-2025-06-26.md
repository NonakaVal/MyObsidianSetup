```python
import os
import re
import sys
import unicodedata
from pathlib import Path
from difflib import SequenceMatcher

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import MAIN_PATH

```