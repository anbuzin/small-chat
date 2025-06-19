#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from gel.models.pydantic import (
    AnyNamedTuple,
    Array,
    GelModel,
    GelTypeMetadata,
    SchemaPath
)

from typing import NamedTuple
from uuid import UUID


#
# tuple type tuple<kind:std::net::RequestFailureKind, message:std::str>
#
class _KindMessage_Tuple_hRjfgQ(NamedTuple):
    kind: std_net.RequestFailureKind
    message: std.str


class KindMessage_Tuple_hRjfgQ(_KindMessage_Tuple_hRjfgQ, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=176916471788808878562760725445109455309)
        name = SchemaPath('tuple<kind:std::net::RequestFailureKind, message:std::str>')

    __slots__ = ()

#
# tuple type tuple<major:std::int16, minor:std::int16>
#
class _MajorMinor_Tuple_K20e_g(NamedTuple):
    major: std.int16
    minor: std.int16


class MajorMinor_Tuple_K20e_g(_MajorMinor_Tuple_K20e_g, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=57723392516177260343067565139426900410)
        name = SchemaPath('tuple<major:std::int16, minor:std::int16>')

    __slots__ = ()

#
# tuple type tuple<major:std::int64, minor:std::int64, stage:std::str, stage_no:std::int64, local:array<std::str>>
#
class _MajorMinorStageStage_noLocal_Tuple_Lh76jQ(NamedTuple):
    major: std.int64
    minor: std.int64
    stage: std.str
    stage_no: std.int64
    local: Array[std.str]


class MajorMinorStageStage_noLocal_Tuple_Lh76jQ(
    _MajorMinorStageStage_noLocal_Tuple_Lh76jQ,
    AnyNamedTuple,
):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=61305338540392200951852396798821552652)
        name = SchemaPath('tuple<major:std::int64, minor:std::int64, stage:std::str, stage_no:std::int64, local:array<std::str>>')

    __slots__ = ()

#
# tuple type tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>
#
class _MajorMinorStageStage_noLocal_Tuple_SKRhXQ(NamedTuple):
    major: std.int64
    minor: std.int64
    stage: sys.VersionStage
    stage_no: std.int64
    local: Array[std.str]


class MajorMinorStageStage_noLocal_Tuple_SKRhXQ(
    _MajorMinorStageStage_noLocal_Tuple_SKRhXQ,
    AnyNamedTuple,
):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=96557927154408612937861582867322211257)
        name = SchemaPath('tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>')

    __slots__ = ()

#
# tuple type tuple<name:std::str, expr:std::str>
#
class _NameExpr_Tuple_9eMVFg(NamedTuple):
    name: std.str
    expr: std.str


class NameExpr_Tuple_9eMVFg(_NameExpr_Tuple_9eMVFg, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=326839938064147697657892507176438779427)
        name = SchemaPath('tuple<name:std::str, expr:std::str>')

    __slots__ = ()

#
# tuple type tuple<text:std::str, refs:array<std::uuid>>
#
class _TextRefs_Tuple_Z5lveg(NamedTuple):
    text: std.str
    refs: Array[std.uuid]


class TextRefs_Tuple_Z5lveg(_TextRefs_Tuple_Z5lveg, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=137707166060458248461855710211730195906)
        name = SchemaPath('tuple<text:std::str, refs:array<std::uuid>>')

    __slots__ = ()

#
# tuple type tuple<name:std::str, value:std::str>
#
class _NameValue_Tuple_CO3mqQ(NamedTuple):
    name: std.str
    value: std.str


class NameValue_Tuple_CO3mqQ(_NameValue_Tuple_CO3mqQ, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=11869076702865716584055616908733573978)
        name = SchemaPath('tuple<name:std::str, value:std::str>')

    __slots__ = ()

#
# tuple type tuple<object:anyobject, score:std::float32>
#
class _ObjectScore_Tuple_wT628Q(NamedTuple):
    object: GelModel
    score: std.float32


class ObjectScore_Tuple_wT628Q(_ObjectScore_Tuple_wT628Q, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=256866636133882169204337367677577691088)
        name = SchemaPath('tuple<object:anyobject, score:std::float32>')

    __slots__ = ()

#
# tuple type tuple<name:std::str, expr:tuple<text:std::str, refs:array<std::uuid>>>
#
class _NameExpr_Tuple_J9gV9A(NamedTuple):
    name: std.str
    expr: TextRefs_Tuple_Z5lveg


class NameExpr_Tuple_J9gV9A(_NameExpr_Tuple_J9gV9A, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=52961873250615995036283599343959502342)
        name = SchemaPath('tuple<name:std::str, expr:tuple<text:std::str, refs:array<std::uuid>>>')

    __slots__ = ()



from ..__variants__ import std, sys  # noqa: E402 F403
from ..__variants__.std import net as std_net  # noqa: E402 F403
