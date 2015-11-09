import SimpleHTTPServer, SocketServer

httpd = SocketServer.TCPServer(("", 8000), SimpleHTTPServer.SimpleHTTPRequestHandler)
print "serving at port", 8000
httpd.serve_forever()
