from sanic import Sanic
from sanic.log import LOGGING_CONFIG_DEFAULTS, logger
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse
from spacy import load
from spacytextblob.spacytextblob import SpacyTextBlob  # noqa: F401
from application.ping.controllers import bp as ping_blueprint
from application.ping.manager import PingManager
from application.processing.controllers import bp as processing_blueprint
from application.processing.manager import ProcessingManager

LOGGING_CONFIG_DEFAULTS["formatters"] = {
    "generic": {"class": "sanic.logging.formatter.JSONFormatter"},
    "access": {"class": "sanic.logging.formatter.JSONFormatter"},
}

app = Sanic("nlp")
app.config.FALLBACK_ERROR_FORMAT = "json"

app.blueprint(ping_blueprint)
app.ext.dependency(PingManager())

app.blueprint(processing_blueprint)
app.ext.dependency(ProcessingManager())


@app.listener("before_server_start")
async def before_server_start(app, _) -> None:
    english_nlp = load("en_core_web_lg")
    english_nlp.add_pipe("spacytextblob")
    app.ctx.nlp = {"en": english_nlp}


@app.middleware("request")
async def callback_request(request: SanicRequest) -> None:
    logger.info(f"Request {request.path} received")


@app.middleware("response")
async def callback_response(request: SanicRequest, _: SanicResponse) -> None:
    logger.info(f"Request {request.path} processing finished")
