import os
import sys
import socket
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello!\n\n'.encode())
        for kv in sorted(os.environ.items()):
            self.wfile.write('{}={}\n'.format(*kv).encode())


pid = os.getpid()
hostname = socket.gethostname()


def heartbeat():
    sys.stdout.write('out: HELLO FROM {}@{}\n'.format(pid, hostname))
    sys.stdout.flush()
    sys.stderr.write('err: HELLO FROM {}@{}\n'.format(pid, hostname))
    sys.stderr.flush()
    threading.Timer(1, heartbeat).start()
threading.Timer(1, heartbeat).start()


server = HTTPServer(('0.0.0.0', 8080), HelloServer)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
