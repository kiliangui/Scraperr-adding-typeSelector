from typing import Optional

import pydantic


class Element(pydantic.BaseModel):
    name: str
    xpath: str
    url: Optional[str] = None
    typeSelector: Optional[str] = None  # "text", "href", "src", "alt", etc.


class CapturedElement(pydantic.BaseModel):
    xpath: str
    text: str
    name: str
