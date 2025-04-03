from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from uuid import uuid4
import asyncio
import os

app = FastAPI()

# Serve static files (HTML, JS, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory document storage
documents = {}  # {document_id: {"content": "", "clients": set()}}

@app.get("/")
async def serve_home():
    return FileResponse("static/index.html")

@app.post("/documents")
async def create_document():
    document_id = str(uuid4())
    documents[document_id] = {"content": "", "clients": set()}
    return {"document_id": document_id}

@app.get("/documents/{document_id}")
async def get_document(document_id: str):
    if document_id not in documents:
        return {"error": "Document not found"}
    return {"document_id": document_id, "content": documents[document_id]["content"]}

@app.websocket("/ws/documents/{document_id}")
async def websocket_endpoint(websocket: WebSocket, document_id: str):
    if document_id not in documents:
        await websocket.close()
        return

    await websocket.accept()
    documents[document_id]["clients"].add(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            documents[document_id]["content"] = data["content"]
            await broadcast(document_id, data["content"])
    except WebSocketDisconnect:
        documents[document_id]["clients"].remove(websocket)

async def broadcast(document_id: str, content: str):
    clients = documents[document_id]["clients"]
    for client in clients:
        await client.send_json({"content": content})
