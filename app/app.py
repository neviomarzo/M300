from flask import Flask

app = Flask(__name__)

VERSION = "1.0.1"

@app.route("/")
def index():
    return f"<h1>Demo App</h1><p>Version: {VERSION}</p>"

@app.route("/health")
def health():
    return {"status": "ok", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)