# file: hora_calculator.py

from datetime import datetime, timedelta
from astral import LocationInfo
from astral.moon import phase
from astral.sun import sun
import pytz
from constants import PLANETS, WEEKDAY_START_PLANET, WEEKDAY_LORD, NAKSHATRAS, TITHI, ZODIAC_SIGNS
import swisseph as swe
import math

class JyotishEngine:
    def __init__(self,  city_name, unix_timestamp, latitude, longitude, timezone_str="UTC"):
        self.city_name =  city_name 
        self.timezone = pytz.timezone(timezone_str)
        self.date_time = datetime.fromtimestamp(unix_timestamp, tz=self.timezone)
        self.date = self.date_time.date()
        self.latitude = latitude
        self.longitude = longitude
        self.city = LocationInfo(latitude=self.latitude, longitude=self.longitude)
        self.sun_times = self.get_sun_times()
        self.tithi = self.get_tithi()
        self.utc_time = self.get_utc_time()
        self.location = LocationInfo(self.city_name, self.timezone, self.latitude, self.longitude)

    def get_sun_times(self):
        observer = self.city.observer
        s = sun(observer, date=self.date, tzinfo=self.timezone)
        return s
    

    def get_utc_time(self):
        # Get current local time in the specified timezone
        # local_time = datetime.datetime.now(pytz.timezone(self.timezone))
        # Convert to UTC
        utc_time = self.date_time.astimezone(pytz.utc)
        return utc_time

# getting the tithi

    def get_tithi(self):
        moon_position = phase(self.date_time)
        tithi = int(moon_position * 27)  # 27 Nakshatras
        tithi = int(tithi / 13.3333)
        # Adjust tithi to be in the range of 0-29   
        # tithi = tithi % 30
        # print(f"Tithi: {tithi}")
        # print(f"Moon Position: {moon_position}")
        # print(f"Moon Phase: {moon_position}")
        #      
        tithi = (tithi + 1) % 30       
        current_tithi = TITHI[tithi + 1]
        # print(f"Current Tithi: {current_tithi}")
        return current_tithi

    def get_starting_planet(self):
        weekday = self.date.weekday()
        return WEEKDAY_START_PLANET[weekday]

    def get_weekday_lord(self):
        weekday = self.date.weekday()
        return WEEKDAY_LORD[weekday]

    def generate_hora_schedule(self):
        sunrise = self.sun_times['sunrise']
        sunset = self.sun_times['sunset']

        day_duration = (sunset - sunrise)
        night_duration = (sunrise + timedelta(days=1)) - sunset

        day_hora_length = day_duration / 12
        night_hora_length = night_duration / 12

        schedule = []
        starting_planet = self.get_starting_planet()
        current_planet_index = PLANETS.index(starting_planet)

        current_time = sunrise
        for _ in range(12):
            planet = PLANETS[current_planet_index % 7]
            next_time = current_time + day_hora_length
            schedule.append((planet, current_time, next_time))
            current_time = next_time
            current_planet_index += 1

        for _ in range(12):
            planet = PLANETS[current_planet_index % 7]
            next_time = current_time + night_hora_length
            schedule.append((planet, current_time, next_time))
            current_time = next_time
            current_planet_index += 1

        return schedule

    def get_current_hora(self):
        now = datetime.now(self.timezone)
        schedule = self.generate_hora_schedule()
        for i, (planet, start, end) in enumerate(schedule, 1):
            if start <= now < end:
                print(f"\n🕒 Current Time: {now.strftime('%H:%M:%S')}")
                print(f"Current Hora: {planet}")
                print(f"Time Period: {start.strftime('%H:%M:%S')} - {end.strftime('%H:%M:%S')}")
                return planet
        print("Current time is outside calculated horas.")
        return None

    def calculate_nakshatra(self):
        """Calculate Nakshatra using Moon longitude approximation."""
        # For simple mock purpose, we simulate Moon longitude
        # In real app, you should use a library like Skyfield
        simulated_moon_longitude = (self.date_time.hour * 15) % 360  # Fake calculation
        nakshatra_index = int(simulated_moon_longitude / (360 / 27))
        return NAKSHATRAS[nakshatra_index]

    def calculate_lagna(self):
        # Convert UTC time to Julian date (required by pyswisseph)
        jd = swe.julday(self.utc_time.year, self.utc_time.month, self.utc_time.day,
                        self.utc_time.hour + self.utc_time.minute / 60.0 + self.utc_time.second / 3600.0)
        
        # Get the sidereal time (this is essential for Lagna calculation)
        sidereal_time = swe.sidtime(jd)
        
        # Calculate the position of the Ascendant (Lagna)
        # The formula involves the observer's latitude and longitude along with sidereal time
        # obliquity = swe.calc(jd, swe.ECLIPTIC)[0][0]  # Earth's axial tilt (ecliptic obliquity)
        
        # Calculate the local sidereal time in degrees
        lst = sidereal_time + (self.longitude / 15.0)  # 1 hour = 15 degrees
        lst = lst % 24.0  # Normalize to 24-hour format
        
        # Convert LST to degrees
        lst_in_deg = lst * 15.0  # 15 degrees per hour
        
        # Calculate the Ascendant (Lagna) using the formula for the tropical zodiac
        ascendant = lst_in_deg + self.latitude / 90.0
        ascendant = ascendant % 360.0  # Ensure it's within 360 degrees
        
        # The result is the degree of the zodiac sign where the Ascendant (Lagna) falls
        return ascendant

    def get_zodiac_sign(self, degree):
        # Zodiac signs as per the tropical zodiac (starting with Aries at 0 degrees)
        
        # Determine the sign based on the degree
        sign_index = math.floor(degree / 30)  # 30 degrees per sign
        return ZODIAC_SIGNS[sign_index]

    def get_lagna_info(self):
        ascendant_degree = self.calculate_lagna()
        zodiac_sign = self.get_zodiac_sign(ascendant_degree)
        return {"Ascendant Degree": ascendant_degree, "Zodiac Sign": zodiac_sign}
    
    def display_schedule(self):
        schedule = self.generate_hora_schedule()
        print(f"\nHora Schedule for {self.date}:")
        for i, (planet, start, end) in enumerate(schedule, 1):
            print(f"{i:02d}. {planet}: {start.strftime('%H:%M:%S')} - {end.strftime('%H:%M:%S')}")

    def show_summary(self):
        sun_rise = self.sun_times['sunrise'].strftime('%H:%M:%S')
        sun_set = self.sun_times['sunset'].strftime('%H:%M:%S')
        weekday_lord = self.get_weekday_lord()
        nakshatra = self.calculate_nakshatra()
        lagna_info = self.get_lagna_info()
        # lagna_degree = lagna_info["Ascendant Degree"]
        # lagna_sign = lagna_info["Zodiac Sign"]
        print(f"\nDate: {self.date}")
        print(f"Sunrise: {sun_rise}")
        print(f"Sunset: {sun_set}")
        print(f"Current Time: {self.date_time.strftime('%H:%M:%S')}")
        print(f"Timezone: {self.timezone.zone}")

        print(f"\nWeekday Lord: {weekday_lord}")
        print(f"Nakshatra: {nakshatra}")
        print(f"Tithi: {getattr(self, 'tithi', 'Not calculated')}")
        print(f"Current Ascendant (Lagna): {lagna_info['Zodiac Sign']} at {lagna_info['Ascendant Degree']:.2f}°")
    
    def get_moon_rise_set(self, date=None):
        # If no date is provided, use the current date
        if date is None:
            date = datetime.now()

        # Use the LocationInfo object's observer to calculate moonrise and moonset
        observer = self.location.observer

        # # Calculate moonrise and moonset times
        # moonrise_time = observer.moonrise(date)
        # moonset_time = observer.moonset(date)

        return observer

# Example Run
if __name__ == "__main__":
    now = datetime.now(pytz.timezone('Europe/Helsinki'))
    unix_timestamp = int(now.timestamp())

    latitude = 65.0121
    longitude = 25.4651
    timezone = "Europe/Helsinki"
    city_name = "Rovaniemi"

    jyotish_engine = JyotishEngine(city_name, unix_timestamp, latitude, longitude, timezone)
    jyotish_engine.display_schedule()
    jyotish_engine.get_current_hora()
    jyotish_engine.show_summary()
    jyotish_engine.get_tithi()
    jyotish_engine.get_starting_planet()
    jyotish_engine.get_weekday_lord()
    jyotish_engine.get_lagna_info() 
    # JyotishEngine.get_moon_rise_set()
    
    moon_calculator = JyotishEngine(city_name='New Delhi', unix_timestamp=unix_timestamp,  latitude=28.7041, longitude=77.1025)
    moonset_time = moon_calculator.get_moon_rise_set()

    # Print the results
    # print(f"Moonrise Time: {moonrise_time}")
    print(f"Moonset Time: {moonset_time}")