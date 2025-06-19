#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from ..__variants__ import cfg as base

from gel.models.pydantic import (
    AnnotatedExpr,
    Array,
    ComputedMultiLink,
    FuncCall,
    MultiLink,
    MultiProperty,
    OptionalLink,
    OptionalProperty,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

from builtins import dict, list, str
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:

    from ..__variants__ import std as ___std__

    import builtins as builtins
    from builtins import type



#
# type cfg::ConfigObject
#
class ConfigObject(base.ConfigObject):
    pass


#
# type cfg::AbstractConfig
#
class AbstractConfig(base.AbstractConfig, ConfigObject):
    default_transaction_access_mode: sys.TransactionAccessMode
    session_idle_timeout: std.duration
    default_transaction_isolation: sys.TransactionIsolation
    default_transaction_deferrable: sys.TransactionDeferrability
    session_idle_transaction_timeout: std.duration
    query_execution_timeout: std.duration
    listen_port: std.int32
    listen_addresses: MultiProperty[std.str, str]
    current_email_provider_name: OptionalProperty[std.str, str]
    allow_dml_in_functions: OptionalProperty[std.bool, bool]
    allow_bare_ddl: OptionalProperty[base.AllowBareDDL, str]
    store_migration_sdl: OptionalProperty[base.StoreMigrationSDL, str]
    apply_access_policies: OptionalProperty[std.bool, bool]
    apply_access_policies_pg: OptionalProperty[std.bool, bool]
    allow_user_specified_id: OptionalProperty[std.bool, bool]
    simple_scoping: OptionalProperty[std.bool, bool]
    warn_old_scoping: OptionalProperty[std.bool, bool]
    cors_allow_origins: MultiProperty[std.str, str]
    auto_rebuild_query_cache: OptionalProperty[std.bool, bool]
    auto_rebuild_query_cache_timeout: OptionalProperty[std.duration, timedelta]
    query_cache_mode: OptionalProperty[base.QueryCacheMode, str]
    http_max_connections: OptionalProperty[std.int64, int]
    shared_buffers: OptionalProperty[base.memory, ConfigMemory]
    query_work_mem: OptionalProperty[base.memory, ConfigMemory]
    maintenance_work_mem: OptionalProperty[base.memory, ConfigMemory]
    effective_cache_size: OptionalProperty[base.memory, ConfigMemory]
    effective_io_concurrency: OptionalProperty[std.int64, int]
    default_statistics_target: OptionalProperty[std.int64, int]
    force_database_error: OptionalProperty[std.str, str]
    _pg_prepared_statement_cache_size: std.int16
    track_query_stats: OptionalProperty[base.QueryStatsOption, str]
    extensions: ComputedMultiLink[ExtensionConfig]
    auth: MultiLink[Auth]
    email_providers: MultiLink[EmailProviderConfig]

#
# type cfg::Auth
#
class Auth(base.Auth, ConfigObject):
    priority: std.int64
    user: MultiProperty[std.str, str]
    comment: OptionalProperty[std.str, str]
    method: OptionalLink[AuthMethod]

#
# type cfg::AuthMethod
#
class AuthMethod(base.AuthMethod, ConfigObject):
    transports: MultiProperty[base.ConnectionTransport, str]

#
# type cfg::EmailProviderConfig
#
class EmailProviderConfig(base.EmailProviderConfig, ConfigObject):
    name: std.str

#
# type cfg::ExtensionConfig
#
class ExtensionConfig(base.ExtensionConfig, ConfigObject):
    cfg: AbstractConfig

#
# type cfg::Config
#
class Config(base.Config, AbstractConfig):
    pass


#
# type cfg::DatabaseConfig
#
class DatabaseConfig(base.DatabaseConfig, AbstractConfig):
    pass


#
# type cfg::InstanceConfig
#
class InstanceConfig(base.InstanceConfig, AbstractConfig):
    pass


#
# type cfg::JWT
#
class JWT(base.JWT, AuthMethod):
    transports: MultiProperty[base.ConnectionTransport, str]

#
# type cfg::Password
#
class Password(base.Password, AuthMethod):
    transports: MultiProperty[base.ConnectionTransport, str]

#
# type cfg::SCRAM
#
class SCRAM(base.SCRAM, AuthMethod):
    transports: MultiProperty[base.ConnectionTransport, str]

#
# type cfg::Trust
#
class Trust(base.Trust, AuthMethod):
    pass


#
# type cfg::mTLS
#
class mTLS(base.mTLS, AuthMethod):
    transports: MultiProperty[base.ConnectionTransport, str]

#
# type cfg::SMTPProviderConfig
#
class SMTPProviderConfig(base.SMTPProviderConfig, EmailProviderConfig):
    sender: OptionalProperty[std.str, str]
    host: OptionalProperty[std.str, str]
    port: OptionalProperty[std.int32, int]
    username: OptionalProperty[std.str, str]
    password: OptionalProperty[std.str, str]
    security: base.SMTPSecurity
    validate_certs: std.bool
    timeout_per_email: std.duration
    timeout_per_attempt: std.duration
def get_config_json(
    *,
    sources: type[Array[___std__.str]] | list[builtins.str] | None | UnspecifiedType = Unspecified,
    max_source: type[___std__.str] | builtins.str | None | UnspecifiedType = Unspecified,
) -> type[___std__.json]:
    args: list[Any] = []
    kw: dict[str, Any] = {"sources": sources, "max_source": max_source}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.json,
        FuncCall(
            fname="cfg::get_config_json",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'json'),
        )
    )



from ..__variants__ import std, sys  # noqa: E402 F403
from ..__variants__.cfg import (  # noqa: E402 F403
    AllowBareDDL,
    ConnectionTransport,
    QueryCacheMode,
    QueryStatsOption,
    SMTPSecurity,
    StoreMigrationSDL,
    memory
)

from gel import ConfigMemory  # noqa: E402 F403

from builtins import bool, int  # noqa: E402 F403
from datetime import timedelta  # noqa: E402 F403


__all__ = (
    'AbstractConfig',
    'AllowBareDDL',
    'Auth',
    'AuthMethod',
    'Config',
    'ConfigObject',
    'ConnectionTransport',
    'DatabaseConfig',
    'EmailProviderConfig',
    'ExtensionConfig',
    'InstanceConfig',
    'JWT',
    'Password',
    'QueryCacheMode',
    'QueryStatsOption',
    'SCRAM',
    'SMTPProviderConfig',
    'SMTPSecurity',
    'StoreMigrationSDL',
    'Trust',
    'mTLS',
    'memory',
)
