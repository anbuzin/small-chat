#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std
from ..__variants__.ext import ai as base

from gel.models.pydantic import (
    AnnotatedExpr,
    Array,
    FuncCall,
    GelModel,
    MultiLink,
    OptionalProperty,
    RequiredMultiLink,
    SchemaPath,
    Unspecified,
    dispatch_overload
)

import builtins as builtins
from builtins import dict, list
from typing import Any, TYPE_CHECKING, overload

if TYPE_CHECKING:

    from .. import std as ___std__
    from ..__types__ import ObjectDistance_Tuple_4ZKj8w

    from gel.models.pydantic import GelType

    import typing as typing
    from builtins import type



#
# type ext::ai::ProviderConfig
#
class ProviderConfig(base.ProviderConfig, cfg.ConfigObject):
    name: std.str
    display_name: std.str
    api_url: std.str
    client_id: OptionalProperty[std.str, str]
    secret: std.str
    api_style: ProviderAPIStyle

#
# type ext::ai::ChatPrompt
#
class ChatPrompt(base.ChatPrompt):
    name: std.str
    messages: RequiredMultiLink[ChatPromptMessage]

#
# type ext::ai::ChatPromptMessage
#
class ChatPromptMessage(base.ChatPromptMessage):
    participant_role: ChatParticipantRole
    participant_name: OptionalProperty[std.str, str]
    content: std.str

#
# type ext::ai::Config
#
class Config(base.Config, cfg.ExtensionConfig):
    indexer_naptime: std.duration
    providers: MultiLink[ProviderConfig]

#
# type ext::ai::Model
#
class Model(base.Model):
    pass


#
# type ext::ai::AnthropicProviderConfig
#
class AnthropicProviderConfig(base.AnthropicProviderConfig, ProviderConfig):
    name: std.str
    display_name: std.str
    api_url: std.str
    api_style: ProviderAPIStyle

#
# type ext::ai::CustomProviderConfig
#
class CustomProviderConfig(base.CustomProviderConfig, ProviderConfig):
    display_name: std.str
    api_style: ProviderAPIStyle

#
# type ext::ai::MistralProviderConfig
#
class MistralProviderConfig(base.MistralProviderConfig, ProviderConfig):
    name: std.str
    display_name: std.str
    api_url: std.str
    api_style: ProviderAPIStyle

#
# type ext::ai::OllamaProviderConfig
#
class OllamaProviderConfig(base.OllamaProviderConfig, ProviderConfig):
    name: std.str
    display_name: std.str
    api_url: std.str
    secret: std.str
    api_style: ProviderAPIStyle

#
# type ext::ai::OpenAIProviderConfig
#
class OpenAIProviderConfig(base.OpenAIProviderConfig, ProviderConfig):
    name: std.str
    display_name: std.str
    api_url: std.str
    api_style: ProviderAPIStyle

#
# type ext::ai::EmbeddingModel
#
class EmbeddingModel(base.EmbeddingModel, Model):
    pass


#
# type ext::ai::TextGenerationModel
#
class TextGenerationModel(base.TextGenerationModel, Model):
    pass


#
# type ext::ai::MistralEmbedModel
#
class MistralEmbedModel(base.MistralEmbedModel, EmbeddingModel):
    pass


#
# type ext::ai::OllamaBgeM3Model
#
class OllamaBgeM3Model(base.OllamaBgeM3Model, EmbeddingModel):
    pass


#
# type ext::ai::OllamaNomicEmbedTextModel
#
class OllamaNomicEmbedTextModel(
    base.OllamaNomicEmbedTextModel,
    EmbeddingModel,
):
    pass


#
# type ext::ai::OpenAITextEmbedding3LargeModel
#
class OpenAITextEmbedding3LargeModel(
    base.OpenAITextEmbedding3LargeModel,
    EmbeddingModel,
):
    pass


#
# type ext::ai::OpenAITextEmbedding3SmallModel
#
class OpenAITextEmbedding3SmallModel(
    base.OpenAITextEmbedding3SmallModel,
    EmbeddingModel,
):
    pass


#
# type ext::ai::OpenAITextEmbeddingAda002Model
#
class OpenAITextEmbeddingAda002Model(
    base.OpenAITextEmbeddingAda002Model,
    EmbeddingModel,
):
    pass


#
# type ext::ai::AnthropicClaude3HaikuModel
#
class AnthropicClaude3HaikuModel(
    base.AnthropicClaude3HaikuModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::AnthropicClaude3OpusModel
#
class AnthropicClaude3OpusModel(
    base.AnthropicClaude3OpusModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::AnthropicClaude3SonnetModel
#
class AnthropicClaude3SonnetModel(
    base.AnthropicClaude3SonnetModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::AnthropicClaude_3_5_HaikuModel
#
class AnthropicClaude_3_5_HaikuModel(
    base.AnthropicClaude_3_5_HaikuModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::AnthropicClaude_3_5_SonnetModel
#
class AnthropicClaude_3_5_SonnetModel(
    base.AnthropicClaude_3_5_SonnetModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::CodestralMamba
#
class CodestralMamba(base.CodestralMamba, TextGenerationModel):
    pass


#
# type ext::ai::CodestralModel
#
class CodestralModel(base.CodestralModel, TextGenerationModel):
    pass


#
# type ext::ai::Ministral_3B_Model
#
class Ministral_3B_Model(base.Ministral_3B_Model, TextGenerationModel):
    pass


#
# type ext::ai::Ministral_8B_Model
#
class Ministral_8B_Model(base.Ministral_8B_Model, TextGenerationModel):
    pass


#
# type ext::ai::MistralLargeModel
#
class MistralLargeModel(base.MistralLargeModel, TextGenerationModel):
    pass


#
# type ext::ai::MistralMediumModel
#
class MistralMediumModel(base.MistralMediumModel, TextGenerationModel):
    pass


#
# type ext::ai::MistralNemo
#
class MistralNemo(base.MistralNemo, TextGenerationModel):
    pass


#
# type ext::ai::MistralSmallModel
#
class MistralSmallModel(base.MistralSmallModel, TextGenerationModel):
    pass


#
# type ext::ai::OllamaLlama_3_2_Model
#
class OllamaLlama_3_2_Model(base.OllamaLlama_3_2_Model, TextGenerationModel):
    pass


#
# type ext::ai::OllamaLlama_3_3_Model
#
class OllamaLlama_3_3_Model(base.OllamaLlama_3_3_Model, TextGenerationModel):
    pass


#
# type ext::ai::OpenAIGPT_3_5_TurboModel
#
class OpenAIGPT_3_5_TurboModel(
    base.OpenAIGPT_3_5_TurboModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::OpenAIGPT_4_Model
#
class OpenAIGPT_4_Model(base.OpenAIGPT_4_Model, TextGenerationModel):
    pass


#
# type ext::ai::OpenAIGPT_4_TurboModel
#
class OpenAIGPT_4_TurboModel(base.OpenAIGPT_4_TurboModel, TextGenerationModel):
    pass


#
# type ext::ai::OpenAIGPT_4_TurboPreviewModel
#
class OpenAIGPT_4_TurboPreviewModel(
    base.OpenAIGPT_4_TurboPreviewModel,
    TextGenerationModel,
):
    pass


#
# type ext::ai::OpenAIGPT_4o_MiniModel
#
class OpenAIGPT_4o_MiniModel(base.OpenAIGPT_4o_MiniModel, TextGenerationModel):
    pass


#
# type ext::ai::OpenAIGPT_4o_Model
#
class OpenAIGPT_4o_Model(base.OpenAIGPT_4o_Model, TextGenerationModel):
    pass


#
# type ext::ai::OpenAI_O1_MiniModel
#
class OpenAI_O1_MiniModel(base.OpenAI_O1_MiniModel, TextGenerationModel):
    pass


#
# type ext::ai::OpenAI_O1_PreviewModel
#
class OpenAI_O1_PreviewModel(base.OpenAI_O1_PreviewModel, TextGenerationModel):
    pass


#
# type ext::ai::PixtralLargeModel
#
class PixtralLargeModel(base.PixtralLargeModel, TextGenerationModel):
    pass


#
# type ext::ai::PixtralModel
#
class PixtralModel(base.PixtralModel, TextGenerationModel):
    pass

def to_context(object: type[GelModel]) -> type[___std__.str]:
    args: list[Any] = [object]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        std.str,
        FuncCall(
            fname="ext::ai::to_context",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def search(  # type: ignore [overload-cannot-match, unused-ignore]
    object: type[GelModel],
    query: type[Array[___std__.float32]],
) -> type[ObjectDistance_Tuple_4ZKj8w]:
    args: list[Any] = [object, query]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        __types__.ObjectDistance_Tuple_4ZKj8w,
        FuncCall(
            fname="ext::ai::search",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<object:anyobject, distance:std::float64>'),
        )
    )

@overload
def search(  # type: ignore [overload-cannot-match, unused-ignore]
    object: type[GelModel],
    query: type[___std__.str],
) -> type[ObjectDistance_Tuple_4ZKj8w]:
    args: list[Any] = [object, query]
    kw: dict[builtins.str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        __types__.ObjectDistance_Tuple_4ZKj8w,
        FuncCall(
            fname="ext::ai::search",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('tuple<object:anyobject, distance:std::float64>'),
        )
    )

def search(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(search, *args, **kwargs)  # type: ignore [no-any-return]



from .. import __types__  # noqa: E402 F403
from ..__variants__.ext.ai import (  # noqa: E402 F403
    ChatParticipantRole,
    DistanceFunction,
    IndexType,
    ProviderAPIStyle
)

from builtins import str  # noqa: E402 F403
from datetime import timedelta  # noqa: E402 F403


__all__ = (
    'AnthropicClaude3HaikuModel',
    'AnthropicClaude3OpusModel',
    'AnthropicClaude3SonnetModel',
    'AnthropicClaude_3_5_HaikuModel',
    'AnthropicClaude_3_5_SonnetModel',
    'AnthropicProviderConfig',
    'ChatParticipantRole',
    'ChatPrompt',
    'ChatPromptMessage',
    'CodestralMamba',
    'CodestralModel',
    'Config',
    'CustomProviderConfig',
    'DistanceFunction',
    'EmbeddingModel',
    'IndexType',
    'Ministral_3B_Model',
    'Ministral_8B_Model',
    'MistralEmbedModel',
    'MistralLargeModel',
    'MistralMediumModel',
    'MistralNemo',
    'MistralProviderConfig',
    'MistralSmallModel',
    'Model',
    'OllamaBgeM3Model',
    'OllamaLlama_3_2_Model',
    'OllamaLlama_3_3_Model',
    'OllamaNomicEmbedTextModel',
    'OllamaProviderConfig',
    'OpenAIGPT_3_5_TurboModel',
    'OpenAIGPT_4_Model',
    'OpenAIGPT_4_TurboModel',
    'OpenAIGPT_4_TurboPreviewModel',
    'OpenAIGPT_4o_MiniModel',
    'OpenAIGPT_4o_Model',
    'OpenAIProviderConfig',
    'OpenAITextEmbedding3LargeModel',
    'OpenAITextEmbedding3SmallModel',
    'OpenAITextEmbeddingAda002Model',
    'OpenAI_O1_MiniModel',
    'OpenAI_O1_PreviewModel',
    'PixtralLargeModel',
    'PixtralModel',
    'ProviderAPIStyle',
    'ProviderConfig',
    'TextGenerationModel',
)
