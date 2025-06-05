from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        payload = {"message": "Mock API success", "status": "ok"}
        self.wfile.write(json.dumps(payload).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8081), MockHandler)
    print("[SIM] Mock API server running at http://localhost:8081")
    server.serve_forever()
