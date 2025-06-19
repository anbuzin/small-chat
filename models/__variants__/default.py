#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std
from .. import std as ___std_1__

from gel.models.pydantic import (
    Cardinality,
    ComputedMultiLink,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    GelPointerReflection,
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

import builtins as ___builtins_2__
import builtins as ___builtins_1__
import builtins as ___builtins__
import datetime as ___datetime__
from builtins import tuple, type
from collections.abc import Callable, Iterable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import default, schema, std as ___std__

    from builtins import dict, str




#
# type default::Chat
#
class __Chat_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=10576472941619173054309745075251488340)
        name = SchemaPath('default', 'Chat')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'title': GelPointerReflection(
                    name='title',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'created_at': GelPointerReflection(
                    name='created_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'archive': GelPointerReflection(
                    name='archive',
                    type=SchemaPath('default', 'Message'),
                    typexpr='default::Message',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'history': GelPointerReflection(
                    name='history',
                    type=SchemaPath('default', 'Message'),
                    typexpr='default::Message',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=True,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=10576472941619173054309745075251488340),
                name='default::Chat',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Chat_typeof__(std.__Object_typeof__, __Chat_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        title = TypeAliasType('title', 'OptionalProperty[std.str, builtins.str]')
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        archive = TypeAliasType('archive', 'MultiLink[Message]')
        history = TypeAliasType('history', 'ComputedMultiLink[Message]')


class __Chat_typeof_partial__(
    std.__Object_typeof_partial__,
    __Chat_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        title = TypeAliasType('title', 'OptionalProperty[std.str, builtins.str]')
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        archive = TypeAliasType('archive', 'MultiLink[Message | Message.__variants__.Partial]')
        history = TypeAliasType('history', 'ComputedMultiLink[Message | Message.__variants__.Partial]')


class Chat(
    __Chat_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=10576472941619173054309745075251488340),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            title: builtins.str | None | DefaultValue = DEFAULT_VALUE,
            created_at: datetime | None | DefaultValue = DEFAULT_VALUE,
            archive: Iterable[Message] = [],
        ) -> None:
            """Create a new default::Chat instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            archive: type[default.Message] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Chat instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            title: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            archive: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
            history: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Chat instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            archive: type[default.Message] | UnspecifiedType = Unspecified,
            history: type[default.Message] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Chat instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            title: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __Chat_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    title: builtins.str | None | DefaultValue = DEFAULT_VALUE,
                    created_at: datetime | None | DefaultValue = DEFAULT_VALUE,
                    archive: Iterable[Message] = [],
                ) -> None:
                    """Create a new default::Chat instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    archive: type[default.Message] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Chat instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    title: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    archive: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
                    history: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Chat instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    archive: type[default.Message] | UnspecifiedType = Unspecified,
                    history: type[default.Message] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Chat instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    title: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Chat_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            title: OptionalProperty[___std_1__.str, builtins.str]
            created_at: OptionalProperty[___std_1__.datetime, datetime]
            archive: MultiLink[___default__.Message | ___default__.Message.__variants__.Partial]
            history: ComputedMultiLink[___default__.Message | ___default__.Message.__variants__.Partial]


        Any = TypeVar("Any", bound="Chat | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    Chat.__variants__.Base = Chat



#
# type default::Fact
#
class __Fact_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=11519382357052310645242296363335087702)
        name = SchemaPath('default', 'Fact')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'key': GelPointerReflection(
                    name='key',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'value': GelPointerReflection(
                    name='value',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'body': GelPointerReflection(
                    name='body',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=True,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'from_message': GelPointerReflection(
                    name='from_message',
                    type=SchemaPath('default', 'Message'),
                    typexpr='default::Message',
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
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=11519382357052310645242296363335087702),
                name='default::Fact',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Fact_typeof__(std.__Object_typeof__, __Fact_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        key = TypeAliasType('key', 'OptionalProperty[std.str, builtins.str]')
        value = TypeAliasType('value', 'OptionalProperty[std.str, builtins.str]')
        body = TypeAliasType('body', 'OptionalComputedProperty[std.str, builtins.str]')
        from_message = TypeAliasType('from_message', 'OptionalLink[Message]')


class __Fact_typeof_partial__(
    std.__Object_typeof_partial__,
    __Fact_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        key = TypeAliasType('key', 'OptionalProperty[std.str, builtins.str]')
        value = TypeAliasType('value', 'OptionalProperty[std.str, builtins.str]')
        body = TypeAliasType('body', 'OptionalComputedProperty[std.str, builtins.str]')
        from_message = TypeAliasType('from_message', 'OptionalLink[Message | Message.__variants__.Partial]')


class Fact(
    __Fact_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=11519382357052310645242296363335087702),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            key: builtins.str | None = None,
            value: builtins.str | None = None,
            from_message: Message | None = None,
        ) -> None:
            """Create a new default::Fact instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            from_message: type[default.Message] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Fact instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            key: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            value: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            from_message: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Fact instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            from_message: type[default.Message] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Fact instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            key: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            value: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __Fact_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    key: builtins.str | None = None,
                    value: builtins.str | None = None,
                    from_message: Message | None = None,
                ) -> None:
                    """Create a new default::Fact instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_message: type[default.Message] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Fact instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    key: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    value: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_message: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Fact instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_message: type[default.Message] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Fact instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    key: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    value: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Fact_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            key: OptionalProperty[___std_1__.str, builtins.str]
            value: OptionalProperty[___std_1__.str, builtins.str]
            body: OptionalComputedProperty[___std_1__.str, builtins.str]
            from_message: OptionalLink[___default__.Message | ___default__.Message.__variants__.Partial]


        Any = TypeVar("Any", bound="Fact | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    Fact.__variants__.Base = Fact



#
# type default::Message
#
class __Message_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=10568999349049202501511467742585521150)
        name = SchemaPath('default', 'Message')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'body': GelPointerReflection(
                    name='body',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'llm_role': GelPointerReflection(
                    name='llm_role',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'tool_args': GelPointerReflection(
                    name='tool_args',
                    type=SchemaPath('std', 'json'),
                    typexpr='std::json',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'tool_name': GelPointerReflection(
                    name='tool_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'created_at': GelPointerReflection(
                    name='created_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'is_evicted': GelPointerReflection(
                    name='is_evicted',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=10568999349049202501511467742585521150),
                name='default::Message',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Message_typeof__(std.__Object_typeof__, __Message_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        body = TypeAliasType('body', 'OptionalProperty[std.str, builtins.str]')
        llm_role = TypeAliasType('llm_role', 'OptionalProperty[std.str, builtins.str]')
        tool_args = TypeAliasType('tool_args', 'OptionalProperty[std.json, builtins.str]')
        tool_name = TypeAliasType('tool_name', 'OptionalProperty[std.str, builtins.str]')
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        is_evicted = TypeAliasType('is_evicted', 'OptionalProperty[std.bool, bool]')


class __Message_typeof_partial__(
    std.__Object_typeof_partial__,
    __Message_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        body = TypeAliasType('body', 'OptionalProperty[std.str, builtins.str]')
        llm_role = TypeAliasType('llm_role', 'OptionalProperty[std.str, builtins.str]')
        tool_args = TypeAliasType('tool_args', 'OptionalProperty[std.json, builtins.str]')
        tool_name = TypeAliasType('tool_name', 'OptionalProperty[std.str, builtins.str]')
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        is_evicted = TypeAliasType('is_evicted', 'OptionalProperty[std.bool, bool]')


class Message(
    __Message_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=10568999349049202501511467742585521150),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            body: builtins.str | None = None,
            llm_role: builtins.str | None = None,
            tool_args: builtins.str | None = None,
            tool_name: builtins.str | None = None,
            created_at: datetime | None | DefaultValue = DEFAULT_VALUE,
            is_evicted: bool | None | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new default::Message instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            llm_role: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            tool_args: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
            tool_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            is_evicted: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Message instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            llm_role: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            tool_args: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.json] | UnspecifiedType = Unspecified,
            tool_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            is_evicted: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Message instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            llm_role: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            tool_args: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
            tool_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            is_evicted: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Message instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            llm_role: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            tool_args: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            tool_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            is_evicted: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __Message_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    body: builtins.str | None = None,
                    llm_role: builtins.str | None = None,
                    tool_args: builtins.str | None = None,
                    tool_name: builtins.str | None = None,
                    created_at: datetime | None | DefaultValue = DEFAULT_VALUE,
                    is_evicted: bool | None | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new default::Message instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    llm_role: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    tool_args: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
                    tool_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    is_evicted: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Message instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    llm_role: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    tool_args: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.json] | UnspecifiedType = Unspecified,
                    tool_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    is_evicted: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Message instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    llm_role: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    tool_args: ___builtins_1__.str | type[___std__.json] | UnspecifiedType = Unspecified,
                    tool_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    is_evicted: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Message instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    llm_role: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    tool_args: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    tool_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    is_evicted: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Message_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            body: OptionalProperty[___std_1__.str, builtins.str]
            llm_role: OptionalProperty[___std_1__.str, builtins.str]
            tool_args: OptionalProperty[___std_1__.json, builtins.str]
            tool_name: OptionalProperty[___std_1__.str, builtins.str]
            created_at: OptionalProperty[___std_1__.datetime, datetime]
            is_evicted: OptionalProperty[___std_1__.bool, bool]


        Any = TypeVar("Any", bound="Message | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    Message.__variants__.Base = Message



#
# type default::Prompt
#
class __Prompt_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=11552181231769965797851073098984005188)
        name = SchemaPath('default', 'Prompt')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'key': GelPointerReflection(
                    name='key',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'value': GelPointerReflection(
                    name='value',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'body': GelPointerReflection(
                    name='body',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=True,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'from_message': GelPointerReflection(
                    name='from_message',
                    type=SchemaPath('default', 'Message'),
                    typexpr='default::Message',
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
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=11552181231769965797851073098984005188),
                name='default::Prompt',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Prompt_typeof__(std.__Object_typeof__, __Prompt_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        key = TypeAliasType('key', 'OptionalProperty[std.str, builtins.str]')
        value = TypeAliasType('value', 'OptionalProperty[std.str, builtins.str]')
        body = TypeAliasType('body', 'OptionalComputedProperty[std.str, builtins.str]')
        from_message = TypeAliasType('from_message', 'OptionalLink[Message]')


class __Prompt_typeof_partial__(
    std.__Object_typeof_partial__,
    __Prompt_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        key = TypeAliasType('key', 'OptionalProperty[std.str, builtins.str]')
        value = TypeAliasType('value', 'OptionalProperty[std.str, builtins.str]')
        body = TypeAliasType('body', 'OptionalComputedProperty[std.str, builtins.str]')
        from_message = TypeAliasType('from_message', 'OptionalLink[Message | Message.__variants__.Partial]')


class Prompt(
    __Prompt_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=11552181231769965797851073098984005188),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            key: builtins.str | None = None,
            value: builtins.str | None = None,
            from_message: Message | None = None,
        ) -> None:
            """Create a new default::Prompt instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            from_message: type[default.Message] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Prompt instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            key: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            value: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            from_message: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Prompt instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            from_message: type[default.Message] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Prompt instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            key: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            value: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __Prompt_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    key: builtins.str | None = None,
                    value: builtins.str | None = None,
                    from_message: Message | None = None,
                ) -> None:
                    """Create a new default::Prompt instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_message: type[default.Message] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Prompt instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    key: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    value: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_message: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.Message] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Prompt instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    value: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    from_message: type[default.Message] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Prompt instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    key: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    value: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Prompt_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            key: OptionalProperty[___std_1__.str, builtins.str]
            value: OptionalProperty[___std_1__.str, builtins.str]
            body: OptionalComputedProperty[___std_1__.str, builtins.str]
            from_message: OptionalLink[___default__.Message | ___default__.Message.__variants__.Partial]


        Any = TypeVar("Any", bound="Prompt | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    Prompt.__variants__.Base = Prompt



#
# type default::Resource
#
class __Resource_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=11561294847303981625856553839242498189)
        name = SchemaPath('default', 'Resource')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'body': GelPointerReflection(
                    name='body',
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
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=11561294847303981625856553839242498189),
                name='default::Resource',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Resource_typeof__(std.__Object_typeof__, __Resource_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        body = TypeAliasType('body', 'OptionalProperty[std.str, builtins.str]')


class __Resource_typeof_partial__(
    std.__Object_typeof_partial__,
    __Resource_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        body = TypeAliasType('body', 'OptionalProperty[std.str, builtins.str]')


class Resource(
    __Resource_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=11561294847303981625856553839242498189),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, body: builtins.str | None = None) -> None:
            """Create a new default::Resource instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Resource instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Resource instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Resource instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __Resource_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    body: builtins.str | None = None,
                ) -> None:
                    """Create a new default::Resource instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Resource instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Resource instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    body: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Resource instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Resource_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            body: OptionalProperty[___std_1__.str, builtins.str]


        Any = TypeVar("Any", bound="Resource | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    Resource.__variants__.Base = Resource



from .. import default as ___default__  # noqa: E402 F403

import builtins as builtins  # noqa: E402 F403
from builtins import bool  # noqa: E402 F403
from datetime import datetime  # noqa: E402 F403
