import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data)
	# the line of code above is not needed but it is nice to check if the code works
if __name__ == "__main__":
#boilerplate "__main__" function
    HOST, PORT = "localhost", 9999
#The host ip is bound to your local ip adress with is always 127.0.0.1

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

#I forgot to link the original github page for this code.
#I think that the comments already included are good enough to explain the code. 
