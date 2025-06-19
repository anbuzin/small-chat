#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .default import Chat, Fact, Message, Prompt, Resource

import importlib as importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from . import cfg, default, ext, schema, std, sys

    from builtins import str
    from typing import Any


if not TYPE_CHECKING:
    def __getattr__(name: str) -> Any:
        mods = frozenset(["default", "cfg", "ext", "schema", "std", "sys"])
        if name in mods:
            return importlib.import_module("." + name, __name__)
        e = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(e)


__all__ = (
    'Chat',
    'Fact',
    'Message',
    'Prompt',
    'Resource',
    'cfg',
    'default',
    'ext',
    'schema',
    'std',
    'sys',
)
