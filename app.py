import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello!\n\n'.encode())
        for kv in sorted(os.environ.items()):
            self.wfile.write('{}={}\n'.format(*kv).encode())

server = HTTPServer(('0.0.0.0', 8080), HelloServer)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
