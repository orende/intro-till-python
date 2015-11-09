import SimpleHTTPServer, SocketServer


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        return ""

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write("<html>Hello world from Python</html>")
        self.wfile.close()


httpd = SocketServer.TCPServer(("", 8000), MyHandler)
print "serving at port", 8000
httpd.serve_forever()
