"""
Example from the website.

The generated schemas are compliant with the specifications: JSON Schema Core, JSON Schema Validation and OpenAPI.
"""
from enum import Enum
from pydantic import BaseModel, Field


class FooBar(BaseModel):
    count: int
    size: float = None


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    foo_bar: FooBar = Field(...)
    gender: Gender = Field(None, alias="Gender")
    snap: int = Field(
        42,
        title="The Snap",
        description="this is the value of snap",
        gt=30,
        lt=50,
    )

    class Config:
        title = "Main"


# this is equivalent to json.dumps(MainModel.schema(), indent=2):
print(MainModel.schema_json(indent=2))
"""
{
  "title": "Main",
  "description": "This is the description of the main model",
  "type": "object",
  "properties": {
    "foo_bar": {
      "$ref": "#/definitions/FooBar"
    },
    "Gender": {
      "$ref": "#/definitions/Gender"
    },
    "snap": {
      "title": "The Snap",
      "description": "this is the value of snap",
      "default": 42,
      "exclusiveMinimum": 30,
      "exclusiveMaximum": 50,
      "type": "integer"
    }
  },
  "required": [
    "foo_bar"
  ],
  "definitions": {
    "FooBar": {
      "title": "FooBar",
      "type": "object",
      "properties": {
        "count": {
          "title": "Count",
          "type": "integer"
        },
        "size": {
          "title": "Size",
          "type": "number"
        }
      },
      "required": [
        "count"
      ]
    },
    "Gender": {
      "title": "Gender",
      "description": "An enumeration.",
      "enum": [
        "male",
        "female",
        "other",
        "not_given"
      ],
      "type": "string"
    }
  }
}
"""
