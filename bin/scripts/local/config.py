import os
from pathlib import Path
HOME=Path(os.environ['HOME']) 
config=HOME/".config/bhStash/config.py"
exec(config.read_bytes())
