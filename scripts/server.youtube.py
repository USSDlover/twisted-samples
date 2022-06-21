from twisted.internet import reactor, protocol
from twisted.internet.protocol import ServerFactory as ServeFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class Server(protocol.Protocol):
    def connectionMade(self):
        print("new connection")
        self.transport.write("Hello From Server".encode('utf-8'))

    def dataReceived(self, data: bytes):
        print('data from client')
        received_data = data.decode('utf-8')
        print(received_data)
        self.transport.write(data)


class ServerFactory(ServeFactory):
    def buildProtocol(self, addr):
        return Server()


def main():
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()


if __name__ == '__main__':
    main()
