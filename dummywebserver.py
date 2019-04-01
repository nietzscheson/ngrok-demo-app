import SimpleHTTPServer
import SocketServer

PORT = 9000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      self.send_response(200)
      self.end_headers()
      #response = BytesIO()
      #response.write(b'This is POST request. ')
      #response.write(b'Received: ')
      #response.write(body)
      #self.wfile.write(response.getvalue())
      print post_body

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()