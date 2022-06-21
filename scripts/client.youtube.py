from twisted.internet import protocol, endpoints, reactor
from twisted.internet.interfaces import IAddress


class Client(protocol.Protocol):
    def connectionMade(self):
        print('Client Connected')

    def dataReceived(self, data: bytes):
        print('Data Received')
        received_data = data.decode('utf-8')
        print(received_data)
        self.transport.write(input(':::').encode('utf-8'))


class ClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr: IAddress) -> "Optional[Protocol]":
        return Client()


def main():
    endpoint = endpoints.TCP4ClientEndpoint(reactor, 'localhost', 2000)
    endpoint.connect(ClientFactory())
    reactor.run()


if __name__ == '__main__':
    main()
