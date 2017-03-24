"""
soundctrl.py is a Python stdlib-only server for changing the volume.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import Popen

class SoundCtrlHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        start = self.path.rindex("/") + 1
        try:
            volume = int(self.path[start:])
            print("Setting volume to {}".format(volume))
            Popen(["osascript", "-e", "set volume output volume {}".format(volume)]).wait()
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return
        except ValueError as e:
            print("Error: {}".format(e))
            self.send_response(500)
            self.end_headers()

bindaddr = ('0.0.0.0', 8001)
server = HTTPServer(bindaddr, SoundCtrlHandler)
server.serve_forever()
