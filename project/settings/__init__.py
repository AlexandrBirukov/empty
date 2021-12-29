from .settings import *

try:
    from .local import *
except ImportError:
    pass
