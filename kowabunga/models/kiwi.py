# coding: utf-8

"""
    Kowabunga API documentation

    Kvm Orchestrator With A BUNch of Goods Added

    The version of the OpenAPI document: 0.52.5
    Contact: maintainers@kowabunga.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Kiwi(BaseModel):
    """
    A Kiwi (Kowabunga Inner Wan Interface) provides edge-network services..
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. ID (auto-generated).")
    name: StrictStr = Field(description="The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. name.")
    description: Optional[StrictStr] = Field(default=None, description="The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. description.")
    agents: Optional[List[StrictStr]] = Field(default=None, description="a list of existing remote agents managing the network gateway.")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "agents"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Kiwi from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Kiwi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "agents": obj.get("agents")
        })
        return _obj


