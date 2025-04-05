# Real-Time Collaborative Document Editor

This project is a real-time collaborative document editing tool built using **FastAPI** and **WebSockets**.

---

## 🚀 Setup & Installation (Local)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SimranBagli/real-time-editor.git
cd real-time-editor
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server (Locally)
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ Open the App in Browser
Visit:
```
http://127.0.0.1:8000/
```

### 5️⃣ Create & Share a Document
- Open the above URL in multiple browser tabs.
- Click "Create Document" to generate a new document.
- Copy the document ID and share it with others.
- Open the same URL on another device or browser and enter the document ID to collaborate in real-time.

---

## 🐳 Docker Setup

### 1️⃣ Build the Docker Image
```bash
docker build -t real-time-editor .
```

### 2️⃣ Run the Container
```bash
docker run -p 8000:8000 real-time-editor
```

### 3️⃣ Open the App in Browser
Visit:
```
http://localhost:8000/
```
