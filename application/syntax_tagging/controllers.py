from sanic import Blueprint
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse
from sanic.response import json
from sanic_ext import validate

from .entities import TaggingRequestBody, TaggingResponseBody
from .manager import TaggingManager

bp = Blueprint("syntax_tagging", url_prefix="/api")


@bp.post("/tagging")
@validate(json=TaggingRequestBody)
async def tagging(
    request: SanicRequest, body: TaggingRequestBody, manager: TaggingManager
) -> SanicResponse:
    response = TaggingResponseBody(
        await manager.get_syntax_tokens(request.app.ctx.nlp, body.text, body.language)
    )

    return json(response.as_dict())
