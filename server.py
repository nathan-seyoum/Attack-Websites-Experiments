from flask import Flask, send_from_directory
import os

app = Flask(__name__)

SERVE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/clean")
def serve_clean():
    return send_from_directory(SERVE_DIR, "ml_docs_clean.html")

@app.route("/injected")
def serve_injected():
    return send_from_directory(SERVE_DIR, "ml_docs_injected.html")

@app.route("/")
def index():
    return (
        "<h2>OpenClaw Experiments</h2>"
        "<ul>"
        "<li><a href='/clean'>/clean</a> &mdash; ml_docs_clean.html (control)</li>"
        "<li><a href='/injected'>/injected</a> &mdash; ml_docs_injected.html (payload)</li>"
        "</ul>"
    )

if __name__ == "__main__":
    print("Serving OpenClaw experiments:")
    print("  http://localhost:8090/clean")
    print("  http://localhost:8090/injected")
    app.run(host="0.0.0.0", port=8090, debug=False)
