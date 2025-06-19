#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std

from gel.models.pydantic import (
    AnyNamedTuple,
    GelModel,
    GelTypeMetadata,
    SchemaPath
)

from typing import NamedTuple
from uuid import UUID


#
# tuple type tuple<m:std::int64, ef_construction:std::int64>
#
class _MEf_construction_Tuple_PC0PsA(NamedTuple):
    m: std.int64
    ef_construction: std.int64


class MEf_construction_Tuple_PC0PsA(
    _MEf_construction_Tuple_PC0PsA,
    AnyNamedTuple,
):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=79987651349120269828064677481444042746)
        name = SchemaPath('tuple<m:std::int64, ef_construction:std::int64>')

    __slots__ = ()

#
# tuple type tuple<object:anyobject, distance:std::float64>
#
class _ObjectDistance_Tuple_4ZKj8w(NamedTuple):
    object: GelModel
    distance: std.float64


class ObjectDistance_Tuple_4ZKj8w(_ObjectDistance_Tuple_4ZKj8w, AnyNamedTuple):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=299837699717646164886779523767558995332)
        name = SchemaPath('tuple<object:anyobject, distance:std::float64>')

    __slots__ = ()

