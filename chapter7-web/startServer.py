from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple Server on port:" + str(httpd.server_port))
httpd.serve_forever()
