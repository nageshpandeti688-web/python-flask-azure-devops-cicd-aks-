
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Azure DevOps Demo</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
            background: #f1f5f9;
          }
          .card {
            background: white;
            padding: 35px;
            margin: auto;
            max-width: 600px;
            border-radius: 12px;
          }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>Azure DevOps CI/CD Demo</h1>
          <p>Flask application running on Azure Kubernetes Service.</p>
          <p>Build | Test | SonarQube | Docker | AKS</p>
          <p>Status: Application is running!</p>
        </div>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)