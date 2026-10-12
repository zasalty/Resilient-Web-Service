from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    server = os.environ.get("SERVER_NAME", "Unknown")

    return f"""
    <h1>Cybersecurity Project</h1>
    <h2>Resilient Web Service</h2>
    <p>Server handling request: {server}</p>
    <p>Status: Online</p>
    """

@app.route("/health")
def health():
    return "OK", 200
