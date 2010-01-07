class LoginError(Exception): pass
class NoFreeChannels(Exception): pass
class DuplicateConsumerTag(Exception): pass
class UnknownConsumerTag(Exception): pass
class RecursiveOperationDetected(Exception): pass
class ContentTransmissionForbidden(Exception): pass

class ConnectionClosed(Exception): pass
class ChannelClosed(Exception): pass

class ProtocolSyntaxError(Exception): pass
class UnexpectedFrameError(ProtocolSyntaxError): pass
class ProtocolVersionMismatch(ProtocolSyntaxError): pass
class BodyTooLongError(ProtocolSyntaxError): pass
class InvalidFrameError(ProtocolSyntaxError): pass
class InvalidProtocolHeader(ProtocolSyntaxError): pass
class InvalidTableError(ProtocolSyntaxError): pass
