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
    UnspecifiedType,
    dispatch_overload
)

from builtins import dict, list, str
from typing import Any, TYPE_CHECKING, overload

if TYPE_CHECKING:

    from ..__variants__ import std
    from ..__variants__.std import cal as base

    from gel import RelativeDuration
    from gel.models.pydantic import GelType

    import builtins as builtins
    import typing as typing
    from builtins import float, int, type
    from datetime import date, time


@overload
def to_local_datetime(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[std.str],
    fmt: type[std.str] | None | UnspecifiedType = Unspecified,
) -> type[base.local_datetime]:
    args: list[Any] = [s, fmt]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_datetime,
        FuncCall(
            fname="std::cal::to_local_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
    )

@overload
def to_local_datetime(  # type: ignore [overload-cannot-match, unused-ignore]
    year: type[std.int64],
    month: type[std.int64],
    day: type[std.int64],
    hour: type[std.int64],
    min: type[std.int64],
    sec: type[std.float64],
) -> type[base.local_datetime]:
    args: list[Any] = [year, month, day, hour, min, sec]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_datetime,
        FuncCall(
            fname="std::cal::to_local_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
    )

@overload
def to_local_datetime(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std.datetime],
    zone: type[std.str],
) -> type[base.local_datetime]:
    args: list[Any] = [dt, zone]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_datetime,
        FuncCall(
            fname="std::cal::to_local_datetime",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
    )

def to_local_datetime(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[GelType]:
    return dispatch_overload(to_local_datetime, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def to_local_date(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[std.str],
    fmt: type[std.str] | None | UnspecifiedType = Unspecified,
) -> type[base.local_date]:
    args: list[Any] = [s, fmt]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_date,
        FuncCall(
            fname="std::cal::to_local_date",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

@overload
def to_local_date(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std.datetime],
    zone: type[std.str],
) -> type[base.local_date]:
    args: list[Any] = [dt, zone]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_date,
        FuncCall(
            fname="std::cal::to_local_date",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

@overload
def to_local_date(  # type: ignore [overload-cannot-match, unused-ignore]
    year: type[std.int64],
    month: type[std.int64],
    day: type[std.int64],
) -> type[base.local_date]:
    args: list[Any] = [year, month, day]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_date,
        FuncCall(
            fname="std::cal::to_local_date",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
    )

def to_local_date(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(to_local_date, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def to_local_time(  # type: ignore [overload-cannot-match, unused-ignore]
    s: type[std.str],
    fmt: type[std.str] | None | UnspecifiedType = Unspecified,
) -> type[base.local_time]:
    args: list[Any] = [s, fmt]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_time,
        FuncCall(
            fname="std::cal::to_local_time",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
    )

@overload
def to_local_time(  # type: ignore [overload-cannot-match, unused-ignore]
    dt: type[std.datetime],
    zone: type[std.str],
) -> type[base.local_time]:
    args: list[Any] = [dt, zone]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_time,
        FuncCall(
            fname="std::cal::to_local_time",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
    )

@overload
def to_local_time(  # type: ignore [overload-cannot-match, unused-ignore]
    hour: type[std.int64],
    min: type[std.int64],
    sec: type[std.float64],
) -> type[base.local_time]:
    args: list[Any] = [hour, min, sec]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.local_time,
        FuncCall(
            fname="std::cal::to_local_time",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
    )

def to_local_time(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(to_local_time, *args, **kwargs)  # type: ignore [no-any-return]

def to_relative_duration(
    *,
    years: type[std.int64] | int | UnspecifiedType = Unspecified,
    months: type[std.int64] | int | UnspecifiedType = Unspecified,
    days: type[std.int64] | int | UnspecifiedType = Unspecified,
    hours: type[std.int64] | int | UnspecifiedType = Unspecified,
    minutes: type[std.int64] | int | UnspecifiedType = Unspecified,
    seconds: type[std.float64] | float | UnspecifiedType = Unspecified,
    microseconds: type[std.int64] | int | UnspecifiedType = Unspecified,
) -> type[base.relative_duration]:
    args: list[Any] = []
    kw: dict[str, Any] = {
        "years": years,
        "months": months,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "microseconds": microseconds,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.relative_duration,
        FuncCall(
            fname="std::cal::to_relative_duration",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
    )

def to_date_duration(
    *,
    years: type[std.int64] | int | UnspecifiedType = Unspecified,
    months: type[std.int64] | int | UnspecifiedType = Unspecified,
    days: type[std.int64] | int | UnspecifiedType = Unspecified,
) -> type[base.date_duration]:
    args: list[Any] = []
    kw: dict[str, Any] = {"years": years, "months": months, "days": days}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.date_duration,
        FuncCall(
            fname="std::cal::to_date_duration",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
    )

def time_get(
    dt: type[base.local_time] | time,
    el: type[std.str] | builtins.str,
) -> type[std.float64]:
    args: list[Any] = [dt, el]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::cal::time_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def date_get(
    dt: type[base.local_date] | date,
    el: type[std.str] | builtins.str,
) -> type[std.float64]:
    args: list[Any] = [dt, el]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.float64,
        FuncCall(
            fname="std::cal::date_get",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'float64'),
        )
    )

def duration_normalize_hours(
    dur: type[base.relative_duration] | RelativeDuration,
) -> type[base.relative_duration]:
    args: list[Any] = [dur]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.relative_duration,
        FuncCall(
            fname="std::cal::duration_normalize_hours",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
    )

@overload
def duration_normalize_days(  # type: ignore [overload-cannot-match, unused-ignore]
    dur: type[base.relative_duration],
) -> type[base.relative_duration]:
    args: list[Any] = [dur]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.relative_duration,
        FuncCall(
            fname="std::cal::duration_normalize_days",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
    )

@overload
def duration_normalize_days(  # type: ignore [overload-cannot-match, unused-ignore]
    dur: type[base.date_duration],
) -> type[base.date_duration]:
    args: list[Any] = [dur]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___base__.date_duration,
        FuncCall(
            fname="std::cal::duration_normalize_days",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
    )

def duration_normalize_days(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> type[GelType]:
    return dispatch_overload(duration_normalize_days, *args, **kwargs)  # type: ignore [no-any-return]



from ..__variants__ import std as ___std__  # noqa: E402 F403
from ..__variants__.std import cal as ___base__  # noqa: E402 F403
from ..__variants__.std.cal import (  # noqa: E402 F403
    date_duration,
    local_date,
    local_datetime,
    local_time,
    relative_duration
)


__all__ = (
    'date_duration',
    'local_date',
    'local_datetime',
    'local_time',
    'relative_duration',
)
