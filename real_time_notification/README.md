# 21 Python Challenge: Real-Time Notification System

Welcome to the **21 Python Challenge**! This repository contains one of the 21 Python applications: a **Real-Time Notification System** built with FastAPI and WebSockets.

## Project Overview
This application demonstrates how to implement a real-time notification system using FastAPI. Users can connect via WebSocket, and notifications can be sent to specific users instantly.

## Features
- WebSocket-based real-time communication
- User-specific notification delivery
- REST API endpoint to trigger notifications
- Simple and extensible code structure

## How It Works
- Users connect to `/ws/{username}` via WebSocket.
- The server keeps track of active connections for each user.
- Notifications can be sent to a user by making a POST request to `/notify` with the username and message.
- The message is delivered in real-time to all active WebSocket connections for that user.

## Getting Started

### Prerequisites
- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/) (for running the server)

### Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd real_time_notification
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
   Or use your preferred package manager (e.g., `uv` or `poetry`).

### Running the Application
Start the FastAPI server with uvicorn:
```bash
uvicorn main:app --reload
```

### Usage
1. **Connect via WebSocket:**
   - Use a WebSocket client (e.g., browser, [websocat](https://github.com/vi/websocat), or Postman) to connect to:
     ```
     ws://localhost:8000/ws/<username>
     ```
2. **Send Notification:**
   - Make a POST request to `/notify` with `username` and `message` as form data or query parameters:
     ```bash
     curl -X POST "http://localhost:8000/notify?username=alice&message=Hello+Alice!"
     ```
   - The message will be delivered in real-time to all WebSocket clients connected as `alice`.

## Example
- Open two browser tabs and connect both to `ws://localhost:8000/ws/alice`.
- Send a notification to `alice` using the `/notify` endpoint.
- Both tabs will receive the message instantly.

## About the 21 Python Challenge
This project is part of the **21 Python Challenge**, a series of 21 practical Python applications designed to help you learn and master Python by building real-world projects. Each application focuses on a different concept or technology in Python.

## License
This project is licensed under the MIT License.

---

**Happy Coding!**
