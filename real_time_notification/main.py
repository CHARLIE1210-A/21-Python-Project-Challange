from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import Dict, List

app = FastAPI()


# ================= HTML PAGE =================
html = """
<!DOCTYPE html>
<html>
<body>
<h2>Notification Client</h2>

<input id="username" placeholder="Enter username">
<button onclick="connect()">Connect</button>

<ul id="messages"></ul>

<script>
let ws;

function connect() {
    const user = document.getElementById("username").value;
    ws = new WebSocket(`ws://127.0.0.1:8000/ws/${user}`);

    ws.onmessage = function(event) {
        let li = document.createElement("li");
        li.textContent = event.data;
        document.getElementById("messages").appendChild(li);
    };

    ws.onclose = () => alert("Connection closed");
}
</script>
</body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


# ================= CONNECTION MANAGER =================
class NotificationManager:
    def __init__(self):
        self.connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        self.connections.setdefault(username, []).append(websocket)

    def disconnect(self, username: str, websocket: WebSocket):
        self.connections[username].remove(websocket)
        if not self.connections[username]:
            del self.connections[username]

    async def send_notification(self, username: str, message: str):
        if username in self.connections:
            for ws in self.connections[username]:
                await ws.send_text(message)


manager = NotificationManager()


# ================= WEBSOCKET =================
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(username, websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(username, websocket)


# ================= SEND NOTIFICATION =================
@app.post("/notify")
async def notify(username: str, message: str):
    await manager.send_notification(username, message)
    return {"status": "Notification sent"}
