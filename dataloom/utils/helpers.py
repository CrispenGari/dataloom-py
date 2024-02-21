from typing import Any


def is_collection(arg: Any) -> bool:
    return isinstance(arg, list) or isinstance(arg, set) or isinstance(arg, tuple)
