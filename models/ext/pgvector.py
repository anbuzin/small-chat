#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std
from ..__variants__.ext import pgvector as base

from gel.models.pydantic import (
    AnnotatedExpr,
    FuncCall,
    SchemaPath,
    Unspecified,
    dispatch_overload
)

from builtins import dict, list, str
from typing import Any, TYPE_CHECKING, overload

if TYPE_CHECKING:

    from .. import std as ___std__

    from gel.models.pydantic import GelType

    import builtins as builtins
    import typing as typing
    from builtins import type



#
# type ext::pgvector::Config
#
class Config(base.Config, cfg.ExtensionConfig):
    probes: std.int64
    ef_search: std.int64
@overload
def euclidean_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[vector],
    b: type[vector],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::euclidean_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def euclidean_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[halfvec],
    b: type[halfvec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::euclidean_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def euclidean_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[sparsevec],
    b: type[sparsevec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::euclidean_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def euclidean_distance(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[GelType]:
    return dispatch_overload(euclidean_distance, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def neg_inner_product(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[vector],
    b: type[vector],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::neg_inner_product",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def neg_inner_product(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[halfvec],
    b: type[halfvec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::neg_inner_product",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def neg_inner_product(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[sparsevec],
    b: type[sparsevec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::neg_inner_product",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def neg_inner_product(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[GelType]:
    return dispatch_overload(neg_inner_product, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def cosine_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[vector],
    b: type[vector],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::cosine_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def cosine_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[halfvec],
    b: type[halfvec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::cosine_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def cosine_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[sparsevec],
    b: type[sparsevec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::cosine_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def cosine_distance(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(cosine_distance, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def taxicab_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[vector],
    b: type[vector],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::taxicab_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def taxicab_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[halfvec],
    b: type[halfvec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::taxicab_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def taxicab_distance(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[sparsevec],
    b: type[sparsevec],
) -> type[___std__.float64]:
    args: list[Any] = [a, b]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::taxicab_distance",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def taxicab_distance(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(taxicab_distance, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def euclidean_norm(a: type[vector]) -> type[___std__.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [a]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::euclidean_norm",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def euclidean_norm(a: type[halfvec]) -> type[___std__.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [a]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::euclidean_norm",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def euclidean_norm(a: type[sparsevec]) -> type[___std__.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [a]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.float64,
        FuncCall(
            fname="ext::pgvector::euclidean_norm",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def euclidean_norm(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(euclidean_norm, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def l2_normalize(a: type[vector]) -> type[vector]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [a]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        vector,
        FuncCall(
            fname="ext::pgvector::l2_normalize",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('ext', 'pgvector', 'vector'),
        )
    )

@overload
def l2_normalize(a: type[halfvec]) -> type[halfvec]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [a]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        halfvec,
        FuncCall(
            fname="ext::pgvector::l2_normalize",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('ext', 'pgvector', 'halfvec'),
        )
    )

@overload
def l2_normalize(a: type[sparsevec]) -> type[sparsevec]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [a]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        sparsevec,
        FuncCall(
            fname="ext::pgvector::l2_normalize",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('ext', 'pgvector', 'sparsevec'),
        )
    )

def l2_normalize(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(l2_normalize, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def subvector(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[vector],
    i: type[___std__.int64],
    len: type[___std__.int64],
) -> type[vector]:
    args: list[Any] = [a, i, len]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        vector,
        FuncCall(
            fname="ext::pgvector::subvector",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('ext', 'pgvector', 'vector'),
        )
    )

@overload
def subvector(  # type: ignore [overload-cannot-match, unused-ignore]
    a: type[halfvec],
    i: type[___std__.int64],
    len: type[___std__.int64],
) -> type[halfvec]:
    args: list[Any] = [a, i, len]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        halfvec,
        FuncCall(
            fname="ext::pgvector::subvector",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('ext', 'pgvector', 'halfvec'),
        )
    )

def subvector(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(subvector, *args, **kwargs)  # type: ignore [no-any-return]

def set_probes(
    num: type[___std__.int64] | builtins.int,
) -> type[___std__.int64]:
    args: list[Any] = [num]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.int64,
        FuncCall(
            fname="ext::pgvector::set_probes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )



from ..__variants__.ext.pgvector import halfvec, sparsevec, vector  # noqa: E402 F403

from builtins import int  # noqa: E402 F403


__all__ = (
    'Config',
    'halfvec',
    'sparsevec',
    'vector',
)
