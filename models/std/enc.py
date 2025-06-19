#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from gel.models.pydantic import (
    AnnotatedExpr,
    FuncCall,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

from builtins import dict, list, str
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:

    from ..__variants__ import std
    from ..__variants__.std import enc as base

    import builtins as builtins
    from builtins import bool, bytes, type


def base64_encode(
    data: type[std.bytes] | bytes,
    *,
    alphabet: type[base.Base64Alphabet] | str | UnspecifiedType = Unspecified,
    padding: type[std.bool] | bool | UnspecifiedType = Unspecified,
) -> type[std.str]:
    args: list[Any] = [data]
    kw: dict[str, Any] = {"alphabet": alphabet, "padding": padding}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.str,
        FuncCall(
            fname="std::enc::base64_encode",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def base64_decode(
    data: type[std.str] | builtins.str,
    *,
    alphabet: type[base.Base64Alphabet] | str | UnspecifiedType = Unspecified,
    padding: type[std.bool] | bool | UnspecifiedType = Unspecified,
) -> type[std.bytes]:
    args: list[Any] = [data]
    kw: dict[str, Any] = {"alphabet": alphabet, "padding": padding}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bytes,
        FuncCall(
            fname="std::enc::base64_decode",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )



from ..__variants__ import std as ___std__  # noqa: E402 F403
from ..__variants__.std.enc import Base64Alphabet  # noqa: E402 F403


__all__ = (
    'Base64Alphabet',
)
