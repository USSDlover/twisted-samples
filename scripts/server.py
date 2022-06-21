from twisted.internet.protocol import Protocol, connectionDone
from twisted.python import failure


class Echo(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently %d open connections.\n" %
            (self.factory.numProtocols,)
        )

    def connectionLost(self, reason: failure.Failure = connectionDone):
        self.factory.numProtocols = self.factory.numProtocols - 1

    # The method simply writes back whatever is written to it
    # and does not respond ta all events.
    def dataReceived(self, data: bytes):
        self.transport.write(data)


class QOTD(Protocol):

    # This method will respond with a nice quote and
    # lose the current connection and will get ready
    # for next events
    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away\r\n")
        self.transport.loseConnection()
