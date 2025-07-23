# # Otaku Stream Tracker 🎥🍜

A web application to track and manage anime series, stream updates, and upcoming episodes.  
Built with **Flask** and modern frontend magic.

## 🌟 Features
- Track multiple anime series
- Manage status: Watching / Completed / Dropped
- Next episode reminders
- Clean and minimal UI

## 🛠️ Tech Stack
- 🐍 Flask (Backend)
- 🌐 HTML + CSS + JS (Frontend)
- 🐘 SQLite (Database, or upgradeable to PostgreSQL)

## 🚀 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/juneikon/otaku_stream_tracker.git
cd otaku_stream_tracker

# 2. Set up a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py  # or however your entry point is named
