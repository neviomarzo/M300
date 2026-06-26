from flask import Flask
import os
import socket

app = Flask(__name__)

VERSION = "1.0.2"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Demo App</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }}
        .card {{ background: #f5f5f5; border-radius: 8px; padding: 20px; margin: 10px 0; }}
        .version {{ background: #0075A8; color: white; border-radius: 8px; padding: 20px; margin: 10px 0; }}
        h1 {{ color: #333; }}
        label {{ font-weight: bold; color: #666; }}
        p {{ margin: 5px 0; font-size: 18px; }}
    </style>
</head>
<body>
    <h1>🚀 M300 Demo App</h1>
    <div class="version">
        <label>Version</label>
        <p>{version}</p>
    </div>
    <div class="card">
        <label>Pod Name</label>
        <p>{pod_name}</p>
    </div>
    <div class="card">
        <label>Node</label>
        <p>{node_name}</p>
    </div>
    <div class="card">
        <label>Namespace</label>
        <p>{namespace}</p>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return HTML.format(
        version=VERSION,
        pod_name=socket.gethostname(),
        node_name=os.environ.get("NODE_NAME", "unknown"),
        namespace=os.environ.get("NAMESPACE", "unknown")
    )

@app.route("/health")
def health():
    return {"status": "ok", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)