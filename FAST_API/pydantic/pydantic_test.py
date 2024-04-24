from pydantic import BaseModel, ValidationError, Field, field_validator


class Tag(BaseModel):
    id: int
    name: str


class City(BaseModel):
    city_id: int
    name: str = Field(alias="cityFullName")  # JS name to Python name
    tags: list[Tag]

    @field_validator("name")
    def name_check(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError("City name should be more than 3 characters")
        return v


intput_data = """
{
    "city_id": 1,
    "cityFullName": "New York",
    "tags": [{
    "id": 1, "name":  "capital"
    },{
    "id": 2, "name":  "big city"
    }
    ]
    
}
"""
try:
    city = City.parse_raw(intput_data)
    print(city)
except ValidationError as e:
    print("Exception:", e.json())  # Errors in JSON format
else:
    tag = city.tags[0]
    print(city.json(by_alias=True))  # Python name to JS name
