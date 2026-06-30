# 🤖 AI Auto Reply Bot

An intelligent AI-powered auto-reply bot built with **Python** that automates conversations in desktop messaging applications. It captures chat history using GUI automation, generates context-aware responses using the **Gemini API**, and automatically sends replies.

> ⚠️ This project uses screen coordinates and GUI automation, making it adaptable to virtually any desktop messaging application by simply changing the coordinates.

---

## ✨ Features

- 🤖 AI-powered replies using Gemini API
- 💬 Reads the latest chat automatically
- 🖱️ GUI automation with PyAutoGUI
- 📋 Clipboard-based chat extraction
- ⚡ Automatically detects new messages
- 🧠 Maintains conversation context
- 🔧 Easily customizable for different desktop applications
- 💻 Lightweight and simple to modify

---

## 🛠️ Tech Stack

- Python 3.x
- PyAutoGUI
- Pyperclip
- Gemini API
- Time Module

---

## 📂 Project Structure

```
AI-Auto-Reply-Bot/
│
├── main.py          # Main automation script
├── client.py        # Gemini API integration
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Auto-Reply-Bot.git
cd AI-Auto-Reply-Bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pyautogui pyperclip openai
```

---

## ⚙️ Configuration

1. Create your AI client inside `client.py`.
2. Add your API key securely.
3. Update the screen coordinates inside `main.py` according to your display and target application.

Example:

```python
pyautogui.click(x, y)
```

You can find coordinates using:

```python
import pyautogui

while True:
    print(pyautogui.position())
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Monitor the chat window.
2. Copy the latest conversation.
3. Send the conversation to Gemini.
4. Generate an AI response.
5. Automatically paste and send the reply.

---

## 📸 How It Works

```
Incoming Message
        │
        ▼
Copy Chat History
        │
        ▼
Send to Gemini API
        │
        ▼
Generate AI Response
        │
        ▼
Paste Response
        │
        ▼
Send Message
```

---

## 📦 Requirements

- Python 3.10+
- Gemini API Key
- Internet Connection
- Desktop Messaging Application
- Correct Screen Coordinates

---

## ⚠️ Disclaimer

This project is intended for **educational and personal automation purposes only**.

Please ensure that your use of this project complies with the Terms of Service of the application you automate. The authors are not responsible for misuse or any consequences resulting from automated interactions.

---

## 🔮 Future Improvements

- Multi-platform support
- Voice input/output
- Image understanding
- OCR-based message reading
- Local LLM support
- Better UI
- Coordinate auto-detection

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Manav Parmar**

Python Developer • AI Enthusiast • Automation Builder

Connect with me on LinkedIn and feel free to contribute or suggest improvements!
