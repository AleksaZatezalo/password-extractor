from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

class SimplePOSTHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        print(f"\n🔔 Received POST request on path: {self.path}")
        print("📄 Headers:")
        for key, value in self.headers.items():
            print(f"  {key}: {value}")
        
        print("\n📝 Parsed Body:")

        content_type = self.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                data = json.loads(post_data)
                for key, value in data.items():
                    print(f"  {key}: {value}")
            except json.JSONDecodeError:
                print("  ⚠️ Invalid JSON data")
        elif "application/x-www-form-urlencoded" in content_type:
            data = parse_qs(post_data)
            for key, value in data.items():
                print(f"  {key}: {', '.join(value)}")
        else:
            print("  🔍 Raw body (unparsed):")
            print(f"  {post_data}")

        print("=" * 60)

        # Respond to client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST data received and printed.\n")


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
