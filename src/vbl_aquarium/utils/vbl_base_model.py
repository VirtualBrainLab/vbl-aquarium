from pydantic import BaseModel
from pydantic.alias_generators import to_pascal


class VBLBaseModel(BaseModel, alias_generator=to_pascal, populate_by_name=True):
    """Base model for all VBL models.

    Configured to use PascalCase for field names.
    """

    def to_json_string(self) -> str:
        return self.model_dump_json(by_alias=True)
