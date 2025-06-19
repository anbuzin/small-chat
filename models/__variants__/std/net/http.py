#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from ... import std

from gel.models.pydantic import (
    AnyEnum,
    Array,
    Cardinality,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    GelPointerReflection,
    LazyClassProperty,
    OptionalComputedLink,
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
from builtins import list, tuple, type
from collections.abc import Callable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import net as ___std_net__
    from ... import std as ___std__
    from .... import schema
    from ....std import __types__ as ___std___types____, __types__ as std___types__
    from ....std.net import http as std_net_http

    from builtins import dict, str


class Method(AnyEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'




#
# type std::net::http::Response
#
class __Response_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=147718222496950996262069719176207702606)
        name = SchemaPath('std', 'net', 'http', 'Response')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'created_at': GelPointerReflection(
                    name='created_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'status': GelPointerReflection(
                    name='status',
                    type=SchemaPath('std', 'int16'),
                    typexpr='std::int16',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'headers': GelPointerReflection(
                    name='headers',
                    type=SchemaPath('array<tuple<name:std::str, value:std::str>>'),
                    typexpr='array<tuple<name:std::str, value:std::str>>',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'body': GelPointerReflection(
                    name='body',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'request': GelPointerReflection(
                    name='request',
                    type=SchemaPath('std', 'net', 'http', 'ScheduledRequest'),
                    typexpr='std::net::http::ScheduledRequest',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=True,
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
            from ....schema import ObjectType
            return ObjectType(
                id=UUID(int=147718222496950996262069719176207702606),
                name='std::net::http::Response',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Response_typeof__(std.__BaseObject_typeof__, __Response_typeof_base__):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        created_at = TypeAliasType('created_at', 'std.datetime')
        status = TypeAliasType('status', 'OptionalProperty[std.int16, int]')
        headers = TypeAliasType('headers', 'OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[builtins.str, builtins.str]]]')
        body = TypeAliasType('body', 'OptionalProperty[std.bytes, bytes]')
        request = TypeAliasType('request', 'OptionalComputedLink[ScheduledRequest]')


class __Response_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __Response_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        status = TypeAliasType('status', 'OptionalProperty[std.int16, int]')
        headers = TypeAliasType('headers', 'OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[builtins.str, builtins.str]]]')
        body = TypeAliasType('body', 'OptionalProperty[std.bytes, bytes]')
        request = TypeAliasType('request', 'OptionalComputedLink[ScheduledRequest | ScheduledRequest.__variants__.Partial]')


class Response(
    __Response_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=147718222496950996262069719176207702606),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime,
            status: int | None = None,
            headers: list[tuple[builtins.str, builtins.str]] | None = None,
            body: bytes | None = None,
        ) -> None:
            """Create a new std::net::http::Response instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            status: ___builtins_1__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update std::net::http::Response instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            status: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
            headers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            request: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::net::http::Response instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            status: ___builtins_1__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            request: type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch std::net::http::Response instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            status: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __Response_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    status: int | None = None,
                    headers: list[tuple[builtins.str, builtins.str]] | None = None,
                    body: bytes | None = None,
                ) -> None:
                    """Create a new std::net::http::Response instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    status: ___builtins_1__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update std::net::http::Response instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    status: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int16] | UnspecifiedType = Unspecified,
                    headers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    request: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::net::http::Response instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    status: ___builtins_1__.int | type[___std__.int16] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    request: type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch std::net::http::Response instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    status: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.BaseObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            created_at: std.datetime

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Response_typeof_partial__,
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
            created_at: OptionalProperty[std.datetime, datetime]
            status: OptionalProperty[std.int16, int]
            headers: OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[builtins.str, builtins.str]]]
            body: OptionalProperty[std.bytes, bytes]
            request: OptionalComputedLink[___std_net_http__.ScheduledRequest | ___std_net_http__.ScheduledRequest.__variants__.Partial]


        Any = TypeVar("Any", bound="Response | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    Response.__variants__.Base = Response



#
# type std::net::http::ScheduledRequest
#
class __ScheduledRequest_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=306714282403613484767691626551873154557)
        name = SchemaPath('std', 'net', 'http', 'ScheduledRequest')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'state': GelPointerReflection(
                    name='state',
                    type=SchemaPath('std', 'net', 'RequestState'),
                    typexpr='std::net::RequestState',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
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
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'updated_at': GelPointerReflection(
                    name='updated_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'failure': GelPointerReflection(
                    name='failure',
                    type=SchemaPath('tuple<kind:std::net::RequestFailureKind, message:std::str>'),
                    typexpr='tuple<kind:std::net::RequestFailureKind, message:std::str>',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'url': GelPointerReflection(
                    name='url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'method': GelPointerReflection(
                    name='method',
                    type=SchemaPath('std', 'net', 'http', 'Method'),
                    typexpr='std::net::http::Method',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'headers': GelPointerReflection(
                    name='headers',
                    type=SchemaPath('array<tuple<name:std::str, value:std::str>>'),
                    typexpr='array<tuple<name:std::str, value:std::str>>',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'body': GelPointerReflection(
                    name='body',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'response': GelPointerReflection(
                    name='response',
                    type=SchemaPath('std', 'net', 'http', 'Response'),
                    typexpr='std::net::http::Response',
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
                | std.__BaseObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ....schema import ObjectType
            return ObjectType(
                id=UUID(int=306714282403613484767691626551873154557),
                name='std::net::http::ScheduledRequest',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __ScheduledRequest_typeof__(
    std.__BaseObject_typeof__,
    __ScheduledRequest_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        state = TypeAliasType('state', 'std_net.RequestState')
        created_at = TypeAliasType('created_at', 'std.datetime')
        updated_at = TypeAliasType('updated_at', 'std.datetime')
        failure = TypeAliasType('failure', 'OptionalProperty[KindMessage_Tuple_hRjfgQ, tuple[___builtins_3__.str, builtins.str]]')
        url = TypeAliasType('url', 'std.str')
        method = TypeAliasType('method', 'Method')
        headers = TypeAliasType('headers', 'OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[builtins.str, builtins.str]]]')
        body = TypeAliasType('body', 'OptionalProperty[std.bytes, bytes]')
        response = TypeAliasType('response', 'OptionalLink[Response]')


class __ScheduledRequest_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __ScheduledRequest_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        state = TypeAliasType('state', 'OptionalProperty[std_net.RequestState, ___builtins_3__.str]')
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        updated_at = TypeAliasType('updated_at', 'OptionalProperty[std.datetime, datetime]')
        failure = TypeAliasType('failure', 'OptionalProperty[KindMessage_Tuple_hRjfgQ, tuple[___builtins_3__.str, builtins.str]]')
        url = TypeAliasType('url', 'OptionalProperty[std.str, builtins.str]')
        method = TypeAliasType('method', 'OptionalProperty[Method, ___builtins_3__.str]')
        headers = TypeAliasType('headers', 'OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[builtins.str, builtins.str]]]')
        body = TypeAliasType('body', 'OptionalProperty[std.bytes, bytes]')
        response = TypeAliasType('response', 'OptionalLink[Response | Response.__variants__.Partial]')


class ScheduledRequest(
    __ScheduledRequest_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=306714282403613484767691626551873154557),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            state: ___builtins_3__.str,
            created_at: datetime,
            updated_at: datetime,
            failure: tuple[___builtins_3__.str, builtins.str] | None = None,
            url: builtins.str,
            method: ___builtins_3__.str,
            headers: list[tuple[builtins.str, builtins.str]] | None = None,
            body: bytes | None = None,
            response: Response | None = None,
        ) -> None:
            """Create a new std::net::http::ScheduledRequest instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            state: type[___std_net__.RequestState] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            updated_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            failure: type[___std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
            url: ___builtins_3__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            method: type[Method] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update std::net::http::ScheduledRequest instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            state: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std_net__.RequestState] | UnspecifiedType = Unspecified,
            created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            updated_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            failure: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
            url: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            method: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Method] | UnspecifiedType = Unspecified,
            headers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            response: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.Response] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::net::http::ScheduledRequest instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            state: type[___std_net__.RequestState] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            updated_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            failure: type[___std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
            url: ___builtins_3__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            method: type[Method] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch std::net::http::ScheduledRequest instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            updated_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            url: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __ScheduledRequest_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    state: ___builtins_3__.str,
                    created_at: datetime,
                    updated_at: datetime,
                    failure: tuple[___builtins_3__.str, builtins.str] | None = None,
                    url: builtins.str,
                    method: ___builtins_3__.str,
                    headers: list[tuple[builtins.str, builtins.str]] | None = None,
                    body: bytes | None = None,
                    response: Response | None = None,
                ) -> None:
                    """Create a new std::net::http::ScheduledRequest instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    state: type[___std_net__.RequestState] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    updated_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    failure: type[___std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
                    url: ___builtins_3__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    method: type[Method] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update std::net::http::ScheduledRequest instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    state: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std_net__.RequestState] | UnspecifiedType = Unspecified,
                    created_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    updated_at: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    failure: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
                    url: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    method: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Method] | UnspecifiedType = Unspecified,
                    headers: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    response: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.Response] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::net::http::ScheduledRequest instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    state: type[___std_net__.RequestState] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    updated_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    failure: type[___std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
                    url: ___builtins_3__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    method: type[Method] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch std::net::http::ScheduledRequest instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    updated_at: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    url: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    body: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.BaseObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            state: std_net.RequestState
            created_at: std.datetime
            updated_at: std.datetime
            url: std.str
            method: Method

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ScheduledRequest_typeof_partial__,
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
            state: OptionalProperty[std_net.RequestState, ___builtins_3__.str]
            created_at: OptionalProperty[std.datetime, datetime]
            updated_at: OptionalProperty[std.datetime, datetime]
            failure: OptionalProperty[KindMessage_Tuple_hRjfgQ, tuple[___builtins_3__.str, builtins.str]]
            url: OptionalProperty[std.str, builtins.str]
            method: OptionalProperty[Method, ___builtins_3__.str]
            headers: OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[builtins.str, builtins.str]]]
            body: OptionalProperty[std.bytes, bytes]
            response: OptionalLink[___std_net_http__.Response | ___std_net_http__.Response.__variants__.Partial]


        Any = TypeVar("Any", bound="ScheduledRequest | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ScheduledRequest.__variants__.Base = ScheduledRequest



from .. import net as std_net  # noqa: E402 F403
from ....std.__types__ import KindMessage_Tuple_hRjfgQ, NameValue_Tuple_CO3mqQ  # noqa: E402 F403
from ....std.net import http as ___std_net_http__  # noqa: E402 F403

import builtins as builtins  # noqa: E402 F403
from builtins import bytes, int  # noqa: E402 F403
from datetime import datetime  # noqa: E402 F403
