import functools

from ..common.registry import ModelRegistry, register_platform_model

from .const import PLATFORM


model_registry = ModelRegistry()
register_model = functools.partial(register_platform_model, model_registry, PLATFORM)
