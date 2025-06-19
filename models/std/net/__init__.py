#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

import importlib as importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from . import http

    from builtins import str
    from typing import Any


if not TYPE_CHECKING:
    def __getattr__(name: str) -> Any:
        mods = frozenset(["http"])
        if name in mods:
            return importlib.import_module("." + name, __name__)
        e = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(e)


from ...__variants__.std.net import RequestFailureKind, RequestState  # noqa: E402 F403


__all__ = (
    'RequestFailureKind',
    'RequestState',
    'http',
)
