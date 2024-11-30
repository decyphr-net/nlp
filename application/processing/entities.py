from dataclasses import dataclass


@dataclass
class ProcessingRequestBody:
    text: str
    language: str


@dataclass
class Tag:
    token: str
    tag: str

    def as_dict(self) -> dict[str, str]:
        return self.__dict__


@dataclass
class Assessment:
    tokens: list[str]
    polarity: float
    subjectivity: float

    def as_dict(self) -> dict[str, list[str] | float]:
        return self.__dict__


@dataclass
class SentimentAnalysis:
    text: str
    polarity: float
    subjectivity: float
    assessment: list[Assessment]

    def as_dict(self) -> dict[str, str | float | list[dict[str, list[str] | float]]]:
        return {
            "text": self.text,
            "polarity": self.polarity,
            "subjectivity": self.subjectivity,
            "assessment": [assessment.as_dict() for assessment in self.assessment],
        }


@dataclass
class ProcessingResponseBody:
    tags: list[Tag]
    analysis: SentimentAnalysis

    def as_dict(
        self,
    ) -> dict[
        str,
        dict[str, str | float | list[dict[str, list[str] | float]]]
        | list[dict[str, str]],
    ]:
        return {
            "tags": [tag.as_dict() for tag in self.tags],
            "analysis": self.analysis.as_dict(),
        }
