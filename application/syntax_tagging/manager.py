from typing import Callable

from spacy.tokens import Doc

from application.syntax_tagging.entities import Tag


class TaggingManager:
    async def get_syntax_tokens(
        self, processors: dict[str, Callable], text: str, language: str
    ) -> list[Tag]:
        doc: Doc = processors[language](text)
        return [Tag(w.text, w.pos_) for w in doc]
