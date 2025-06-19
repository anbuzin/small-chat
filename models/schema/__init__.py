#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from ..__variants__ import schema as base

from gel.models import pydantic
from gel.models.pydantic import (
    ComputedMultiLink,
    ComputedProperty,
    MultiLink,
    MultiLinkWithProps,
    MultiProperty,
    OptionalLink,
    OptionalProperty
)

import builtins as builtins
from builtins import list, tuple



#
# type schema::Object
#
class Object(base.Object):
    name: std.str
    internal: std.bool
    builtin: std.bool
    computed_fields: OptionalProperty[pydantic.Array[std.str], list[str]]

#
# type schema::TupleElement
#
class TupleElement(base.TupleElement):
    name: OptionalProperty[std.str, str]
    type: Type

#
# type schema::AnnotationSubject
#
class AnnotationSubject(base.AnnotationSubject, Object):
    annotations: MultiLinkWithProps[AnnotationSubject.__links__.annotations, Annotation]

#
# type schema::Delta
#
class Delta(base.Delta, Object):
    parents: MultiLink[Delta]

#
# type schema::FutureBehavior
#
class FutureBehavior(base.FutureBehavior, Object):
    pass


#
# type schema::Parameter
#
class Parameter(base.Parameter, Object):
    typemod: base.TypeModifier
    kind: base.ParameterKind
    num: std.int64
    default: OptionalProperty[std.str, str]
    type: Type

#
# type schema::Source
#
class Source(base.Source, Object):
    pointers: MultiLinkWithProps[Source.__links__.pointers, Pointer]
    indexes: MultiLinkWithProps[Source.__links__.indexes, Index]

#
# type schema::SubclassableObject
#
class SubclassableObject(base.SubclassableObject, Object):
    abstract: OptionalProperty[std.bool, bool]
    final: ComputedProperty[std.bool, bool]

#
# type schema::VolatilitySubject
#
class VolatilitySubject(base.VolatilitySubject, Object):
    volatility: OptionalProperty[base.Volatility, builtins.str]

#
# type schema::Alias
#
class Alias(base.Alias, AnnotationSubject):
    expr: std.str
    type: OptionalLink[Type]

#
# type schema::CallableObject
#
class CallableObject(base.CallableObject, AnnotationSubject):
    return_typemod: OptionalProperty[base.TypeModifier, builtins.str]
    params: MultiLinkWithProps[CallableObject.__links__.params, Parameter]
    return_type: OptionalLink[Type]

#
# type schema::Extension
#
class Extension(base.Extension, AnnotationSubject, Object):
    package: sys.ExtensionPackage

#
# type schema::Global
#
class Global(base.Global, AnnotationSubject):
    default: OptionalProperty[std.str, str]
    required: OptionalProperty[std.bool, bool]
    cardinality: OptionalProperty[base.Cardinality, builtins.str]
    expr: OptionalProperty[std.str, str]
    target: OptionalLink[Type]

#
# type schema::Migration
#
class Migration(base.Migration, AnnotationSubject, Object):
    script: std.str
    sdl: OptionalProperty[std.str, str]
    message: OptionalProperty[std.str, str]
    generated_by: OptionalProperty[base.MigrationGeneratedBy, builtins.str]
    parents: MultiLink[Migration]

#
# type schema::Module
#
class Module(base.Module, AnnotationSubject, Object):
    pass


#
# type schema::InheritingObject
#
class InheritingObject(base.InheritingObject, SubclassableObject):
    inherited_fields: OptionalProperty[pydantic.Array[std.str], list[str]]
    bases: MultiLinkWithProps[InheritingObject.__links__.bases, InheritingObject]
    ancestors: MultiLinkWithProps[InheritingObject.__links__.ancestors, InheritingObject]

#
# type schema::Type
#
class Type(base.Type, SubclassableObject, AnnotationSubject):
    expr: OptionalProperty[std.str, str]
    from_alias: OptionalProperty[std.bool, bool]

#
# type schema::Cast
#
class Cast(base.Cast, AnnotationSubject, VolatilitySubject):
    allow_implicit: OptionalProperty[std.bool, bool]
    allow_assignment: OptionalProperty[std.bool, bool]
    from_type: OptionalLink[Type]
    to_type: OptionalLink[Type]

#
# type schema::Function
#
class Function(base.Function, CallableObject, VolatilitySubject):
    preserves_optionality: OptionalProperty[std.bool, bool]
    body: OptionalProperty[std.str, str]
    language: std.str
    used_globals: MultiLinkWithProps[Function.__links__.used_globals, Global]

#
# type schema::Operator
#
class Operator(base.Operator, CallableObject, VolatilitySubject):
    operator_kind: OptionalProperty[base.OperatorKind, builtins.str]
    abstract: OptionalProperty[std.bool, bool]

#
# type schema::AccessPolicy
#
class AccessPolicy(base.AccessPolicy, InheritingObject, AnnotationSubject):
    access_kinds: MultiProperty[base.AccessKind, builtins.str]
    condition: OptionalProperty[std.str, str]
    action: base.AccessPolicyAction
    expr: OptionalProperty[std.str, str]
    errmessage: OptionalProperty[std.str, str]
    subject: ObjectType

#
# type schema::Annotation
#
class Annotation(base.Annotation, InheritingObject, AnnotationSubject):
    inheritable: OptionalProperty[std.bool, bool]

#
# type schema::ConsistencySubject
#
class ConsistencySubject(
    base.ConsistencySubject,
    InheritingObject,
    AnnotationSubject,
):
    constraints: MultiLinkWithProps[ConsistencySubject.__links__.constraints, Constraint]

#
# type schema::Constraint
#
class Constraint(base.Constraint, CallableObject, InheritingObject):
    expr: OptionalProperty[std.str, str]
    subjectexpr: OptionalProperty[std.str, str]
    finalexpr: OptionalProperty[std.str, str]
    errmessage: OptionalProperty[std.str, str]
    delegated: OptionalProperty[std.bool, bool]
    except_expr: OptionalProperty[std.str, str]
    subject: OptionalLink[ConsistencySubject]
    params: MultiLinkWithProps[Constraint.__links__.params, Parameter]

#
# type schema::Index
#
class Index(base.Index, InheritingObject, AnnotationSubject):
    expr: OptionalProperty[std.str, str]
    except_expr: OptionalProperty[std.str, str]
    deferrability: OptionalProperty[base.IndexDeferrability, builtins.str]
    deferred: OptionalProperty[std.bool, bool]
    kwargs: OptionalProperty[pydantic.Array[NameExpr_Tuple_9eMVFg], list[tuple[str, str]]]
    params: MultiLinkWithProps[Index.__links__.params, Parameter]

#
# type schema::Rewrite
#
class Rewrite(base.Rewrite, InheritingObject, AnnotationSubject):
    kind: base.TriggerKind
    expr: std.str
    subject: Pointer

#
# type schema::Trigger
#
class Trigger(base.Trigger, InheritingObject, AnnotationSubject):
    timing: base.TriggerTiming
    kinds: MultiProperty[base.TriggerKind, builtins.str]
    scope: base.TriggerScope
    expr: OptionalProperty[std.str, str]
    condition: OptionalProperty[std.str, str]
    subject: ObjectType

#
# type schema::PrimitiveType
#
class PrimitiveType(base.PrimitiveType, Type):
    pass


#
# type schema::PseudoType
#
class PseudoType(base.PseudoType, InheritingObject, Type):
    pass


#
# type schema::ObjectType
#
class ObjectType(
    base.ObjectType,
    Source,
    ConsistencySubject,
    InheritingObject,
    Type,
    AnnotationSubject,
):
    compound_type: ComputedProperty[std.bool, bool]
    union_of: MultiLink[ObjectType]
    intersection_of: MultiLink[ObjectType]
    links: ComputedMultiLink[Link]
    properties: ComputedMultiLink[Property]
    access_policies: MultiLinkWithProps[ObjectType.__links__.access_policies, AccessPolicy]
    triggers: MultiLinkWithProps[ObjectType.__links__.triggers, Trigger]

#
# type schema::Pointer
#
class Pointer(base.Pointer, ConsistencySubject, AnnotationSubject):
    cardinality: OptionalProperty[base.Cardinality, builtins.str]
    required: OptionalProperty[std.bool, bool]
    readonly: OptionalProperty[std.bool, bool]
    default: OptionalProperty[std.str, str]
    expr: OptionalProperty[std.str, str]
    secret: OptionalProperty[std.bool, bool]
    source: OptionalLink[Source]
    target: OptionalLink[Type]
    rewrites: MultiLinkWithProps[Pointer.__links__.rewrites, Rewrite]

#
# type schema::CollectionType
#
class CollectionType(base.CollectionType, PrimitiveType):
    pass


#
# type schema::ScalarType
#
class ScalarType(
    base.ScalarType,
    PrimitiveType,
    ConsistencySubject,
    AnnotationSubject,
):
    default: OptionalProperty[std.str, str]
    enum_values: OptionalProperty[pydantic.Array[std.str], list[str]]
    arg_values: OptionalProperty[pydantic.Array[std.str], list[str]]

#
# type schema::Link
#
class Link(base.Link, Pointer, Source):
    on_target_delete: OptionalProperty[base.TargetDeleteAction, builtins.str]
    on_source_delete: OptionalProperty[base.SourceDeleteAction, builtins.str]
    target: OptionalLink[ObjectType]
    properties: ComputedMultiLink[Property]

#
# type schema::Property
#
class Property(base.Property, Pointer):
    pass


#
# type schema::Array
#
class Array(base.Array, CollectionType):
    dimensions: OptionalProperty[pydantic.Array[std.int16], list[int]]
    element_type: Type

#
# type schema::MultiRange
#
class MultiRange(base.MultiRange, CollectionType):
    element_type: Type

#
# type schema::Range
#
class Range(base.Range, CollectionType):
    element_type: Type

#
# type schema::Tuple
#
class Tuple(base.Tuple, CollectionType):
    named: std.bool
    element_types: MultiLinkWithProps[Tuple.__links__.element_types, TupleElement]

#
# type schema::ArrayExprAlias
#
class ArrayExprAlias(base.ArrayExprAlias, Array):
    pass


#
# type schema::MultiRangeExprAlias
#
class MultiRangeExprAlias(base.MultiRangeExprAlias, MultiRange):
    pass


#
# type schema::RangeExprAlias
#
class RangeExprAlias(base.RangeExprAlias, Range):
    pass


#
# type schema::TupleExprAlias
#
class TupleExprAlias(base.TupleExprAlias, Tuple):
    pass



from .. import sys  # noqa: E402 F403
from ..__variants__ import std  # noqa: E402 F403
from ..__variants__.schema import (  # noqa: E402 F403
    AccessKind,
    AccessPolicyAction,
    Cardinality,
    IndexDeferrability,
    MigrationGeneratedBy,
    OperatorKind,
    ParameterKind,
    RewriteKind,
    SourceDeleteAction,
    TargetDeleteAction,
    TriggerKind,
    TriggerScope,
    TriggerTiming,
    TypeModifier,
    Volatility
)
from ..std.__types__ import NameExpr_Tuple_9eMVFg  # noqa: E402 F403

from builtins import bool, int, str  # noqa: E402 F403


__all__ = (
    'AccessKind',
    'AccessPolicy',
    'AccessPolicyAction',
    'Alias',
    'Annotation',
    'AnnotationSubject',
    'Array',
    'ArrayExprAlias',
    'CallableObject',
    'Cardinality',
    'Cast',
    'CollectionType',
    'ConsistencySubject',
    'Constraint',
    'Delta',
    'Extension',
    'Function',
    'FutureBehavior',
    'Global',
    'Index',
    'IndexDeferrability',
    'InheritingObject',
    'Link',
    'Migration',
    'MigrationGeneratedBy',
    'Module',
    'MultiRange',
    'MultiRangeExprAlias',
    'Object',
    'ObjectType',
    'Operator',
    'OperatorKind',
    'Parameter',
    'ParameterKind',
    'Pointer',
    'PrimitiveType',
    'Property',
    'PseudoType',
    'Range',
    'RangeExprAlias',
    'Rewrite',
    'RewriteKind',
    'ScalarType',
    'Source',
    'SourceDeleteAction',
    'SubclassableObject',
    'TargetDeleteAction',
    'Trigger',
    'TriggerKind',
    'TriggerScope',
    'TriggerTiming',
    'Tuple',
    'TupleElement',
    'TupleExprAlias',
    'Type',
    'TypeModifier',
    'Volatility',
    'VolatilitySubject',
)
