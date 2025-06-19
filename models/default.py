#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std
from .__variants__ import default as base
from .std.net import http as ___std_net_http__

from gel.models.pydantic import (
    AnnotatedExpr,
    ComputedMultiLink,
    FuncCall,
    MultiLink,
    OptionalComputedProperty,
    OptionalLink,
    OptionalProperty,
    SchemaPath,
    Unspecified
)

import builtins as ___builtins__
from builtins import dict, list
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:

    from . import std as ___std__
    from .std.net import http as std_net_http

    import builtins as builtins
    import datetime as ___datetime__
    from builtins import type
    from uuid import UUID



#
# type default::Chat
#
class Chat(base.Chat):
    title: OptionalProperty[std.str, str]
    created_at: OptionalProperty[std.datetime, datetime]
    archive: MultiLink[Message]
    history: ComputedMultiLink[Message]

#
# type default::Fact
#
class Fact(base.Fact):
    key: OptionalProperty[std.str, str]
    value: OptionalProperty[std.str, str]
    body: OptionalComputedProperty[std.str, str]
    from_message: OptionalLink[Message]

#
# type default::Message
#
class Message(base.Message):
    body: OptionalProperty[std.str, str]
    llm_role: OptionalProperty[std.str, str]
    tool_args: OptionalProperty[std.json, str]
    tool_name: OptionalProperty[std.str, str]
    created_at: OptionalProperty[std.datetime, datetime]
    is_evicted: OptionalProperty[std.bool, bool]

#
# type default::Prompt
#
class Prompt(base.Prompt):
    key: OptionalProperty[std.str, str]
    value: OptionalProperty[std.str, str]
    body: OptionalComputedProperty[std.str, str]
    from_message: OptionalLink[Message]

#
# type default::Resource
#
class Resource(base.Resource):
    body: OptionalProperty[std.str, str]
def insert_summary(
    chat_id: type[___std__.uuid] | UUID,
    cutoff: type[___std__.datetime] | ___datetime__.datetime,
    summary: type[___std__.str] | builtins.str,
    summary_datetime: type[___std__.datetime] | ___datetime__.datetime,
) -> type[Chat]:
    args: list[Any] = [chat_id, cutoff, summary, summary_datetime]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        Chat,
        FuncCall(
            fname="default::insert_summary",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('default', 'Chat'),
        )
    )

def request_summary(
    chat_id: type[___std__.uuid] | UUID,
    cutoff: type[___std__.datetime] | ___datetime__.datetime,
) -> type[std_net_http.ScheduledRequest]:
    args: list[Any] = [chat_id, cutoff]
    kw: dict[___builtins__.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std_net_http__.ScheduledRequest,
        FuncCall(
            fname="default::request_summary",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'net', 'http', 'ScheduledRequest'),
        )
    )



from builtins import bool, str  # noqa: E402 F403
from datetime import datetime  # noqa: E402 F403


__all__ = (
    'Chat',
    'Fact',
    'Message',
    'Prompt',
    'Resource',
)
