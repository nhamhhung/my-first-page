"""my-first-page — a web app: password login -> dashboard -> one bounded 'Ask AI' action (optional)."""
import hashlib
import json
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse

PASSWORD = os.environ.get("SITE_PASSWORD", "demo-site-password-0000")
SESSION = hashlib.sha256(PASSWORD.encode()).hexdigest()
app = FastAPI()
authed = lambda r: r.cookies.get("session") == SESSION


def page(body):
    return HTMLResponse(f'<!doctype html><meta charset="utf-8"><title>my-first-page</title>'
                        f'<body style="font-family:sans-serif;max-width:40rem;margin:3rem auto">{body}')


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/.well-known/agent-card.json")
def card():
    return json.load(open(os.path.join(os.path.dirname(__file__), ".well-known/agent-card.json")))


@app.post("/login")
async def login(request: Request):
    form = await request.form()
    if form.get("password") != PASSWORD:
        return page('wrong password — <a href="/">retry</a>')
    r = RedirectResponse("/", status_code=302)
    r.set_cookie("session", SESSION, httponly=True, samesite="lax")
    return r




@app.get("/")
def home(request: Request):
    if not authed(request):
        return page('<h1>my-first-page</h1><form method="post" action="/login">'
                    '<input type="password" name="password" placeholder="password" autofocus>'
                    '<button>Log in</button></form>')
    ai_ui = ""
    return page(f"<h1>Hello, World!</h1>{ai_ui}")
