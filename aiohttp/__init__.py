__version__ = '3.6.1'

import logging
from typing import Tuple  # noqa

from . import hdrs
from .client import (
    BaseConnector,
    ClientConnectionError,
    ClientConnectorCertificateError,
    ClientConnectorError,
    ClientConnectorSSLError,
    ClientError,
    ClientHttpProxyError,
    ClientOSError,
    ClientPayloadError,
    ClientProxyConnectionError,
    ClientResponse,
    ClientRequest,
    ClientResponseError,
    ClientSSLError,
    ClientSession,
    ClientTimeout,
    ClientWebSocketResponse,
    ContentTypeError,
    Fingerprint,
    InvalidURL,
    RequestInfo,
    ServerConnectionError,
    ServerDisconnectedError,
    ServerFingerprintMismatch,
    ServerTimeoutError,
    TCPConnector,
    UnixConnector,
    WSServerHandshakeError,
    request
)

from .cookiejar import CookieJar, DummyCookieJar
from .formdata import FormData
from .helpers import BasicAuth, ChainMapProxy
from .http import (
    HttpVersion,
    HttpVersion10,
    HttpVersion11,
    WSMsgType,
    WSCloseCode,
    WSMessage,
    WebSocketError
)

from .multipart import (
    BadContentDispositionHeader,
    BadContentDispositionParam,
    BodyPartReader,
    MultipartReader,
    MultipartWriter,
    content_disposition_filename,
    parse_content_disposition
)

from .payload import (
    AsyncIterablePayload,
    BufferedReaderPayload,
    BytesIOPayload,
    BytesPayload,
    IOBasePayload,
    JsonPayload,
    PAYLOAD_REGISTRY,
    Payload,
    StringIOPayload,
    StringPayload,
    TextIOPayload,
    get_payload,
    payload_type
)

from .resolver import AsyncResolver, DefaultResolver, ThreadedResolver

from .signals import Signal

from .streams import (
    DataQueue,
    EMPTY_PAYLOAD,
    EofStream,
    FlowControlDataQueue,
    StreamReader
)

from .tracing import (
    TraceConfig,
    TraceConnectionCreateEndParams,
    TraceConnectionCreateStartParams,
    TraceConnectionQueuedEndParams,
    TraceConnectionQueuedStartParams,
    TraceConnectionReuseconnParams,
    TraceDnsCacheHitParams,
    TraceDnsCacheMissParams,
    TraceDnsResolveHostEndParams,
    TraceDnsResolveHostStartParams,
    TraceRequestChunkSentParams,
    TraceRequestEndParams,
    TraceRequestExceptionParams,
    TraceRequestRedirectParams,
    TraceRequestStartParams,
    TraceResponseChunkReceivedParams
)

__all__ = (
    'hdrs',
    # client
    'BaseConnector',
    'ClientConnectionError',
    'ClientConnectorCertificateError',
    'ClientConnectorError',
    'ClientConnectorSSLError',
    'ClientError',
    'ClientHttpProxyError',
    'ClientOSError',
    'ClientPayloadError',
    'ClientProxyConnectionError',
    'ClientResponse',
    'ClientRequest',
    'ClientResponseError',
    'ClientSSLError',
    'ClientSession',
    'ClientTimeout',
    'ClientWebSocketResponse',
    'ContentTypeError',
    'Fingerprint',
    'InvalidURL',
    'RequestInfo',
    'ServerConnectionError',
    'ServerDisconnectedError',
    'ServerFingerprintMismatch',
    'ServerTimeoutError',
    'TCPConnector',
    'UnixConnector',
    'WSServerHandshakeError',
    'request',
    # cookiejar
    'CookieJar',
    'DummyCookieJar',
    # formdata
    'FormData',
    # helpers
    'BasicAuth',
    'ChainMapProxy',
    # http
    'HttpVersion',
    'HttpVersion10',
    'HttpVersion11',
    'WSMsgType',
    'WSCloseCode',
    'WSMessage',
    'WebSocketError',
    # multipart
    'BadContentDispositionHeader',
    'BadContentDispositionParam',
    'BodyPartReader',
    'MultipartReader',
    'MultipartWriter',
    'content_disposition_filename',
    'parse_content_disposition',
    # payload
    'AsyncIterablePayload',
    'BufferedReaderPayload',
    'BytesIOPayload',
    'BytesPayload',
    'IOBasePayload',
    'JsonPayload',
    'PAYLOAD_REGISTRY',
    'Payload',
    'StringIOPayload',
    'StringPayload',
    'TextIOPayload',
    'get_payload',
    'payload_type',
    # resolver
    'AsyncResolver',
    'DefaultResolver',
    'ThreadedResolver',
    # signals
    'Signal',
    'DataQueue',
    'EMPTY_PAYLOAD',
    'EofStream',
    'FlowControlDataQueue',
    'StreamReader',
    # tracing
    'TraceConfig',
    'TraceConnectionCreateEndParams',
    'TraceConnectionCreateStartParams',
    'TraceConnectionQueuedEndParams',
    'TraceConnectionQueuedStartParams',
    'TraceConnectionReuseconnParams',
    'TraceDnsCacheHitParams',
    'TraceDnsCacheMissParams',
    'TraceDnsResolveHostEndParams',
    'TraceDnsResolveHostStartParams',
    'TraceRequestChunkSentParams',
    'TraceRequestEndParams',
    'TraceRequestExceptionParams',
    'TraceRequestRedirectParams',
    'TraceRequestStartParams',
    'TraceResponseChunkReceivedParams',
)  # type: Tuple[str, ...]

logging.basicConfig(
    level=logging.WARNING,
    format="PID(%(process)d) - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
logger.warning("This lib was created to solve a issue, however the original lib wasn't publish a stable release with this fix, perhaps will need to be change on future ")
try:
    from .worker import GunicornWebWorker, GunicornUVLoopWebWorker  # noqa
    __all__ += ('GunicornWebWorker', 'GunicornUVLoopWebWorker')
except ImportError:  # pragma: no cover
    pass
