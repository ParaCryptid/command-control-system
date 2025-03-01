# Command-Control System

## Overview
This is a professional-grade Command and Control system with:
- **AI-Powered Command Analysis** (via Hugging Face Transformers)
- **Real-time WebSocket Communication** (Flask-SocketIO)
- **Integrated PostgreSQL & Redis Support**

## 🚀 Installation

### Prerequisites
Ensure you have Python 3.8+ installed.

### Setup Steps:
1. **Clone the repository**:
   ```bash
   git clone <repo_url>
   cd command-control-system-main
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Run tests**:
   ```bash
   pytest
   ```

## 🔌 WebSocket Usage
Connect using WebSockets to `ws://localhost:5000` and emit commands:
```json
{
  "command": "Deploy resources immediately."
}
```

## 📜 License
This project is licensed under the MIT License.
