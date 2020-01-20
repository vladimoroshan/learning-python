#!/usr/bin/env python3

from http.server import HTTPServer
from server import Server

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(f"Server Starts - {HOST_NAME}, {PORT_NUMBER}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(f"Server Stops - {HOST_NAME}, {PORT_NUMBER}")
