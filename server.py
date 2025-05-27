from http.server import BaseHTTPRequestHandler, HTTPServer

class SimplePOSTHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get content length from headers
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the body of the request
        post_data = self.rfile.read(content_length)
        
        # Print the request to stdout
        print(f"\nReceived POST request on path: {self.path}")
        print("Headers:")
        print(self.headers)
        print("Body:")
        print(post_data.decode('utf-8'))
        print("="*60)

        # Send a simple response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Received POST request\n")

def run(server_class=HTTPServer, handler_class=SimplePOSTHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}... (press Ctrl+C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple POST request HTTP server")
    parser.add_argument('--port', type=int, default=8080, help='Port number to listen on (default: 8080)')
    args = parser.parse_args()

    run(port=args.port)
