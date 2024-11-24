from sanic import Sanic
from sanic.log import logger, LOGGING_CONFIG_DEFAULTS
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse

from application.ping.controllers import bp as ping_blueprint
from application.ping.manager import PingManager

LOGGING_CONFIG_DEFAULTS["formatters"] = {
    "generic": {
        "class": "sanic.logging.formatter.JSONFormatter"
    },
    "access": {
        "class": "sanic.logging.formatter.JSONFormatter"
    }
}

app = Sanic("nlp")

app.config.FALLBACK_ERROR_FORMAT = "json"

app.blueprint(ping_blueprint)
app.ext.dependency(PingManager())


@app.middleware("request")
async def callback_request(request: SanicRequest) -> None:
    logger.info(f"Request {request.path} received")


@app.middleware("response")
async def callback_response(request: SanicRequest, _: SanicResponse) -> None:
    logger.info(f"Request {request.path} processing finished")
