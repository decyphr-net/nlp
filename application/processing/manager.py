from typing import Callable

from spacy.tokens import Doc
from .entities import Assessment, SentimentAnalysis, Tag


class ProcessingManager:
    async def get_syntax_tokens(
        self, processors: dict[str, Callable], text: str, language: str
    ) -> list[Tag]:
        doc: Doc = processors[language](text)
        return [Tag(w.text, w.pos_) for w in doc]

    async def get_sentament_analysis(
        self, processors: dict[str, Callable], text: str, language: str
    ) -> SentimentAnalysis:
        processor = processors[language]
        doc = processor(text)

        analysis = SentimentAnalysis(
            text=text,
            polarity=doc._.blob.polarity,
            subjectivity=doc._.blob.subjectivity,
            assessment=[
                Assessment(
                    tokens=assessment[0],
                    polarity=assessment[1],
                    subjectivity=assessment[2],
                )
                for assessment in doc._.blob.sentiment_assessments.assessments
            ],
        )
        return analysis
