#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import schema

from gel.models import pydantic
from gel.models.pydantic import (
    AnyEnum,
    Array,
    Cardinality,
    ComputedProperty,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    LazyClassProperty,
    MultiLink,
    OptionalComputedProperty,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    PointerKind,
    PyConstType,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as ___builtins_3__
import builtins as ___builtins_2__
import builtins as ___builtins_1__
import builtins as ___builtins__
import datetime as ___datetime__
import datetime as ___datetime_1__
from builtins import list, tuple, type
from collections.abc import Callable, Iterable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as ___std__
    from ... import schema as ___schema__, sys
    from ...std import __types__ as ___std___types____, __types__ as std___types__

    from gel.models.pydantic import GelPointerReflection

    from builtins import dict, str


class OutputFormat(AnyEnum):
    BINARY = 'BINARY'
    JSON = 'JSON'
    JSON_ELEMENTS = 'JSON_ELEMENTS'
    NONE = 'NONE'


class QueryType(AnyEnum):
    EdgeQL = 'EdgeQL'
    SQL = 'SQL'


class TransactionAccessMode(AnyEnum):
    ReadOnly = 'ReadOnly'
    ReadWrite = 'ReadWrite'


class TransactionDeferrability(AnyEnum):
    Deferrable = 'Deferrable'
    NotDeferrable = 'NotDeferrable'


class TransactionIsolation(AnyEnum):
    RepeatableRead = 'RepeatableRead'
    Serializable = 'Serializable'


class VersionStage(AnyEnum):
    dev = 'dev'
    alpha = 'alpha'
    beta = 'beta'
    rc = 'rc'
    final = 'final'




#
# type sys::SystemObject
#
class __SystemObject_typeof_base__(schema.__Object_typeof_base__):
    class __gel_reflection__(schema.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=90350303980132584494185812701624669976)
        name = SchemaPath('sys', 'SystemObject')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | schema.__Object_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=90350303980132584494185812701624669976),
                name='sys::SystemObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __SystemObject_typeof__(
    schema.__Object_typeof__,
    __SystemObject_typeof_base__,
):
    class __typeof__(schema.__Object_typeof__.__typeof__):
        pass


class __SystemObject_typeof_partial__(
    schema.__Object_typeof_partial__,
    __SystemObject_typeof_base__,
):
    class __typeof__(schema.__Object_typeof_partial__.__typeof__):
        pass


class SystemObject(
    __SystemObject_typeof__,
    schema.Object,
    __gel_type_id__=UUID(int=90350303980132584494185812701624669976),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
        ) -> None:
            """Create a new sys::SystemObject instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::SystemObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::SystemObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::SystemObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(schema.Object.__variants__):
        class Base(
            __SystemObject_typeof__,
            schema.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                ) -> None:
                    """Create a new sys::SystemObject instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::SystemObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::SystemObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::SystemObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            schema.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __SystemObject_typeof_partial__,
            Base,
            schema.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            schema.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="SystemObject | Base | Required | Partial")
    class __links__(schema.Object.__links__):
        pass
    class __links_partial__(schema.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    SystemObject.__variants__.Base = SystemObject



#
# type sys::ExtensionPackage
#
class __ExtensionPackage_typeof_base__(
    __SystemObject_typeof_base__,
    schema.__AnnotationSubject_typeof_base__,
):
    class __gel_reflection__(
        __SystemObject_typeof_base__.__gel_reflection__,
        schema.__AnnotationSubject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=180071320089194630696024936739719303821)
        name = SchemaPath('sys', 'ExtensionPackage')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'script': pydantic.GelPointerReflection(
                    name='script',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'version': pydantic.GelPointerReflection(
                    name='version',
                    type=SchemaPath('tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>'),
                    typexpr='tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>',
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
                | __SystemObject_typeof_base__.__gel_reflection__.pointers
                | schema.__AnnotationSubject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=180071320089194630696024936739719303821),
                name='sys::ExtensionPackage',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __ExtensionPackage_typeof__(
    __SystemObject_typeof__,
    schema.__AnnotationSubject_typeof__,
    __ExtensionPackage_typeof_base__,
):
    class __typeof__(
        __SystemObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        script = TypeAliasType('script', 'std.str')
        version = TypeAliasType('version', 'MajorMinorStageStage_noLocal_Tuple_SKRhXQ')


class __ExtensionPackage_typeof_partial__(
    __SystemObject_typeof_partial__,
    schema.__AnnotationSubject_typeof_partial__,
    __ExtensionPackage_typeof_base__,
):
    class __typeof__(
        __SystemObject_typeof_partial__.__typeof__,
        schema.__AnnotationSubject_typeof_partial__.__typeof__,
    ):
        script = TypeAliasType('script', 'OptionalProperty[std.str, builtins.str]')
        version = TypeAliasType('version', 'OptionalProperty[MajorMinorStageStage_noLocal_Tuple_SKRhXQ, tuple[int, int, ___builtins_1__.str, int, list[builtins.str]]]')


class ExtensionPackage(
    __ExtensionPackage_typeof__,
    SystemObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=180071320089194630696024936739719303821),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            script: builtins.str,
            version: tuple[int, int, ___builtins_1__.str, int, list[builtins.str]],
        ) -> None:
            """Create a new sys::ExtensionPackage instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::ExtensionPackage instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            script: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackage instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackage instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            script: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SystemObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __ExtensionPackage_typeof__,
            SystemObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    script: builtins.str,
                    version: tuple[int, int, ___builtins_1__.str, int, list[builtins.str]],
                ) -> None:
                    """Create a new sys::ExtensionPackage instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::ExtensionPackage instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackage instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackage instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    script: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            SystemObject.__variants__.Required,
            schema.AnnotationSubject.__variants__.Required,
            __gel_variant__="Required",
        ):
            script: std.str
            version: MajorMinorStageStage_noLocal_Tuple_SKRhXQ

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ExtensionPackage_typeof_partial__,
            Base,
            SystemObject.__variants__.PartialBase,
            schema.AnnotationSubject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            SystemObject.__variants__.Partial,
            schema.AnnotationSubject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            script: OptionalProperty[std.str, builtins.str]
            version: OptionalProperty[MajorMinorStageStage_noLocal_Tuple_SKRhXQ, tuple[int, int, ___builtins_1__.str, int, list[builtins.str]]]


        Any = TypeVar("Any", bound="ExtensionPackage | Base | Required | Partial")
    class __links__(
        SystemObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass
    class __links_partial__(
        SystemObject.__links_partial__,
        schema.AnnotationSubject.__links_partial__,
    ):
        pass

if not TYPE_CHECKING:
    ExtensionPackage.__variants__.Base = ExtensionPackage



#
# type sys::ExtensionPackageMigration
#
class __ExtensionPackageMigration_typeof_base__(
    __SystemObject_typeof_base__,
    schema.__AnnotationSubject_typeof_base__,
):
    class __gel_reflection__(
        __SystemObject_typeof_base__.__gel_reflection__,
        schema.__AnnotationSubject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=302620932575936177542260435729933168552)
        name = SchemaPath('sys', 'ExtensionPackageMigration')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'script': pydantic.GelPointerReflection(
                    name='script',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'from_version': pydantic.GelPointerReflection(
                    name='from_version',
                    type=SchemaPath('tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>'),
                    typexpr='tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'to_version': pydantic.GelPointerReflection(
                    name='to_version',
                    type=SchemaPath('tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>'),
                    typexpr='tuple<major:std::int64, minor:std::int64, stage:sys::VersionStage, stage_no:std::int64, local:array<std::str>>',
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
                | __SystemObject_typeof_base__.__gel_reflection__.pointers
                | schema.__AnnotationSubject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=302620932575936177542260435729933168552),
                name='sys::ExtensionPackageMigration',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __ExtensionPackageMigration_typeof__(
    __SystemObject_typeof__,
    schema.__AnnotationSubject_typeof__,
    __ExtensionPackageMigration_typeof_base__,
):
    class __typeof__(
        __SystemObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        script = TypeAliasType('script', 'std.str')
        from_version = TypeAliasType('from_version', 'MajorMinorStageStage_noLocal_Tuple_SKRhXQ')
        to_version = TypeAliasType('to_version', 'MajorMinorStageStage_noLocal_Tuple_SKRhXQ')


class __ExtensionPackageMigration_typeof_partial__(
    __SystemObject_typeof_partial__,
    schema.__AnnotationSubject_typeof_partial__,
    __ExtensionPackageMigration_typeof_base__,
):
    class __typeof__(
        __SystemObject_typeof_partial__.__typeof__,
        schema.__AnnotationSubject_typeof_partial__.__typeof__,
    ):
        script = TypeAliasType('script', 'OptionalProperty[std.str, builtins.str]')
        from_version = TypeAliasType('from_version', 'OptionalProperty[MajorMinorStageStage_noLocal_Tuple_SKRhXQ, tuple[int, int, ___builtins_1__.str, int, list[builtins.str]]]')
        to_version = TypeAliasType('to_version', 'OptionalProperty[MajorMinorStageStage_noLocal_Tuple_SKRhXQ, tuple[int, int, ___builtins_1__.str, int, list[builtins.str]]]')


class ExtensionPackageMigration(
    __ExtensionPackageMigration_typeof__,
    SystemObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=302620932575936177542260435729933168552),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            script: builtins.str,
            from_version: tuple[int, int, ___builtins_1__.str, int, list[builtins.str]],
            to_version: tuple[int, int, ___builtins_1__.str, int, list[builtins.str]],
        ) -> None:
            """Create a new sys::ExtensionPackageMigration instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::ExtensionPackageMigration instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            script: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            from_version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            to_version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackageMigration instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackageMigration instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            script: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SystemObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __ExtensionPackageMigration_typeof__,
            SystemObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    script: builtins.str,
                    from_version: tuple[int, int, ___builtins_1__.str, int, list[builtins.str]],
                    to_version: tuple[int, int, ___builtins_1__.str, int, list[builtins.str]],
                ) -> None:
                    """Create a new sys::ExtensionPackageMigration instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::ExtensionPackageMigration instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    to_version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackageMigration instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackageMigration instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    script: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            SystemObject.__variants__.Required,
            schema.AnnotationSubject.__variants__.Required,
            __gel_variant__="Required",
        ):
            script: std.str
            from_version: MajorMinorStageStage_noLocal_Tuple_SKRhXQ
            to_version: MajorMinorStageStage_noLocal_Tuple_SKRhXQ

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ExtensionPackageMigration_typeof_partial__,
            Base,
            SystemObject.__variants__.PartialBase,
            schema.AnnotationSubject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            SystemObject.__variants__.Partial,
            schema.AnnotationSubject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            script: OptionalProperty[std.str, builtins.str]
            from_version: OptionalProperty[MajorMinorStageStage_noLocal_Tuple_SKRhXQ, tuple[int, int, ___builtins_1__.str, int, list[builtins.str]]]
            to_version: OptionalProperty[MajorMinorStageStage_noLocal_Tuple_SKRhXQ, tuple[int, int, ___builtins_1__.str, int, list[builtins.str]]]


        Any = TypeVar("Any", bound="ExtensionPackageMigration | Base | Required | Partial")
    class __links__(
        SystemObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass
    class __links_partial__(
        SystemObject.__links_partial__,
        schema.AnnotationSubject.__links_partial__,
    ):
        pass

if not TYPE_CHECKING:
    ExtensionPackageMigration.__variants__.Base = ExtensionPackageMigration



#
# type sys::ExternalObject
#
class __ExternalObject_typeof_base__(__SystemObject_typeof_base__):
    class __gel_reflection__(__SystemObject_typeof_base__.__gel_reflection__):
        id = UUID(int=302417707415983282126938051159487614287)
        name = SchemaPath('sys', 'ExternalObject')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {}
            return (
                my_ptrs
                | __SystemObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=302417707415983282126938051159487614287),
                name='sys::ExternalObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __ExternalObject_typeof__(
    __SystemObject_typeof__,
    __ExternalObject_typeof_base__,
):
    class __typeof__(__SystemObject_typeof__.__typeof__):
        pass


class __ExternalObject_typeof_partial__(
    __SystemObject_typeof_partial__,
    __ExternalObject_typeof_base__,
):
    class __typeof__(__SystemObject_typeof_partial__.__typeof__):
        pass


class ExternalObject(
    __ExternalObject_typeof__,
    SystemObject,
    __gel_type_id__=UUID(int=302417707415983282126938051159487614287),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
        ) -> None:
            """Create a new sys::ExternalObject instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::ExternalObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::ExternalObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::ExternalObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(SystemObject.__variants__):
        class Base(
            __ExternalObject_typeof__,
            SystemObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                ) -> None:
                    """Create a new sys::ExternalObject instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::ExternalObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::ExternalObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::ExternalObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            SystemObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ExternalObject_typeof_partial__,
            Base,
            SystemObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            SystemObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="ExternalObject | Base | Required | Partial")
    class __links__(SystemObject.__links__):
        pass
    class __links_partial__(SystemObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ExternalObject.__variants__.Base = ExternalObject



#
# type sys::Role
#
class __Role_typeof_base__(
    __SystemObject_typeof_base__,
    schema.__InheritingObject_typeof_base__,
    schema.__AnnotationSubject_typeof_base__,
):
    class __gel_reflection__(
        __SystemObject_typeof_base__.__gel_reflection__,
        schema.__InheritingObject_typeof_base__.__gel_reflection__,
        schema.__AnnotationSubject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=6415088929791825864887870917823511316)
        name = SchemaPath('sys', 'Role')
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
                'superuser': pydantic.GelPointerReflection(
                    name='superuser',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'is_superuser': pydantic.GelPointerReflection(
                    name='is_superuser',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=True,
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
                'member_of': pydantic.GelPointerReflection(
                    name='member_of',
                    type=SchemaPath('sys', 'Role'),
                    typexpr='sys::Role',
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
                | __SystemObject_typeof_base__.__gel_reflection__.pointers
                | schema.__InheritingObject_typeof_base__.__gel_reflection__.pointers
                | schema.__AnnotationSubject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=6415088929791825864887870917823511316),
                name='sys::Role',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Role_typeof__(
    __SystemObject_typeof__,
    schema.__InheritingObject_typeof__,
    schema.__AnnotationSubject_typeof__,
    __Role_typeof_base__,
):
    class __typeof__(
        __SystemObject_typeof__.__typeof__,
        schema.__InheritingObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        name = TypeAliasType('name', 'std.str')
        superuser = TypeAliasType('superuser', 'std.bool')
        is_superuser = TypeAliasType('is_superuser', 'ComputedProperty[std.bool, bool]')
        password = TypeAliasType('password', 'OptionalProperty[std.str, builtins.str]')
        member_of = TypeAliasType('member_of', 'MultiLink[Role]')


class __Role_typeof_partial__(
    __SystemObject_typeof_partial__,
    schema.__InheritingObject_typeof_partial__,
    schema.__AnnotationSubject_typeof_partial__,
    __Role_typeof_base__,
):
    class __typeof__(
        __SystemObject_typeof_partial__.__typeof__,
        schema.__InheritingObject_typeof_partial__.__typeof__,
        schema.__AnnotationSubject_typeof_partial__.__typeof__,
    ):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        superuser = TypeAliasType('superuser', 'OptionalProperty[std.bool, bool]')
        is_superuser = TypeAliasType('is_superuser', 'OptionalComputedProperty[std.bool, bool]')
        password = TypeAliasType('password', 'OptionalProperty[std.str, builtins.str]')
        member_of = TypeAliasType('member_of', 'MultiLink[Role | Role.__variants__.Partial]')


class Role(
    __Role_typeof__,
    SystemObject,
    schema.InheritingObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=6415088929791825864887870917823511316),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            abstract: bool | None | DefaultValue = DEFAULT_VALUE,
            inherited_fields: list[builtins.str] | None = None,
            bases: Iterable[schema.InheritingObject] = [],
            ancestors: Iterable[schema.InheritingObject] = [],
            superuser: bool,
            password: builtins.str | None = None,
            member_of: Iterable[Role] = [],
        ) -> None:
            """Create a new sys::Role instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            abstract: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            bases: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
            superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            member_of: type[sys.Role] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::Role instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            abstract: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            final: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            bases: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
            superuser: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            is_superuser: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            password: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            member_of: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Role] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::Role instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            abstract: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            final: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            bases: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
            superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            is_superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            member_of: type[sys.Role] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::Role instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            abstract: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            final: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            superuser: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            is_superuser: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            password: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SystemObject.__variants__,
        schema.InheritingObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __Role_typeof__,
            SystemObject.__variants__.Base,
            schema.InheritingObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    abstract: bool | None | DefaultValue = DEFAULT_VALUE,
                    inherited_fields: list[builtins.str] | None = None,
                    bases: Iterable[schema.InheritingObject] = [],
                    ancestors: Iterable[schema.InheritingObject] = [],
                    superuser: bool,
                    password: builtins.str | None = None,
                    member_of: Iterable[Role] = [],
                ) -> None:
                    """Create a new sys::Role instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    abstract: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    member_of: type[sys.Role] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::Role instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    abstract: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    final: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    bases: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    superuser: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    is_superuser: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    password: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    member_of: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Role] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::Role instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    abstract: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    final: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[___schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    is_superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    password: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    member_of: type[sys.Role] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::Role instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    abstract: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    final: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    superuser: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    is_superuser: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    password: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            SystemObject.__variants__.Required,
            schema.InheritingObject.__variants__.Required,
            schema.AnnotationSubject.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: std.str
            superuser: std.bool
            is_superuser: ComputedProperty[std.bool, bool]

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Role_typeof_partial__,
            Base,
            SystemObject.__variants__.PartialBase,
            schema.InheritingObject.__variants__.PartialBase,
            schema.AnnotationSubject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            SystemObject.__variants__.Partial,
            schema.InheritingObject.__variants__.Partial,
            schema.AnnotationSubject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[std.str, builtins.str]
            superuser: OptionalProperty[std.bool, bool]
            is_superuser: OptionalComputedProperty[std.bool, bool]
            password: OptionalProperty[std.str, builtins.str]
            member_of: MultiLink[___sys__.Role | ___sys__.Role.__variants__.Partial]


        Any = TypeVar("Any", bound="Role | Base | Required | Partial")
    class __links__(
        SystemObject.__links__,
        schema.InheritingObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass
    class __links_partial__(
        SystemObject.__links_partial__,
        schema.InheritingObject.__links_partial__,
        schema.AnnotationSubject.__links_partial__,
    ):
        pass

if not TYPE_CHECKING:
    Role.__variants__.Base = Role



#
# type sys::Branch
#
class __Branch_typeof_base__(
    __ExternalObject_typeof_base__,
    schema.__AnnotationSubject_typeof_base__,
):
    class __gel_reflection__(
        __ExternalObject_typeof_base__.__gel_reflection__,
        schema.__AnnotationSubject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=49778529390898516016872303811592688699)
        name = SchemaPath('sys', 'Branch')
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
                'last_migration': pydantic.GelPointerReflection(
                    name='last_migration',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ExternalObject_typeof_base__.__gel_reflection__.pointers
                | schema.__AnnotationSubject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=49778529390898516016872303811592688699),
                name='sys::Branch',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Branch_typeof__(
    __ExternalObject_typeof__,
    schema.__AnnotationSubject_typeof__,
    __Branch_typeof_base__,
):
    class __typeof__(
        __ExternalObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        name = TypeAliasType('name', 'std.str')
        last_migration = TypeAliasType('last_migration', 'OptionalProperty[std.str, builtins.str]')


class __Branch_typeof_partial__(
    __ExternalObject_typeof_partial__,
    schema.__AnnotationSubject_typeof_partial__,
    __Branch_typeof_base__,
):
    class __typeof__(
        __ExternalObject_typeof_partial__.__typeof__,
        schema.__AnnotationSubject_typeof_partial__.__typeof__,
    ):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        last_migration = TypeAliasType('last_migration', 'OptionalProperty[std.str, builtins.str]')


class Branch(
    __Branch_typeof__,
    ExternalObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=49778529390898516016872303811592688699),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            last_migration: builtins.str | None = None,
        ) -> None:
            """Create a new sys::Branch instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            last_migration: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::Branch instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            last_migration: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::Branch instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
            last_migration: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::Branch instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            last_migration: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        ExternalObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __Branch_typeof__,
            ExternalObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    last_migration: builtins.str | None = None,
                ) -> None:
                    """Create a new sys::Branch instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    last_migration: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::Branch instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    last_migration: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::Branch instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[___schema__.Annotation] | UnspecifiedType = Unspecified,
                    last_migration: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::Branch instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    last_migration: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ExternalObject.__variants__.Required,
            schema.AnnotationSubject.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: std.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Branch_typeof_partial__,
            Base,
            ExternalObject.__variants__.PartialBase,
            schema.AnnotationSubject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ExternalObject.__variants__.Partial,
            schema.AnnotationSubject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[std.str, builtins.str]
            last_migration: OptionalProperty[std.str, builtins.str]


        Any = TypeVar("Any", bound="Branch | Base | Required | Partial")
    class __links__(
        ExternalObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass
    class __links_partial__(
        ExternalObject.__links_partial__,
        schema.AnnotationSubject.__links_partial__,
    ):
        pass

if not TYPE_CHECKING:
    Branch.__variants__.Base = Branch



#
# type sys::QueryStats
#
class __QueryStats_typeof_base__(__ExternalObject_typeof_base__):
    class __gel_reflection__(
        __ExternalObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=274580524048681063750167790732145947985)
        name = SchemaPath('sys', 'QueryStats')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {
                'query': pydantic.GelPointerReflection(
                    name='query',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'query_type': pydantic.GelPointerReflection(
                    name='query_type',
                    type=SchemaPath('sys', 'QueryType'),
                    typexpr='sys::QueryType',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'tag': pydantic.GelPointerReflection(
                    name='tag',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'compilation_config': pydantic.GelPointerReflection(
                    name='compilation_config',
                    type=SchemaPath('std', 'json'),
                    typexpr='std::json',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'protocol_version': pydantic.GelPointerReflection(
                    name='protocol_version',
                    type=SchemaPath('tuple<major:std::int16, minor:std::int16>'),
                    typexpr='tuple<major:std::int16, minor:std::int16>',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'default_namespace': pydantic.GelPointerReflection(
                    name='default_namespace',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'namespace_aliases': pydantic.GelPointerReflection(
                    name='namespace_aliases',
                    type=SchemaPath('std', 'json'),
                    typexpr='std::json',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'output_format': pydantic.GelPointerReflection(
                    name='output_format',
                    type=SchemaPath('sys', 'OutputFormat'),
                    typexpr='sys::OutputFormat',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'expect_one': pydantic.GelPointerReflection(
                    name='expect_one',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'implicit_limit': pydantic.GelPointerReflection(
                    name='implicit_limit',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'inline_typeids': pydantic.GelPointerReflection(
                    name='inline_typeids',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'inline_typenames': pydantic.GelPointerReflection(
                    name='inline_typenames',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'inline_objectids': pydantic.GelPointerReflection(
                    name='inline_objectids',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'plans': pydantic.GelPointerReflection(
                    name='plans',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'total_plan_time': pydantic.GelPointerReflection(
                    name='total_plan_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'min_plan_time': pydantic.GelPointerReflection(
                    name='min_plan_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'max_plan_time': pydantic.GelPointerReflection(
                    name='max_plan_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'mean_plan_time': pydantic.GelPointerReflection(
                    name='mean_plan_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'stddev_plan_time': pydantic.GelPointerReflection(
                    name='stddev_plan_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'calls': pydantic.GelPointerReflection(
                    name='calls',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'total_exec_time': pydantic.GelPointerReflection(
                    name='total_exec_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'min_exec_time': pydantic.GelPointerReflection(
                    name='min_exec_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'max_exec_time': pydantic.GelPointerReflection(
                    name='max_exec_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'mean_exec_time': pydantic.GelPointerReflection(
                    name='mean_exec_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'stddev_exec_time': pydantic.GelPointerReflection(
                    name='stddev_exec_time',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'rows': pydantic.GelPointerReflection(
                    name='rows',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'stats_since': pydantic.GelPointerReflection(
                    name='stats_since',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'minmax_stats_since': pydantic.GelPointerReflection(
                    name='minmax_stats_since',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'branch': pydantic.GelPointerReflection(
                    name='branch',
                    type=SchemaPath('sys', 'Branch'),
                    typexpr='sys::Branch',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ExternalObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["___schema__.ObjectType"]
        @classmethod
        def object(cls) -> ___schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=274580524048681063750167790732145947985),
                name='sys::QueryStats',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __QueryStats_typeof__(
    __ExternalObject_typeof__,
    __QueryStats_typeof_base__,
):
    class __typeof__(__ExternalObject_typeof__.__typeof__):
        query = TypeAliasType('query', 'OptionalProperty[std.str, builtins.str]')
        query_type = TypeAliasType('query_type', 'OptionalProperty[QueryType, ___builtins_1__.str]')
        tag = TypeAliasType('tag', 'OptionalProperty[std.str, builtins.str]')
        compilation_config = TypeAliasType('compilation_config', 'OptionalProperty[std.json, builtins.str]')
        protocol_version = TypeAliasType('protocol_version', 'OptionalProperty[MajorMinor_Tuple_K20e_g, tuple[int, int]]')
        default_namespace = TypeAliasType('default_namespace', 'OptionalProperty[std.str, builtins.str]')
        namespace_aliases = TypeAliasType('namespace_aliases', 'OptionalProperty[std.json, builtins.str]')
        output_format = TypeAliasType('output_format', 'OptionalProperty[OutputFormat, ___builtins_1__.str]')
        expect_one = TypeAliasType('expect_one', 'OptionalProperty[std.bool, bool]')
        implicit_limit = TypeAliasType('implicit_limit', 'OptionalProperty[std.int64, int]')
        inline_typeids = TypeAliasType('inline_typeids', 'OptionalProperty[std.bool, bool]')
        inline_typenames = TypeAliasType('inline_typenames', 'OptionalProperty[std.bool, bool]')
        inline_objectids = TypeAliasType('inline_objectids', 'OptionalProperty[std.bool, bool]')
        plans = TypeAliasType('plans', 'OptionalProperty[std.int64, int]')
        total_plan_time = TypeAliasType('total_plan_time', 'OptionalProperty[std.duration, timedelta]')
        min_plan_time = TypeAliasType('min_plan_time', 'OptionalProperty[std.duration, timedelta]')
        max_plan_time = TypeAliasType('max_plan_time', 'OptionalProperty[std.duration, timedelta]')
        mean_plan_time = TypeAliasType('mean_plan_time', 'OptionalProperty[std.duration, timedelta]')
        stddev_plan_time = TypeAliasType('stddev_plan_time', 'OptionalProperty[std.duration, timedelta]')
        calls = TypeAliasType('calls', 'OptionalProperty[std.int64, int]')
        total_exec_time = TypeAliasType('total_exec_time', 'OptionalProperty[std.duration, timedelta]')
        min_exec_time = TypeAliasType('min_exec_time', 'OptionalProperty[std.duration, timedelta]')
        max_exec_time = TypeAliasType('max_exec_time', 'OptionalProperty[std.duration, timedelta]')
        mean_exec_time = TypeAliasType('mean_exec_time', 'OptionalProperty[std.duration, timedelta]')
        stddev_exec_time = TypeAliasType('stddev_exec_time', 'OptionalProperty[std.duration, timedelta]')
        rows = TypeAliasType('rows', 'OptionalProperty[std.int64, int]')
        stats_since = TypeAliasType('stats_since', 'OptionalProperty[std.datetime, datetime]')
        minmax_stats_since = TypeAliasType('minmax_stats_since', 'OptionalProperty[std.datetime, datetime]')
        branch = TypeAliasType('branch', 'OptionalLink[Branch]')


class __QueryStats_typeof_partial__(
    __ExternalObject_typeof_partial__,
    __QueryStats_typeof_base__,
):
    class __typeof__(__ExternalObject_typeof_partial__.__typeof__):
        query = TypeAliasType('query', 'OptionalProperty[std.str, builtins.str]')
        query_type = TypeAliasType('query_type', 'OptionalProperty[QueryType, ___builtins_1__.str]')
        tag = TypeAliasType('tag', 'OptionalProperty[std.str, builtins.str]')
        compilation_config = TypeAliasType('compilation_config', 'OptionalProperty[std.json, builtins.str]')
        protocol_version = TypeAliasType('protocol_version', 'OptionalProperty[MajorMinor_Tuple_K20e_g, tuple[int, int]]')
        default_namespace = TypeAliasType('default_namespace', 'OptionalProperty[std.str, builtins.str]')
        namespace_aliases = TypeAliasType('namespace_aliases', 'OptionalProperty[std.json, builtins.str]')
        output_format = TypeAliasType('output_format', 'OptionalProperty[OutputFormat, ___builtins_1__.str]')
        expect_one = TypeAliasType('expect_one', 'OptionalProperty[std.bool, bool]')
        implicit_limit = TypeAliasType('implicit_limit', 'OptionalProperty[std.int64, int]')
        inline_typeids = TypeAliasType('inline_typeids', 'OptionalProperty[std.bool, bool]')
        inline_typenames = TypeAliasType('inline_typenames', 'OptionalProperty[std.bool, bool]')
        inline_objectids = TypeAliasType('inline_objectids', 'OptionalProperty[std.bool, bool]')
        plans = TypeAliasType('plans', 'OptionalProperty[std.int64, int]')
        total_plan_time = TypeAliasType('total_plan_time', 'OptionalProperty[std.duration, timedelta]')
        min_plan_time = TypeAliasType('min_plan_time', 'OptionalProperty[std.duration, timedelta]')
        max_plan_time = TypeAliasType('max_plan_time', 'OptionalProperty[std.duration, timedelta]')
        mean_plan_time = TypeAliasType('mean_plan_time', 'OptionalProperty[std.duration, timedelta]')
        stddev_plan_time = TypeAliasType('stddev_plan_time', 'OptionalProperty[std.duration, timedelta]')
        calls = TypeAliasType('calls', 'OptionalProperty[std.int64, int]')
        total_exec_time = TypeAliasType('total_exec_time', 'OptionalProperty[std.duration, timedelta]')
        min_exec_time = TypeAliasType('min_exec_time', 'OptionalProperty[std.duration, timedelta]')
        max_exec_time = TypeAliasType('max_exec_time', 'OptionalProperty[std.duration, timedelta]')
        mean_exec_time = TypeAliasType('mean_exec_time', 'OptionalProperty[std.duration, timedelta]')
        stddev_exec_time = TypeAliasType('stddev_exec_time', 'OptionalProperty[std.duration, timedelta]')
        rows = TypeAliasType('rows', 'OptionalProperty[std.int64, int]')
        stats_since = TypeAliasType('stats_since', 'OptionalProperty[std.datetime, datetime]')
        minmax_stats_since = TypeAliasType('minmax_stats_since', 'OptionalProperty[std.datetime, datetime]')
        branch = TypeAliasType('branch', 'OptionalLink[Branch | Branch.__variants__.Partial]')


class QueryStats(
    __QueryStats_typeof__,
    ExternalObject,
    __gel_type_id__=UUID(int=274580524048681063750167790732145947985),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            internal: bool | DefaultValue = DEFAULT_VALUE,
            builtin: bool | DefaultValue = DEFAULT_VALUE,
            computed_fields: list[builtins.str] | None = None,
            query: builtins.str | None = None,
            query_type: ___builtins_1__.str | None = None,
            tag: builtins.str | None = None,
            compilation_config: builtins.str | None = None,
            protocol_version: tuple[int, int] | None = None,
            default_namespace: builtins.str | None = None,
            namespace_aliases: builtins.str | None = None,
            output_format: ___builtins_1__.str | None = None,
            expect_one: bool | None = None,
            implicit_limit: int | None = None,
            inline_typeids: bool | None = None,
            inline_typenames: bool | None = None,
            inline_objectids: bool | None = None,
            plans: int | None = None,
            total_plan_time: timedelta | None = None,
            min_plan_time: timedelta | None = None,
            max_plan_time: timedelta | None = None,
            mean_plan_time: timedelta | None = None,
            stddev_plan_time: timedelta | None = None,
            calls: int | None = None,
            total_exec_time: timedelta | None = None,
            min_exec_time: timedelta | None = None,
            max_exec_time: timedelta | None = None,
            mean_exec_time: timedelta | None = None,
            stddev_exec_time: timedelta | None = None,
            rows: int | None = None,
            stats_since: datetime | None = None,
            minmax_stats_since: datetime | None = None,
            branch: Branch | None = None,
        ) -> None:
            """Create a new sys::QueryStats instance from keyword arguments.

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
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            query: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            query_type: type[QueryType] | UnspecifiedType = Unspecified,
            tag: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            compilation_config: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
            protocol_version: type[___std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
            default_namespace: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
            output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
            expect_one: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            implicit_limit: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            inline_typeids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            inline_typenames: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            inline_objectids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            plans: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            total_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            min_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            max_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            mean_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            stddev_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            calls: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            total_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            min_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            max_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            mean_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            stddev_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            rows: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            minmax_stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            branch: type[sys.Branch] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::QueryStats instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            query: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            query_type: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryType] | UnspecifiedType = Unspecified,
            tag: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            compilation_config: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.json] | UnspecifiedType = Unspecified,
            protocol_version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
            default_namespace: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.json] | UnspecifiedType = Unspecified,
            output_format: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[OutputFormat] | UnspecifiedType = Unspecified,
            expect_one: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            implicit_limit: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            inline_typeids: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            inline_typenames: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            inline_objectids: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            plans: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            total_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            min_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            max_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            mean_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            stddev_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            calls: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            total_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            min_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            max_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            mean_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            stddev_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            rows: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            stats_since: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            minmax_stats_since: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            branch: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Branch] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::QueryStats instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
            query: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            query_type: type[QueryType] | UnspecifiedType = Unspecified,
            tag: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            compilation_config: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
            protocol_version: type[___std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
            default_namespace: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
            output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
            expect_one: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            implicit_limit: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            inline_typeids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            inline_typenames: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            inline_objectids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            plans: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            total_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            min_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            max_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            mean_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            stddev_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            calls: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            total_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            min_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            max_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            mean_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            stddev_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            rows: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            minmax_stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            branch: type[sys.Branch] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::QueryStats instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            query: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            tag: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            compilation_config: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            default_namespace: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            expect_one: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            implicit_limit: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            inline_typeids: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            inline_typenames: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            inline_objectids: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            plans: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            total_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            min_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            max_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            mean_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            stddev_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            calls: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            total_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            min_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            max_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            mean_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            stddev_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            rows: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            stats_since: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            minmax_stats_since: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ExternalObject.__variants__):
        class Base(
            __QueryStats_typeof__,
            ExternalObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    internal: bool | DefaultValue = DEFAULT_VALUE,
                    builtin: bool | DefaultValue = DEFAULT_VALUE,
                    computed_fields: list[builtins.str] | None = None,
                    query: builtins.str | None = None,
                    query_type: ___builtins_1__.str | None = None,
                    tag: builtins.str | None = None,
                    compilation_config: builtins.str | None = None,
                    protocol_version: tuple[int, int] | None = None,
                    default_namespace: builtins.str | None = None,
                    namespace_aliases: builtins.str | None = None,
                    output_format: ___builtins_1__.str | None = None,
                    expect_one: bool | None = None,
                    implicit_limit: int | None = None,
                    inline_typeids: bool | None = None,
                    inline_typenames: bool | None = None,
                    inline_objectids: bool | None = None,
                    plans: int | None = None,
                    total_plan_time: timedelta | None = None,
                    min_plan_time: timedelta | None = None,
                    max_plan_time: timedelta | None = None,
                    mean_plan_time: timedelta | None = None,
                    stddev_plan_time: timedelta | None = None,
                    calls: int | None = None,
                    total_exec_time: timedelta | None = None,
                    min_exec_time: timedelta | None = None,
                    max_exec_time: timedelta | None = None,
                    mean_exec_time: timedelta | None = None,
                    stddev_exec_time: timedelta | None = None,
                    rows: int | None = None,
                    stats_since: datetime | None = None,
                    minmax_stats_since: datetime | None = None,
                    branch: Branch | None = None,
                ) -> None:
                    """Create a new sys::QueryStats instance from keyword arguments.

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
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    query: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    query_type: type[QueryType] | UnspecifiedType = Unspecified,
                    tag: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    compilation_config: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
                    protocol_version: type[___std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
                    default_namespace: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
                    output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
                    expect_one: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    implicit_limit: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    inline_typeids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inline_typenames: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inline_objectids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    plans: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    total_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    min_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    max_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    mean_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    stddev_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    calls: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    total_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    min_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    max_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    mean_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    stddev_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    rows: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    minmax_stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    branch: type[sys.Branch] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::QueryStats instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    query: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    query_type: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryType] | UnspecifiedType = Unspecified,
                    tag: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    compilation_config: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.json] | UnspecifiedType = Unspecified,
                    protocol_version: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
                    default_namespace: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.json] | UnspecifiedType = Unspecified,
                    output_format: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[OutputFormat] | UnspecifiedType = Unspecified,
                    expect_one: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    implicit_limit: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    inline_typeids: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inline_typenames: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inline_objectids: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    plans: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    total_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    min_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    max_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    mean_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    stddev_plan_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    calls: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    total_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    min_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    max_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    mean_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    stddev_exec_time: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    rows: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    stats_since: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    minmax_stats_since: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    branch: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Branch] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::QueryStats instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    internal: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    builtin: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[___std__.str]] | UnspecifiedType = Unspecified,
                    query: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    query_type: type[QueryType] | UnspecifiedType = Unspecified,
                    tag: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    compilation_config: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
                    protocol_version: type[___std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
                    default_namespace: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
                    output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
                    expect_one: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    implicit_limit: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    inline_typeids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inline_typenames: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    inline_objectids: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    plans: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    total_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    min_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    max_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    mean_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    stddev_plan_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    calls: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    total_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    min_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    max_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    mean_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    stddev_exec_time: ___datetime__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    rows: ___builtins_3__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    minmax_stats_since: ___datetime_1__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    branch: type[sys.Branch] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::QueryStats instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    internal: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    query: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    tag: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    compilation_config: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    default_namespace: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    expect_one: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    implicit_limit: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    inline_typeids: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    inline_typenames: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    inline_objectids: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    plans: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    total_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    min_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    max_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    mean_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    stddev_plan_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    calls: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    total_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    min_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    max_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    mean_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    stddev_exec_time: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    rows: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    stats_since: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    minmax_stats_since: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ExternalObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __QueryStats_typeof_partial__,
            Base,
            ExternalObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ExternalObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            query: OptionalProperty[std.str, builtins.str]
            query_type: OptionalProperty[QueryType, ___builtins_1__.str]
            tag: OptionalProperty[std.str, builtins.str]
            compilation_config: OptionalProperty[std.json, builtins.str]
            protocol_version: OptionalProperty[MajorMinor_Tuple_K20e_g, tuple[int, int]]
            default_namespace: OptionalProperty[std.str, builtins.str]
            namespace_aliases: OptionalProperty[std.json, builtins.str]
            output_format: OptionalProperty[OutputFormat, ___builtins_1__.str]
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
            branch: OptionalLink[___sys__.Branch | ___sys__.Branch.__variants__.Partial]


        Any = TypeVar("Any", bound="QueryStats | Base | Required | Partial")
    class __links__(ExternalObject.__links__):
        pass
    class __links_partial__(ExternalObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    QueryStats.__variants__.Base = QueryStats



from .. import std  # noqa: E402 F403
from ... import sys as ___sys__  # noqa: E402 F403
from ...std.__types__ import (  # noqa: E402 F403
    MajorMinorStageStage_noLocal_Tuple_SKRhXQ,
    MajorMinor_Tuple_K20e_g
)

import builtins as builtins  # noqa: E402 F403
from builtins import bool, int  # noqa: E402 F403
from datetime import datetime, timedelta  # noqa: E402 F403
