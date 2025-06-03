from flask import Flask, request
import requests
import json

app = Flask(__name__)

# === KONFIGURATION ===
CLIENT_ID = "1379513076189106268"
CLIENT_SECRET = "ZxR3kULDCUoG4GgFtTOD59mEQT-XDyxN"  # Direkt eingetragen
REDIRECT_URI = "https://astonishing-mercy.up.railway.app/auth"  # Ersetze mit Railway-URL
USERS_FILE = "users.json"

def save_user(data):
    try:
        with open(USERS_FILE, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    if not any(u["id"] == data["id"] for u in users):
        users.append(data)
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=2)

@app.route("/auth")
def auth():
    code = request.args.get("code")
    if not code:
        return "No code provided", 400

    token_res = requests.post(
        "https://discord.com/api/oauth2/token",
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    token_json = token_res.json()
    access_token = token_json.get("access_token")
    refresh_token = token_json.get("refresh_token")

    if not access_token:
        return f"Failed to get access token: {token_json}", 400

    user_res = requests.get(
        "https://discord.com/api/users/@me",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    user_json = user_res.json()

    save_user({
        "id": user_json["id"],
        "username": user_json["username"],
        "access_token": access_token,
        "refresh_token": refresh_token
    })

    return "✅ Erfolgreich verbunden. Du kannst das Fenster schließen."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
