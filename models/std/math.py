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
    dispatch_overload
)

from builtins import dict, list, str
from typing import Any, TYPE_CHECKING, overload

if TYPE_CHECKING:

    from ..__variants__ import std

    from gel.models.pydantic import GelType

    import typing as typing
    from builtins import float, int, type
    from decimal import Decimal


@overload
def lg(x: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::lg",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def lg(x: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::lg",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def lg(x: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::lg",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def lg(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(lg, *args, **kwargs)  # type: ignore [no-any-return]

def log(
    x: type[std.decimal] | Decimal,
    *,
    base: type[std.decimal] | Decimal,
) -> type[std.decimal]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {"base": base}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::log",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def sqrt(x: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::sqrt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def sqrt(x: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::sqrt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def sqrt(x: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::sqrt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

def sqrt(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(sqrt, *args, **kwargs)  # type: ignore [no-any-return]

def abs(x: type[std.anyreal] | Decimal | float | int) -> type[std.anyreal]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.anyreal,
        FuncCall(
            fname="std::math::abs",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anyreal'),
        )
    )

@overload
def ceil(x: type[std.int64]) -> type[std.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.int64,
        FuncCall(
            fname="std::math::ceil",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def ceil(x: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::ceil",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def ceil(x: type[std.bigint]) -> type[std.bigint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bigint,
        FuncCall(
            fname="std::math::ceil",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bigint'),
        )
    )

@overload
def ceil(x: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::ceil",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

def ceil(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(ceil, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def floor(x: type[std.int64]) -> type[std.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.int64,
        FuncCall(
            fname="std::math::floor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def floor(x: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::floor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def floor(x: type[std.bigint]) -> type[std.bigint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bigint,
        FuncCall(
            fname="std::math::floor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bigint'),
        )
    )

@overload
def floor(x: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::floor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

def floor(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(floor, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def ln(x: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::ln",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def ln(x: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::ln",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def ln(x: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::ln",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

def ln(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(ln, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def mean(vals: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::mean",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def mean(vals: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::mean",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def mean(vals: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::mean",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def mean(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(mean, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def stddev(vals: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::stddev",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def stddev(vals: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::stddev",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def stddev(vals: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::stddev",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def stddev(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(stddev, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def stddev_pop(vals: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::stddev_pop",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def stddev_pop(vals: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::stddev_pop",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def stddev_pop(vals: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::stddev_pop",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def stddev_pop(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(stddev_pop, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def var(vals: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::var",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def var(vals: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::var",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def var(vals: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::var",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def var(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(var, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def var_pop(vals: type[std.decimal]) -> type[std.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.decimal,
        FuncCall(
            fname="std::math::var_pop",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def var_pop(vals: type[std.int64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::var_pop",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def var_pop(vals: type[std.float64]) -> type[std.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::var_pop",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def var_pop(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(var_pop, *args, **kwargs)  # type: ignore [no-any-return]

def pi() -> type[std.float64]:
    args: list[Any] = []
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::pi",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def acos(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::acos",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def asin(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::asin",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def atan(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::atan",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def atan2(
    y: type[std.float64] | float,
    x: type[std.float64] | float,
) -> type[std.float64]:
    args: list[Any] = [y, x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::atan2",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def cos(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::cos",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def cot(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::cot",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def sin(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::sin",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def tan(x: type[std.float64] | float) -> type[std.float64]:
    args: list[Any] = [x]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::math::tan",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )



from ..__variants__ import std as ___std__  # noqa: E402 F403
