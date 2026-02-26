# 🌐 Minimalist Terminal Browser

A simple, text-mode web browser designed to run directly in the terminal. This project was built using **Python**, following **Extreme Programming (XP)** principles and **Test-Driven Development (TDD)**.

## 🚀 Features

- 📄 **Text-only rendering**: Fast and distraction-free navigation.
- 🔗 **Link Mapping**: Numbered links for easy keyboard navigation.
- 🎨 **Colorized UI**: Uses Rich to distinguish headers, links, and text.
- 🔒 **Secure by default**: No JavaScript execution or tracking cookies.
- 🗺️ **Relative URL Resolution**: Smart navigation between pages.

## 🛠️ Tech Stack

- **Python 3.13+**
- **HTTPX**: For fast HTTP requests.
- **BeautifulSoup4**: For robust HTML parsing.
- **Rich**: For terminal formatting and colors.
- **Pytest**: For the TDD test suite.

## 📦 Installation & Setup

1. **Clone the repository**:
   git clone https://github.com/mapaba79/python_terminal_browser.git
   cd python_terminal_browser

2. **Create and activate a virtual environment**:
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**:
   pip install -r requirements.txt

## 🖥️ Usage

To start the browser, run:
python main.py

- Enter a URL to start browsing (e.g., https://www.python.org).
- Type the **number** in brackets (e.g., [5]) to follow a link.
- Type **'q'** to quit.

## 🧪 Running Tests

This project follows TDD. To ensure everything is working correctly, run:
pytest test_browser.py

## 📜 Principles Applied (XP)

- ✨ **Simplicity**: Focus on content (H1, P, A tags) without complex CSS rendering.
- 📦 **Small Releases**: A fully functional browser in a few lines of code.
- 🧪 **TDD**: Core logic is covered by unit tests before implementation.
