from typing import Optional, Self, Union

from torch._dynamo.source import Source
from torch._dynamo.variables.base import VariableTracker

from . import compiled_autograd, eval_frame, guards  # noqa: F401

class VariableTrackerCache:
    def lookup(self, value: object, source: Source) -> Optional[VariableTracker]: ...
    def add(self, value: object, source: Source, vt: VariableTracker) -> None: ...
    def clone(self) -> Self: ...
    def clear(self) -> None: ...

def strip_function_call(name: str) -> str: ...
def is_valid_var_name(name: str) -> Union[bool, int]: ...
