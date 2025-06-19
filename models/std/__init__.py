#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

import gel as ___gel__
import gel as gel
from gel.models.pydantic import (
    AnnotatedExpr,
    AnyTuple,
    Array,
    DateTimeLike,
    ExprCompatible,
    FuncCall,
    GelType,
    GelType_T,
    InfixOp,
    MultiRange,
    Range,
    SchemaPath,
    Tuple,
    Unspecified,
    UnspecifiedType,
    dispatch_overload
)

import builtins as ___builtins_3__
import builtins as ___builtins_4__
import builtins as ___builtins__
import datetime as ___datetime_1__
import decimal as ___decimal__
import importlib as importlib
import uuid as ___uuid__
from builtins import dict, list, tuple
from typing import Any, TYPE_CHECKING, overload

if TYPE_CHECKING:

    from . import cal, enc, fts, math, net, pg
    from .. import schema
    from ..__variants__ import cfg, std as base
    from ..__variants__.std import cal as std_cal

    from gel.models import pydantic

    import builtins as builtins
    import builtins as ___builtins_2__
    import builtins as ___builtins_1__
    import datetime as ___datetime__
    import typing as typing
    from builtins import float, int, type
    from datetime import timedelta
    from decimal import Decimal


def assert_single(
    input: type[GelType_T],
    *,
    message: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[GelType_T]:
    args: list[Any] = [input]
    kw: dict[___builtins__.str, Any] = {"message": message}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::assert_single",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

def assert_exists(
    input: type[GelType_T],
    *,
    message: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[GelType_T]:
    args: list[Any] = [input]
    kw: dict[___builtins__.str, Any] = {"message": message}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::assert_exists",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

def assert_distinct(
    input: type[GelType_T],
    *,
    message: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[GelType_T]:
    args: list[Any] = [input]
    kw: dict[___builtins__.str, Any] = {"message": message}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::assert_distinct",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

def assert_(
    input: type[base.bool] | ___builtins_1__.bool,
    *,
    message: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.bool]:
    args: list[Any] = [input]
    kw: dict[___builtins__.str, Any] = {"message": message}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::assert",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def materialized(input: type[GelType_T]) -> type[GelType_T]:
    args: list[Any] = [input]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::materialized",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

@overload
def len(str: type[base.str]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [str]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::len",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def len(bytes: type[base.bytes]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [bytes]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::len",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def len(array: type[Array[GelType_T]]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [array]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::len",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def len(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(len, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def sum(s: type[base.bigint]) -> type[base.bigint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bigint,
        FuncCall(
            fname="std::sum",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bigint'),
        )
    )

@overload
def sum(s: type[base.decimal]) -> type[base.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.decimal,
        FuncCall(
            fname="std::sum",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def sum(s: type[base.int32]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::sum",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def sum(s: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::sum",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def sum(s: type[base.float32]) -> type[base.float32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float32,
        FuncCall(
            fname="std::sum",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float32'),
        )
    )

@overload
def sum(s: type[base.float64]) -> type[base.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::sum",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def sum(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(sum, *args, **kwargs)  # type: ignore [no-any-return]

def count(s: type[GelType_T]) -> type[base.int64]:
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::count",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def random() -> type[base.float64]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::random",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def min(vals: type[GelType_T]) -> type[GelType_T]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

@overload
def min(vals: type[base.anyreal]) -> type[base.anyreal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anyreal,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anyreal'),
        )
    )

@overload
def min(vals: type[base.anyenum]) -> type[base.anyenum]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anyenum,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anyenum'),
        )
    )

@overload
def min(vals: type[base.str]) -> type[base.str]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def min(vals: type[base.datetime]) -> type[base.datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def min(vals: type[base.duration]) -> type[base.duration]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.duration,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'duration'),
        )
    )

@overload
def min(vals: type[std_cal.local_datetime]) -> type[std_cal.local_datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_datetime,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
    )

@overload
def min(vals: type[std_cal.local_date]) -> type[std_cal.local_date]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_date,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

@overload
def min(vals: type[std_cal.local_time]) -> type[std_cal.local_time]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_time,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
    )

@overload
def min(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[std_cal.relative_duration],
) -> type[std_cal.relative_duration]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.relative_duration,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
    )

@overload
def min(vals: type[std_cal.date_duration]) -> type[std_cal.date_duration]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.date_duration,
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
    )

@overload
def min(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.local_datetime]],
) -> type[Array[std_cal.local_datetime]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.local_datetime],
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::local_datetime>'),
        )
    )

@overload
def min(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.local_date]],
) -> type[Array[std_cal.local_date]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.local_date],
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::local_date>'),
        )
    )

@overload
def min(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.local_time]],
) -> type[Array[std_cal.local_time]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.local_time],
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::local_time>'),
        )
    )

@overload
def min(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.relative_duration]],
) -> type[Array[std_cal.relative_duration]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.relative_duration],
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::relative_duration>'),
        )
    )

@overload
def min(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.date_duration]],
) -> type[Array[std_cal.date_duration]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.date_duration],
        FuncCall(
            fname="std::min",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::date_duration>'),
        )
    )

def min(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(min, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def max(vals: type[GelType_T]) -> type[GelType_T]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

@overload
def max(vals: type[base.anyreal]) -> type[base.anyreal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anyreal,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anyreal'),
        )
    )

@overload
def max(vals: type[base.anyenum]) -> type[base.anyenum]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anyenum,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anyenum'),
        )
    )

@overload
def max(vals: type[base.str]) -> type[base.str]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def max(vals: type[base.datetime]) -> type[base.datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def max(vals: type[base.duration]) -> type[base.duration]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.duration,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'duration'),
        )
    )

@overload
def max(vals: type[std_cal.local_datetime]) -> type[std_cal.local_datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_datetime,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
    )

@overload
def max(vals: type[std_cal.local_date]) -> type[std_cal.local_date]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_date,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

@overload
def max(vals: type[std_cal.local_time]) -> type[std_cal.local_time]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_time,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
    )

@overload
def max(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[std_cal.relative_duration],
) -> type[std_cal.relative_duration]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.relative_duration,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
    )

@overload
def max(vals: type[std_cal.date_duration]) -> type[std_cal.date_duration]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.date_duration,
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
    )

@overload
def max(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.local_datetime]],
) -> type[Array[std_cal.local_datetime]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.local_datetime],
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::local_datetime>'),
        )
    )

@overload
def max(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.local_date]],
) -> type[Array[std_cal.local_date]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.local_date],
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::local_date>'),
        )
    )

@overload
def max(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.local_time]],
) -> type[Array[std_cal.local_time]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.local_time],
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::local_time>'),
        )
    )

@overload
def max(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.relative_duration]],
) -> type[Array[std_cal.relative_duration]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.relative_duration],
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::relative_duration>'),
        )
    )

@overload
def max(  # type: ignore [overload-cannot-match, unused-ignore]
    vals: type[Array[std_cal.date_duration]],
) -> type[Array[std_cal.date_duration]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___std_cal__.date_duration],
        FuncCall(
            fname="std::max",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::cal::date_duration>'),
        )
    )

def max(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(max, *args, **kwargs)  # type: ignore [no-any-return]

def all(vals: type[base.bool] | ___builtins_1__.bool) -> type[base.bool]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::all",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def any(vals: type[base.bool] | ___builtins_1__.bool) -> type[base.bool]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::any",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def enumerate(vals: type[GelType_T]) -> type[Tuple[base.int64, GelType_T]]:
    args: list[Any] = [vals]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Tuple[___base__.int64, GelType_T],
        FuncCall(
            fname="std::enumerate",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<std::int64, anytype>'),
        )
    )

@overload
def round(val: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::round",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def round(val: type[base.float64]) -> type[base.float64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::round",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def round(val: type[base.bigint]) -> type[base.bigint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bigint,
        FuncCall(
            fname="std::round",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bigint'),
        )
    )

@overload
def round(val: type[base.decimal]) -> type[base.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.decimal,
        FuncCall(
            fname="std::round",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def round(val: type[base.decimal], d: type[base.int64]) -> type[base.decimal]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, d]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.decimal,
        FuncCall(
            fname="std::round",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

def round(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(round, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[base.str],
    needle: type[base.str],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[base.bytes],
    needle: type[base.bytes],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[Array[GelType_T]],
    needle: type[GelType_T],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[base.json],
    needle: type[base.json],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[Range[base.anypoint]],
    needle: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[Range[base.anypoint]],
    needle: type[base.anypoint],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[MultiRange[base.anypoint]],
    needle: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[MultiRange[base.anypoint]],
    needle: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[MultiRange[base.anypoint]],
    needle: type[base.anypoint],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[Range[std_cal.local_date]],
    needle: type[std_cal.local_date],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def contains(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[MultiRange[std_cal.local_date]],
    needle: type[std_cal.local_date],
) -> type[base.bool]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::contains",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def contains(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(contains, *args, **kwargs)  # type: ignore [no-any-return]

def array_fill(
    val: type[GelType_T],
    n: type[base.int64] | int,
) -> type[Array[GelType_T]]:
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[GelType_T],
        FuncCall(
            fname="std::array_fill",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<anytype>'),
        )
    )

@overload
def find(haystack: type[base.str], needle: type[base.str]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::find",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def find(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[base.bytes],
    needle: type[base.bytes],
) -> type[base.int64]:
    args: list[Any] = [haystack, needle]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::find",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def find(  # type: ignore [overload-cannot-match, unused-ignore]
    haystack: type[Array[GelType_T]],
    needle: type[GelType_T],
    from_pos: type[base.int64] | UnspecifiedType = Unspecified,
) -> type[base.int64]:
    args: list[Any] = [haystack, needle, from_pos]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::find",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def find(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(find, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_and(l: type[base.int16], r: type[base.int16]) -> type[base.int16]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::bit_and",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def bit_and(l: type[base.int32], r: type[base.int32]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::bit_and",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def bit_and(l: type[base.int64], r: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_and",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_and(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(bit_and, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_or(l: type[base.int16], r: type[base.int16]) -> type[base.int16]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::bit_or",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def bit_or(l: type[base.int32], r: type[base.int32]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::bit_or",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def bit_or(l: type[base.int64], r: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_or",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_or(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(bit_or, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_xor(l: type[base.int16], r: type[base.int16]) -> type[base.int16]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::bit_xor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def bit_xor(l: type[base.int32], r: type[base.int32]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::bit_xor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def bit_xor(l: type[base.int64], r: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_xor",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_xor(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(bit_xor, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_not(r: type[base.int16]) -> type[base.int16]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::bit_not",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def bit_not(r: type[base.int32]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::bit_not",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def bit_not(r: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_not",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_not(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(bit_not, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_rshift(val: type[base.int16], n: type[base.int64]) -> type[base.int16]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::bit_rshift",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def bit_rshift(val: type[base.int32], n: type[base.int64]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::bit_rshift",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def bit_rshift(val: type[base.int64], n: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_rshift",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_rshift(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(bit_rshift, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_lshift(val: type[base.int16], n: type[base.int64]) -> type[base.int16]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::bit_lshift",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def bit_lshift(val: type[base.int32], n: type[base.int64]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::bit_lshift",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def bit_lshift(val: type[base.int64], n: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_lshift",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_lshift(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(bit_lshift, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bit_count(val: type[base.int16]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_count",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def bit_count(val: type[base.int32]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_count",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def bit_count(val: type[base.int64]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_count",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def bit_count(bytes: type[base.bytes]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [bytes]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bit_count",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def bit_count(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(bit_count, *args, **kwargs)  # type: ignore [no-any-return]

def array_agg(s: type[GelType_T]) -> type[Array[GelType_T]]:
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[GelType_T],
        FuncCall(
            fname="std::array_agg",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<anytype>'),
        )
    )

def array_unpack(
    array: type[Array[GelType_T]] | list[GelType_T],
) -> type[GelType_T]:
    args: list[Any] = [array]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::array_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

def array_replace(
    array: type[Array[GelType_T]] | list[GelType_T],
    old: type[GelType_T],
    new: type[GelType_T],
) -> type[Array[GelType_T]]:
    args: list[Any] = [array, old, new]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[GelType_T],
        FuncCall(
            fname="std::array_replace",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<anytype>'),
        )
    )

def array_get(
    array: type[Array[GelType_T]] | list[GelType_T],
    idx: type[base.int64] | int,
    *,
    default: type[GelType_T] | None | UnspecifiedType = Unspecified,
) -> type[GelType_T]:
    args: list[Any] = [array, idx]
    kw: dict[___builtins__.str, Any] = {"default": default}
    return AnnotatedExpr(  # type: ignore [return-value]
        GelType,
        FuncCall(
            fname="std::array_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('anytype'),
        )
    )

def array_set(
    array: type[Array[GelType_T]] | list[GelType_T],
    idx: type[base.int64] | int,
    val: type[GelType_T],
) -> type[Array[GelType_T]]:
    args: list[Any] = [array, idx, val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[GelType_T],
        FuncCall(
            fname="std::array_set",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<anytype>'),
        )
    )

def array_insert(
    array: type[Array[GelType_T]] | list[GelType_T],
    idx: type[base.int64] | int,
    val: type[GelType_T],
) -> type[Array[GelType_T]]:
    args: list[Any] = [array, idx, val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[GelType_T],
        FuncCall(
            fname="std::array_insert",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<anytype>'),
        )
    )

@overload
def array_join(  # type: ignore [overload-cannot-match, unused-ignore]
    array: type[Array[base.str]],
    delimiter: type[base.str],
) -> type[base.str]:
    args: list[Any] = [array, delimiter]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::array_join",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def array_join(  # type: ignore [overload-cannot-match, unused-ignore]
    array: type[Array[base.bytes]],
    delimiter: type[base.bytes],
) -> type[base.bytes]:
    args: list[Any] = [array, delimiter]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::array_join",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

def array_join(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(array_join, *args, **kwargs)  # type: ignore [no-any-return]

def bytes_get_bit(
    bytes: type[base.bytes] | ___builtins_2__.bytes,
    num: type[base.int64] | int,
) -> type[base.int64]:
    args: list[Any] = [bytes, num]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::bytes_get_bit",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def datetime_current() -> type[base.datetime]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::datetime_current",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

def datetime_of_transaction() -> type[base.datetime]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::datetime_of_transaction",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

def datetime_of_statement() -> type[base.datetime]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::datetime_of_statement",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def datetime_get(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[base.datetime],
    el: type[base.str],
) -> type[base.float64]:
    args: list[Any] = [dt, el]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::datetime_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def datetime_get(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std_cal.local_datetime],
    el: type[base.str],
) -> type[base.float64]:
    args: list[Any] = [dt, el]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::datetime_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def datetime_get(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(datetime_get, *args, **kwargs)  # type: ignore [no-any-return]

def datetime_truncate(
    dt: type[base.datetime] | ___datetime__.datetime,
    unit: type[base.str] | builtins.str,
) -> type[base.datetime]:
    args: list[Any] = [dt, unit]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::datetime_truncate",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

def str_pad_start(
    s: type[base.str] | builtins.str,
    n: type[base.int64] | int,
    fill: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, n, fill]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_pad_start",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_lpad(
    s: type[base.str] | builtins.str,
    n: type[base.int64] | int,
    fill: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, n, fill]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_lpad",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def duration_get(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[base.duration],
    el: type[base.str],
) -> type[base.float64]:
    args: list[Any] = [dt, el]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::duration_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def duration_get(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std_cal.date_duration],
    el: type[base.str],
) -> type[base.float64]:
    args: list[Any] = [dt, el]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::duration_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def duration_get(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std_cal.relative_duration],
    el: type[base.str],
) -> type[base.float64]:
    args: list[Any] = [dt, el]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::duration_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def duration_get(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(duration_get, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def duration_truncate(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[base.duration],
    unit: type[base.str],
) -> type[base.duration]:
    args: list[Any] = [dt, unit]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.duration,
        FuncCall(
            fname="std::duration_truncate",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'duration'),
        )
    )

@overload
def duration_truncate(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std_cal.date_duration],
    unit: type[base.str],
) -> type[std_cal.date_duration]:
    args: list[Any] = [dt, unit]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.date_duration,
        FuncCall(
            fname="std::duration_truncate",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
    )

@overload
def duration_truncate(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std_cal.relative_duration],
    unit: type[base.str],
) -> type[std_cal.relative_duration]:
    args: list[Any] = [dt, unit]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.relative_duration,
        FuncCall(
            fname="std::duration_truncate",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
    )

def duration_truncate(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(duration_truncate, *args, **kwargs)  # type: ignore [no-any-return]

def duration_to_seconds(
    dur: type[base.duration] | timedelta,
) -> type[base.decimal]:
    args: list[Any] = [dur]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.decimal,
        FuncCall(
            fname="std::duration_to_seconds",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

def json_typeof(json: type[base.json] | builtins.str) -> type[base.str]:
    args: list[Any] = [json]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::json_typeof",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def json_array_unpack(
    array: type[base.json] | builtins.str,
) -> type[base.json]:
    args: list[Any] = [array]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.json,
        FuncCall(
            fname="std::json_array_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )

def json_object_unpack(
    obj: type[base.json] | builtins.str,
) -> type[Tuple[base.str, base.json]]:
    args: list[Any] = [obj]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Tuple[___base__.str, ___base__.json],
        FuncCall(
            fname="std::json_object_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<std::str, std::json>'),
        )
    )

def json_object_pack(
    pairs: type[Tuple[base.str, base.json]] | tuple[builtins.str, builtins.str],
) -> type[base.json]:
    args: list[Any] = [pairs]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.json,
        FuncCall(
            fname="std::json_object_pack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )

def json_get(
    json: type[base.json] | builtins.str,
    default: type[base.json] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.json]:
    args: list[Any] = [json]
    kw: dict[___builtins__.str, Any] = {"default": default}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.json,
        FuncCall(
            fname="std::json_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )

def json_set(
    target: type[base.json] | builtins.str,
    value: type[base.json] | builtins.str | None,
    create_if_missing: type[base.bool] | ___builtins_1__.bool | UnspecifiedType = Unspecified,
    empty_treatment: type[base.JsonEmpty] | ___builtins__.str | UnspecifiedType = Unspecified,
) -> type[base.json]:
    args: list[Any] = [target]
    kw: dict[___builtins__.str, Any] = {
        "value": value,
        "create_if_missing": create_if_missing,
        "empty_treatment": empty_treatment,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.json,
        FuncCall(
            fname="std::json_set",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )

def re_match(
    pattern: type[base.str] | builtins.str,
    str: type[base.str] | builtins.str,
) -> type[Array[base.str]]:
    args: list[Any] = [pattern, str]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___base__.str],
        FuncCall(
            fname="std::re_match",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::str>'),
        )
    )

def re_match_all(
    pattern: type[base.str] | builtins.str,
    str: type[base.str] | builtins.str,
) -> type[Array[base.str]]:
    args: list[Any] = [pattern, str]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___base__.str],
        FuncCall(
            fname="std::re_match_all",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::str>'),
        )
    )

def re_test(
    pattern: type[base.str] | builtins.str,
    str: type[base.str] | builtins.str,
) -> type[base.bool]:
    args: list[Any] = [pattern, str]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::re_test",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def re_replace(
    pattern: type[base.str] | builtins.str,
    sub: type[base.str] | builtins.str,
    str: type[base.str] | builtins.str,
    *,
    flags: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [pattern, sub, str]
    kw: dict[___builtins__.str, Any] = {"flags": flags}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::re_replace",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_repeat(
    s: type[base.str] | builtins.str,
    n: type[base.int64] | int,
) -> type[base.str]:
    args: list[Any] = [s, n]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_repeat",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_lower(s: type[base.str] | builtins.str) -> type[base.str]:
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_lower",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_upper(s: type[base.str] | builtins.str) -> type[base.str]:
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_upper",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_title(s: type[base.str] | builtins.str) -> type[base.str]:
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_title",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_pad_end(
    s: type[base.str] | builtins.str,
    n: type[base.int64] | int,
    fill: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, n, fill]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_pad_end",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_rpad(
    s: type[base.str] | builtins.str,
    n: type[base.int64] | int,
    fill: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, n, fill]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_rpad",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_trim_start(
    s: type[base.str] | builtins.str,
    tr: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, tr]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_trim_start",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_ltrim(
    s: type[base.str] | builtins.str,
    tr: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, tr]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_ltrim",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_trim_end(
    s: type[base.str] | builtins.str,
    tr: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, tr]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_trim_end",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_rtrim(
    s: type[base.str] | builtins.str,
    tr: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, tr]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_rtrim",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_trim(
    s: type[base.str] | builtins.str,
    tr: type[base.str] | builtins.str | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [s, tr]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_trim",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_split(
    s: type[base.str] | builtins.str,
    delimiter: type[base.str] | builtins.str,
) -> type[Array[base.str]]:
    args: list[Any] = [s, delimiter]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Array[___base__.str],
        FuncCall(
            fname="std::str_split",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('array<std::str>'),
        )
    )

def str_replace(
    s: type[base.str] | builtins.str,
    old: type[base.str] | builtins.str,
    new: type[base.str] | builtins.str,
) -> type[base.str]:
    args: list[Any] = [s, old, new]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_replace",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def str_reverse(s: type[base.str] | builtins.str) -> type[base.str]:
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::str_reverse",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def uuid_generate_v1mc() -> type[base.uuid]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.uuid,
        FuncCall(
            fname="std::uuid_generate_v1mc",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'uuid'),
        )
    )

def uuid_generate_v4() -> type[base.uuid]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.uuid,
        FuncCall(
            fname="std::uuid_generate_v4",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'uuid'),
        )
    )

def range(
    lower: type[base.anypoint] | Decimal | ___datetime__.datetime | float | int | timedelta | None | UnspecifiedType = Unspecified,
    upper: type[base.anypoint] | Decimal | ___datetime__.datetime | float | int | timedelta | None | UnspecifiedType = Unspecified,
    *,
    inc_lower: type[base.bool] | ___builtins_1__.bool | UnspecifiedType = Unspecified,
    inc_upper: type[base.bool] | ___builtins_1__.bool | UnspecifiedType = Unspecified,
    empty: type[base.bool] | ___builtins_1__.bool | UnspecifiedType = Unspecified,
) -> type[Range[base.anypoint]]:
    args: list[Any] = [lower, upper]
    kw: dict[___builtins__.str, Any] = {
        "inc_lower": inc_lower,
        "inc_upper": inc_upper,
        "empty": empty,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.anypoint],
        FuncCall(
            fname="std::range",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::anypoint>'),
        )
    )

def multirange(
    ranges: type[Array[Range[base.anypoint]]] | list[gel.Range[Decimal | ___datetime__.datetime | float | int | timedelta]],
) -> type[MultiRange[base.anypoint]]:
    args: list[Any] = [ranges]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        MultiRange[___base__.anypoint],
        FuncCall(
            fname="std::multirange",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('multirange<std::anypoint>'),
        )
    )

@overload
def range_is_empty(val: type[Range[base.anypoint]]) -> type[base.bool]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::range_is_empty",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def range_is_empty(val: type[MultiRange[base.anypoint]]) -> type[base.bool]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::range_is_empty",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def range_is_empty(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(range_is_empty, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def range_unpack(val: type[Range[base.int32]]) -> type[base.int32]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[base.int32]],
    step: type[base.int32],
) -> type[base.int32]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def range_unpack(val: type[Range[base.int64]]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[base.int64]],
    step: type[base.int64],
) -> type[base.int64]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[base.float32]],
    step: type[base.float32],
) -> type[base.float32]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float32,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float32'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[base.float64]],
    step: type[base.float64],
) -> type[base.float64]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[base.decimal]],
    step: type[base.decimal],
) -> type[base.decimal]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.decimal,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[base.datetime]],
    step: type[base.duration],
) -> type[base.datetime]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[std_cal.local_datetime]],
    step: type[std_cal.relative_duration],
) -> type[std_cal.local_datetime]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_datetime,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[std_cal.local_date]],
) -> type[std_cal.local_date]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_date,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

@overload
def range_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[Range[std_cal.local_date]],
    step: type[std_cal.date_duration],
) -> type[std_cal.local_date]:
    args: list[Any] = [val, step]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_cal__.local_date,
        FuncCall(
            fname="std::range_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

def range_unpack(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(range_unpack, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def range_get_upper(r: type[Range[base.anypoint]]) -> type[base.anypoint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anypoint,
        FuncCall(
            fname="std::range_get_upper",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anypoint'),
        )
    )

@overload
def range_get_upper(r: type[MultiRange[base.anypoint]]) -> type[base.anypoint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anypoint,
        FuncCall(
            fname="std::range_get_upper",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anypoint'),
        )
    )

def range_get_upper(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(range_get_upper, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def range_get_lower(r: type[Range[base.anypoint]]) -> type[base.anypoint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anypoint,
        FuncCall(
            fname="std::range_get_lower",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anypoint'),
        )
    )

@overload
def range_get_lower(r: type[MultiRange[base.anypoint]]) -> type[base.anypoint]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.anypoint,
        FuncCall(
            fname="std::range_get_lower",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'anypoint'),
        )
    )

def range_get_lower(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(range_get_lower, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def range_is_inclusive_upper(r: type[Range[base.anypoint]]) -> type[base.bool]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::range_is_inclusive_upper",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def range_is_inclusive_upper(  # type: ignore [overload-cannot-match, unused-ignore]
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::range_is_inclusive_upper",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def range_is_inclusive_upper(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(range_is_inclusive_upper, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def range_is_inclusive_lower(r: type[Range[base.anypoint]]) -> type[base.bool]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::range_is_inclusive_lower",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def range_is_inclusive_lower(  # type: ignore [overload-cannot-match, unused-ignore]
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::range_is_inclusive_lower",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def range_is_inclusive_lower(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(range_is_inclusive_lower, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def overlaps(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[Range[base.anypoint]],
    r: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::overlaps",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def overlaps(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[MultiRange[base.anypoint]],
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::overlaps",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def overlaps(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(overlaps, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[base.int32]],
) -> type[Range[base.int32]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.int32],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::int32>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[base.int64]],
) -> type[Range[base.int64]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.int64],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::int64>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[base.float32]],
) -> type[Range[base.float32]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.float32],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::float32>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[base.float64]],
) -> type[Range[base.float64]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.float64],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::float64>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[base.decimal]],
) -> type[Range[base.decimal]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.decimal],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::decimal>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[base.datetime]],
) -> type[Range[base.datetime]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___base__.datetime],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::datetime>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[std_cal.local_datetime]],
) -> type[Range[std_cal.local_datetime]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___std_cal__.local_datetime],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::cal::local_datetime>'),
        )
    )

@overload
def multirange_unpack(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[MultiRange[std_cal.local_date]],
) -> type[Range[std_cal.local_date]]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Range[___std_cal__.local_date],
        FuncCall(
            fname="std::multirange_unpack",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('range<std::cal::local_date>'),
        )
    )

def multirange_unpack(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(multirange_unpack, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def strictly_below(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[Range[base.anypoint]],
    r: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::strictly_below",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def strictly_below(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[MultiRange[base.anypoint]],
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::strictly_below",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def strictly_below(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(strictly_below, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def strictly_above(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[Range[base.anypoint]],
    r: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::strictly_above",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def strictly_above(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[MultiRange[base.anypoint]],
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::strictly_above",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def strictly_above(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(strictly_above, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bounded_above(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[Range[base.anypoint]],
    r: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::bounded_above",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def bounded_above(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[MultiRange[base.anypoint]],
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::bounded_above",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def bounded_above(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(bounded_above, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def bounded_below(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[Range[base.anypoint]],
    r: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::bounded_below",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def bounded_below(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[MultiRange[base.anypoint]],
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::bounded_below",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def bounded_below(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(bounded_below, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def adjacent(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[Range[base.anypoint]],
    r: type[Range[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::adjacent",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

@overload
def adjacent(  # type: ignore [overload-cannot-match, unused-ignore]
    l: type[MultiRange[base.anypoint]],
    r: type[MultiRange[base.anypoint]],
) -> type[base.bool]:
    args: list[Any] = [l, r]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bool,
        FuncCall(
            fname="std::adjacent",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bool'),
        )
    )

def adjacent(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(adjacent, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[base.datetime],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [dt, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    td: type[base.duration],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [td, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    i: type[base.int64],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [i, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    f: type[base.float64],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [f, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    d: type[base.bigint],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [d, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    d: type[base.decimal],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [d, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    array: type[Array[base.str]],
    delimiter: type[base.str],
) -> type[base.str]:
    args: list[Any] = [array, delimiter]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    json: type[base.json],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [json, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(b: type[base.bytes]) -> type[base.str]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [b]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std_cal.local_datetime],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [dt, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    d: type[std_cal.local_date],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [d, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    nt: type[std_cal.local_time],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [nt, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def to_str(  # type: ignore [overload-cannot-match, unused-ignore]
    rd: type[std_cal.relative_duration],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.str]:
    args: list[Any] = [rd, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.str,
        FuncCall(
            fname="std::to_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def to_str(*args: typing.Any, **kwargs: typing.Any) -> type[pydantic.GelType]:
    return dispatch_overload(to_str, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def to_bytes(s: type[base.str]) -> type[base.bytes]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [s]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::to_bytes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def to_bytes(j: type[base.json]) -> type[base.bytes]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [j]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::to_bytes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def to_bytes(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[base.int16],
    endian: type[base.Endian],
) -> type[base.bytes]:
    args: list[Any] = [val, endian]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::to_bytes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def to_bytes(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[base.int32],
    endian: type[base.Endian],
) -> type[base.bytes]:
    args: list[Any] = [val, endian]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::to_bytes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def to_bytes(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[base.int64],
    endian: type[base.Endian],
) -> type[base.bytes]:
    args: list[Any] = [val, endian]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::to_bytes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def to_bytes(val: type[base.uuid]) -> type[base.bytes]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bytes,
        FuncCall(
            fname="std::to_bytes",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

def to_bytes(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(to_bytes, *args, **kwargs)  # type: ignore [no-any-return]

def to_json(str: type[base.str] | builtins.str) -> type[base.json]:
    args: list[Any] = [str]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.json,
        FuncCall(
            fname="std::to_json",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )

@overload
def to_datetime(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[base.str],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.datetime]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::to_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def to_datetime(  # type: ignore [overload-cannot-match, unused-ignore]
    year: type[base.int64],
    month: type[base.int64],
    day: type[base.int64],
    hour: type[base.int64],
    min: type[base.int64],
    sec: type[base.float64],
    timezone: type[base.str],
) -> type[base.datetime]:
    args: list[Any] = [year, month, day, hour, min, sec, timezone]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::to_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def to_datetime(epochseconds: type[base.float64]) -> type[base.datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [epochseconds]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::to_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def to_datetime(epochseconds: type[base.int64]) -> type[base.datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [epochseconds]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::to_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def to_datetime(epochseconds: type[base.decimal]) -> type[base.datetime]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [epochseconds]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::to_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

@overload
def to_datetime(  # type: ignore [overload-cannot-match, unused-ignore]
    local: type[std_cal.local_datetime],
    zone: type[base.str],
) -> type[base.datetime]:
    args: list[Any] = [local, zone]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.datetime,
        FuncCall(
            fname="std::to_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

def to_datetime(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(to_datetime, *args, **kwargs)  # type: ignore [no-any-return]

def to_duration(
    *,
    hours: type[base.int64] | int | UnspecifiedType = Unspecified,
    minutes: type[base.int64] | int | UnspecifiedType = Unspecified,
    seconds: type[base.float64] | float | UnspecifiedType = Unspecified,
    microseconds: type[base.int64] | int | UnspecifiedType = Unspecified,
) -> type[base.duration]:
    args: list[Any] = []
    kw: dict[___builtins__.str, Any] = {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "microseconds": microseconds,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.duration,
        FuncCall(
            fname="std::to_duration",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'duration'),
        )
    )

def to_bigint(
    s: type[base.str] | builtins.str,
    fmt: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.bigint]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.bigint,
        FuncCall(
            fname="std::to_bigint",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bigint'),
        )
    )

def to_decimal(
    s: type[base.str] | builtins.str,
    fmt: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.decimal]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.decimal,
        FuncCall(
            fname="std::to_decimal",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'decimal'),
        )
    )

@overload
def to_int64(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[base.str],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.int64]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::to_int64",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def to_int64(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[base.bytes],
    endian: type[base.Endian],
) -> type[base.int64]:
    args: list[Any] = [val, endian]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::to_int64",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def to_int64(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(to_int64, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def to_int32(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[base.str],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.int32]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::to_int32",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

@overload
def to_int32(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[base.bytes],
    endian: type[base.Endian],
) -> type[base.int32]:
    args: list[Any] = [val, endian]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int32,
        FuncCall(
            fname="std::to_int32",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int32'),
        )
    )

def to_int32(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(to_int32, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def to_int16(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[base.str],
    fmt: type[base.str] | None | UnspecifiedType = Unspecified,
) -> type[base.int16]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::to_int16",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

@overload
def to_int16(  # type: ignore [overload-cannot-match, unused-ignore]
    val: type[base.bytes],
    endian: type[base.Endian],
) -> type[base.int16]:
    args: list[Any] = [val, endian]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int16,
        FuncCall(
            fname="std::to_int16",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int16'),
        )
    )

def to_int16(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(to_int16, *args, **kwargs)  # type: ignore [no-any-return]

def to_float64(
    s: type[base.str] | builtins.str,
    fmt: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.float64]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float64,
        FuncCall(
            fname="std::to_float64",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def to_float32(
    s: type[base.str] | builtins.str,
    fmt: type[base.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[base.float32]:
    args: list[Any] = [s, fmt]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.float32,
        FuncCall(
            fname="std::to_float32",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float32'),
        )
    )

def to_uuid(val: type[base.bytes] | ___builtins_2__.bytes) -> type[base.uuid]:
    args: list[Any] = [val]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.uuid,
        FuncCall(
            fname="std::to_uuid",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'uuid'),
        )
    )

@overload
def sequence_reset(  # type: ignore [overload-cannot-match, unused-ignore]
    seq: type[schema.ScalarType],
    value: type[base.int64],
) -> type[base.int64]:
    args: list[Any] = [seq, value]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::sequence_reset",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def sequence_reset(seq: type[schema.ScalarType]) -> type[base.int64]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [seq]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::sequence_reset",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

def sequence_reset(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[pydantic.GelType]:
    return dispatch_overload(sequence_reset, *args, **kwargs)  # type: ignore [no-any-return]

def sequence_next(seq: type[schema.ScalarType]) -> type[base.int64]:
    args: list[Any] = [seq]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.int64,
        FuncCall(
            fname="std::sequence_next",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'int64'),
        )
    )

@overload
def coal_eq(
    cls: ___builtins_3__.type[AnyTuple | Array[GelType_T] | BaseObject | MultiRange[base.anypoint] | Range[base.anypoint] | base.anyenum | base.anyint | base.anyscalar | base.bigint | base.bool | base.bytes | base.datetime | base.decimal | base.duration | base.float32 | base.float64 | base.int16 | base.int32 | base.int64 | base.json | base.str | base.uuid | cfg.memory | std_cal.local_date | std_cal.local_datetime | std_cal.local_time | std_cal.relative_duration],
    other: Array[GelType_T] | DateTimeLike | MultiRange[base.anypoint] | Range[base.anypoint] | ___builtins_3__.type[AnyTuple] | ___builtins_3__.type[Array[GelType_T]] | ___builtins_3__.type[BaseObject] | ___builtins_3__.type[MultiRange[base.anypoint]] | ___builtins_3__.type[Range[base.anypoint]] | ___builtins_3__.type[base.anyenum] | ___builtins_3__.type[base.anyint] | ___builtins_3__.type[base.anyscalar] | ___builtins_3__.type[base.bigint] | ___builtins_3__.type[base.bool] | ___builtins_3__.type[base.bytes] | ___builtins_3__.type[base.datetime] | ___builtins_3__.type[base.decimal] | ___builtins_3__.type[base.duration] | ___builtins_3__.type[base.float32] | ___builtins_3__.type[base.float64] | ___builtins_3__.type[base.int16] | ___builtins_3__.type[base.int32] | ___builtins_3__.type[base.int64] | ___builtins_3__.type[base.json] | ___builtins_3__.type[base.str] | ___builtins_3__.type[base.uuid] | ___builtins_3__.type[cfg.memory] | ___builtins_3__.type[std_cal.date_duration] | ___builtins_3__.type[std_cal.local_date] | ___builtins_3__.type[std_cal.local_datetime] | ___builtins_3__.type[std_cal.local_time] | ___builtins_3__.type[std_cal.relative_duration] | ___builtins_4__.bool | ___builtins_4__.bytes | ___builtins_4__.float | ___builtins_4__.int | ___builtins_4__.str | ___datetime_1__.date | ___datetime_1__.time | ___datetime_1__.timedelta | ___decimal__.Decimal | ___gel__.ConfigMemory | ___gel__.DateDuration | ___gel__.RelativeDuration | ___uuid__.UUID | base.anyenum | base.anyint | base.anyscalar | base.bigint | base.bool | base.bytes | base.datetime | base.decimal | base.duration | base.float32 | base.float64 | base.int16 | base.int32 | base.int64 | base.json | base.str | base.uuid | cfg.memory | std_cal.date_duration | std_cal.local_date | std_cal.local_datetime | std_cal.local_time | std_cal.relative_duration,
) -> type[base.bool]:
    match other:
        case ___gel__.ConfigMemory():
            other = ___cfg__.memory(other)
        case ___builtins_4__.bytes():
            other = ___base__.bytes(other)
        case ___builtins_4__.int():
            other = ___base__.bigint(other)
        case ___builtins_4__.float():
            other = ___base__.float64(other)
        case ___datetime_1__.date():
            other = ___std_cal__.local_date(other)
        case ___gel__.RelativeDuration():
            other = ___std_cal__.relative_duration(other)
        case ___builtins_4__.str():
            other = ___base__.str(other)
        case ___builtins_4__.bool():
            other = ___base__.bool(other)
        case ___decimal__.Decimal():
            other = ___base__.decimal(other)
        case ___datetime_1__.time():
            other = ___std_cal__.local_time(other)
        case ___datetime_1__.timedelta():
            other = ___base__.duration(other)
        case ___gel__.DateDuration():
            other = ___std_cal__.date_duration(other)
        case DateTimeLike():
            other = ___base__.datetime(other)
        case ___uuid__.UUID():
            other = ___base__.uuid(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="?=",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def coal_eq(
    other: DateTimeLike | ___builtins_4__.bool | ___builtins_4__.bytes | ___builtins_4__.float | ___builtins_4__.int | ___builtins_4__.str | ___datetime_1__.date | ___datetime_1__.time | ___datetime_1__.timedelta | ___decimal__.Decimal | ___gel__.ConfigMemory | ___gel__.DateDuration | ___gel__.RelativeDuration | ___uuid__.UUID,
    cls: ___builtins_3__.type[AnyTuple | Array[GelType_T] | BaseObject | MultiRange[base.anypoint] | Range[base.anypoint] | base.anyenum | base.anyint | base.anyscalar | base.bigint | base.bool | base.bytes | base.datetime | base.decimal | base.duration | base.float32 | base.float64 | base.int16 | base.int32 | base.int64 | base.json | base.str | base.uuid | cfg.memory | std_cal.local_date | std_cal.local_datetime | std_cal.local_time | std_cal.relative_duration],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___gel__.ConfigMemory():
            operand = ___cfg__.memory(other)
        case ___builtins_4__.bytes():
            operand = ___base__.bytes(other)
        case ___builtins_4__.int():
            operand = ___base__.bigint(other)
        case ___builtins_4__.float():
            operand = ___base__.float64(other)
        case ___datetime_1__.date():
            operand = ___std_cal__.local_date(other)
        case ___gel__.RelativeDuration():
            operand = ___std_cal__.relative_duration(other)
        case ___builtins_4__.str():
            operand = ___base__.str(other)
        case ___builtins_4__.bool():
            operand = ___base__.bool(other)
        case ___decimal__.Decimal():
            operand = ___base__.decimal(other)
        case ___datetime_1__.time():
            operand = ___std_cal__.local_time(other)
        case ___datetime_1__.timedelta():
            operand = ___base__.duration(other)
        case ___gel__.DateDuration():
            operand = ___std_cal__.date_duration(other)
        case DateTimeLike():
            operand = ___base__.datetime(other)
        case ___uuid__.UUID():
            operand = ___base__.uuid(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="?=",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def coal_eq(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(coal_eq, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def coal_neq(
    cls: ___builtins_3__.type[AnyTuple | Array[GelType_T] | BaseObject | MultiRange[base.anypoint] | Range[base.anypoint] | base.anyenum | base.anyint | base.anyscalar | base.bigint | base.bool | base.bytes | base.datetime | base.decimal | base.duration | base.float32 | base.float64 | base.int16 | base.int32 | base.int64 | base.json | base.str | base.uuid | cfg.memory | std_cal.local_date | std_cal.local_datetime | std_cal.local_time | std_cal.relative_duration],
    other: Array[GelType_T] | DateTimeLike | MultiRange[base.anypoint] | Range[base.anypoint] | ___builtins_3__.type[AnyTuple] | ___builtins_3__.type[Array[GelType_T]] | ___builtins_3__.type[BaseObject] | ___builtins_3__.type[MultiRange[base.anypoint]] | ___builtins_3__.type[Range[base.anypoint]] | ___builtins_3__.type[base.anyenum] | ___builtins_3__.type[base.anyint] | ___builtins_3__.type[base.anyscalar] | ___builtins_3__.type[base.bigint] | ___builtins_3__.type[base.bool] | ___builtins_3__.type[base.bytes] | ___builtins_3__.type[base.datetime] | ___builtins_3__.type[base.decimal] | ___builtins_3__.type[base.duration] | ___builtins_3__.type[base.float32] | ___builtins_3__.type[base.float64] | ___builtins_3__.type[base.int16] | ___builtins_3__.type[base.int32] | ___builtins_3__.type[base.int64] | ___builtins_3__.type[base.json] | ___builtins_3__.type[base.str] | ___builtins_3__.type[base.uuid] | ___builtins_3__.type[cfg.memory] | ___builtins_3__.type[std_cal.date_duration] | ___builtins_3__.type[std_cal.local_date] | ___builtins_3__.type[std_cal.local_datetime] | ___builtins_3__.type[std_cal.local_time] | ___builtins_3__.type[std_cal.relative_duration] | ___builtins_4__.bool | ___builtins_4__.bytes | ___builtins_4__.float | ___builtins_4__.int | ___builtins_4__.str | ___datetime_1__.date | ___datetime_1__.time | ___datetime_1__.timedelta | ___decimal__.Decimal | ___gel__.ConfigMemory | ___gel__.DateDuration | ___gel__.RelativeDuration | ___uuid__.UUID | base.anyenum | base.anyint | base.anyscalar | base.bigint | base.bool | base.bytes | base.datetime | base.decimal | base.duration | base.float32 | base.float64 | base.int16 | base.int32 | base.int64 | base.json | base.str | base.uuid | cfg.memory | std_cal.date_duration | std_cal.local_date | std_cal.local_datetime | std_cal.local_time | std_cal.relative_duration,
) -> type[base.bool]:
    match other:
        case ___gel__.ConfigMemory():
            other = ___cfg__.memory(other)
        case ___builtins_4__.bytes():
            other = ___base__.bytes(other)
        case ___builtins_4__.int():
            other = ___base__.bigint(other)
        case ___builtins_4__.float():
            other = ___base__.float64(other)
        case ___datetime_1__.date():
            other = ___std_cal__.local_date(other)
        case ___gel__.RelativeDuration():
            other = ___std_cal__.relative_duration(other)
        case ___builtins_4__.str():
            other = ___base__.str(other)
        case ___builtins_4__.bool():
            other = ___base__.bool(other)
        case ___decimal__.Decimal():
            other = ___base__.decimal(other)
        case ___datetime_1__.time():
            other = ___std_cal__.local_time(other)
        case ___datetime_1__.timedelta():
            other = ___base__.duration(other)
        case ___gel__.DateDuration():
            other = ___std_cal__.date_duration(other)
        case DateTimeLike():
            other = ___base__.datetime(other)
        case ___uuid__.UUID():
            other = ___base__.uuid(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="?!=",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def coal_neq(
    other: DateTimeLike | ___builtins_4__.bool | ___builtins_4__.bytes | ___builtins_4__.float | ___builtins_4__.int | ___builtins_4__.str | ___datetime_1__.date | ___datetime_1__.time | ___datetime_1__.timedelta | ___decimal__.Decimal | ___gel__.ConfigMemory | ___gel__.DateDuration | ___gel__.RelativeDuration | ___uuid__.UUID,
    cls: ___builtins_3__.type[AnyTuple | Array[GelType_T] | BaseObject | MultiRange[base.anypoint] | Range[base.anypoint] | base.anyenum | base.anyint | base.anyscalar | base.bigint | base.bool | base.bytes | base.datetime | base.decimal | base.duration | base.float32 | base.float64 | base.int16 | base.int32 | base.int64 | base.json | base.str | base.uuid | cfg.memory | std_cal.local_date | std_cal.local_datetime | std_cal.local_time | std_cal.relative_duration],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___gel__.ConfigMemory():
            operand = ___cfg__.memory(other)
        case ___builtins_4__.bytes():
            operand = ___base__.bytes(other)
        case ___builtins_4__.int():
            operand = ___base__.bigint(other)
        case ___builtins_4__.float():
            operand = ___base__.float64(other)
        case ___datetime_1__.date():
            operand = ___std_cal__.local_date(other)
        case ___gel__.RelativeDuration():
            operand = ___std_cal__.relative_duration(other)
        case ___builtins_4__.str():
            operand = ___base__.str(other)
        case ___builtins_4__.bool():
            operand = ___base__.bool(other)
        case ___decimal__.Decimal():
            operand = ___base__.decimal(other)
        case ___datetime_1__.time():
            operand = ___std_cal__.local_time(other)
        case ___datetime_1__.timedelta():
            operand = ___base__.duration(other)
        case ___gel__.DateDuration():
            operand = ___std_cal__.date_duration(other)
        case DateTimeLike():
            operand = ___base__.datetime(other)
        case ___uuid__.UUID():
            operand = ___base__.uuid(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="?!=",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def coal_neq(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(coal_neq, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def or_(
    cls: ___builtins_3__.type[base.bool],
    other: ___builtins_3__.type[base.bool] | ___builtins_4__.bool | base.bool,
) -> type[base.bool]:
    match other:
        case ___builtins_4__.bool():
            other = ___base__.bool(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="OR",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def or_(
    other: ___builtins_4__.bool,
    cls: ___builtins_3__.type[base.bool],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___builtins_4__.bool():
            operand = ___base__.bool(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="OR",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def or_(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(or_, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def and_(
    cls: ___builtins_3__.type[base.bool],
    other: ___builtins_3__.type[base.bool] | ___builtins_4__.bool | base.bool,
) -> type[base.bool]:
    match other:
        case ___builtins_4__.bool():
            other = ___base__.bool(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="AND",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def and_(
    other: ___builtins_4__.bool,
    cls: ___builtins_3__.type[base.bool],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___builtins_4__.bool():
            operand = ___base__.bool(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="AND",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def and_(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(and_, *args, **kwargs)  # type: ignore [no-any-return]

def not_in(
    cls: ___builtins_3__.type[GelType_T],
    other: ___builtins_3__.type[GelType_T],
) -> type[base.bool]:
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="NOT IN",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def union(
    cls: ___builtins_3__.type[GelType_T],
    other: ___builtins_3__.type[GelType_T],
) -> type[GelType_T]:
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="UNION",
        rexpr=rexpr,
        type_=SchemaPath('anytype'),
    )
    return AnnotatedExpr(GelType, op)  # type: ignore [return-value]

def except_(
    cls: ___builtins_3__.type[GelType_T],
    other: ___builtins_3__.type[GelType_T],
) -> type[GelType_T]:
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="EXCEPT",
        rexpr=rexpr,
        type_=SchemaPath('anytype'),
    )
    return AnnotatedExpr(GelType, op)  # type: ignore [return-value]

def intersect(
    cls: ___builtins_3__.type[GelType_T],
    other: ___builtins_3__.type[GelType_T],
) -> type[GelType_T]:
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="INTERSECT",
        rexpr=rexpr,
        type_=SchemaPath('anytype'),
    )
    return AnnotatedExpr(GelType, op)  # type: ignore [return-value]

def coalesce(
    cls: ___builtins_3__.type[GelType_T],
    other: ___builtins_3__.type[GelType_T],
) -> type[GelType_T]:
    rexpr: ExprCompatible = other
    op = InfixOp(lexpr=cls, op="??", rexpr=rexpr, type_=SchemaPath('anytype'))
    return AnnotatedExpr(GelType, op)  # type: ignore [return-value]

@overload
def like(
    cls: ___builtins_3__.type[base.str],
    other: ___builtins_3__.type[base.str] | ___builtins_4__.str | base.str,
) -> type[base.bool]:
    match other:
        case ___builtins_4__.str():
            other = ___base__.str(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="LIKE",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def like(
    other: ___builtins_4__.str,
    cls: ___builtins_3__.type[base.str],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___builtins_4__.str():
            operand = ___base__.str(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="LIKE",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def like(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(like, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def ilike(
    cls: ___builtins_3__.type[base.str],
    other: ___builtins_3__.type[base.str] | ___builtins_4__.str | base.str,
) -> type[base.bool]:
    match other:
        case ___builtins_4__.str():
            other = ___base__.str(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="ILIKE",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def ilike(
    other: ___builtins_4__.str,
    cls: ___builtins_3__.type[base.str],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___builtins_4__.str():
            operand = ___base__.str(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="ILIKE",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def ilike(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(ilike, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def not_like(
    cls: ___builtins_3__.type[base.str],
    other: ___builtins_3__.type[base.str] | ___builtins_4__.str | base.str,
) -> type[base.bool]:
    match other:
        case ___builtins_4__.str():
            other = ___base__.str(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="NOT LIKE",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def not_like(
    other: ___builtins_4__.str,
    cls: ___builtins_3__.type[base.str],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___builtins_4__.str():
            operand = ___base__.str(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="NOT LIKE",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def not_like(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(not_like, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def not_ilike(
    cls: ___builtins_3__.type[base.str],
    other: ___builtins_3__.type[base.str] | ___builtins_4__.str | base.str,
) -> type[base.bool]:
    match other:
        case ___builtins_4__.str():
            other = ___base__.str(other)
    rexpr: ExprCompatible = other
    op = InfixOp(
        lexpr=cls,
        op="NOT ILIKE",
        rexpr=rexpr,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

@overload
def not_ilike(
    other: ___builtins_4__.str,
    cls: ___builtins_3__.type[base.str],
) -> type[base.bool]:
    operand: ExprCompatible
    match other:
        case ___builtins_4__.str():
            operand = ___base__.str(other)
        case _:
            operand = other
    op = InfixOp(
        lexpr=operand,
        op="NOT ILIKE",
        rexpr=cls,
        type_=SchemaPath('std', 'bool'),
    )
    return AnnotatedExpr(___base__.bool, op)  # type: ignore [return-value]

def not_ilike(*args: Any, **kwargs: Any) -> ___builtins_3__.type:
    return dispatch_overload(not_ilike, *args, **kwargs)  # type: ignore [no-any-return]

if not TYPE_CHECKING:
    def __getattr__(name: builtins.str) -> typing.Any:
        mods = frozenset(["pg", "net", "math", "fts", "enc", "cal"])
        if name in mods:
            return importlib.import_module("." + name, __name__)
        e = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(e)


from ..__variants__ import cfg as ___cfg__, std as ___base__  # noqa: E402 F403
from ..__variants__.std import (  # noqa: E402 F403
    BaseObject,
    Endian,
    FreeObject,
    JsonEmpty,
    Object,
    anycontiguous,
    anydiscrete,
    anyenum,
    anyfloat,
    anyint,
    anynumeric,
    anypoint,
    anyreal,
    anyscalar,
    bigint,
    bool,
    bytes,
    cal as ___std_cal__,
    datetime,
    decimal,
    duration,
    float32,
    float64,
    int16,
    int32,
    int64,
    json,
    sequence,
    str,
    uuid
)


__all__ = (
    'BaseObject',
    'Endian',
    'FreeObject',
    'JsonEmpty',
    'Object',
    'anycontiguous',
    'anydiscrete',
    'anyenum',
    'anyfloat',
    'anyint',
    'anynumeric',
    'anypoint',
    'anyreal',
    'anyscalar',
    'bigint',
    'bool',
    'bytes',
    'cal',
    'datetime',
    'decimal',
    'duration',
    'enc',
    'float32',
    'float64',
    'fts',
    'int16',
    'int32',
    'int64',
    'json',
    'math',
    'net',
    'pg',
    'sequence',
    'str',
    'uuid',
)
