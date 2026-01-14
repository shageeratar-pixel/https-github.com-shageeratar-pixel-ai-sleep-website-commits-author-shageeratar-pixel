from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Sleep Monitoring Website</h1>
    <p>Status: Running Successfully</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000
