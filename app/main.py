from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Webvory DevOps Assignment</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 50px;
            }
            .card {
                background: #1e293b;
                padding: 30px;
                border-radius: 15px;
                width: 60%;
                margin: auto;
            }
            .status {
                color: #22c55e;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 DevOps Production Deployment</h1>
            <p>Assignment for Webvory</p>

            <h2>Status: <span class="status">Running</span></h2>

            <p>FastAPI + PostgreSQL + Redis + NGINX</p>
            <p>Dockerized | CI/CD Enabled | Health Checks Active</p>

            <p>Hosted on Azure VPS</p>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "healthy"}