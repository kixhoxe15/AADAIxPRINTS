from flask import Flask, send_from_directory, abort
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:filename>")
def files(filename):
    file_path = BASE_DIR / filename
    if not file_path.is_file() or BASE_DIR not in file_path.resolve().parents:
        abort(404)
    return send_from_directory(BASE_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
