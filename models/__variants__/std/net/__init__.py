#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from gel.models.pydantic import AnyEnum


class RequestFailureKind(AnyEnum):
    NetworkError = 'NetworkError'
    Timeout = 'Timeout'


class RequestState(AnyEnum):
    Pending = 'Pending'
    InProgress = 'InProgress'
    Completed = 'Completed'
    Failed = 'Failed'


