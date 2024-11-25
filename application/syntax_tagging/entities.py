from dataclasses import dataclass
from orjson import loads


@dataclass
class TaggingRequestBody:
    text: str
    language: str


@dataclass
class Tag:
    token: str
    tag: str

    def as_dict(self) -> dict[str, str]:
        return self.__dict__


@dataclass
class TaggingResponseBody:
    tags: list[Tag]

    def as_dict(self) -> dict[str, list[dict[str, str]]]:
        return {
            "tags": [tag.as_dict() for tag in self.tags]
        }
