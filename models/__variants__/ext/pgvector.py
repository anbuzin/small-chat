#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std as ___std_1__
from ... import std

from gel.models.pydantic import (
    Cardinality,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    GelPointerReflection,
    LazyClassProperty,
    OptionalProperty,
    PathAlias,
    PointerKind,
    PyConstType,
    PyTypeScalar,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as builtins
import builtins as ___builtins__
from array import array
from builtins import tuple, type
from collections.abc import Callable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from ... import cfg as ___cfg__, schema, std as ___std__

    from builtins import dict, str
    from typing import ClassVar



class __halfvec_meta__(std.__anyscalar_meta__):
    pass
if TYPE_CHECKING:
    class halfvec(std.anyscalar, metaclass=__halfvec_meta__):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=100565809169829271649541133902763999323)
            name = SchemaPath('ext', 'pgvector', 'halfvec')

if not TYPE_CHECKING:
    class halfvec(std.anyscalar):
        __gel_type_class__: ClassVar[type] = __halfvec_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=100565809169829271649541133902763999323)
            name = SchemaPath('ext', 'pgvector', 'halfvec')



class __sparsevec_meta__(std.__anyscalar_meta__):
    pass
if TYPE_CHECKING:
    class sparsevec(std.anyscalar, metaclass=__sparsevec_meta__):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=323287489991937762022315450044794834)
            name = SchemaPath('ext', 'pgvector', 'sparsevec')

if not TYPE_CHECKING:
    class sparsevec(std.anyscalar):
        __gel_type_class__: ClassVar[type] = __sparsevec_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=323287489991937762022315450044794834)
            name = SchemaPath('ext', 'pgvector', 'sparsevec')



class __vector_meta__(std.__anyscalar_meta__):
    pass
if TYPE_CHECKING:
    class vector(
        PyTypeScalar[array],
        std.anyscalar,
        metaclass=__vector_meta__,
    ):
        class __gel_reflection__(___std__.anyscalar.__gel_reflection__):
            id = UUID(int=198583886543751203159911086977260689445)
            name = SchemaPath('ext', 'pgvector', 'vector')

if not TYPE_CHECKING:
    class vector(array, PyTypeScalar[array], std.anyscalar):
        __gel_type_class__: ClassVar[type] = __vector_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=198583886543751203159911086977260689445)
            name = SchemaPath('ext', 'pgvector', 'vector')




#
# type ext::pgvector::Config
#
class __Config_typeof_base__(cfg.__ExtensionConfig_typeof_base__):
    class __gel_reflection__(
        cfg.__ExtensionConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=38597838681751752283639360405565348316)
        name = SchemaPath('ext', 'pgvector', 'Config')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'probes': GelPointerReflection(
                    name='probes',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'ef_search': GelPointerReflection(
                    name='ef_search',
                    type=SchemaPath('std', 'int64'),
                    typexpr='std::int64',
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
                | cfg.__ExtensionConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=38597838681751752283639360405565348316),
                name='ext::pgvector::Config',
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
        probes = TypeAliasType('probes', '___std_1__.int64')
        ef_search = TypeAliasType('ef_search', '___std_1__.int64')


class __Config_typeof_partial__(
    cfg.__ExtensionConfig_typeof_partial__,
    __Config_typeof_base__,
):
    class __typeof__(cfg.__ExtensionConfig_typeof_partial__.__typeof__):
        probes = TypeAliasType('probes', 'OptionalProperty[___std_1__.int64, int]')
        ef_search = TypeAliasType('ef_search', 'OptionalProperty[___std_1__.int64, int]')


class Config(
    __Config_typeof__,
    cfg.ExtensionConfig,
    __gel_type_id__=UUID(int=38597838681751752283639360405565348316),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            cfg: cfg.AbstractConfig | None = None,
            probes: int | DefaultValue = DEFAULT_VALUE,
            ef_search: int | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::pgvector::Config instance from keyword arguments.

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
            probes: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            ef_search: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::pgvector::Config instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            probes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            ef_search: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::pgvector::Config instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            probes: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
            ef_search: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::pgvector::Config instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            probes: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            ef_search: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
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
                    probes: int | DefaultValue = DEFAULT_VALUE,
                    ef_search: int | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::pgvector::Config instance from keyword arguments.

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
                    probes: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    ef_search: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::pgvector::Config instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    probes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    ef_search: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.int64] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::pgvector::Config instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    probes: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                    ef_search: ___builtins__.int | type[___std__.int64] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::pgvector::Config instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    probes: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    ef_search: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ExtensionConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            probes: std.int64
            ef_search: std.int64

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
            probes: OptionalProperty[std.int64, int]
            ef_search: OptionalProperty[std.int64, int]


        Any = TypeVar("Any", bound="Config | Base | Required | Partial")
    class __links__(cfg.ExtensionConfig.__links__):
        pass
    class __links_partial__(cfg.ExtensionConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    Config.__variants__.Base = Config



from builtins import int  # noqa: E402 F403
