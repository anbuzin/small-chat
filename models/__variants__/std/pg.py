#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std

from gel.models.pydantic import SchemaPath

from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as ___std__

    from typing import ClassVar



class __date_meta__(std.__anydiscrete_meta__):
    pass
if TYPE_CHECKING:
    class date(std.anydiscrete, metaclass=__date_meta__):
        class __gel_reflection__(___std__.anydiscrete.__gel_reflection__):
            id = UUID(int=16777220)
            name = SchemaPath('std', 'pg', 'date')

if not TYPE_CHECKING:
    class date(std.anydiscrete):
        __gel_type_class__: ClassVar[type] = __date_meta__

        class __gel_reflection__(std.anydiscrete.__gel_reflection__):
            id = UUID(int=16777220)
            name = SchemaPath('std', 'pg', 'date')



class __interval_meta__(std.__anycontiguous_meta__):
    pass
if TYPE_CHECKING:
    class interval(std.anycontiguous, metaclass=__interval_meta__):
        class __gel_reflection__(___std__.anycontiguous.__gel_reflection__):
            id = UUID(int=16777221)
            name = SchemaPath('std', 'pg', 'interval')

if not TYPE_CHECKING:
    class interval(std.anycontiguous):
        __gel_type_class__: ClassVar[type] = __interval_meta__

        class __gel_reflection__(std.anycontiguous.__gel_reflection__):
            id = UUID(int=16777221)
            name = SchemaPath('std', 'pg', 'interval')



class __json_meta__(std.__anyscalar_meta__):
    pass
if TYPE_CHECKING:
    class json(std.anyscalar, metaclass=__json_meta__):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=16777217)
            name = SchemaPath('std', 'pg', 'json')

if not TYPE_CHECKING:
    class json(std.anyscalar):
        __gel_type_class__: ClassVar[type] = __json_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=16777217)
            name = SchemaPath('std', 'pg', 'json')



class __timestamp_meta__(std.__anycontiguous_meta__):
    pass
if TYPE_CHECKING:
    class timestamp(std.anycontiguous, metaclass=__timestamp_meta__):
        class __gel_reflection__(___std__.anycontiguous.__gel_reflection__):
            id = UUID(int=16777219)
            name = SchemaPath('std', 'pg', 'timestamp')

if not TYPE_CHECKING:
    class timestamp(std.anycontiguous):
        __gel_type_class__: ClassVar[type] = __timestamp_meta__

        class __gel_reflection__(std.anycontiguous.__gel_reflection__):
            id = UUID(int=16777219)
            name = SchemaPath('std', 'pg', 'timestamp')



class __timestamptz_meta__(std.__anycontiguous_meta__):
    pass
if TYPE_CHECKING:
    class timestamptz(std.anycontiguous, metaclass=__timestamptz_meta__):
        class __gel_reflection__(___std__.anycontiguous.__gel_reflection__):
            id = UUID(int=16777218)
            name = SchemaPath('std', 'pg', 'timestamptz')

if not TYPE_CHECKING:
    class timestamptz(std.anycontiguous):
        __gel_type_class__: ClassVar[type] = __timestamptz_meta__

        class __gel_reflection__(std.anycontiguous.__gel_reflection__):
            id = UUID(int=16777218)
            name = SchemaPath('std', 'pg', 'timestamptz')


