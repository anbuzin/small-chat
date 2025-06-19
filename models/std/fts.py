#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from gel.models.pydantic import (
    AnnotatedExpr,
    Array,
    FuncCall,
    GelModel,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as builtins
from builtins import dict, list
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:

    from ..__variants__ import std
    from ..__variants__.std import fts as base
    from .__types__ import ObjectScore_Tuple_wT628Q

    from builtins import float, str, type


def with_options(
    text: type[std.str] | str,
    *,
    language: type[std.anyenum] | str,
    weight_category: type[base.Weight] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.document]:
    args: list[Any] = [text]
    kw: dict[builtins.str, Any] = {
        "language": language,
        "weight_category": weight_category,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.document,
        FuncCall(
            fname="std::fts::with_options",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'fts', 'document'),
        )
    )

def search(
    object: type[GelModel],
    query: type[std.str] | str,
    *,
    language: type[std.str] | str | UnspecifiedType = Unspecified,
    weights: type[Array[std.float64]] | list[float] | None | UnspecifiedType = Unspecified,
) -> type[ObjectScore_Tuple_wT628Q]:
    args: list[Any] = [object, query]
    kw: dict[builtins.str, Any] = {"language": language, "weights": weights}
    return AnnotatedExpr(  # type: ignore [return-value]
        std___types__.ObjectScore_Tuple_wT628Q,
        FuncCall(
            fname="std::fts::search",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<object:anyobject, score:std::float32>'),
        )
    )



from . import __types__ as std___types__  # noqa: E402 F403
from ..__variants__.std import fts as ___base__  # noqa: E402 F403
from ..__variants__.std.fts import (  # noqa: E402 F403
    ElasticLanguage,
    Language,
    LuceneLanguage,
    PGLanguage,
    Weight,
    document
)


__all__ = (
    'ElasticLanguage',
    'Language',
    'LuceneLanguage',
    'PGLanguage',
    'Weight',
    'document',
)
