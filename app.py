from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket
import psycopg


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/about":
            message = """
            <h1>About This Application</h1>
            <p>This is an enhanced Docker Compose web application.</p>
            <p>Feature update: About page added successfully!</p>
            <p><a href="/">Return to Home</a></p>
            """
        elif self.path == "/":
            try:
                with psycopg.connect(
                    host=os.getenv("DB_HOST", "db"),
                    dbname=os.getenv("POSTGRES_DB", "appdb"),
                    user=os.getenv("POSTGRES_USER", "appuser"),
                    password=os.environ["POSTGRES_PASSWORD"],
                    connect_timeout=3,
                ) as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT 1")
                        cur.fetchone()
                db_status = "Connected"
            except Exception as e:
                db_status = f"Unavailable: {type(e).__name__}"

            message = f"""
            <h1>Hello, World!</h1>
            <p>Docker Compose web application is running.</p>
            <p>Container: {socket.gethostname()}</p>
            <p>Database status: {db_status}</p>
            <p><a href="/about">About this application</a></p>
            """
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found")
            return

        body = message.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()