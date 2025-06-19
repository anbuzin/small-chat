#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import schema
from ..__variants__ import sys as base

from gel.models.pydantic import (
    AnnotatedExpr,
    ComputedProperty,
    FuncCall,
    MultiLink,
    OptionalLink,
    OptionalProperty,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as builtins
from builtins import dict, list, tuple
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:

    from ..__variants__ import std as ___std__, sys as ___base__
    from ..std import __types__ as std___types__

    import builtins as ___builtins_1__
    import builtins as ___builtins__
    from builtins import type
    from uuid import UUID



#
# type sys::SystemObject
#
class SystemObject(base.SystemObject, schema.Object):
    pass


#
# type sys::ExtensionPackage
#
class ExtensionPackage(
    base.ExtensionPackage,
    SystemObject,
    schema.AnnotationSubject,
):
    script: std.str
    version: MajorMinorStageStage_noLocal_Tuple_SKRhXQ

#
# type sys::ExtensionPackageMigration
#
class ExtensionPackageMigration(
    base.ExtensionPackageMigration,
    SystemObject,
    schema.AnnotationSubject,
):
    script: std.str
    from_version: MajorMinorStageStage_noLocal_Tuple_SKRhXQ
    to_version: MajorMinorStageStage_noLocal_Tuple_SKRhXQ

#
# type sys::ExternalObject
#
class ExternalObject(base.ExternalObject, SystemObject):
    pass


#
# type sys::Role
#
class Role(
    base.Role,
    SystemObject,
    schema.InheritingObject,
    schema.AnnotationSubject,
):
    name: std.str
    superuser: std.bool
    is_superuser: ComputedProperty[std.bool, bool]
    password: OptionalProperty[std.str, str]
    member_of: MultiLink[Role]

#
# type sys::Branch
#
class Branch(base.Branch, ExternalObject, schema.AnnotationSubject):
    name: std.str
    last_migration: OptionalProperty[std.str, str]

#
# type sys::QueryStats
#
class QueryStats(base.QueryStats, ExternalObject):
    query: OptionalProperty[std.str, str]
    query_type: OptionalProperty[base.QueryType, builtins.str]
    tag: OptionalProperty[std.str, str]
    compilation_config: OptionalProperty[std.json, str]
    protocol_version: OptionalProperty[MajorMinor_Tuple_K20e_g, tuple[int, int]]
    default_namespace: OptionalProperty[std.str, str]
    namespace_aliases: OptionalProperty[std.json, str]
    output_format: OptionalProperty[base.OutputFormat, builtins.str]
    expect_one: OptionalProperty[std.bool, bool]
    implicit_limit: OptionalProperty[std.int64, int]
    inline_typeids: OptionalProperty[std.bool, bool]
    inline_typenames: OptionalProperty[std.bool, bool]
    inline_objectids: OptionalProperty[std.bool, bool]
    plans: OptionalProperty[std.int64, int]
    total_plan_time: OptionalProperty[std.duration, timedelta]
    min_plan_time: OptionalProperty[std.duration, timedelta]
    max_plan_time: OptionalProperty[std.duration, timedelta]
    mean_plan_time: OptionalProperty[std.duration, timedelta]
    stddev_plan_time: OptionalProperty[std.duration, timedelta]
    calls: OptionalProperty[std.int64, int]
    total_exec_time: OptionalProperty[std.duration, timedelta]
    min_exec_time: OptionalProperty[std.duration, timedelta]
    max_exec_time: OptionalProperty[std.duration, timedelta]
    mean_exec_time: OptionalProperty[std.duration, timedelta]
    stddev_exec_time: OptionalProperty[std.duration, timedelta]
    rows: OptionalProperty[std.int64, int]
    stats_since: OptionalProperty[std.datetime, datetime]
    minmax_stats_since: OptionalProperty[std.datetime, datetime]
    branch: OptionalLink[Branch]
def reset_query_stats(
    *,
    branch_name: type[___std__.str] | ___builtins__.str | None | UnspecifiedType = Unspecified,
    id: type[___std__.uuid] | UUID | None | UnspecifiedType = Unspecified,
    minmax_only: type[___std__.bool] | ___builtins_1__.bool | None | UnspecifiedType = Unspecified,
) -> type[___std__.datetime]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {
        "branch_name": branch_name,
        "id": id,
        "minmax_only": minmax_only,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        std.datetime,
        FuncCall(
            fname="sys::reset_query_stats",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'datetime'),
        )
    )

def get_version(
    
) -> type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        MajorMinorStageStage_noLocal_Tuple_SKRhXQ,
        FuncCall(
            fname="sys::get_version",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>'),
        )
    )

def get_version_as_str() -> type[___std__.str]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.str,
        FuncCall(
            fname="sys::get_version_as_str",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def get_instance_name() -> type[___std__.str]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.str,
        FuncCall(
            fname="sys::get_instance_name",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def get_transaction_isolation() -> type[___base__.TransactionIsolation]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        base.TransactionIsolation,
        FuncCall(
            fname="sys::get_transaction_isolation",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('sys', 'TransactionIsolation'),
        )
    )

def get_current_database() -> type[___std__.str]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.str,
        FuncCall(
            fname="sys::get_current_database",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def get_current_branch() -> type[___std__.str]:
    args: list[Any] = []
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.str,
        FuncCall(
            fname="sys::get_current_branch",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )



from ..__variants__ import std  # noqa: E402 F403
from ..__variants__.sys import (  # noqa: E402 F403
    OutputFormat,
    QueryType,
    TransactionAccessMode,
    TransactionDeferrability,
    TransactionIsolation,
    VersionStage
)
from ..std.__types__ import (  # noqa: E402 F403
    MajorMinorStageStage_noLocal_Tuple_SKRhXQ,
    MajorMinor_Tuple_K20e_g
)

from builtins import bool, int, str  # noqa: E402 F403
from datetime import datetime, timedelta  # noqa: E402 F403


__all__ = (
    'Branch',
    'ExtensionPackage',
    'ExtensionPackageMigration',
    'ExternalObject',
    'OutputFormat',
    'QueryStats',
    'QueryType',
    'Role',
    'SystemObject',
    'TransactionAccessMode',
    'TransactionDeferrability',
    'TransactionIsolation',
    'VersionStage',
)
