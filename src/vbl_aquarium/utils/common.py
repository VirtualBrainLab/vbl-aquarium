"""Common utility functions for building VBL Aquarium models."""

from __future__ import annotations

from inspect import getmembers, isclass
from typing import TYPE_CHECKING

from vbl_aquarium.utils.vbl_base_model import VBLBaseModel

if TYPE_CHECKING:
    from types import ModuleType


def get_model_classes(module: ModuleType) -> list[type[VBLBaseModel]]:
    """Get all VBL models in a module.

    Looks for all classes in a module that subclass VBLBaseModel (excluding VBLBaseModel itself).

    Args:
        module: The module to search for models in.

    Returns:
        A list of all model classes in the module.
    """
    return [
        class_object
        for _, class_object in getmembers(module, isclass)
        if issubclass(class_object, VBLBaseModel) and class_object != VBLBaseModel
    ]
