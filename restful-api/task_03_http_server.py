#!/usr/bin/python3
"""
simple API
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler_API(BaseHTTPRequestHandler):
    """
    Handler_API
    """
    def do_GET(self):
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            information = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(information).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=Handler_API, port=8000):
    """
    function
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Serve on port {}...".format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    """
    testing
    """
    run()
