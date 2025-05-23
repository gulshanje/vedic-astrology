
# Jyotish Engine

Welcome to Jyotish Engine — a Python-based astrology engine that calculates Lagna, Planetary Positions, Nakshatras, Dashas (Mahadasha, Antardasha, Pratyantardasha, Sookshma Dasha), and generates charts using Swiss Ephemeris and advanced astrology calculations!

- Features

  - Calculate Lagna (Ascendant), Rashi (Zodiac Sign), and Nakshatra.
  - Planetary Positions (Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, Rahu, Ketu).
  - Dasha Tree generation up to Sookshma level.
  - Moon Chart & Lagna Chart plotting using Matplotlib or Plotly.
  - Export charts and Dashas to JSON or Excel.
  - REST API ready for Flask/FastAPI.
  - Simple UI using Streamlit.
  - All constants managed separately for easy updates.
  - Interactive visualization.

- Tech Stack

  - Python 3.8+
  - Swiss Ephemeris (pyswisseph)
  - Matplotlib or Plotly
  - Flask / FastAPI (for API serving)
  - Streamlit (for UI)
  - Pandas (for exporting to Excel)
  - Pytest / Unittest (for testing)

- Installation

1. Clone the repository

> git clone https://github.com/your-username/jyotish-engine.git
> cd jyotish-engine

2. Set up virtual environment (Recommended)

> python -m venv venv
> source venv/bin/activate # On Windows use: venv\Scripts\activate

3. Install dependencies

> pip install -r requirements.txt

4. Install Swiss Ephemeris

> pip install pyswisseph
