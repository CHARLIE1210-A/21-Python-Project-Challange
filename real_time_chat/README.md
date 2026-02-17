# Real-Time Chat Application (Project 17 of 21 Python Project Challenge)

This project is the 17th application in the "21 Python Project Challenge." It is a real-time chat application built using FastAPI and WebSockets, allowing multiple users to communicate instantly through a web interface.

## Features
- Real-time messaging using WebSockets
- Broadcasts messages to all connected clients
- Simple and clean HTML frontend
- Built with FastAPI for high performance

## How It Works
- Users connect to the chat via a web browser.
- Each message sent by a user is broadcast to all connected users in real time.
- The backend manages active WebSocket connections and handles message distribution.

## Getting Started

### Prerequisites
- Python 3.8+
- [uvicorn](https://www.uvicorn.org/) (ASGI server)
- [FastAPI](https://fastapi.tiangolo.com/)

### Installation
1. Clone this repository or download the project files.
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

### Running the Application
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the chat interface.

## Project Structure
- `main.py` - FastAPI backend with WebSocket support
- `index.html` - Frontend chat interface
- `pyproject.toml` - Project metadata and dependencies

## Usage
- Open the app in multiple browser tabs or devices to test real-time chat.
- Type a message and press enter to send. All connected users will see the message instantly.

## License
This project is for educational purposes as part of the 21 Python Project Challenge.

---
**Project 17 of 21**
