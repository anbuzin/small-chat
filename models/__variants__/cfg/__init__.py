#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std

import gel as gel
from gel import ConfigMemory
from gel.models import pydantic
from gel.models.pydantic import (
    AnnotatedExpr,
    AnyEnum,
    Cardinality,
    ComputedMultiLink,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    InfixOp,
    LazyClassProperty,
    MultiLink,
    MultiProperty,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    PointerKind,
    PyConstType,
    PyTypeScalar,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as ___builtins_3__
import builtins as ___builtins_2__
import builtins as ___builtins_1__
import builtins as ___builtins__
import datetime as datetime
from builtins import tuple, type
from collections.abc import Callable, Iterable
from typing import Any, Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as ___std__, sys as ___sys__
    from ... import cfg, schema

    from gel.models.pydantic import GelPointerReflection

    import builtins as builtins
    from builtins import dict, str
    from typing import ClassVar


class AllowBareDDL(AnyEnum):
    AlwaysAllow = 'AlwaysAllow'
    NeverAllow = 'NeverAllow'


class ConnectionTransport(AnyEnum):
    TCP = 'TCP'
    TCP_PG = 'TCP_PG'
    HTTP = 'HTTP'
    SIMPLE_HTTP = 'SIMPLE_HTTP'
    HTTP_METRICS = 'HTTP_METRICS'
    HTTP_HEALTH = 'HTTP_HEALTH'


class QueryCacheMode(AnyEnum):
    InMemory = 'InMemory'
    RegInline = 'RegInline'
    PgFunc = 'PgFunc'
    Default = 'Default'


class QueryStatsOption(AnyEnum):
    None_ = 'None'
    All = 'All'


class SMTPSecurity(AnyEnum):
    PlainText = 'PlainText'
    TLS = 'TLS'
    STARTTLS = 'STARTTLS'
    STARTTLSOrPlainText = 'STARTTLSOrPlainText'


class StoreMigrationSDL(AnyEnum):
    AlwaysStore = 'AlwaysStore'
    NeverStore = 'NeverStore'



class __memory_meta__(std.__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
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
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
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
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
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
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
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
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
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
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[___std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        rexpr: ExprCompatible = other
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=rexpr,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class memory(
        PyTypeScalar[ConfigMemory],
        std.anyscalar,
        metaclass=__memory_meta__,
    ):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=304)
            name = SchemaPath('cfg', 'memory')

if not TYPE_CHECKING:
    class memory(ConfigMemory, PyTypeScalar[ConfigMemory], std.anyscalar):
        __gel_type_class__: ClassVar[type] = __memory_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=304)
            name = SchemaPath('cfg', 'memory')




#
# type cfg::ConfigObject
#
class __ConfigObject_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=281837877222500969229845324319074851211)
        name = SchemaPath('cfg', 'ConfigObject')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | std.__BaseObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=281837877222500969229845324319074851211),
                name='cfg::ConfigObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __ConfigObject_typeof__(
    std.__BaseObject_typeof__,
    __ConfigObject_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        pass


class __ConfigObject_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __ConfigObject_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        pass


class ConfigObject(
    __ConfigObject_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=281837877222500969229845324319074851211),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new cfg::ConfigObject instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::ConfigObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::ConfigObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::ConfigObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __ConfigObject_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new cfg::ConfigObject instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::ConfigObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::ConfigObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::ConfigObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.BaseObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ConfigObject_typeof_partial__,
            Base,
            std.BaseObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.BaseObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="ConfigObject | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ConfigObject.__variants__.Base = ConfigObject



#
# type cfg::AbstractConfig
#
class __AbstractConfig_typeof_base__(__ConfigObject_typeof_base__):
    class __gel_reflection__(__ConfigObject_typeof_base__.__gel_reflection__):
        id = UUID(int=185296995099711029544002424773202172471)
        name = SchemaPath('cfg', 'AbstractConfig')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'default_transaction_access_mode': pydantic.GelPointerReflection(
                    name='default_transaction_access_mode',
                    type=SchemaPath('sys', 'TransactionAccessMode'),
                    typexpr='sys::TransactionAccessMode',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'session_idle_timeout': pydantic.GelPointerReflection(
                    name='session_idle_timeout',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'default_transaction_isolation': pydantic.GelPointerReflection(
                    name='default_transaction_isolation',
                    type=SchemaPath('sys', 'TransactionIsolation'),
                    typexpr='sys::TransactionIsolation',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'default_transaction_deferrable': pydantic.GelPointerReflection(
                    name='default_transaction_deferrable',
                    type=SchemaPath('sys', 'TransactionDeferrability'),
                    typexpr='sys::TransactionDeferrability',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'session_idle_transaction_timeout': pydantic.GelPointerReflection(
                    name='session_idle_transaction_timeout',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'query_execution_timeout': pydantic.GelPointerReflection(
                    name='query_execution_timeout',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'listen_port': pydantic.GelPointerReflection(
                    name='listen_port',
                    type=SchemaPath('std', 'int32'),
                    typexpr='std::int32',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'listen_addresses': pydantic.GelPointerReflection(
                    name='listen_addresses',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'current_email_provider_name': pydantic.GelPointerReflection(
                    name='current_email_provider_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'allow_dml_in_functions': pydantic.GelPointerReflection(
                    name='allow_dml_in_functions',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'allow_bare_ddl': pydantic.GelPointerReflection(
                    name='allow_bare_ddl',
                    type=SchemaPath('cfg', 'AllowBareDDL'),
                    typexpr='cfg::AllowBareDDL',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'store_migration_sdl': pydantic.GelPointerReflection(
                    name='store_migration_sdl',
                    type=SchemaPath('cfg', 'StoreMigrationSDL'),
                    typexpr='cfg::StoreMigrationSDL',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'apply_access_policies': pydantic.GelPointerReflection(
                    name='apply_access_policies',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'apply_access_policies_pg': pydantic.GelPointerReflection(
                    name='apply_access_policies_pg',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'allow_user_specified_id': pydantic.GelPointerReflection(
                    name='allow_user_specified_id',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'simple_scoping': pydantic.GelPointerReflection(
                    name='simple_scoping',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'warn_old_scoping': pydantic.GelPointerReflection(
                    name='warn_old_scoping',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'cors_allow_origins': pydantic.GelPointerReflection(
                    name='cors_allow_origins',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'auto_rebuild_query_cache': pydantic.GelPointerReflection(
                    name='auto_rebuild_query_cache',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'auto_rebuild_query_cache_timeout': pydantic.GelPointerReflection(
                    name='auto_rebuild_query_cache_timeout',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'query_cache_mode': pydantic.GelPointerReflection(
                    name='query_cache_mode',
                    type=SchemaPath('cfg', 'QueryCacheMode'),
                    typexpr='cfg::QueryCacheMode',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'http_max_connections': pydantic.GelPointerReflection(
                    name='http_max_connections',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'shared_buffers': pydantic.GelPointerReflection(
                    name='shared_buffers',
                    type=SchemaPath('cfg', 'memory'),
                    typexpr='cfg::memory',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'query_work_mem': pydantic.GelPointerReflection(
                    name='query_work_mem',
                    type=SchemaPath('cfg', 'memory'),
                    typexpr='cfg::memory',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'maintenance_work_mem': pydantic.GelPointerReflection(
                    name='maintenance_work_mem',
                    type=SchemaPath('cfg', 'memory'),
                    typexpr='cfg::memory',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'effective_cache_size': pydantic.GelPointerReflection(
                    name='effective_cache_size',
                    type=SchemaPath('cfg', 'memory'),
                    typexpr='cfg::memory',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'effective_io_concurrency': pydantic.GelPointerReflection(
                    name='effective_io_concurrency',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'default_statistics_target': pydantic.GelPointerReflection(
                    name='default_statistics_target',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'force_database_error': pydantic.GelPointerReflection(
                    name='force_database_error',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                '_pg_prepared_statement_cache_size': pydantic.GelPointerReflection(
                    name='_pg_prepared_statement_cache_size',
                    type=SchemaPath('std', 'int16'),
                    typexpr='std::int16',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'track_query_stats': pydantic.GelPointerReflection(
                    name='track_query_stats',
                    type=SchemaPath('cfg', 'QueryStatsOption'),
                    typexpr='cfg::QueryStatsOption',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'extensions': pydantic.GelPointerReflection(
                    name='extensions',
                    type=SchemaPath('cfg', 'ExtensionConfig'),
                    typexpr='cfg::ExtensionConfig',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=True,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'auth': pydantic.GelPointerReflection(
                    name='auth',
                    type=SchemaPath('cfg', 'Auth'),
                    typexpr='cfg::Auth',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'email_providers': pydantic.GelPointerReflection(
                    name='email_providers',
                    type=SchemaPath('cfg', 'EmailProviderConfig'),
                    typexpr='cfg::EmailProviderConfig',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=185296995099711029544002424773202172471),
                name='cfg::AbstractConfig',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AbstractConfig_typeof__(
    __ConfigObject_typeof__,
    __AbstractConfig_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof__.__typeof__):
        default_transaction_access_mode = TypeAliasType('default_transaction_access_mode', 'sys.TransactionAccessMode')
        session_idle_timeout = TypeAliasType('session_idle_timeout', 'std.duration')
        default_transaction_isolation = TypeAliasType('default_transaction_isolation', 'sys.TransactionIsolation')
        default_transaction_deferrable = TypeAliasType('default_transaction_deferrable', 'sys.TransactionDeferrability')
        session_idle_transaction_timeout = TypeAliasType('session_idle_transaction_timeout', 'std.duration')
        query_execution_timeout = TypeAliasType('query_execution_timeout', 'std.duration')
        listen_port = TypeAliasType('listen_port', 'std.int32')
        listen_addresses = TypeAliasType('listen_addresses', 'MultiProperty[std.str, ___builtins_1__.str]')
        current_email_provider_name = TypeAliasType('current_email_provider_name', 'OptionalProperty[std.str, ___builtins_1__.str]')
        allow_dml_in_functions = TypeAliasType('allow_dml_in_functions', 'OptionalProperty[std.bool, bool]')
        allow_bare_ddl = TypeAliasType('allow_bare_ddl', 'OptionalProperty[AllowBareDDL, ___builtins_1__.str]')
        store_migration_sdl = TypeAliasType('store_migration_sdl', 'OptionalProperty[StoreMigrationSDL, ___builtins_1__.str]')
        apply_access_policies = TypeAliasType('apply_access_policies', 'OptionalProperty[std.bool, bool]')
        apply_access_policies_pg = TypeAliasType('apply_access_policies_pg', 'OptionalProperty[std.bool, bool]')
        allow_user_specified_id = TypeAliasType('allow_user_specified_id', 'OptionalProperty[std.bool, bool]')
        simple_scoping = TypeAliasType('simple_scoping', 'OptionalProperty[std.bool, bool]')
        warn_old_scoping = TypeAliasType('warn_old_scoping', 'OptionalProperty[std.bool, bool]')
        cors_allow_origins = TypeAliasType('cors_allow_origins', 'MultiProperty[std.str, ___builtins_1__.str]')
        auto_rebuild_query_cache = TypeAliasType('auto_rebuild_query_cache', 'OptionalProperty[std.bool, bool]')
        auto_rebuild_query_cache_timeout = TypeAliasType('auto_rebuild_query_cache_timeout', 'OptionalProperty[std.duration, timedelta]')
        query_cache_mode = TypeAliasType('query_cache_mode', 'OptionalProperty[QueryCacheMode, ___builtins_1__.str]')
        http_max_connections = TypeAliasType('http_max_connections', 'OptionalProperty[std.int64, int]')
        shared_buffers = TypeAliasType('shared_buffers', 'OptionalProperty[memory, ConfigMemory]')
        query_work_mem = TypeAliasType('query_work_mem', 'OptionalProperty[memory, ConfigMemory]')
        maintenance_work_mem = TypeAliasType('maintenance_work_mem', 'OptionalProperty[memory, ConfigMemory]')
        effective_cache_size = TypeAliasType('effective_cache_size', 'OptionalProperty[memory, ConfigMemory]')
        effective_io_concurrency = TypeAliasType('effective_io_concurrency', 'OptionalProperty[std.int64, int]')
        default_statistics_target = TypeAliasType('default_statistics_target', 'OptionalProperty[std.int64, int]')
        force_database_error = TypeAliasType('force_database_error', 'OptionalProperty[std.str, ___builtins_1__.str]')
        _pg_prepared_statement_cache_size = TypeAliasType('_pg_prepared_statement_cache_size', 'std.int16')
        track_query_stats = TypeAliasType('track_query_stats', 'OptionalProperty[QueryStatsOption, ___builtins_1__.str]')
        extensions = TypeAliasType('extensions', 'ComputedMultiLink[ExtensionConfig]')
        auth = TypeAliasType('auth', 'MultiLink[Auth]')
        email_providers = TypeAliasType('email_providers', 'MultiLink[EmailProviderConfig]')


class __AbstractConfig_typeof_partial__(
    __ConfigObject_typeof_partial__,
    __AbstractConfig_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof_partial__.__typeof__):
        default_transaction_access_mode = TypeAliasType('default_transaction_access_mode', 'OptionalProperty[sys.TransactionAccessMode, ___builtins_1__.str]')
        session_idle_timeout = TypeAliasType('session_idle_timeout', 'OptionalProperty[std.duration, timedelta]')
        default_transaction_isolation = TypeAliasType('default_transaction_isolation', 'OptionalProperty[sys.TransactionIsolation, ___builtins_1__.str]')
        default_transaction_deferrable = TypeAliasType('default_transaction_deferrable', 'OptionalProperty[sys.TransactionDeferrability, ___builtins_1__.str]')
        session_idle_transaction_timeout = TypeAliasType('session_idle_transaction_timeout', 'OptionalProperty[std.duration, timedelta]')
        query_execution_timeout = TypeAliasType('query_execution_timeout', 'OptionalProperty[std.duration, timedelta]')
        listen_port = TypeAliasType('listen_port', 'OptionalProperty[std.int32, int]')
        listen_addresses = TypeAliasType('listen_addresses', 'MultiProperty[std.str, ___builtins_1__.str]')
        current_email_provider_name = TypeAliasType('current_email_provider_name', 'OptionalProperty[std.str, ___builtins_1__.str]')
        allow_dml_in_functions = TypeAliasType('allow_dml_in_functions', 'OptionalProperty[std.bool, bool]')
        allow_bare_ddl = TypeAliasType('allow_bare_ddl', 'OptionalProperty[AllowBareDDL, ___builtins_1__.str]')
        store_migration_sdl = TypeAliasType('store_migration_sdl', 'OptionalProperty[StoreMigrationSDL, ___builtins_1__.str]')
        apply_access_policies = TypeAliasType('apply_access_policies', 'OptionalProperty[std.bool, bool]')
        apply_access_policies_pg = TypeAliasType('apply_access_policies_pg', 'OptionalProperty[std.bool, bool]')
        allow_user_specified_id = TypeAliasType('allow_user_specified_id', 'OptionalProperty[std.bool, bool]')
        simple_scoping = TypeAliasType('simple_scoping', 'OptionalProperty[std.bool, bool]')
        warn_old_scoping = TypeAliasType('warn_old_scoping', 'OptionalProperty[std.bool, bool]')
        cors_allow_origins = TypeAliasType('cors_allow_origins', 'MultiProperty[std.str, ___builtins_1__.str]')
        auto_rebuild_query_cache = TypeAliasType('auto_rebuild_query_cache', 'OptionalProperty[std.bool, bool]')
        auto_rebuild_query_cache_timeout = TypeAliasType('auto_rebuild_query_cache_timeout', 'OptionalProperty[std.duration, timedelta]')
        query_cache_mode = TypeAliasType('query_cache_mode', 'OptionalProperty[QueryCacheMode, ___builtins_1__.str]')
        http_max_connections = TypeAliasType('http_max_connections', 'OptionalProperty[std.int64, int]')
        shared_buffers = TypeAliasType('shared_buffers', 'OptionalProperty[memory, ConfigMemory]')
        query_work_mem = TypeAliasType('query_work_mem', 'OptionalProperty[memory, ConfigMemory]')
        maintenance_work_mem = TypeAliasType('maintenance_work_mem', 'OptionalProperty[memory, ConfigMemory]')
        effective_cache_size = TypeAliasType('effective_cache_size', 'OptionalProperty[memory, ConfigMemory]')
        effective_io_concurrency = TypeAliasType('effective_io_concurrency', 'OptionalProperty[std.int64, int]')
        default_statistics_target = TypeAliasType('default_statistics_target', 'OptionalProperty[std.int64, int]')
        force_database_error = TypeAliasType('force_database_error', 'OptionalProperty[std.str, ___builtins_1__.str]')
        _pg_prepared_statement_cache_size = TypeAliasType('_pg_prepared_statement_cache_size', 'OptionalProperty[std.int16, int]')
        track_query_stats = TypeAliasType('track_query_stats', 'OptionalProperty[QueryStatsOption, ___builtins_1__.str]')
        extensions = TypeAliasType('extensions', 'ComputedMultiLink[ExtensionConfig | ExtensionConfig.__variants__.Partial]')
        auth = TypeAliasType('auth', 'MultiLink[Auth | Auth.__variants__.Partial]')
        email_providers = TypeAliasType('email_providers', 'MultiLink[EmailProviderConfig | EmailProviderConfig.__variants__.Partial]')


class AbstractConfig(
    __AbstractConfig_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=185296995099711029544002424773202172471),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            query_execution_timeout: timedelta,
            listen_port: int | DefaultValue = DEFAULT_VALUE,
            listen_addresses: Iterable[___builtins_1__.str] = [],
            current_email_provider_name: ___builtins_1__.str | None = None,
            allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[___builtins_1__.str] = [],
            auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
            auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
            query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
            track_query_stats: ___builtins_1__.str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::AbstractConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::AbstractConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::AbstractConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::AbstractConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(
            __AbstractConfig_typeof__,
            ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    query_execution_timeout: timedelta,
                    listen_port: int | DefaultValue = DEFAULT_VALUE,
                    listen_addresses: Iterable[___builtins_1__.str] = [],
                    current_email_provider_name: ___builtins_1__.str | None = None,
                    allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[___builtins_1__.str] = [],
                    auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
                    auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
                    query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
                    track_query_stats: ___builtins_1__.str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::AbstractConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::AbstractConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::AbstractConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::AbstractConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            default_transaction_access_mode: sys.TransactionAccessMode
            session_idle_timeout: std.duration
            default_transaction_isolation: sys.TransactionIsolation
            default_transaction_deferrable: sys.TransactionDeferrability
            session_idle_transaction_timeout: std.duration
            query_execution_timeout: std.duration
            listen_port: std.int32
            _pg_prepared_statement_cache_size: std.int16

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AbstractConfig_typeof_partial__,
            Base,
            ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            default_transaction_access_mode: OptionalProperty[sys.TransactionAccessMode, ___builtins_1__.str]
            session_idle_timeout: OptionalProperty[std.duration, timedelta]
            default_transaction_isolation: OptionalProperty[sys.TransactionIsolation, ___builtins_1__.str]
            default_transaction_deferrable: OptionalProperty[sys.TransactionDeferrability, ___builtins_1__.str]
            session_idle_transaction_timeout: OptionalProperty[std.duration, timedelta]
            query_execution_timeout: OptionalProperty[std.duration, timedelta]
            listen_port: OptionalProperty[std.int32, int]
            listen_addresses: MultiProperty[std.str, ___builtins_1__.str]
            current_email_provider_name: OptionalProperty[std.str, ___builtins_1__.str]
            allow_dml_in_functions: OptionalProperty[std.bool, bool]
            allow_bare_ddl: OptionalProperty[AllowBareDDL, ___builtins_1__.str]
            store_migration_sdl: OptionalProperty[StoreMigrationSDL, ___builtins_1__.str]
            apply_access_policies: OptionalProperty[std.bool, bool]
            apply_access_policies_pg: OptionalProperty[std.bool, bool]
            allow_user_specified_id: OptionalProperty[std.bool, bool]
            simple_scoping: OptionalProperty[std.bool, bool]
            warn_old_scoping: OptionalProperty[std.bool, bool]
            cors_allow_origins: MultiProperty[std.str, ___builtins_1__.str]
            auto_rebuild_query_cache: OptionalProperty[std.bool, bool]
            auto_rebuild_query_cache_timeout: OptionalProperty[std.duration, timedelta]
            query_cache_mode: OptionalProperty[QueryCacheMode, ___builtins_1__.str]
            http_max_connections: OptionalProperty[std.int64, int]
            shared_buffers: OptionalProperty[memory, ConfigMemory]
            query_work_mem: OptionalProperty[memory, ConfigMemory]
            maintenance_work_mem: OptionalProperty[memory, ConfigMemory]
            effective_cache_size: OptionalProperty[memory, ConfigMemory]
            effective_io_concurrency: OptionalProperty[std.int64, int]
            default_statistics_target: OptionalProperty[std.int64, int]
            force_database_error: OptionalProperty[std.str, ___builtins_1__.str]
            _pg_prepared_statement_cache_size: OptionalProperty[std.int16, int]
            track_query_stats: OptionalProperty[QueryStatsOption, ___builtins_1__.str]
            extensions: ComputedMultiLink[___cfg__.ExtensionConfig | ___cfg__.ExtensionConfig.__variants__.Partial]
            auth: MultiLink[___cfg__.Auth | ___cfg__.Auth.__variants__.Partial]
            email_providers: MultiLink[___cfg__.EmailProviderConfig | ___cfg__.EmailProviderConfig.__variants__.Partial]


        Any = TypeVar("Any", bound="AbstractConfig | Base | Required | Partial")
    class __links__(ConfigObject.__links__):
        pass
    class __links_partial__(ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    AbstractConfig.__variants__.Base = AbstractConfig



#
# type cfg::Auth
#
class __Auth_typeof_base__(__ConfigObject_typeof_base__):
    class __gel_reflection__(__ConfigObject_typeof_base__.__gel_reflection__):
        id = UUID(int=216303077383272593199434166037523439239)
        name = SchemaPath('cfg', 'Auth')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'priority': pydantic.GelPointerReflection(
                    name='priority',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'user': pydantic.GelPointerReflection(
                    name='user',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'comment': pydantic.GelPointerReflection(
                    name='comment',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'method': pydantic.GelPointerReflection(
                    name='method',
                    type=SchemaPath('cfg', 'AuthMethod'),
                    typexpr='cfg::AuthMethod',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=216303077383272593199434166037523439239),
                name='cfg::Auth',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Auth_typeof__(__ConfigObject_typeof__, __Auth_typeof_base__):
    class __typeof__(__ConfigObject_typeof__.__typeof__):
        priority = TypeAliasType('priority', 'std.int64')
        user = TypeAliasType('user', 'MultiProperty[std.str, ___builtins_1__.str]')
        comment = TypeAliasType('comment', 'OptionalProperty[std.str, ___builtins_1__.str]')
        method = TypeAliasType('method', 'OptionalLink[AuthMethod]')


class __Auth_typeof_partial__(
    __ConfigObject_typeof_partial__,
    __Auth_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof_partial__.__typeof__):
        priority = TypeAliasType('priority', 'OptionalProperty[std.int64, int]')
        user = TypeAliasType('user', 'MultiProperty[std.str, ___builtins_1__.str]')
        comment = TypeAliasType('comment', 'OptionalProperty[std.str, ___builtins_1__.str]')
        method = TypeAliasType('method', 'OptionalLink[AuthMethod | AuthMethod.__variants__.Partial]')


class Auth(
    __Auth_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=216303077383272593199434166037523439239),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            priority: int,
            user: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
            comment: ___builtins_1__.str | None = None,
            method: AuthMethod | None = None,
        ) -> None:
            """Create a new cfg::Auth instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::Auth instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            priority: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            user: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            comment: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            method: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Auth instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            priority: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            user: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            comment: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            method: type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Auth instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            priority: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            user: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            comment: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(
            __Auth_typeof__,
            ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    priority: int,
                    user: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
                    comment: ___builtins_1__.str | None = None,
                    method: AuthMethod | None = None,
                ) -> None:
                    """Create a new cfg::Auth instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::Auth instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    priority: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    user: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    comment: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    method: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Auth instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    priority: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    user: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    comment: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    method: type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Auth instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    priority: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    user: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    comment: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            priority: std.int64

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Auth_typeof_partial__,
            Base,
            ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            priority: OptionalProperty[std.int64, int]
            user: MultiProperty[std.str, ___builtins_1__.str]
            comment: OptionalProperty[std.str, ___builtins_1__.str]
            method: OptionalLink[___cfg__.AuthMethod | ___cfg__.AuthMethod.__variants__.Partial]


        Any = TypeVar("Any", bound="Auth | Base | Required | Partial")
    class __links__(ConfigObject.__links__):
        pass
    class __links_partial__(ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    Auth.__variants__.Base = Auth



#
# type cfg::AuthMethod
#
class __AuthMethod_typeof_base__(__ConfigObject_typeof_base__):
    class __gel_reflection__(__ConfigObject_typeof_base__.__gel_reflection__):
        id = UUID(int=24672750186835429802611635273495390145)
        name = SchemaPath('cfg', 'AuthMethod')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'transports': pydantic.GelPointerReflection(
                    name='transports',
                    type=SchemaPath('cfg', 'ConnectionTransport'),
                    typexpr='cfg::ConnectionTransport',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=24672750186835429802611635273495390145),
                name='cfg::AuthMethod',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AuthMethod_typeof__(
    __ConfigObject_typeof__,
    __AuthMethod_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class __AuthMethod_typeof_partial__(
    __ConfigObject_typeof_partial__,
    __AuthMethod_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof_partial__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class AuthMethod(
    __AuthMethod_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=24672750186835429802611635273495390145),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            transports: Iterable[___builtins_1__.str] = [],
        ) -> None:
            """Create a new cfg::AuthMethod instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::AuthMethod instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::AuthMethod instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::AuthMethod instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(
            __AuthMethod_typeof__,
            ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[___builtins_1__.str] = [],
                ) -> None:
                    """Create a new cfg::AuthMethod instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::AuthMethod instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::AuthMethod instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::AuthMethod instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AuthMethod_typeof_partial__,
            Base,
            ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            transports: MultiProperty[ConnectionTransport, ___builtins_1__.str]


        Any = TypeVar("Any", bound="AuthMethod | Base | Required | Partial")
    class __links__(ConfigObject.__links__):
        pass
    class __links_partial__(ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    AuthMethod.__variants__.Base = AuthMethod



#
# type cfg::EmailProviderConfig
#
class __EmailProviderConfig_typeof_base__(__ConfigObject_typeof_base__):
    class __gel_reflection__(__ConfigObject_typeof_base__.__gel_reflection__):
        id = UUID(int=16835018147630535051531832564638176924)
        name = SchemaPath('cfg', 'EmailProviderConfig')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'name': pydantic.GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=16835018147630535051531832564638176924),
                name='cfg::EmailProviderConfig',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __EmailProviderConfig_typeof__(
    __ConfigObject_typeof__,
    __EmailProviderConfig_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')


class __EmailProviderConfig_typeof_partial__(
    __ConfigObject_typeof_partial__,
    __EmailProviderConfig_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins_1__.str]')


class EmailProviderConfig(
    __EmailProviderConfig_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=16835018147630535051531832564638176924),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, name: ___builtins_1__.str) -> None:
            """Create a new cfg::EmailProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::EmailProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::EmailProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::EmailProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(
            __EmailProviderConfig_typeof__,
            ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self, /, *, name: ___builtins_1__.str) -> None:
                    """Create a new cfg::EmailProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::EmailProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::EmailProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::EmailProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: std.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __EmailProviderConfig_typeof_partial__,
            Base,
            ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[std.str, ___builtins_1__.str]


        Any = TypeVar("Any", bound="EmailProviderConfig | Base | Required | Partial")
    class __links__(ConfigObject.__links__):
        pass
    class __links_partial__(ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    EmailProviderConfig.__variants__.Base = EmailProviderConfig



#
# type cfg::ExtensionConfig
#
class __ExtensionConfig_typeof_base__(__ConfigObject_typeof_base__):
    class __gel_reflection__(__ConfigObject_typeof_base__.__gel_reflection__):
        id = UUID(int=183410656785745777641344889607547842952)
        name = SchemaPath('cfg', 'ExtensionConfig')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'cfg': pydantic.GelPointerReflection(
                    name='cfg',
                    type=SchemaPath('cfg', 'AbstractConfig'),
                    typexpr='cfg::AbstractConfig',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=183410656785745777641344889607547842952),
                name='cfg::ExtensionConfig',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __ExtensionConfig_typeof__(
    __ConfigObject_typeof__,
    __ExtensionConfig_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof__.__typeof__):
        cfg = TypeAliasType('cfg', 'AbstractConfig')


class __ExtensionConfig_typeof_partial__(
    __ConfigObject_typeof_partial__,
    __ExtensionConfig_typeof_base__,
):
    class __typeof__(__ConfigObject_typeof_partial__.__typeof__):
        cfg = TypeAliasType('cfg', 'AbstractConfig | AbstractConfig.__variants__.Partial')


class ExtensionConfig(
    __ExtensionConfig_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=183410656785745777641344889607547842952),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, cfg: AbstractConfig | None = None) -> None:
            """Create a new cfg::ExtensionConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::ExtensionConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::ExtensionConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::ExtensionConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(
            __ExtensionConfig_typeof__,
            ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    cfg: AbstractConfig | None = None,
                ) -> None:
                    """Create a new cfg::ExtensionConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::ExtensionConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::ExtensionConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::ExtensionConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            cfg: ___cfg__.AbstractConfig

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ExtensionConfig_typeof_partial__,
            Base,
            ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            cfg: ___cfg__.AbstractConfig | ___cfg__.AbstractConfig.__variants__.Partial


        Any = TypeVar("Any", bound="ExtensionConfig | Base | Required | Partial")
    class __links__(ConfigObject.__links__):
        pass
    class __links_partial__(ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ExtensionConfig.__variants__.Base = ExtensionConfig



#
# type cfg::Config
#
class __Config_typeof_base__(__AbstractConfig_typeof_base__):
    class __gel_reflection__(
        __AbstractConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=72033782817016315085961485882846453927)
        name = SchemaPath('cfg', 'Config')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | __AbstractConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=72033782817016315085961485882846453927),
                name='cfg::Config',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Config_typeof__(__AbstractConfig_typeof__, __Config_typeof_base__):
    class __typeof__(__AbstractConfig_typeof__.__typeof__):
        pass


class __Config_typeof_partial__(
    __AbstractConfig_typeof_partial__,
    __Config_typeof_base__,
):
    class __typeof__(__AbstractConfig_typeof_partial__.__typeof__):
        pass


class Config(
    __Config_typeof__,
    AbstractConfig,
    __gel_type_id__=UUID(int=72033782817016315085961485882846453927),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            query_execution_timeout: timedelta,
            listen_port: int | DefaultValue = DEFAULT_VALUE,
            listen_addresses: Iterable[___builtins_1__.str] = [],
            current_email_provider_name: ___builtins_1__.str | None = None,
            allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[___builtins_1__.str] = [],
            auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
            auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
            query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
            track_query_stats: ___builtins_1__.str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::Config instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::Config instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Config instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Config instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AbstractConfig.__variants__):
        class Base(
            __Config_typeof__,
            AbstractConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    query_execution_timeout: timedelta,
                    listen_port: int | DefaultValue = DEFAULT_VALUE,
                    listen_addresses: Iterable[___builtins_1__.str] = [],
                    current_email_provider_name: ___builtins_1__.str | None = None,
                    allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[___builtins_1__.str] = [],
                    auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
                    auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
                    query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
                    track_query_stats: ___builtins_1__.str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::Config instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::Config instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Config instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Config instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AbstractConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Config_typeof_partial__,
            Base,
            AbstractConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AbstractConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="Config | Base | Required | Partial")
    class __links__(AbstractConfig.__links__):
        pass
    class __links_partial__(AbstractConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    Config.__variants__.Base = Config



#
# type cfg::DatabaseConfig
#
class __DatabaseConfig_typeof_base__(__AbstractConfig_typeof_base__):
    class __gel_reflection__(
        __AbstractConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=255578330159211281383176570602312393311)
        name = SchemaPath('cfg', 'DatabaseConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | __AbstractConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=255578330159211281383176570602312393311),
                name='cfg::DatabaseConfig',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __DatabaseConfig_typeof__(
    __AbstractConfig_typeof__,
    __DatabaseConfig_typeof_base__,
):
    class __typeof__(__AbstractConfig_typeof__.__typeof__):
        pass


class __DatabaseConfig_typeof_partial__(
    __AbstractConfig_typeof_partial__,
    __DatabaseConfig_typeof_base__,
):
    class __typeof__(__AbstractConfig_typeof_partial__.__typeof__):
        pass


class DatabaseConfig(
    __DatabaseConfig_typeof__,
    AbstractConfig,
    __gel_type_id__=UUID(int=255578330159211281383176570602312393311),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            query_execution_timeout: timedelta,
            listen_port: int | DefaultValue = DEFAULT_VALUE,
            listen_addresses: Iterable[___builtins_1__.str] = [],
            current_email_provider_name: ___builtins_1__.str | None = None,
            allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[___builtins_1__.str] = [],
            auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
            auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
            query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
            track_query_stats: ___builtins_1__.str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::DatabaseConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::DatabaseConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::DatabaseConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::DatabaseConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AbstractConfig.__variants__):
        class Base(
            __DatabaseConfig_typeof__,
            AbstractConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    query_execution_timeout: timedelta,
                    listen_port: int | DefaultValue = DEFAULT_VALUE,
                    listen_addresses: Iterable[___builtins_1__.str] = [],
                    current_email_provider_name: ___builtins_1__.str | None = None,
                    allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[___builtins_1__.str] = [],
                    auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
                    auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
                    query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
                    track_query_stats: ___builtins_1__.str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::DatabaseConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::DatabaseConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::DatabaseConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::DatabaseConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AbstractConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __DatabaseConfig_typeof_partial__,
            Base,
            AbstractConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AbstractConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="DatabaseConfig | Base | Required | Partial")
    class __links__(AbstractConfig.__links__):
        pass
    class __links_partial__(AbstractConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    DatabaseConfig.__variants__.Base = DatabaseConfig



#
# type cfg::InstanceConfig
#
class __InstanceConfig_typeof_base__(__AbstractConfig_typeof_base__):
    class __gel_reflection__(
        __AbstractConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=289657214145582360006880454642360258952)
        name = SchemaPath('cfg', 'InstanceConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | __AbstractConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=289657214145582360006880454642360258952),
                name='cfg::InstanceConfig',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __InstanceConfig_typeof__(
    __AbstractConfig_typeof__,
    __InstanceConfig_typeof_base__,
):
    class __typeof__(__AbstractConfig_typeof__.__typeof__):
        pass


class __InstanceConfig_typeof_partial__(
    __AbstractConfig_typeof_partial__,
    __InstanceConfig_typeof_base__,
):
    class __typeof__(__AbstractConfig_typeof_partial__.__typeof__):
        pass


class InstanceConfig(
    __InstanceConfig_typeof__,
    AbstractConfig,
    __gel_type_id__=UUID(int=289657214145582360006880454642360258952),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
            query_execution_timeout: timedelta,
            listen_port: int | DefaultValue = DEFAULT_VALUE,
            listen_addresses: Iterable[___builtins_1__.str] = [],
            current_email_provider_name: ___builtins_1__.str | None = None,
            allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
            apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
            allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[___builtins_1__.str] = [],
            auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
            auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
            query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
            _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
            track_query_stats: ___builtins_1__.str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::InstanceConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::InstanceConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::InstanceConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::InstanceConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AbstractConfig.__variants__):
        class Base(
            __InstanceConfig_typeof__,
            AbstractConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    default_transaction_isolation: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    default_transaction_deferrable: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    session_idle_transaction_timeout: timedelta | DefaultValue = DEFAULT_VALUE,
                    query_execution_timeout: timedelta,
                    listen_port: int | DefaultValue = DEFAULT_VALUE,
                    listen_addresses: Iterable[___builtins_1__.str] = [],
                    current_email_provider_name: ___builtins_1__.str | None = None,
                    allow_dml_in_functions: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_bare_ddl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    store_migration_sdl: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies: bool | None | DefaultValue = DEFAULT_VALUE,
                    apply_access_policies_pg: bool | None | DefaultValue = DEFAULT_VALUE,
                    allow_user_specified_id: bool | None | DefaultValue = DEFAULT_VALUE,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[___builtins_1__.str] = [],
                    auto_rebuild_query_cache: bool | None | DefaultValue = DEFAULT_VALUE,
                    auto_rebuild_query_cache_timeout: timedelta | None | DefaultValue = DEFAULT_VALUE,
                    query_cache_mode: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    http_max_connections: int | None | DefaultValue = DEFAULT_VALUE,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: ___builtins_1__.str | None | DefaultValue = DEFAULT_VALUE,
                    _pg_prepared_statement_cache_size: int | DefaultValue = DEFAULT_VALUE,
                    track_query_stats: ___builtins_1__.str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::InstanceConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::InstanceConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::InstanceConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[___sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[___sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[___sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: ___builtins_2__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: ___builtins_2__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::InstanceConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AbstractConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __InstanceConfig_typeof_partial__,
            Base,
            AbstractConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AbstractConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="InstanceConfig | Base | Required | Partial")
    class __links__(AbstractConfig.__links__):
        pass
    class __links_partial__(AbstractConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    InstanceConfig.__variants__.Base = InstanceConfig



#
# type cfg::JWT
#
class __JWT_typeof_base__(__AuthMethod_typeof_base__):
    class __gel_reflection__(__AuthMethod_typeof_base__.__gel_reflection__):
        id = UUID(int=104309744397328972677767160567727635579)
        name = SchemaPath('cfg', 'JWT')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'transports': pydantic.GelPointerReflection(
                    name='transports',
                    type=SchemaPath('cfg', 'ConnectionTransport'),
                    typexpr='cfg::ConnectionTransport',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __AuthMethod_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=104309744397328972677767160567727635579),
                name='cfg::JWT',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __JWT_typeof__(__AuthMethod_typeof__, __JWT_typeof_base__):
    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class __JWT_typeof_partial__(
    __AuthMethod_typeof_partial__,
    __JWT_typeof_base__,
):
    class __typeof__(__AuthMethod_typeof_partial__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class JWT(
    __JWT_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=104309744397328972677767160567727635579),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new cfg::JWT instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::JWT instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::JWT instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::JWT instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(
            __JWT_typeof__,
            AuthMethod.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new cfg::JWT instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::JWT instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::JWT instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::JWT instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AuthMethod.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __JWT_typeof_partial__,
            Base,
            AuthMethod.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AuthMethod.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            transports: MultiProperty[ConnectionTransport, ___builtins_1__.str]


        Any = TypeVar("Any", bound="JWT | Base | Required | Partial")
    class __links__(AuthMethod.__links__):
        pass
    class __links_partial__(AuthMethod.__links_partial__):
        pass

if not TYPE_CHECKING:
    JWT.__variants__.Base = JWT



#
# type cfg::Password
#
class __Password_typeof_base__(__AuthMethod_typeof_base__):
    class __gel_reflection__(__AuthMethod_typeof_base__.__gel_reflection__):
        id = UUID(int=209980488735293693782775477209127049182)
        name = SchemaPath('cfg', 'Password')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'transports': pydantic.GelPointerReflection(
                    name='transports',
                    type=SchemaPath('cfg', 'ConnectionTransport'),
                    typexpr='cfg::ConnectionTransport',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __AuthMethod_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=209980488735293693782775477209127049182),
                name='cfg::Password',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Password_typeof__(__AuthMethod_typeof__, __Password_typeof_base__):
    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class __Password_typeof_partial__(
    __AuthMethod_typeof_partial__,
    __Password_typeof_base__,
):
    class __typeof__(__AuthMethod_typeof_partial__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class Password(
    __Password_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=209980488735293693782775477209127049182),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new cfg::Password instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::Password instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Password instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Password instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(
            __Password_typeof__,
            AuthMethod.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new cfg::Password instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::Password instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Password instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Password instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AuthMethod.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Password_typeof_partial__,
            Base,
            AuthMethod.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AuthMethod.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            transports: MultiProperty[ConnectionTransport, ___builtins_1__.str]


        Any = TypeVar("Any", bound="Password | Base | Required | Partial")
    class __links__(AuthMethod.__links__):
        pass
    class __links_partial__(AuthMethod.__links_partial__):
        pass

if not TYPE_CHECKING:
    Password.__variants__.Base = Password



#
# type cfg::SCRAM
#
class __SCRAM_typeof_base__(__AuthMethod_typeof_base__):
    class __gel_reflection__(__AuthMethod_typeof_base__.__gel_reflection__):
        id = UUID(int=268855757711039848843614875827541315364)
        name = SchemaPath('cfg', 'SCRAM')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'transports': pydantic.GelPointerReflection(
                    name='transports',
                    type=SchemaPath('cfg', 'ConnectionTransport'),
                    typexpr='cfg::ConnectionTransport',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __AuthMethod_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=268855757711039848843614875827541315364),
                name='cfg::SCRAM',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __SCRAM_typeof__(__AuthMethod_typeof__, __SCRAM_typeof_base__):
    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class __SCRAM_typeof_partial__(
    __AuthMethod_typeof_partial__,
    __SCRAM_typeof_base__,
):
    class __typeof__(__AuthMethod_typeof_partial__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class SCRAM(
    __SCRAM_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=268855757711039848843614875827541315364),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new cfg::SCRAM instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::SCRAM instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::SCRAM instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::SCRAM instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(
            __SCRAM_typeof__,
            AuthMethod.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new cfg::SCRAM instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::SCRAM instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::SCRAM instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::SCRAM instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AuthMethod.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __SCRAM_typeof_partial__,
            Base,
            AuthMethod.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AuthMethod.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            transports: MultiProperty[ConnectionTransport, ___builtins_1__.str]


        Any = TypeVar("Any", bound="SCRAM | Base | Required | Partial")
    class __links__(AuthMethod.__links__):
        pass
    class __links_partial__(AuthMethod.__links_partial__):
        pass

if not TYPE_CHECKING:
    SCRAM.__variants__.Base = SCRAM



#
# type cfg::Trust
#
class __Trust_typeof_base__(__AuthMethod_typeof_base__):
    class __gel_reflection__(__AuthMethod_typeof_base__.__gel_reflection__):
        id = UUID(int=169812016296800753534565771606745733954)
        name = SchemaPath('cfg', 'Trust')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | __AuthMethod_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=169812016296800753534565771606745733954),
                name='cfg::Trust',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Trust_typeof__(__AuthMethod_typeof__, __Trust_typeof_base__):
    class __typeof__(__AuthMethod_typeof__.__typeof__):
        pass


class __Trust_typeof_partial__(
    __AuthMethod_typeof_partial__,
    __Trust_typeof_base__,
):
    class __typeof__(__AuthMethod_typeof_partial__.__typeof__):
        pass


class Trust(
    __Trust_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=169812016296800753534565771606745733954),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            transports: Iterable[___builtins_1__.str] = [],
        ) -> None:
            """Create a new cfg::Trust instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::Trust instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Trust instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Trust instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(
            __Trust_typeof__,
            AuthMethod.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[___builtins_1__.str] = [],
                ) -> None:
                    """Create a new cfg::Trust instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::Trust instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Trust instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Trust instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AuthMethod.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Trust_typeof_partial__,
            Base,
            AuthMethod.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AuthMethod.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="Trust | Base | Required | Partial")
    class __links__(AuthMethod.__links__):
        pass
    class __links_partial__(AuthMethod.__links_partial__):
        pass

if not TYPE_CHECKING:
    Trust.__variants__.Base = Trust



#
# type cfg::mTLS
#
class __mTLS_typeof_base__(__AuthMethod_typeof_base__):
    class __gel_reflection__(__AuthMethod_typeof_base__.__gel_reflection__):
        id = UUID(int=310279763571120869801632341122484800782)
        name = SchemaPath('cfg', 'mTLS')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'transports': pydantic.GelPointerReflection(
                    name='transports',
                    type=SchemaPath('cfg', 'ConnectionTransport'),
                    typexpr='cfg::ConnectionTransport',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __AuthMethod_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=310279763571120869801632341122484800782),
                name='cfg::mTLS',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __mTLS_typeof__(__AuthMethod_typeof__, __mTLS_typeof_base__):
    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class __mTLS_typeof_partial__(
    __AuthMethod_typeof_partial__,
    __mTLS_typeof_base__,
):
    class __typeof__(__AuthMethod_typeof_partial__.__typeof__):
        transports = TypeAliasType('transports', 'MultiProperty[ConnectionTransport, ___builtins_1__.str]')


class mTLS(
    __mTLS_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=310279763571120869801632341122484800782),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new cfg::mTLS instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update cfg::mTLS instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::mTLS instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::mTLS instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(
            __mTLS_typeof__,
            AuthMethod.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[___builtins_1__.str] | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new cfg::mTLS instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update cfg::mTLS instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::mTLS instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::mTLS instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            AuthMethod.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __mTLS_typeof_partial__,
            Base,
            AuthMethod.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            AuthMethod.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            transports: MultiProperty[ConnectionTransport, ___builtins_1__.str]


        Any = TypeVar("Any", bound="mTLS | Base | Required | Partial")
    class __links__(AuthMethod.__links__):
        pass
    class __links_partial__(AuthMethod.__links_partial__):
        pass

if not TYPE_CHECKING:
    mTLS.__variants__.Base = mTLS



#
# type cfg::SMTPProviderConfig
#
class __SMTPProviderConfig_typeof_base__(__EmailProviderConfig_typeof_base__):
    class __gel_reflection__(
        __EmailProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=108468146439474883053972930104863702727)
        name = SchemaPath('cfg', 'SMTPProviderConfig')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'sender': pydantic.GelPointerReflection(
                    name='sender',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'host': pydantic.GelPointerReflection(
                    name='host',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'port': pydantic.GelPointerReflection(
                    name='port',
                    type=SchemaPath('std', 'int32'),
                    typexpr='std::int32',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'username': pydantic.GelPointerReflection(
                    name='username',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'password': pydantic.GelPointerReflection(
                    name='password',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'security': pydantic.GelPointerReflection(
                    name='security',
                    type=SchemaPath('cfg', 'SMTPSecurity'),
                    typexpr='cfg::SMTPSecurity',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'validate_certs': pydantic.GelPointerReflection(
                    name='validate_certs',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'timeout_per_email': pydantic.GelPointerReflection(
                    name='timeout_per_email',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'timeout_per_attempt': pydantic.GelPointerReflection(
                    name='timeout_per_attempt',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __EmailProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=108468146439474883053972930104863702727),
                name='cfg::SMTPProviderConfig',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __SMTPProviderConfig_typeof__(
    __EmailProviderConfig_typeof__,
    __SMTPProviderConfig_typeof_base__,
):
    class __typeof__(__EmailProviderConfig_typeof__.__typeof__):
        sender = TypeAliasType('sender', 'OptionalProperty[std.str, ___builtins_1__.str]')
        host = TypeAliasType('host', 'OptionalProperty[std.str, ___builtins_1__.str]')
        port = TypeAliasType('port', 'OptionalProperty[std.int32, int]')
        username = TypeAliasType('username', 'OptionalProperty[std.str, ___builtins_1__.str]')
        password = TypeAliasType('password', 'OptionalProperty[std.str, ___builtins_1__.str]')
        security = TypeAliasType('security', 'SMTPSecurity')
        validate_certs = TypeAliasType('validate_certs', 'std.bool')
        timeout_per_email = TypeAliasType('timeout_per_email', 'std.duration')
        timeout_per_attempt = TypeAliasType('timeout_per_attempt', 'std.duration')


class __SMTPProviderConfig_typeof_partial__(
    __EmailProviderConfig_typeof_partial__,
    __SMTPProviderConfig_typeof_base__,
):
    class __typeof__(__EmailProviderConfig_typeof_partial__.__typeof__):
        sender = TypeAliasType('sender', 'OptionalProperty[std.str, ___builtins_1__.str]')
        host = TypeAliasType('host', 'OptionalProperty[std.str, ___builtins_1__.str]')
        port = TypeAliasType('port', 'OptionalProperty[std.int32, int]')
        username = TypeAliasType('username', 'OptionalProperty[std.str, ___builtins_1__.str]')
        password = TypeAliasType('password', 'OptionalProperty[std.str, ___builtins_1__.str]')
        security = TypeAliasType('security', 'OptionalProperty[SMTPSecurity, ___builtins_1__.str]')
        validate_certs = TypeAliasType('validate_certs', 'OptionalProperty[std.bool, bool]')
        timeout_per_email = TypeAliasType('timeout_per_email', 'OptionalProperty[std.duration, timedelta]')
        timeout_per_attempt = TypeAliasType('timeout_per_attempt', 'OptionalProperty[std.duration, timedelta]')


class SMTPProviderConfig(
    __SMTPProviderConfig_typeof__,
    EmailProviderConfig,
    __gel_type_id__=UUID(int=108468146439474883053972930104863702727),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins_1__.str,
            sender: ___builtins_1__.str | None = None,
            host: ___builtins_1__.str | None = None,
            port: int | None = None,
            username: ___builtins_1__.str | None = None,
            password: ___builtins_1__.str | None = None,
            security: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            validate_certs: bool | DefaultValue = DEFAULT_VALUE,
            timeout_per_email: timedelta | DefaultValue = DEFAULT_VALUE,
            timeout_per_attempt: timedelta | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new cfg::SMTPProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            sender: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            host: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            username: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
            validate_certs: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            timeout_per_email: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            timeout_per_attempt: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::SMTPProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            sender: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            host: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
            username: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            password: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            security: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[SMTPSecurity] | UnspecifiedType = Unspecified,
            validate_certs: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            timeout_per_email: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            timeout_per_attempt: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::SMTPProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            sender: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            host: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
            username: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
            validate_certs: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            timeout_per_email: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            timeout_per_attempt: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::SMTPProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            sender: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            host: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            username: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            password: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            validate_certs: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            timeout_per_email: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            timeout_per_attempt: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmailProviderConfig.__variants__):
        class Base(
            __SMTPProviderConfig_typeof__,
            EmailProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins_1__.str,
                    sender: ___builtins_1__.str | None = None,
                    host: ___builtins_1__.str | None = None,
                    port: int | None = None,
                    username: ___builtins_1__.str | None = None,
                    password: ___builtins_1__.str | None = None,
                    security: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    validate_certs: bool | DefaultValue = DEFAULT_VALUE,
                    timeout_per_email: timedelta | DefaultValue = DEFAULT_VALUE,
                    timeout_per_attempt: timedelta | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new cfg::SMTPProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    sender: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    host: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    username: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
                    validate_certs: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    timeout_per_email: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::SMTPProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    sender: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    host: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    port: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int32] | UnspecifiedType = Unspecified,
                    username: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    password: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    security: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[SMTPSecurity] | UnspecifiedType = Unspecified,
                    validate_certs: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    timeout_per_email: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::SMTPProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    sender: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    host: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    port: ___builtins_2__.int | type[___std__.int32] | UnspecifiedType = Unspecified,
                    username: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
                    validate_certs: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    timeout_per_email: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::SMTPProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    sender: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    host: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    port: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    username: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    password: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    validate_certs: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    timeout_per_email: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmailProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            security: SMTPSecurity
            validate_certs: std.bool
            timeout_per_email: std.duration
            timeout_per_attempt: std.duration

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __SMTPProviderConfig_typeof_partial__,
            Base,
            EmailProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmailProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            sender: OptionalProperty[std.str, ___builtins_1__.str]
            host: OptionalProperty[std.str, ___builtins_1__.str]
            port: OptionalProperty[std.int32, int]
            username: OptionalProperty[std.str, ___builtins_1__.str]
            password: OptionalProperty[std.str, ___builtins_1__.str]
            security: OptionalProperty[SMTPSecurity, ___builtins_1__.str]
            validate_certs: OptionalProperty[std.bool, bool]
            timeout_per_email: OptionalProperty[std.duration, timedelta]
            timeout_per_attempt: OptionalProperty[std.duration, timedelta]


        Any = TypeVar("Any", bound="SMTPProviderConfig | Base | Required | Partial")
    class __links__(EmailProviderConfig.__links__):
        pass
    class __links_partial__(EmailProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    SMTPProviderConfig.__variants__.Base = SMTPProviderConfig



from .. import sys  # noqa: E402 F403
from ... import cfg as ___cfg__  # noqa: E402 F403

from builtins import bool, int  # noqa: E402 F403
from datetime import timedelta  # noqa: E402 F403
