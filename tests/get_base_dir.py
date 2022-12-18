
import sys
from pathlib import Path


# Устанавливает базовую директорию на 1 каталог выше уровнем.
sys.path.append(str(Path(sys.argv[0]).parents[1]))
