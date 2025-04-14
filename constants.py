PLANETS = [
    "Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn",
    "Rahu", "Ketu"
]

# House system constants
HOUSE_SYSTEMS = {
    "Placidus": b'P',
    "Koch": b'K',
    "Campanus": b'C',
    "Topocentric": b'T',
    "Equal": b'E',
    "Regiomontanus": b'R',
}

# Planet constants (for quick lookup)
PLANET_NAMES = {
    "SUN": 0,
    "MOON": 1,
    "MARS": 4,
    "MERCURY": 2,
    "VENUS": 3,
    "JUPITER": 5,
    "SATURN": 6,
}


RASHI_LIST = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
AKSHASA_RASHI_LIST = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni']

PLANETS = {
    'Sun': {'Rashi': 'Leo', 'Nakshatra': 'Magha', 'Lagna': 'Leo'},
    'Moon': {'Rashi': 'Cancer', 'Nakshatra': 'Pushya', 'Lagna': 'Cancer'},
    'Mars': {'Rashi': 'Aries', 'Nakshatra': 'Ashwini', 'Lagna': 'Aries'},
    # Add other planets similarly...
}


# Dummy constants — you probably already have this
DASHA_SEQUENCE = ['Ketu', 'Venus', 'Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury']

DASHA_YEARS = {
    'Ketu': 7,
    'Venus': 20,
    'Sun': 6,
    'Moon': 10,
    'Mars': 7,
    'Rahu': 18,
    'Jupiter': 16,
    'Saturn': 19,
    'Mercury': 17
}

WEEKDAY_START_PLANET = {
    0: "Moon",  # Monday
    1: "Mars",  # Tuesday
    2: "Mercury",  # Wednesday
    3: "Jupiter",  # Thursday
    4: "Venus",  # Friday
    5: "Saturn",  # Saturday
    6: "Sun"    # Sunday
}

WEEKDAY_LORD = {
    0: "Moon",  # Monday
    1: "Mars",  # Tuesday
    2: "Mercury",  # Wednesday
    3: "Jupiter",  # Thursday
    4: "Venus",  # Friday
    5: "Saturn",  # Saturday
    6: "Sun"    # Sunday
}

PLANETS = ['Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon']

WEEKDAY_START_PLANET = {
    0: 'Moon', 1: 'Mars', 2: 'Mercury', 3: 'Jupiter', 4: 'Venus', 5: 'Saturn', 6: 'Sun'
}

NAKSHATRAS = [
    "Ashwini",
    "Bharani",
    "Krittika",
    "Rohini",
    "Mrigashirsha",
    "Ardra",
    "Punarvasu",
    "Pushya",
    "Ashlesha",
    "Magha",
    "Purva Phalguni",
    "Uttara Phalguni",
    "Hasta",
    "Chitra",
    "Swati",
    "Vishakha",
    "Anuradha",
    "Jyeshtha",
    "Mula",
    "Purva Ashadha",
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha",
    "Purva Bhadrapada",
    "Uttara Bhadrapada",
    "Revati"
]

TITHI = [
            "Pratipada", "Dviteeya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami",
            "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
            "Pratipada", "Dviteeya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami",
            "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima"
        ]

ZODIAC_SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
                    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']