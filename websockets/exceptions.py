__all__ = [
    'InvalidHandshake', 'InvalidMessage', 'InvalidOrigin', 'InvalidState',
    'InvalidStatusCode', 'InvalidURI', 'ConnectionClosed', 'PayloadTooBig',
    'WebSocketProtocolError',
]


class InvalidHandshake(Exception):
    """
    Exception raised when a handshake request or response is invalid.

    """


class InvalidMessage(InvalidHandshake):
    """
    Exception raised when the HTTP message in a handshake request is malformed.

    """


class InvalidOrigin(InvalidHandshake):
    """
    Exception raised when the origin in a handshake request is forbidden.

    """


class InvalidStatusCode(InvalidHandshake):
    """
    Exception raised when a handshake response status code is invalid.

    Provides the integer status code in its ``code`` attribute.

    """
    def __init__(self, code):
        self.code = code
        message = 'Status code not 101: {}'.format(code)
        super().__init__(message)


class InvalidState(Exception):
    """
    Exception raised when an operation is forbidden in the current state.

    """


class ConnectionClosed(InvalidState):
    """
    Exception raised when trying to read or write on a closed connection.

    Provides the connection close code and reason in its ``code`` and
    ``reason`` attributes respectively.

    """
    def __init__(self, code, reason):
        self.code = code
        self.reason = reason
        message = 'WebSocket connection is closed: '
        message += 'code = {}, '.format(code) if code else 'no code, '
        message += 'reason = {}.'.format(reason) if reason else 'no reason.'
        super().__init__(message)


class InvalidURI(Exception):
    """
    Exception raised when an URI isn't a valid websocket URI.

    """


class PayloadTooBig(Exception):
    """
    Exception raised when a frame's payload exceeds the maximum size.

    """


class WebSocketProtocolError(Exception):
    """
    Internal exception raised when the remote side breaks the protocol.

    """
