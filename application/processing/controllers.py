from sanic import Blueprint
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse
from sanic.response import json
from sanic_ext import validate

from .entities import ProcessingRequestBody, ProcessingResponseBody
from .manager import ProcessingManager

bp = Blueprint("processing", url_prefix="/api")


@bp.post("/processing")
@validate(json=ProcessingRequestBody)
async def processing(
    request: SanicRequest, body: ProcessingRequestBody, manager: ProcessingManager
) -> SanicResponse:
    response = ProcessingResponseBody(
        tags=await manager.get_syntax_tokens(
            request.app.ctx.nlp, body.text, body.language
        ),
        analysis=await manager.get_sentament_analysis(
            request.app.ctx.nlp, body.text, body.language
        ),
    )

    return json(response.as_dict())
