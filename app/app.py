import os
from http.server import BaseHTTPRequestHandler, HTTPServer

name = os.getenv("STUDENT_NAME", "Dastan")
surname = os.getenv("STUDENT_SURNAME", "Temirbek")
group = os.getenv("STUDENT_GROUP", "IT2-2308")
student_id = os.getenv("STUDENT_ID", "37621")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"""==============================
DevOps Student Application
==============================
Name: {name}
Surname: {surname}
Group: {group}
Student ID: {student_id}

Application is running successfully!
"""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

print("==============================")
print("DevOps Student Application")
print("==============================")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Group: {group}")
print(f"Student ID: {student_id}")
print("Application is running on port 8080", flush=True)

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
