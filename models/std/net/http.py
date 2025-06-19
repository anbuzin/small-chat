#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from ...__variants__.std.net import http as base

from gel.models.pydantic import (
    AnnotatedExpr,
    Array,
    FuncCall,
    OptionalComputedLink,
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

    from .. import __types__ as std___types__
    from ...__variants__ import std as ___std__
    from ...__variants__.std.net import http as ___base__

    import builtins as ___builtins_1__
    import builtins as ___builtins__
    from builtins import type



#
# type std::net::http::Response
#
class Response(base.Response):
    created_at: std.datetime
    status: OptionalProperty[std.int16, int]
    headers: OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[str, str]]]
    body: OptionalProperty[std.bytes, bytes]
    request: OptionalComputedLink[ScheduledRequest]

#
# type std::net::http::ScheduledRequest
#
class ScheduledRequest(base.ScheduledRequest):
    state: std_net.RequestState
    created_at: std.datetime
    updated_at: std.datetime
    failure: OptionalProperty[KindMessage_Tuple_hRjfgQ, tuple[builtins.str, str]]
    url: std.str
    method: base.Method
    headers: OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[str, str]]]
    body: OptionalProperty[std.bytes, bytes]
    response: OptionalLink[Response]
def schedule_request(
    url: type[___std__.str] | ___builtins__.str,
    *,
    body: type[___std__.bytes] | ___builtins_1__.bytes | None | UnspecifiedType = Unspecified,
    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | list[tuple[___builtins__.str, ___builtins__.str]] | None | UnspecifiedType = Unspecified,
    method: type[___base__.Method] | builtins.str | UnspecifiedType = Unspecified,
) -> type[ScheduledRequest]:
    args: list[Any] = [url]
    kw: dict[builtins.str, Any] = {
        "body": body,
        "headers": headers,
        "method": method,
    }
    return AnnotatedExpr(  # type: ignore [return-value]
        ScheduledRequest,
        FuncCall(
            fname="std::net::http::schedule_request",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'net', 'http', 'ScheduledRequest'),
        )
    )



from ...__variants__ import std  # noqa: E402 F403
from ...__variants__.std import net as std_net  # noqa: E402 F403
from ...__variants__.std.net.http import Method  # noqa: E402 F403
from ..__types__ import KindMessage_Tuple_hRjfgQ, NameValue_Tuple_CO3mqQ  # noqa: E402 F403

from builtins import bytes, int, str  # noqa: E402 F403
from datetime import datetime  # noqa: E402 F403


__all__ = (
    'Method',
    'Response',
    'ScheduledRequest',
)
