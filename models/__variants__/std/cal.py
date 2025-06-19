#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std

import gel as gel
from gel import DateDuration, RelativeDuration
from gel.models.pydantic import (
    AnnotatedExpr,
    DateImpl,
    DateTimeImpl,
    DateTimeLike,
    ExprCompatible,
    InfixOp,
    PrefixOp,
    PyTypeScalar,
    SchemaPath,
    TimeImpl,
    dispatch_overload
)

import datetime as ___datetime__
import datetime as datetime
from builtins import type
from datetime import date, time
from typing import Any, TYPE_CHECKING, overload
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as ___std__

    import builtins as builtins
    from typing import ClassVar



class __date_duration_meta__(std.__anyscalar_meta__):
    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[local_date]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[date_duration]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __radd__(cls, other: datetime.date) -> builtins.type[local_date]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case datetime.date():
                operand = local_date(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    @overload
    def __radd__(cls, other: gel.DateDuration) -> builtins.type[date_duration]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case gel.DateDuration():
                operand = date_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __radd__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[date_duration]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __rsub__(cls, other: gel.DateDuration) -> builtins.type[date_duration]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case gel.DateDuration():
                operand = date_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class date_duration(
        PyTypeScalar[DateDuration],
        std.anyscalar,
        metaclass=__date_duration_meta__,
    ):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=274)
            name = SchemaPath('std', 'cal', 'date_duration')

if not TYPE_CHECKING:
    class date_duration(
        DateDuration,
        PyTypeScalar[DateDuration],
        std.anyscalar,
    ):
        __gel_type_class__: ClassVar[type] = __date_duration_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=274)
            name = SchemaPath('std', 'cal', 'date_duration')



class __local_date_meta__(std.__anydiscrete_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | datetime.timedelta | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case datetime.timedelta():
                other = std.duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[local_date]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __radd__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.RelativeDuration,
    ) -> builtins.type[local_datetime]:
        operand: ExprCompatible
        match other:
            case datetime.timedelta():
                operand = std.duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __radd__(cls, other: gel.DateDuration) -> builtins.type[local_date]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case gel.DateDuration():
                operand = date_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    def __radd__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | datetime.timedelta | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case datetime.timedelta():
                other = std.duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[local_date]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[date_duration]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __rsub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.RelativeDuration,
    ) -> builtins.type[local_datetime]:
        operand: ExprCompatible
        match other:
            case datetime.timedelta():
                operand = std.duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __rsub__(cls, other: gel.DateDuration) -> builtins.type[local_date]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case gel.DateDuration():
                operand = date_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    @overload
    def __rsub__(cls, other: datetime.date) -> builtins.type[date_duration]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case datetime.date():
                operand = local_date(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __rsub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class local_date(
        PyTypeScalar[date],
        std.anydiscrete,
        metaclass=__local_date_meta__,
    ):
        class __gel_reflection__(___std__.anydiscrete.__gel_reflection__):
            id = UUID(int=268)
            name = SchemaPath('std', 'cal', 'local_date')

if not TYPE_CHECKING:
    class local_date(DateImpl, PyTypeScalar[date], std.anydiscrete):
        __gel_type_class__: ClassVar[type] = __local_date_meta__

        class __gel_reflection__(std.anydiscrete.__gel_reflection__):
            id = UUID(int=268)
            name = SchemaPath('std', 'cal', 'local_date')



class __local_datetime_meta__(std.__anycontiguous_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case datetime.timedelta():
                other = std.duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    def __radd__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.DateDuration | gel.RelativeDuration,
    ) -> builtins.type[local_datetime]:
        operand: ExprCompatible
        match other:
            case datetime.timedelta():
                operand = std.duration(other)
            case gel.DateDuration():
                operand = date_duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case datetime.timedelta():
                other = std.duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[relative_duration]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __rsub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.DateDuration | gel.RelativeDuration,
    ) -> builtins.type[local_datetime]:
        operand: ExprCompatible
        match other:
            case datetime.timedelta():
                operand = std.duration(other)
            case gel.DateDuration():
                operand = date_duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __rsub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date,
    ) -> builtins.type[relative_duration]:
        operand: ExprCompatible
        match other:
            case datetime.date():
                operand = local_date(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __rsub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class local_datetime(
        PyTypeScalar[___datetime__.datetime],
        std.anycontiguous,
        metaclass=__local_datetime_meta__,
    ):
        class __gel_reflection__(___std__.anycontiguous.__gel_reflection__):
            id = UUID(int=267)
            name = SchemaPath('std', 'cal', 'local_datetime')

if not TYPE_CHECKING:
    class local_datetime(
        DateTimeImpl,
        PyTypeScalar[___datetime__.datetime],
        std.anycontiguous,
    ):
        __gel_type_class__: ClassVar[type] = __local_datetime_meta__

        class __gel_reflection__(std.anycontiguous.__gel_reflection__):
            id = UUID(int=267)
            name = SchemaPath('std', 'cal', 'local_datetime')



class __local_time_meta__(std.__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[___std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_time]:
        match other:
            case datetime.timedelta():
                other = std.duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    def __radd__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.DateDuration | gel.RelativeDuration,
    ) -> builtins.type[local_time]:
        operand: ExprCompatible
        match other:
            case datetime.timedelta():
                operand = std.duration(other)
            case gel.DateDuration():
                operand = date_duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_time]:
        match other:
            case datetime.timedelta():
                other = std.duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[relative_duration]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __rsub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.DateDuration | gel.RelativeDuration,
    ) -> builtins.type[local_time]:
        operand: ExprCompatible
        match other:
            case datetime.timedelta():
                operand = std.duration(other)
            case gel.DateDuration():
                operand = date_duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __rsub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time,
    ) -> builtins.type[relative_duration]:
        operand: ExprCompatible
        match other:
            case datetime.time():
                operand = local_time(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __rsub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class local_time(
        PyTypeScalar[time],
        std.anyscalar,
        metaclass=__local_time_meta__,
    ):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=269)
            name = SchemaPath('std', 'cal', 'local_time')

if not TYPE_CHECKING:
    class local_time(TimeImpl, PyTypeScalar[time], std.anyscalar):
        __gel_type_class__: ClassVar[type] = __local_time_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=269)
            name = SchemaPath('std', 'cal', 'local_time')



class __relative_duration_meta__(std.__anyscalar_meta__):
    def __neg__(cls) -> builtins.type[relative_duration]:
        return AnnotatedExpr(  # type: ignore [return-value]
            relative_duration,
            PrefixOp(
            expr=cls,
            op="-",
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        ),
        )

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | ___std__.datetime | type[___std__.datetime],
    ) -> builtins.type[___std__.datetime]:
        match other:
            case DateTimeLike():
                other = std.datetime(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'datetime'),
        )
        return AnnotatedExpr(std.datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[local_datetime]:
        match other:
            case datetime.date():
                other = local_date(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[local_time]:
        match other:
            case datetime.time():
                other = local_time(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[relative_duration]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __radd__(cls, other: DateTimeLike) -> builtins.type[___std__.datetime]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case DateTimeLike():
                operand = std.datetime(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'datetime'),
        )
        return AnnotatedExpr(std.datetime, op)  # type: ignore [return-value]

    @overload
    def __radd__(cls, other: datetime.date) -> builtins.type[local_datetime]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case datetime.date():
                operand = local_date(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __radd__(cls, other: datetime.time) -> builtins.type[local_time]:  # type: ignore [override, unused-ignore]
        operand: ExprCompatible
        match other:
            case datetime.time():
                operand = local_time(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __radd__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.DateDuration | gel.RelativeDuration,
    ) -> builtins.type[relative_duration]:
        operand: ExprCompatible
        match other:
            case gel.DateDuration():
                operand = date_duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case datetime.timedelta():
                operand = std.duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="+",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __radd__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: ___std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[___std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[relative_duration]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
            case gel.RelativeDuration():
                other = relative_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=rexpr,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __rsub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.timedelta | gel.DateDuration | gel.RelativeDuration,
    ) -> builtins.type[relative_duration]:
        operand: ExprCompatible
        match other:
            case gel.DateDuration():
                operand = date_duration(other)
            case gel.RelativeDuration():
                operand = relative_duration(other)
            case datetime.timedelta():
                operand = std.duration(other)
            case _:
                operand = other
        op = InfixOp(
            lexpr=operand,
            op="-",
            rexpr=cls,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class relative_duration(
        PyTypeScalar[RelativeDuration],
        std.anyscalar,
        metaclass=__relative_duration_meta__,
    ):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=273)
            name = SchemaPath('std', 'cal', 'relative_duration')

if not TYPE_CHECKING:
    class relative_duration(
        RelativeDuration,
        PyTypeScalar[RelativeDuration],
        std.anyscalar,
    ):
        __gel_type_class__: ClassVar[type] = __relative_duration_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=273)
            name = SchemaPath('std', 'cal', 'relative_duration')


