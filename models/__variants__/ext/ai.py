#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std
from ... import std as ___std_1__

from gel.models.pydantic import (
    AnyEnum,
    Cardinality,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    GelPointerReflection,
    LazyClassProperty,
    MultiLink,
    OptionalProperty,
    PathAlias,
    PointerKind,
    PyConstType,
    RequiredMultiLink,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as ___builtins_1__
import builtins as ___builtins__
import datetime as datetime
from builtins import tuple, type
from collections.abc import Callable, Iterable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from ... import cfg as ___cfg__, schema, std as ___std__
    from ...ext import ai as ext_ai

    from gel.models import pydantic

    from builtins import dict, str


class ChatParticipantRole(AnyEnum):
    System = 'System'
    User = 'User'
    Assistant = 'Assistant'
    Tool = 'Tool'


class DistanceFunction(AnyEnum):
    Cosine = 'Cosine'
    InnerProduct = 'InnerProduct'
    L2 = 'L2'


class IndexType(AnyEnum):
    HNSW = 'HNSW'


class ProviderAPIStyle(AnyEnum):
    OpenAI = 'OpenAI'
    Anthropic = 'Anthropic'
    Ollama = 'Ollama'




#
# type ext::ai::ProviderConfig
#
class __ProviderConfig_typeof_base__(cfg.__ConfigObject_typeof_base__):
    class __gel_reflection__(
        cfg.__ConfigObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=239064927547599299673428706603055147738)
        name = SchemaPath('ext', 'ai', 'ProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'api_url': GelPointerReflection(
                    name='api_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'client_id': GelPointerReflection(
                    name='client_id',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'secret': GelPointerReflection(
                    name='secret',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'api_style': GelPointerReflection(
                    name='api_style',
                    type=SchemaPath('ext', 'ai', 'ProviderAPIStyle'),
                    typexpr='ext::ai::ProviderAPIStyle',
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
                | cfg.__ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=239064927547599299673428706603055147738),
                name='ext::ai::ProviderConfig',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __ProviderConfig_typeof__(
    cfg.__ConfigObject_typeof__,
    __ProviderConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        api_url = TypeAliasType('api_url', 'std.str')
        client_id = TypeAliasType('client_id', 'OptionalProperty[std.str, builtins.str]')
        secret = TypeAliasType('secret', 'std.str')
        api_style = TypeAliasType('api_style', 'ProviderAPIStyle')


class __ProviderConfig_typeof_partial__(
    cfg.__ConfigObject_typeof_partial__,
    __ProviderConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, builtins.str]')
        api_url = TypeAliasType('api_url', 'OptionalProperty[std.str, builtins.str]')
        client_id = TypeAliasType('client_id', 'OptionalProperty[std.str, builtins.str]')
        secret = TypeAliasType('secret', 'OptionalProperty[std.str, builtins.str]')
        api_style = TypeAliasType('api_style', 'OptionalProperty[ProviderAPIStyle, ___builtins__.str]')


class ProviderConfig(
    __ProviderConfig_typeof__,
    cfg.ConfigObject,
    __gel_type_id__=UUID(int=239064927547599299673428706603055147738),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            display_name: builtins.str,
            api_url: builtins.str,
            client_id: builtins.str | None = None,
            secret: builtins.str,
            api_style: ___builtins__.str,
        ) -> None:
            """Create a new ext::ai::ProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::ProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::ProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::ProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(cfg.ConfigObject.__variants__):
        class Base(
            __ProviderConfig_typeof__,
            cfg.ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    display_name: builtins.str,
                    api_url: builtins.str,
                    client_id: builtins.str | None = None,
                    secret: builtins.str,
                    api_style: ___builtins__.str,
                ) -> None:
                    """Create a new ext::ai::ProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::ProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::ProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::ProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str
            api_url: ___std_1__.str
            secret: ___std_1__.str
            api_style: ___ext_ai__.ProviderAPIStyle

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ProviderConfig_typeof_partial__,
            Base,
            cfg.ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            cfg.ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, builtins.str]
            display_name: OptionalProperty[___std_1__.str, builtins.str]
            api_url: OptionalProperty[___std_1__.str, builtins.str]
            client_id: OptionalProperty[___std_1__.str, builtins.str]
            secret: OptionalProperty[___std_1__.str, builtins.str]
            api_style: OptionalProperty[___ext_ai__.ProviderAPIStyle, ___builtins__.str]


        Any = TypeVar("Any", bound="ProviderConfig | Base | Required | Partial")
    class __links__(cfg.ConfigObject.__links__):
        pass
    class __links_partial__(cfg.ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ProviderConfig.__variants__.Base = ProviderConfig



#
# type ext::ai::ChatPrompt
#
class __ChatPrompt_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=305455604430406941398276820075415927650)
        name = SchemaPath('ext', 'ai', 'ChatPrompt')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
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
                'messages': GelPointerReflection(
                    name='messages',
                    type=SchemaPath('ext', 'ai', 'ChatPromptMessage'),
                    typexpr='ext::ai::ChatPromptMessage',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtLeastOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | std.__BaseObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=305455604430406941398276820075415927650),
                name='ext::ai::ChatPrompt',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __ChatPrompt_typeof__(
    std.__BaseObject_typeof__,
    __ChatPrompt_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        messages = TypeAliasType('messages', 'RequiredMultiLink[ChatPromptMessage]')


class __ChatPrompt_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __ChatPrompt_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        messages = TypeAliasType('messages', 'RequiredMultiLink[ChatPromptMessage | ChatPromptMessage.__variants__.Partial]')


class ChatPrompt(
    __ChatPrompt_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=305455604430406941398276820075415927650),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            messages: Iterable[ChatPromptMessage] = [],
        ) -> None:
            """Create a new ext::ai::ChatPrompt instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            messages: type[ext_ai.ChatPromptMessage] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::ChatPrompt instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            messages: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ChatPromptMessage] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::ChatPrompt instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            messages: type[ext_ai.ChatPromptMessage] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::ChatPrompt instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __ChatPrompt_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    messages: Iterable[ChatPromptMessage] = [],
                ) -> None:
                    """Create a new ext::ai::ChatPrompt instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    messages: type[ext_ai.ChatPromptMessage] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::ChatPrompt instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    messages: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ChatPromptMessage] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::ChatPrompt instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    messages: type[ext_ai.ChatPromptMessage] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::ChatPrompt instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.BaseObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            messages: RequiredMultiLink[___ext_ai__.ChatPromptMessage]

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ChatPrompt_typeof_partial__,
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
            name: OptionalProperty[___std_1__.str, builtins.str]
            messages: RequiredMultiLink[___ext_ai__.ChatPromptMessage | ___ext_ai__.ChatPromptMessage.__variants__.Partial]


        Any = TypeVar("Any", bound="ChatPrompt | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ChatPrompt.__variants__.Base = ChatPrompt



#
# type ext::ai::ChatPromptMessage
#
class __ChatPromptMessage_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=136555288198560297577554991694011973724)
        name = SchemaPath('ext', 'ai', 'ChatPromptMessage')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'participant_role': GelPointerReflection(
                    name='participant_role',
                    type=SchemaPath('ext', 'ai', 'ChatParticipantRole'),
                    typexpr='ext::ai::ChatParticipantRole',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'participant_name': GelPointerReflection(
                    name='participant_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'content': GelPointerReflection(
                    name='content',
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
                | std.__BaseObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=136555288198560297577554991694011973724),
                name='ext::ai::ChatPromptMessage',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __ChatPromptMessage_typeof__(
    std.__BaseObject_typeof__,
    __ChatPromptMessage_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        participant_role = TypeAliasType('participant_role', 'ChatParticipantRole')
        participant_name = TypeAliasType('participant_name', 'OptionalProperty[std.str, builtins.str]')
        content = TypeAliasType('content', 'std.str')


class __ChatPromptMessage_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __ChatPromptMessage_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        participant_role = TypeAliasType('participant_role', 'OptionalProperty[ChatParticipantRole, ___builtins__.str]')
        participant_name = TypeAliasType('participant_name', 'OptionalProperty[std.str, builtins.str]')
        content = TypeAliasType('content', 'OptionalProperty[std.str, builtins.str]')


class ChatPromptMessage(
    __ChatPromptMessage_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=136555288198560297577554991694011973724),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            participant_role: ___builtins__.str,
            participant_name: builtins.str | None = None,
            content: builtins.str,
        ) -> None:
            """Create a new ext::ai::ChatPromptMessage instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            participant_role: type[ext_ai.ChatParticipantRole] | UnspecifiedType = Unspecified,
            participant_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            content: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::ChatPromptMessage instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            participant_role: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ChatParticipantRole] | UnspecifiedType = Unspecified,
            participant_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            content: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::ChatPromptMessage instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            participant_role: type[ext_ai.ChatParticipantRole] | UnspecifiedType = Unspecified,
            participant_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            content: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::ChatPromptMessage instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            participant_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            content: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __ChatPromptMessage_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    participant_role: ___builtins__.str,
                    participant_name: builtins.str | None = None,
                    content: builtins.str,
                ) -> None:
                    """Create a new ext::ai::ChatPromptMessage instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    participant_role: type[ext_ai.ChatParticipantRole] | UnspecifiedType = Unspecified,
                    participant_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    content: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::ChatPromptMessage instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    participant_role: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ChatParticipantRole] | UnspecifiedType = Unspecified,
                    participant_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    content: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::ChatPromptMessage instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    participant_role: type[ext_ai.ChatParticipantRole] | UnspecifiedType = Unspecified,
                    participant_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    content: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::ChatPromptMessage instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    participant_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    content: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.BaseObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            participant_role: ___ext_ai__.ChatParticipantRole
            content: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ChatPromptMessage_typeof_partial__,
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
            participant_role: OptionalProperty[___ext_ai__.ChatParticipantRole, ___builtins__.str]
            participant_name: OptionalProperty[___std_1__.str, builtins.str]
            content: OptionalProperty[___std_1__.str, builtins.str]


        Any = TypeVar("Any", bound="ChatPromptMessage | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ChatPromptMessage.__variants__.Base = ChatPromptMessage



#
# type ext::ai::Config
#
class __Config_typeof_base__(cfg.__ExtensionConfig_typeof_base__):
    class __gel_reflection__(
        cfg.__ExtensionConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=315155330267289575628254047593178499400)
        name = SchemaPath('ext', 'ai', 'Config')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'indexer_naptime': GelPointerReflection(
                    name='indexer_naptime',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'providers': GelPointerReflection(
                    name='providers',
                    type=SchemaPath('ext', 'ai', 'ProviderConfig'),
                    typexpr='ext::ai::ProviderConfig',
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
                | cfg.__ExtensionConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=315155330267289575628254047593178499400),
                name='ext::ai::Config',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Config_typeof__(
    cfg.__ExtensionConfig_typeof__,
    __Config_typeof_base__,
):
    class __typeof__(cfg.__ExtensionConfig_typeof__.__typeof__):
        indexer_naptime = TypeAliasType('indexer_naptime', 'std.duration')
        providers = TypeAliasType('providers', 'MultiLink[ProviderConfig]')


class __Config_typeof_partial__(
    cfg.__ExtensionConfig_typeof_partial__,
    __Config_typeof_base__,
):
    class __typeof__(cfg.__ExtensionConfig_typeof_partial__.__typeof__):
        indexer_naptime = TypeAliasType('indexer_naptime', 'OptionalProperty[std.duration, timedelta]')
        providers = TypeAliasType('providers', 'MultiLink[ProviderConfig | ProviderConfig.__variants__.Partial]')


class Config(
    __Config_typeof__,
    cfg.ExtensionConfig,
    __gel_type_id__=UUID(int=315155330267289575628254047593178499400),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            cfg: cfg.AbstractConfig | None = None,
            indexer_naptime: timedelta | DefaultValue = DEFAULT_VALUE,
            providers: Iterable[ProviderConfig] = [],
        ) -> None:
            """Create a new ext::ai::Config instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            indexer_naptime: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            providers: type[ext_ai.ProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::Config instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            indexer_naptime: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            providers: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::Config instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            indexer_naptime: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            providers: type[ext_ai.ProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::Config instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            indexer_naptime: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(cfg.ExtensionConfig.__variants__):
        class Base(
            __Config_typeof__,
            cfg.ExtensionConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    cfg: cfg.AbstractConfig | None = None,
                    indexer_naptime: timedelta | DefaultValue = DEFAULT_VALUE,
                    providers: Iterable[ProviderConfig] = [],
                ) -> None:
                    """Create a new ext::ai::Config instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    indexer_naptime: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    providers: type[ext_ai.ProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::Config instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    indexer_naptime: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    providers: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::Config instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    indexer_naptime: datetime.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    providers: type[ext_ai.ProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::Config instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    indexer_naptime: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ExtensionConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            indexer_naptime: ___std_1__.duration

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Config_typeof_partial__,
            Base,
            cfg.ExtensionConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            cfg.ExtensionConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            indexer_naptime: OptionalProperty[___std_1__.duration, timedelta]
            providers: MultiLink[___ext_ai__.ProviderConfig | ___ext_ai__.ProviderConfig.__variants__.Partial]


        Any = TypeVar("Any", bound="Config | Base | Required | Partial")
    class __links__(cfg.ExtensionConfig.__links__):
        pass
    class __links_partial__(cfg.ExtensionConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    Config.__variants__.Base = Config



#
# type ext::ai::Model
#
class __Model_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=114809198205363281988144613900879887091)
        name = SchemaPath('ext', 'ai', 'Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | std.__BaseObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=114809198205363281988144613900879887091),
                name='ext::ai::Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __Model_typeof__(std.__BaseObject_typeof__, __Model_typeof_base__):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        pass


class __Model_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __Model_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        pass


class Model(
    __Model_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=114809198205363281988144613900879887091),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __Model_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
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
            __Model_typeof_partial__,
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


        Any = TypeVar("Any", bound="Model | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    Model.__variants__.Base = Model



#
# type ext::ai::AnthropicProviderConfig
#
class __AnthropicProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=199930721627745452910100237396016552183)
        name = SchemaPath('ext', 'ai', 'AnthropicProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_url': GelPointerReflection(
                    name='api_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_style': GelPointerReflection(
                    name='api_style',
                    type=SchemaPath('ext', 'ai', 'ProviderAPIStyle'),
                    typexpr='ext::ai::ProviderAPIStyle',
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
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=199930721627745452910100237396016552183),
                name='ext::ai::AnthropicProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __AnthropicProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __AnthropicProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        api_url = TypeAliasType('api_url', 'std.str')
        api_style = TypeAliasType('api_style', 'ProviderAPIStyle')


class __AnthropicProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __AnthropicProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, builtins.str]')
        api_url = TypeAliasType('api_url', 'OptionalProperty[std.str, builtins.str]')
        api_style = TypeAliasType('api_style', 'OptionalProperty[ProviderAPIStyle, ___builtins__.str]')


class AnthropicProviderConfig(
    __AnthropicProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=199930721627745452910100237396016552183),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str | DefaultValue = DEFAULT_VALUE,
            display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
            api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
            client_id: builtins.str | None = None,
            secret: builtins.str,
            api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::ai::AnthropicProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::AnthropicProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __AnthropicProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
                    client_id: builtins.str | None = None,
                    secret: builtins.str,
                    api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::ai::AnthropicProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::AnthropicProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str
            api_url: ___std_1__.str
            api_style: ___ext_ai__.ProviderAPIStyle

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AnthropicProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, builtins.str]
            display_name: OptionalProperty[___std_1__.str, builtins.str]
            api_url: OptionalProperty[___std_1__.str, builtins.str]
            api_style: OptionalProperty[___ext_ai__.ProviderAPIStyle, ___builtins__.str]


        Any = TypeVar("Any", bound="AnthropicProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    AnthropicProviderConfig.__variants__.Base = AnthropicProviderConfig



#
# type ext::ai::CustomProviderConfig
#
class __CustomProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=315577562007178926612683925810930560849)
        name = SchemaPath('ext', 'ai', 'CustomProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_style': GelPointerReflection(
                    name='api_style',
                    type=SchemaPath('ext', 'ai', 'ProviderAPIStyle'),
                    typexpr='ext::ai::ProviderAPIStyle',
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
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=315577562007178926612683925810930560849),
                name='ext::ai::CustomProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __CustomProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __CustomProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        display_name = TypeAliasType('display_name', 'std.str')
        api_style = TypeAliasType('api_style', 'ProviderAPIStyle')


class __CustomProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __CustomProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, builtins.str]')
        api_style = TypeAliasType('api_style', 'OptionalProperty[ProviderAPIStyle, ___builtins__.str]')


class CustomProviderConfig(
    __CustomProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=315577562007178926612683925810930560849),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str,
            display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
            api_url: builtins.str,
            client_id: builtins.str | None = None,
            secret: builtins.str,
            api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::ai::CustomProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::CustomProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::CustomProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::CustomProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __CustomProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str,
                    display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    api_url: builtins.str,
                    client_id: builtins.str | None = None,
                    secret: builtins.str,
                    api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::ai::CustomProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::CustomProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::CustomProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::CustomProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            display_name: ___std_1__.str
            api_style: ___ext_ai__.ProviderAPIStyle

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __CustomProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            display_name: OptionalProperty[___std_1__.str, builtins.str]
            api_style: OptionalProperty[___ext_ai__.ProviderAPIStyle, ___builtins__.str]


        Any = TypeVar("Any", bound="CustomProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    CustomProviderConfig.__variants__.Base = CustomProviderConfig



#
# type ext::ai::MistralProviderConfig
#
class __MistralProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=296587393137292619457294705098738614539)
        name = SchemaPath('ext', 'ai', 'MistralProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_url': GelPointerReflection(
                    name='api_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_style': GelPointerReflection(
                    name='api_style',
                    type=SchemaPath('ext', 'ai', 'ProviderAPIStyle'),
                    typexpr='ext::ai::ProviderAPIStyle',
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
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=296587393137292619457294705098738614539),
                name='ext::ai::MistralProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __MistralProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __MistralProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        api_url = TypeAliasType('api_url', 'std.str')
        api_style = TypeAliasType('api_style', 'ProviderAPIStyle')


class __MistralProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __MistralProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, builtins.str]')
        api_url = TypeAliasType('api_url', 'OptionalProperty[std.str, builtins.str]')
        api_style = TypeAliasType('api_style', 'OptionalProperty[ProviderAPIStyle, ___builtins__.str]')


class MistralProviderConfig(
    __MistralProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=296587393137292619457294705098738614539),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str | DefaultValue = DEFAULT_VALUE,
            display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
            api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
            client_id: builtins.str | None = None,
            secret: builtins.str,
            api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::ai::MistralProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::MistralProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::MistralProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::MistralProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __MistralProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
                    client_id: builtins.str | None = None,
                    secret: builtins.str,
                    api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::ai::MistralProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::MistralProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str
            api_url: ___std_1__.str
            api_style: ___ext_ai__.ProviderAPIStyle

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MistralProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, builtins.str]
            display_name: OptionalProperty[___std_1__.str, builtins.str]
            api_url: OptionalProperty[___std_1__.str, builtins.str]
            api_style: OptionalProperty[___ext_ai__.ProviderAPIStyle, ___builtins__.str]


        Any = TypeVar("Any", bound="MistralProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    MistralProviderConfig.__variants__.Base = MistralProviderConfig



#
# type ext::ai::OllamaProviderConfig
#
class __OllamaProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=326828658564379000100804876271020876608)
        name = SchemaPath('ext', 'ai', 'OllamaProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_url': GelPointerReflection(
                    name='api_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'secret': GelPointerReflection(
                    name='secret',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_style': GelPointerReflection(
                    name='api_style',
                    type=SchemaPath('ext', 'ai', 'ProviderAPIStyle'),
                    typexpr='ext::ai::ProviderAPIStyle',
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
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=326828658564379000100804876271020876608),
                name='ext::ai::OllamaProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __OllamaProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __OllamaProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        api_url = TypeAliasType('api_url', 'std.str')
        secret = TypeAliasType('secret', 'std.str')
        api_style = TypeAliasType('api_style', 'ProviderAPIStyle')


class __OllamaProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __OllamaProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, builtins.str]')
        api_url = TypeAliasType('api_url', 'OptionalProperty[std.str, builtins.str]')
        secret = TypeAliasType('secret', 'OptionalProperty[std.str, builtins.str]')
        api_style = TypeAliasType('api_style', 'OptionalProperty[ProviderAPIStyle, ___builtins__.str]')


class OllamaProviderConfig(
    __OllamaProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=326828658564379000100804876271020876608),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str | DefaultValue = DEFAULT_VALUE,
            display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
            api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
            client_id: builtins.str | None = None,
            secret: builtins.str | DefaultValue = DEFAULT_VALUE,
            api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::ai::OllamaProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::OllamaProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __OllamaProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
                    client_id: builtins.str | None = None,
                    secret: builtins.str | DefaultValue = DEFAULT_VALUE,
                    api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::ai::OllamaProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::OllamaProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str
            api_url: ___std_1__.str
            secret: ___std_1__.str
            api_style: ___ext_ai__.ProviderAPIStyle

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OllamaProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, builtins.str]
            display_name: OptionalProperty[___std_1__.str, builtins.str]
            api_url: OptionalProperty[___std_1__.str, builtins.str]
            secret: OptionalProperty[___std_1__.str, builtins.str]
            api_style: OptionalProperty[___ext_ai__.ProviderAPIStyle, ___builtins__.str]


        Any = TypeVar("Any", bound="OllamaProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    OllamaProviderConfig.__variants__.Base = OllamaProviderConfig



#
# type ext::ai::OpenAIProviderConfig
#
class __OpenAIProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=260382159296029060506233529683811099499)
        name = SchemaPath('ext', 'ai', 'OpenAIProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_url': GelPointerReflection(
                    name='api_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'api_style': GelPointerReflection(
                    name='api_style',
                    type=SchemaPath('ext', 'ai', 'ProviderAPIStyle'),
                    typexpr='ext::ai::ProviderAPIStyle',
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
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=260382159296029060506233529683811099499),
                name='ext::ai::OpenAIProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __OpenAIProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __OpenAIProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        api_url = TypeAliasType('api_url', 'std.str')
        api_style = TypeAliasType('api_style', 'ProviderAPIStyle')


class __OpenAIProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __OpenAIProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, builtins.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, builtins.str]')
        api_url = TypeAliasType('api_url', 'OptionalProperty[std.str, builtins.str]')
        api_style = TypeAliasType('api_style', 'OptionalProperty[ProviderAPIStyle, ___builtins__.str]')


class OpenAIProviderConfig(
    __OpenAIProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=260382159296029060506233529683811099499),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: builtins.str | DefaultValue = DEFAULT_VALUE,
            display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
            api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
            client_id: builtins.str | None = None,
            secret: builtins.str,
            api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::ai::OpenAIProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::ai::OpenAIProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
            secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __OpenAIProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    display_name: builtins.str | DefaultValue = DEFAULT_VALUE,
                    api_url: builtins.str | DefaultValue = DEFAULT_VALUE,
                    client_id: builtins.str | None = None,
                    secret: builtins.str,
                    api_style: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::ai::OpenAIProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::ai::OpenAIProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_url: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    api_style: type[ext_ai.ProviderAPIStyle] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    api_url: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                    secret: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str
            api_url: ___std_1__.str
            api_style: ___ext_ai__.ProviderAPIStyle

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, builtins.str]
            display_name: OptionalProperty[___std_1__.str, builtins.str]
            api_url: OptionalProperty[___std_1__.str, builtins.str]
            api_style: OptionalProperty[___ext_ai__.ProviderAPIStyle, ___builtins__.str]


        Any = TypeVar("Any", bound="OpenAIProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIProviderConfig.__variants__.Base = OpenAIProviderConfig



#
# type ext::ai::EmbeddingModel
#
class __EmbeddingModel_typeof_base__(__Model_typeof_base__):
    class __gel_reflection__(__Model_typeof_base__.__gel_reflection__):
        id = UUID(int=58319906403359763627365387341246501243)
        name = SchemaPath('ext', 'ai', 'EmbeddingModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __Model_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=58319906403359763627365387341246501243),
                name='ext::ai::EmbeddingModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __EmbeddingModel_typeof__(
    __Model_typeof__,
    __EmbeddingModel_typeof_base__,
):
    class __typeof__(__Model_typeof__.__typeof__):
        pass


class __EmbeddingModel_typeof_partial__(
    __Model_typeof_partial__,
    __EmbeddingModel_typeof_base__,
):
    class __typeof__(__Model_typeof_partial__.__typeof__):
        pass


class EmbeddingModel(
    __EmbeddingModel_typeof__,
    Model,
    __gel_type_id__=UUID(int=58319906403359763627365387341246501243),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::EmbeddingModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::EmbeddingModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::EmbeddingModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::EmbeddingModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Model.__variants__):
        class Base(
            __EmbeddingModel_typeof__,
            Model.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::EmbeddingModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::EmbeddingModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::EmbeddingModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::EmbeddingModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Model.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __EmbeddingModel_typeof_partial__,
            Base,
            Model.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Model.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="EmbeddingModel | Base | Required | Partial")
    class __links__(Model.__links__):
        pass
    class __links_partial__(Model.__links_partial__):
        pass

if not TYPE_CHECKING:
    EmbeddingModel.__variants__.Base = EmbeddingModel



#
# type ext::ai::TextGenerationModel
#
class __TextGenerationModel_typeof_base__(__Model_typeof_base__):
    class __gel_reflection__(__Model_typeof_base__.__gel_reflection__):
        id = UUID(int=319242015374593498865837715086683286924)
        name = SchemaPath('ext', 'ai', 'TextGenerationModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __Model_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=319242015374593498865837715086683286924),
                name='ext::ai::TextGenerationModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __TextGenerationModel_typeof__(
    __Model_typeof__,
    __TextGenerationModel_typeof_base__,
):
    class __typeof__(__Model_typeof__.__typeof__):
        pass


class __TextGenerationModel_typeof_partial__(
    __Model_typeof_partial__,
    __TextGenerationModel_typeof_base__,
):
    class __typeof__(__Model_typeof_partial__.__typeof__):
        pass


class TextGenerationModel(
    __TextGenerationModel_typeof__,
    Model,
    __gel_type_id__=UUID(int=319242015374593498865837715086683286924),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::TextGenerationModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::TextGenerationModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::TextGenerationModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::TextGenerationModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Model.__variants__):
        class Base(
            __TextGenerationModel_typeof__,
            Model.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::TextGenerationModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::TextGenerationModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::TextGenerationModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::TextGenerationModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Model.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __TextGenerationModel_typeof_partial__,
            Base,
            Model.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Model.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="TextGenerationModel | Base | Required | Partial")
    class __links__(Model.__links__):
        pass
    class __links_partial__(Model.__links_partial__):
        pass

if not TYPE_CHECKING:
    TextGenerationModel.__variants__.Base = TextGenerationModel



#
# type ext::ai::MistralEmbedModel
#
class __MistralEmbedModel_typeof_base__(__EmbeddingModel_typeof_base__):
    class __gel_reflection__(
        __EmbeddingModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=268365843505481712162380815034188364377)
        name = SchemaPath('ext', 'ai', 'MistralEmbedModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __EmbeddingModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=268365843505481712162380815034188364377),
                name='ext::ai::MistralEmbedModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __MistralEmbedModel_typeof__(
    __EmbeddingModel_typeof__,
    __MistralEmbedModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof__.__typeof__):
        pass


class __MistralEmbedModel_typeof_partial__(
    __EmbeddingModel_typeof_partial__,
    __MistralEmbedModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof_partial__.__typeof__):
        pass


class MistralEmbedModel(
    __MistralEmbedModel_typeof__,
    EmbeddingModel,
    __gel_type_id__=UUID(int=268365843505481712162380815034188364377),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::MistralEmbedModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::MistralEmbedModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::MistralEmbedModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::MistralEmbedModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmbeddingModel.__variants__):
        class Base(
            __MistralEmbedModel_typeof__,
            EmbeddingModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::MistralEmbedModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::MistralEmbedModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralEmbedModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralEmbedModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmbeddingModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MistralEmbedModel_typeof_partial__,
            Base,
            EmbeddingModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmbeddingModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="MistralEmbedModel | Base | Required | Partial")
    class __links__(EmbeddingModel.__links__):
        pass
    class __links_partial__(EmbeddingModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    MistralEmbedModel.__variants__.Base = MistralEmbedModel



#
# type ext::ai::OllamaBgeM3Model
#
class __OllamaBgeM3Model_typeof_base__(__EmbeddingModel_typeof_base__):
    class __gel_reflection__(
        __EmbeddingModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=103447839867780710834356761126370298739)
        name = SchemaPath('ext', 'ai', 'OllamaBgeM3Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __EmbeddingModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=103447839867780710834356761126370298739),
                name='ext::ai::OllamaBgeM3Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OllamaBgeM3Model_typeof__(
    __EmbeddingModel_typeof__,
    __OllamaBgeM3Model_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof__.__typeof__):
        pass


class __OllamaBgeM3Model_typeof_partial__(
    __EmbeddingModel_typeof_partial__,
    __OllamaBgeM3Model_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof_partial__.__typeof__):
        pass


class OllamaBgeM3Model(
    __OllamaBgeM3Model_typeof__,
    EmbeddingModel,
    __gel_type_id__=UUID(int=103447839867780710834356761126370298739),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OllamaBgeM3Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OllamaBgeM3Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaBgeM3Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaBgeM3Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmbeddingModel.__variants__):
        class Base(
            __OllamaBgeM3Model_typeof__,
            EmbeddingModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OllamaBgeM3Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OllamaBgeM3Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaBgeM3Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaBgeM3Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmbeddingModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OllamaBgeM3Model_typeof_partial__,
            Base,
            EmbeddingModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmbeddingModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OllamaBgeM3Model | Base | Required | Partial")
    class __links__(EmbeddingModel.__links__):
        pass
    class __links_partial__(EmbeddingModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OllamaBgeM3Model.__variants__.Base = OllamaBgeM3Model



#
# type ext::ai::OllamaNomicEmbedTextModel
#
class __OllamaNomicEmbedTextModel_typeof_base__(
    __EmbeddingModel_typeof_base__,
):
    class __gel_reflection__(
        __EmbeddingModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=154105092220329929129100608368232760929)
        name = SchemaPath('ext', 'ai', 'OllamaNomicEmbedTextModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __EmbeddingModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=154105092220329929129100608368232760929),
                name='ext::ai::OllamaNomicEmbedTextModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OllamaNomicEmbedTextModel_typeof__(
    __EmbeddingModel_typeof__,
    __OllamaNomicEmbedTextModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof__.__typeof__):
        pass


class __OllamaNomicEmbedTextModel_typeof_partial__(
    __EmbeddingModel_typeof_partial__,
    __OllamaNomicEmbedTextModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof_partial__.__typeof__):
        pass


class OllamaNomicEmbedTextModel(
    __OllamaNomicEmbedTextModel_typeof__,
    EmbeddingModel,
    __gel_type_id__=UUID(int=154105092220329929129100608368232760929),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OllamaNomicEmbedTextModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OllamaNomicEmbedTextModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaNomicEmbedTextModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaNomicEmbedTextModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmbeddingModel.__variants__):
        class Base(
            __OllamaNomicEmbedTextModel_typeof__,
            EmbeddingModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OllamaNomicEmbedTextModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OllamaNomicEmbedTextModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaNomicEmbedTextModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaNomicEmbedTextModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmbeddingModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OllamaNomicEmbedTextModel_typeof_partial__,
            Base,
            EmbeddingModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmbeddingModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OllamaNomicEmbedTextModel | Base | Required | Partial")
    class __links__(EmbeddingModel.__links__):
        pass
    class __links_partial__(EmbeddingModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OllamaNomicEmbedTextModel.__variants__.Base = OllamaNomicEmbedTextModel



#
# type ext::ai::OpenAITextEmbedding3LargeModel
#
class __OpenAITextEmbedding3LargeModel_typeof_base__(
    __EmbeddingModel_typeof_base__,
):
    class __gel_reflection__(
        __EmbeddingModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=233844593006439801798153539455487499063)
        name = SchemaPath('ext', 'ai', 'OpenAITextEmbedding3LargeModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __EmbeddingModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=233844593006439801798153539455487499063),
                name='ext::ai::OpenAITextEmbedding3LargeModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAITextEmbedding3LargeModel_typeof__(
    __EmbeddingModel_typeof__,
    __OpenAITextEmbedding3LargeModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof__.__typeof__):
        pass


class __OpenAITextEmbedding3LargeModel_typeof_partial__(
    __EmbeddingModel_typeof_partial__,
    __OpenAITextEmbedding3LargeModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof_partial__.__typeof__):
        pass


class OpenAITextEmbedding3LargeModel(
    __OpenAITextEmbedding3LargeModel_typeof__,
    EmbeddingModel,
    __gel_type_id__=UUID(int=233844593006439801798153539455487499063),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAITextEmbedding3LargeModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAITextEmbedding3LargeModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAITextEmbedding3LargeModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAITextEmbedding3LargeModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmbeddingModel.__variants__):
        class Base(
            __OpenAITextEmbedding3LargeModel_typeof__,
            EmbeddingModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAITextEmbedding3LargeModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAITextEmbedding3LargeModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAITextEmbedding3LargeModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAITextEmbedding3LargeModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmbeddingModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAITextEmbedding3LargeModel_typeof_partial__,
            Base,
            EmbeddingModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmbeddingModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAITextEmbedding3LargeModel | Base | Required | Partial")
    class __links__(EmbeddingModel.__links__):
        pass
    class __links_partial__(EmbeddingModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAITextEmbedding3LargeModel.__variants__.Base = OpenAITextEmbedding3LargeModel



#
# type ext::ai::OpenAITextEmbedding3SmallModel
#
class __OpenAITextEmbedding3SmallModel_typeof_base__(
    __EmbeddingModel_typeof_base__,
):
    class __gel_reflection__(
        __EmbeddingModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=51828342966917618216269929047272115093)
        name = SchemaPath('ext', 'ai', 'OpenAITextEmbedding3SmallModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __EmbeddingModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=51828342966917618216269929047272115093),
                name='ext::ai::OpenAITextEmbedding3SmallModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAITextEmbedding3SmallModel_typeof__(
    __EmbeddingModel_typeof__,
    __OpenAITextEmbedding3SmallModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof__.__typeof__):
        pass


class __OpenAITextEmbedding3SmallModel_typeof_partial__(
    __EmbeddingModel_typeof_partial__,
    __OpenAITextEmbedding3SmallModel_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof_partial__.__typeof__):
        pass


class OpenAITextEmbedding3SmallModel(
    __OpenAITextEmbedding3SmallModel_typeof__,
    EmbeddingModel,
    __gel_type_id__=UUID(int=51828342966917618216269929047272115093),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAITextEmbedding3SmallModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAITextEmbedding3SmallModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAITextEmbedding3SmallModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAITextEmbedding3SmallModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmbeddingModel.__variants__):
        class Base(
            __OpenAITextEmbedding3SmallModel_typeof__,
            EmbeddingModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAITextEmbedding3SmallModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAITextEmbedding3SmallModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAITextEmbedding3SmallModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAITextEmbedding3SmallModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmbeddingModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAITextEmbedding3SmallModel_typeof_partial__,
            Base,
            EmbeddingModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmbeddingModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAITextEmbedding3SmallModel | Base | Required | Partial")
    class __links__(EmbeddingModel.__links__):
        pass
    class __links_partial__(EmbeddingModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAITextEmbedding3SmallModel.__variants__.Base = OpenAITextEmbedding3SmallModel



#
# type ext::ai::OpenAITextEmbeddingAda002Model
#
class __OpenAITextEmbeddingAda002Model_typeof_base__(
    __EmbeddingModel_typeof_base__,
):
    class __gel_reflection__(
        __EmbeddingModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=221884035243765275364172999678223820727)
        name = SchemaPath('ext', 'ai', 'OpenAITextEmbeddingAda002Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __EmbeddingModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=221884035243765275364172999678223820727),
                name='ext::ai::OpenAITextEmbeddingAda002Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAITextEmbeddingAda002Model_typeof__(
    __EmbeddingModel_typeof__,
    __OpenAITextEmbeddingAda002Model_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof__.__typeof__):
        pass


class __OpenAITextEmbeddingAda002Model_typeof_partial__(
    __EmbeddingModel_typeof_partial__,
    __OpenAITextEmbeddingAda002Model_typeof_base__,
):
    class __typeof__(__EmbeddingModel_typeof_partial__.__typeof__):
        pass


class OpenAITextEmbeddingAda002Model(
    __OpenAITextEmbeddingAda002Model_typeof__,
    EmbeddingModel,
    __gel_type_id__=UUID(int=221884035243765275364172999678223820727),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAITextEmbeddingAda002Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAITextEmbeddingAda002Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAITextEmbeddingAda002Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAITextEmbeddingAda002Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmbeddingModel.__variants__):
        class Base(
            __OpenAITextEmbeddingAda002Model_typeof__,
            EmbeddingModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAITextEmbeddingAda002Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAITextEmbeddingAda002Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAITextEmbeddingAda002Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAITextEmbeddingAda002Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmbeddingModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAITextEmbeddingAda002Model_typeof_partial__,
            Base,
            EmbeddingModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmbeddingModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAITextEmbeddingAda002Model | Base | Required | Partial")
    class __links__(EmbeddingModel.__links__):
        pass
    class __links_partial__(EmbeddingModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAITextEmbeddingAda002Model.__variants__.Base = OpenAITextEmbeddingAda002Model



#
# type ext::ai::AnthropicClaude3HaikuModel
#
class __AnthropicClaude3HaikuModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=237433772027756241139820493221213094208)
        name = SchemaPath('ext', 'ai', 'AnthropicClaude3HaikuModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=237433772027756241139820493221213094208),
                name='ext::ai::AnthropicClaude3HaikuModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AnthropicClaude3HaikuModel_typeof__(
    __TextGenerationModel_typeof__,
    __AnthropicClaude3HaikuModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __AnthropicClaude3HaikuModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __AnthropicClaude3HaikuModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class AnthropicClaude3HaikuModel(
    __AnthropicClaude3HaikuModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=237433772027756241139820493221213094208),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::AnthropicClaude3HaikuModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::AnthropicClaude3HaikuModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude3HaikuModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude3HaikuModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __AnthropicClaude3HaikuModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::AnthropicClaude3HaikuModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::AnthropicClaude3HaikuModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude3HaikuModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude3HaikuModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AnthropicClaude3HaikuModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="AnthropicClaude3HaikuModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    AnthropicClaude3HaikuModel.__variants__.Base = AnthropicClaude3HaikuModel



#
# type ext::ai::AnthropicClaude3OpusModel
#
class __AnthropicClaude3OpusModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=45768730791159983261982563152128403392)
        name = SchemaPath('ext', 'ai', 'AnthropicClaude3OpusModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=45768730791159983261982563152128403392),
                name='ext::ai::AnthropicClaude3OpusModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AnthropicClaude3OpusModel_typeof__(
    __TextGenerationModel_typeof__,
    __AnthropicClaude3OpusModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __AnthropicClaude3OpusModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __AnthropicClaude3OpusModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class AnthropicClaude3OpusModel(
    __AnthropicClaude3OpusModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=45768730791159983261982563152128403392),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::AnthropicClaude3OpusModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::AnthropicClaude3OpusModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude3OpusModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude3OpusModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __AnthropicClaude3OpusModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::AnthropicClaude3OpusModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::AnthropicClaude3OpusModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude3OpusModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude3OpusModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AnthropicClaude3OpusModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="AnthropicClaude3OpusModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    AnthropicClaude3OpusModel.__variants__.Base = AnthropicClaude3OpusModel



#
# type ext::ai::AnthropicClaude3SonnetModel
#
class __AnthropicClaude3SonnetModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=93224555998339317822489716009860233432)
        name = SchemaPath('ext', 'ai', 'AnthropicClaude3SonnetModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=93224555998339317822489716009860233432),
                name='ext::ai::AnthropicClaude3SonnetModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AnthropicClaude3SonnetModel_typeof__(
    __TextGenerationModel_typeof__,
    __AnthropicClaude3SonnetModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __AnthropicClaude3SonnetModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __AnthropicClaude3SonnetModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class AnthropicClaude3SonnetModel(
    __AnthropicClaude3SonnetModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=93224555998339317822489716009860233432),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::AnthropicClaude3SonnetModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::AnthropicClaude3SonnetModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude3SonnetModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude3SonnetModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __AnthropicClaude3SonnetModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::AnthropicClaude3SonnetModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::AnthropicClaude3SonnetModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude3SonnetModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude3SonnetModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AnthropicClaude3SonnetModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="AnthropicClaude3SonnetModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    AnthropicClaude3SonnetModel.__variants__.Base = AnthropicClaude3SonnetModel



#
# type ext::ai::AnthropicClaude_3_5_HaikuModel
#
class __AnthropicClaude_3_5_HaikuModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=57344321938556700939952672286588333797)
        name = SchemaPath('ext', 'ai', 'AnthropicClaude_3_5_HaikuModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=57344321938556700939952672286588333797),
                name='ext::ai::AnthropicClaude_3_5_HaikuModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AnthropicClaude_3_5_HaikuModel_typeof__(
    __TextGenerationModel_typeof__,
    __AnthropicClaude_3_5_HaikuModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __AnthropicClaude_3_5_HaikuModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __AnthropicClaude_3_5_HaikuModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class AnthropicClaude_3_5_HaikuModel(
    __AnthropicClaude_3_5_HaikuModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=57344321938556700939952672286588333797),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::AnthropicClaude_3_5_HaikuModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::AnthropicClaude_3_5_HaikuModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude_3_5_HaikuModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude_3_5_HaikuModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __AnthropicClaude_3_5_HaikuModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::AnthropicClaude_3_5_HaikuModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::AnthropicClaude_3_5_HaikuModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude_3_5_HaikuModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude_3_5_HaikuModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AnthropicClaude_3_5_HaikuModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="AnthropicClaude_3_5_HaikuModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    AnthropicClaude_3_5_HaikuModel.__variants__.Base = AnthropicClaude_3_5_HaikuModel



#
# type ext::ai::AnthropicClaude_3_5_SonnetModel
#
class __AnthropicClaude_3_5_SonnetModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=338003899884219999188704112923817217883)
        name = SchemaPath('ext', 'ai', 'AnthropicClaude_3_5_SonnetModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=338003899884219999188704112923817217883),
                name='ext::ai::AnthropicClaude_3_5_SonnetModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __AnthropicClaude_3_5_SonnetModel_typeof__(
    __TextGenerationModel_typeof__,
    __AnthropicClaude_3_5_SonnetModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __AnthropicClaude_3_5_SonnetModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __AnthropicClaude_3_5_SonnetModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class AnthropicClaude_3_5_SonnetModel(
    __AnthropicClaude_3_5_SonnetModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=338003899884219999188704112923817217883),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::AnthropicClaude_3_5_SonnetModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::AnthropicClaude_3_5_SonnetModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude_3_5_SonnetModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::AnthropicClaude_3_5_SonnetModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __AnthropicClaude_3_5_SonnetModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::AnthropicClaude_3_5_SonnetModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::AnthropicClaude_3_5_SonnetModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude_3_5_SonnetModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::AnthropicClaude_3_5_SonnetModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AnthropicClaude_3_5_SonnetModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="AnthropicClaude_3_5_SonnetModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    AnthropicClaude_3_5_SonnetModel.__variants__.Base = AnthropicClaude_3_5_SonnetModel



#
# type ext::ai::CodestralMamba
#
class __CodestralMamba_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=109185864641366287300294456954268173140)
        name = SchemaPath('ext', 'ai', 'CodestralMamba')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=109185864641366287300294456954268173140),
                name='ext::ai::CodestralMamba',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __CodestralMamba_typeof__(
    __TextGenerationModel_typeof__,
    __CodestralMamba_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __CodestralMamba_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __CodestralMamba_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class CodestralMamba(
    __CodestralMamba_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=109185864641366287300294456954268173140),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::CodestralMamba instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::CodestralMamba instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::CodestralMamba instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::CodestralMamba instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __CodestralMamba_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::CodestralMamba instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::CodestralMamba instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::CodestralMamba instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::CodestralMamba instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __CodestralMamba_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="CodestralMamba | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    CodestralMamba.__variants__.Base = CodestralMamba



#
# type ext::ai::CodestralModel
#
class __CodestralModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=182922077531884172092168190870704407561)
        name = SchemaPath('ext', 'ai', 'CodestralModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=182922077531884172092168190870704407561),
                name='ext::ai::CodestralModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __CodestralModel_typeof__(
    __TextGenerationModel_typeof__,
    __CodestralModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __CodestralModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __CodestralModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class CodestralModel(
    __CodestralModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=182922077531884172092168190870704407561),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::CodestralModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::CodestralModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::CodestralModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::CodestralModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __CodestralModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::CodestralModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::CodestralModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::CodestralModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::CodestralModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __CodestralModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="CodestralModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    CodestralModel.__variants__.Base = CodestralModel



#
# type ext::ai::Ministral_3B_Model
#
class __Ministral_3B_Model_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=187341830779006648856485494600597821197)
        name = SchemaPath('ext', 'ai', 'Ministral_3B_Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=187341830779006648856485494600597821197),
                name='ext::ai::Ministral_3B_Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __Ministral_3B_Model_typeof__(
    __TextGenerationModel_typeof__,
    __Ministral_3B_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __Ministral_3B_Model_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __Ministral_3B_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class Ministral_3B_Model(
    __Ministral_3B_Model_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=187341830779006648856485494600597821197),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::Ministral_3B_Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::Ministral_3B_Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::Ministral_3B_Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::Ministral_3B_Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __Ministral_3B_Model_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::Ministral_3B_Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::Ministral_3B_Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::Ministral_3B_Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::Ministral_3B_Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Ministral_3B_Model_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="Ministral_3B_Model | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    Ministral_3B_Model.__variants__.Base = Ministral_3B_Model



#
# type ext::ai::Ministral_8B_Model
#
class __Ministral_8B_Model_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=299552133269247513105589709418547769527)
        name = SchemaPath('ext', 'ai', 'Ministral_8B_Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=299552133269247513105589709418547769527),
                name='ext::ai::Ministral_8B_Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __Ministral_8B_Model_typeof__(
    __TextGenerationModel_typeof__,
    __Ministral_8B_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __Ministral_8B_Model_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __Ministral_8B_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class Ministral_8B_Model(
    __Ministral_8B_Model_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=299552133269247513105589709418547769527),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::Ministral_8B_Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::Ministral_8B_Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::Ministral_8B_Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::Ministral_8B_Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __Ministral_8B_Model_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::Ministral_8B_Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::Ministral_8B_Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::Ministral_8B_Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::Ministral_8B_Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Ministral_8B_Model_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="Ministral_8B_Model | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    Ministral_8B_Model.__variants__.Base = Ministral_8B_Model



#
# type ext::ai::MistralLargeModel
#
class __MistralLargeModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=148491261779955221402288241871397790497)
        name = SchemaPath('ext', 'ai', 'MistralLargeModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=148491261779955221402288241871397790497),
                name='ext::ai::MistralLargeModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __MistralLargeModel_typeof__(
    __TextGenerationModel_typeof__,
    __MistralLargeModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __MistralLargeModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __MistralLargeModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class MistralLargeModel(
    __MistralLargeModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=148491261779955221402288241871397790497),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::MistralLargeModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::MistralLargeModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::MistralLargeModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::MistralLargeModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __MistralLargeModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::MistralLargeModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::MistralLargeModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralLargeModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralLargeModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MistralLargeModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="MistralLargeModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    MistralLargeModel.__variants__.Base = MistralLargeModel



#
# type ext::ai::MistralMediumModel
#
class __MistralMediumModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=61214453657926200701168209179898852841)
        name = SchemaPath('ext', 'ai', 'MistralMediumModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=61214453657926200701168209179898852841),
                name='ext::ai::MistralMediumModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __MistralMediumModel_typeof__(
    __TextGenerationModel_typeof__,
    __MistralMediumModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __MistralMediumModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __MistralMediumModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class MistralMediumModel(
    __MistralMediumModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=61214453657926200701168209179898852841),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::MistralMediumModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::MistralMediumModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::MistralMediumModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::MistralMediumModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __MistralMediumModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::MistralMediumModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::MistralMediumModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralMediumModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralMediumModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MistralMediumModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="MistralMediumModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    MistralMediumModel.__variants__.Base = MistralMediumModel



#
# type ext::ai::MistralNemo
#
class __MistralNemo_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=188728853478286181356788061737094211137)
        name = SchemaPath('ext', 'ai', 'MistralNemo')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=188728853478286181356788061737094211137),
                name='ext::ai::MistralNemo',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __MistralNemo_typeof__(
    __TextGenerationModel_typeof__,
    __MistralNemo_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __MistralNemo_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __MistralNemo_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class MistralNemo(
    __MistralNemo_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=188728853478286181356788061737094211137),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::MistralNemo instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::MistralNemo instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::MistralNemo instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::MistralNemo instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __MistralNemo_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::MistralNemo instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::MistralNemo instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralNemo instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralNemo instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MistralNemo_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="MistralNemo | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    MistralNemo.__variants__.Base = MistralNemo



#
# type ext::ai::MistralSmallModel
#
class __MistralSmallModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=246659766913708420630617513638417418793)
        name = SchemaPath('ext', 'ai', 'MistralSmallModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=246659766913708420630617513638417418793),
                name='ext::ai::MistralSmallModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __MistralSmallModel_typeof__(
    __TextGenerationModel_typeof__,
    __MistralSmallModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __MistralSmallModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __MistralSmallModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class MistralSmallModel(
    __MistralSmallModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=246659766913708420630617513638417418793),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::MistralSmallModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::MistralSmallModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::MistralSmallModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::MistralSmallModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __MistralSmallModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::MistralSmallModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::MistralSmallModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralSmallModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::MistralSmallModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MistralSmallModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="MistralSmallModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    MistralSmallModel.__variants__.Base = MistralSmallModel



#
# type ext::ai::OllamaLlama_3_2_Model
#
class __OllamaLlama_3_2_Model_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=339734375535918463077887431249995406866)
        name = SchemaPath('ext', 'ai', 'OllamaLlama_3_2_Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=339734375535918463077887431249995406866),
                name='ext::ai::OllamaLlama_3_2_Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OllamaLlama_3_2_Model_typeof__(
    __TextGenerationModel_typeof__,
    __OllamaLlama_3_2_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OllamaLlama_3_2_Model_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OllamaLlama_3_2_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OllamaLlama_3_2_Model(
    __OllamaLlama_3_2_Model_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=339734375535918463077887431249995406866),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OllamaLlama_3_2_Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OllamaLlama_3_2_Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaLlama_3_2_Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaLlama_3_2_Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OllamaLlama_3_2_Model_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OllamaLlama_3_2_Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OllamaLlama_3_2_Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaLlama_3_2_Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaLlama_3_2_Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OllamaLlama_3_2_Model_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OllamaLlama_3_2_Model | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OllamaLlama_3_2_Model.__variants__.Base = OllamaLlama_3_2_Model



#
# type ext::ai::OllamaLlama_3_3_Model
#
class __OllamaLlama_3_3_Model_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=319237494904542304507106945161561666531)
        name = SchemaPath('ext', 'ai', 'OllamaLlama_3_3_Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=319237494904542304507106945161561666531),
                name='ext::ai::OllamaLlama_3_3_Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OllamaLlama_3_3_Model_typeof__(
    __TextGenerationModel_typeof__,
    __OllamaLlama_3_3_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OllamaLlama_3_3_Model_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OllamaLlama_3_3_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OllamaLlama_3_3_Model(
    __OllamaLlama_3_3_Model_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=319237494904542304507106945161561666531),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OllamaLlama_3_3_Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OllamaLlama_3_3_Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaLlama_3_3_Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OllamaLlama_3_3_Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OllamaLlama_3_3_Model_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OllamaLlama_3_3_Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OllamaLlama_3_3_Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaLlama_3_3_Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OllamaLlama_3_3_Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OllamaLlama_3_3_Model_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OllamaLlama_3_3_Model | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OllamaLlama_3_3_Model.__variants__.Base = OllamaLlama_3_3_Model



#
# type ext::ai::OpenAIGPT_3_5_TurboModel
#
class __OpenAIGPT_3_5_TurboModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=234048008240191131271157163649508287782)
        name = SchemaPath('ext', 'ai', 'OpenAIGPT_3_5_TurboModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=234048008240191131271157163649508287782),
                name='ext::ai::OpenAIGPT_3_5_TurboModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAIGPT_3_5_TurboModel_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAIGPT_3_5_TurboModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAIGPT_3_5_TurboModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAIGPT_3_5_TurboModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAIGPT_3_5_TurboModel(
    __OpenAIGPT_3_5_TurboModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=234048008240191131271157163649508287782),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAIGPT_3_5_TurboModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAIGPT_3_5_TurboModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_3_5_TurboModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_3_5_TurboModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAIGPT_3_5_TurboModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAIGPT_3_5_TurboModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAIGPT_3_5_TurboModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_3_5_TurboModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_3_5_TurboModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIGPT_3_5_TurboModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAIGPT_3_5_TurboModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIGPT_3_5_TurboModel.__variants__.Base = OpenAIGPT_3_5_TurboModel



#
# type ext::ai::OpenAIGPT_4_Model
#
class __OpenAIGPT_4_Model_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=209875582584778130566687133144445474290)
        name = SchemaPath('ext', 'ai', 'OpenAIGPT_4_Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=209875582584778130566687133144445474290),
                name='ext::ai::OpenAIGPT_4_Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAIGPT_4_Model_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAIGPT_4_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAIGPT_4_Model_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAIGPT_4_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAIGPT_4_Model(
    __OpenAIGPT_4_Model_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=209875582584778130566687133144445474290),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAIGPT_4_Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAIGPT_4_Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4_Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4_Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAIGPT_4_Model_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAIGPT_4_Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAIGPT_4_Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4_Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4_Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIGPT_4_Model_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAIGPT_4_Model | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIGPT_4_Model.__variants__.Base = OpenAIGPT_4_Model



#
# type ext::ai::OpenAIGPT_4_TurboModel
#
class __OpenAIGPT_4_TurboModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=225753853814638537168061119257425746429)
        name = SchemaPath('ext', 'ai', 'OpenAIGPT_4_TurboModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=225753853814638537168061119257425746429),
                name='ext::ai::OpenAIGPT_4_TurboModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAIGPT_4_TurboModel_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAIGPT_4_TurboModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAIGPT_4_TurboModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAIGPT_4_TurboModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAIGPT_4_TurboModel(
    __OpenAIGPT_4_TurboModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=225753853814638537168061119257425746429),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAIGPT_4_TurboModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAIGPT_4_TurboModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4_TurboModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4_TurboModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAIGPT_4_TurboModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAIGPT_4_TurboModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAIGPT_4_TurboModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4_TurboModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4_TurboModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIGPT_4_TurboModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAIGPT_4_TurboModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIGPT_4_TurboModel.__variants__.Base = OpenAIGPT_4_TurboModel



#
# type ext::ai::OpenAIGPT_4_TurboPreviewModel
#
class __OpenAIGPT_4_TurboPreviewModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=313264042614559775302328686049363974042)
        name = SchemaPath('ext', 'ai', 'OpenAIGPT_4_TurboPreviewModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=313264042614559775302328686049363974042),
                name='ext::ai::OpenAIGPT_4_TurboPreviewModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAIGPT_4_TurboPreviewModel_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAIGPT_4_TurboPreviewModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAIGPT_4_TurboPreviewModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAIGPT_4_TurboPreviewModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAIGPT_4_TurboPreviewModel(
    __OpenAIGPT_4_TurboPreviewModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=313264042614559775302328686049363974042),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAIGPT_4_TurboPreviewModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAIGPT_4_TurboPreviewModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4_TurboPreviewModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4_TurboPreviewModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAIGPT_4_TurboPreviewModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAIGPT_4_TurboPreviewModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAIGPT_4_TurboPreviewModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4_TurboPreviewModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4_TurboPreviewModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIGPT_4_TurboPreviewModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAIGPT_4_TurboPreviewModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIGPT_4_TurboPreviewModel.__variants__.Base = OpenAIGPT_4_TurboPreviewModel



#
# type ext::ai::OpenAIGPT_4o_MiniModel
#
class __OpenAIGPT_4o_MiniModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=27760511408009151205888074233301334014)
        name = SchemaPath('ext', 'ai', 'OpenAIGPT_4o_MiniModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=27760511408009151205888074233301334014),
                name='ext::ai::OpenAIGPT_4o_MiniModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAIGPT_4o_MiniModel_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAIGPT_4o_MiniModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAIGPT_4o_MiniModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAIGPT_4o_MiniModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAIGPT_4o_MiniModel(
    __OpenAIGPT_4o_MiniModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=27760511408009151205888074233301334014),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAIGPT_4o_MiniModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAIGPT_4o_MiniModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4o_MiniModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4o_MiniModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAIGPT_4o_MiniModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAIGPT_4o_MiniModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAIGPT_4o_MiniModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4o_MiniModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4o_MiniModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIGPT_4o_MiniModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAIGPT_4o_MiniModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIGPT_4o_MiniModel.__variants__.Base = OpenAIGPT_4o_MiniModel



#
# type ext::ai::OpenAIGPT_4o_Model
#
class __OpenAIGPT_4o_Model_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=104542954511623876188796080437320409669)
        name = SchemaPath('ext', 'ai', 'OpenAIGPT_4o_Model')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=104542954511623876188796080437320409669),
                name='ext::ai::OpenAIGPT_4o_Model',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAIGPT_4o_Model_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAIGPT_4o_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAIGPT_4o_Model_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAIGPT_4o_Model_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAIGPT_4o_Model(
    __OpenAIGPT_4o_Model_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=104542954511623876188796080437320409669),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAIGPT_4o_Model instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAIGPT_4o_Model instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4o_Model instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAIGPT_4o_Model instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAIGPT_4o_Model_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAIGPT_4o_Model instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAIGPT_4o_Model instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4o_Model instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAIGPT_4o_Model instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAIGPT_4o_Model_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAIGPT_4o_Model | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAIGPT_4o_Model.__variants__.Base = OpenAIGPT_4o_Model



#
# type ext::ai::OpenAI_O1_MiniModel
#
class __OpenAI_O1_MiniModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=53425907798101726312833253200075438175)
        name = SchemaPath('ext', 'ai', 'OpenAI_O1_MiniModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=53425907798101726312833253200075438175),
                name='ext::ai::OpenAI_O1_MiniModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAI_O1_MiniModel_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAI_O1_MiniModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAI_O1_MiniModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAI_O1_MiniModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAI_O1_MiniModel(
    __OpenAI_O1_MiniModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=53425907798101726312833253200075438175),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAI_O1_MiniModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAI_O1_MiniModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAI_O1_MiniModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAI_O1_MiniModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAI_O1_MiniModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAI_O1_MiniModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAI_O1_MiniModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAI_O1_MiniModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAI_O1_MiniModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAI_O1_MiniModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAI_O1_MiniModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAI_O1_MiniModel.__variants__.Base = OpenAI_O1_MiniModel



#
# type ext::ai::OpenAI_O1_PreviewModel
#
class __OpenAI_O1_PreviewModel_typeof_base__(
    __TextGenerationModel_typeof_base__,
):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=311915980691839713734365196698040986914)
        name = SchemaPath('ext', 'ai', 'OpenAI_O1_PreviewModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=311915980691839713734365196698040986914),
                name='ext::ai::OpenAI_O1_PreviewModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OpenAI_O1_PreviewModel_typeof__(
    __TextGenerationModel_typeof__,
    __OpenAI_O1_PreviewModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __OpenAI_O1_PreviewModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __OpenAI_O1_PreviewModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class OpenAI_O1_PreviewModel(
    __OpenAI_O1_PreviewModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=311915980691839713734365196698040986914),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::OpenAI_O1_PreviewModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::OpenAI_O1_PreviewModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAI_O1_PreviewModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::OpenAI_O1_PreviewModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __OpenAI_O1_PreviewModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::OpenAI_O1_PreviewModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::OpenAI_O1_PreviewModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAI_O1_PreviewModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::OpenAI_O1_PreviewModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenAI_O1_PreviewModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="OpenAI_O1_PreviewModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenAI_O1_PreviewModel.__variants__.Base = OpenAI_O1_PreviewModel



#
# type ext::ai::PixtralLargeModel
#
class __PixtralLargeModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=32357837288514177586891716741383401627)
        name = SchemaPath('ext', 'ai', 'PixtralLargeModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=32357837288514177586891716741383401627),
                name='ext::ai::PixtralLargeModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __PixtralLargeModel_typeof__(
    __TextGenerationModel_typeof__,
    __PixtralLargeModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __PixtralLargeModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __PixtralLargeModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class PixtralLargeModel(
    __PixtralLargeModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=32357837288514177586891716741383401627),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::PixtralLargeModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::PixtralLargeModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::PixtralLargeModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::PixtralLargeModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __PixtralLargeModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::PixtralLargeModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::PixtralLargeModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::PixtralLargeModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::PixtralLargeModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __PixtralLargeModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="PixtralLargeModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    PixtralLargeModel.__variants__.Base = PixtralLargeModel



#
# type ext::ai::PixtralModel
#
class __PixtralModel_typeof_base__(__TextGenerationModel_typeof_base__):
    class __gel_reflection__(
        __TextGenerationModel_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=115317575121372078059973601427586773211)
        name = SchemaPath('ext', 'ai', 'PixtralModel')
        @LazyClassProperty["dict[str, pydantic.GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, pydantic.GelPointerReflection]:
            my_ptrs: dict[str, pydantic.GelPointerReflection] = {}
            return (
                my_ptrs
                | __TextGenerationModel_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=115317575121372078059973601427586773211),
                name='ext::ai::PixtralModel',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __PixtralModel_typeof__(
    __TextGenerationModel_typeof__,
    __PixtralModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof__.__typeof__):
        pass


class __PixtralModel_typeof_partial__(
    __TextGenerationModel_typeof_partial__,
    __PixtralModel_typeof_base__,
):
    class __typeof__(__TextGenerationModel_typeof_partial__.__typeof__):
        pass


class PixtralModel(
    __PixtralModel_typeof__,
    TextGenerationModel,
    __gel_type_id__=UUID(int=115317575121372078059973601427586773211),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new ext::ai::PixtralModel instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::ai::PixtralModel instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::ai::PixtralModel instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::ai::PixtralModel instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
            id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(TextGenerationModel.__variants__):
        class Base(
            __PixtralModel_typeof__,
            TextGenerationModel.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new ext::ai::PixtralModel instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::ai::PixtralModel instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::ai::PixtralModel instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::ai::PixtralModel instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str],
                    id: Direction | ___builtins_1__.str | ___builtins_1__.str | ___builtins_1__.bool | tuple[Direction | ___builtins_1__.str, EmptyDirection | ___builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            TextGenerationModel.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __PixtralModel_typeof_partial__,
            Base,
            TextGenerationModel.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            TextGenerationModel.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            pass


        Any = TypeVar("Any", bound="PixtralModel | Base | Required | Partial")
    class __links__(TextGenerationModel.__links__):
        pass
    class __links_partial__(TextGenerationModel.__links_partial__):
        pass

if not TYPE_CHECKING:
    PixtralModel.__variants__.Base = PixtralModel



from ...ext import ai as ___ext_ai__  # noqa: E402 F403

import builtins as builtins  # noqa: E402 F403
from datetime import timedelta  # noqa: E402 F403
