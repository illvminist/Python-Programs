import tkinter as tk
from tkinter import ttk, messagebox
import ephem
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import pygame

# Initialize pygame for sound
pygame.mixer.init()

# Predefined list of cities for the dropdown
city_list = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
    'London', 'Tokyo', 'Paris', 'Berlin', 'Sydney', 
    'San Francisco', 'Miami', 'Las Vegas', 'Dallas', 'Boston'
]

# Zodiac signs and their personality traits
zodiac_traits = {
    'Aries': 'Adventurous, independent, energetic, confident.',
    'Taurus': 'Reliable, patient, determined, practical.',
    'Gemini': 'Curious, adaptable, outgoing, witty.',
    'Cancer': 'Compassionate, intuitive, protective, loyal.',
    'Leo': 'Generous, enthusiastic, warm-hearted, creative.',
    'Virgo': 'Analytical, diligent, practical, reliable.',
    'Libra': 'Charming, fair-minded, diplomatic, cooperative.',
    'Scorpio': 'Resourceful, determined, focused, passionate.',
    'Sagittarius': 'Optimistic, free-spirited, adventurous, curious.',
    'Capricorn': 'Responsible, disciplined, ambitious, practical.',
    'Aquarius': 'Innovative, original, humanitarian, independent.',
    'Pisces': 'Compassionate, artistic, empathetic, intuitive.'
}

# Predefined constellations and their meanings
constellations = {
    'Aries': "The Ram. Symbolizes courage, leadership, and new beginnings.",
    'Taurus': "The Bull. Represents stability, sensuality, and materialism.",
    'Gemini': "The Twins. Symbolizes duality, communication, and adaptability.",
    'Cancer': "The Crab. Represents emotional depth, protection, and intuition.",
    'Leo': "The Lion. Symbolizes creativity, leadership, and strength.",
    'Virgo': "The Virgin. Represents intellect, purity, and service.",
    'Libra': "The Scales. Symbolizes balance, harmony, and justice.",
    'Scorpio': "The Scorpion. Represents intensity, transformation, and mystery.",
    'Sagittarius': "The Archer. Symbolizes exploration, truth, and freedom.",
    'Capricorn': "The Goat. Represents ambition, discipline, and resilience.",
    'Aquarius': "The Water Bearer. Symbolizes originality, freedom, and idealism.",
    'Pisces': "The Fishes. Represents empathy, intuition, and artistic ability."
}

# Function to get coordinates from city
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="astrologyApp")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        messagebox.showerror("Location Error", f"Could not find coordinates for {city_name}.")
        return None, None

# Function to calculate birth chart based on input
def calculate_birth_chart():
    try:
        city = city_var.get()
        date = date_var.get()
        time = time_var.get()
        
        # Get coordinates for the city
        lat, lon = get_coordinates(city)
        if lat is None or lon is None:
            return
        
        # Parse date and time using ephem.Date()
        birth_date = ephem.Date(date + ' ' + time)
        
        # Convert ephem.Date to Python datetime for formatting
        birth_date_time = datetime.utcfromtimestamp(birth_date)
        
        # Create observer (the user) based on location
        observer = ephem.Observer()
        observer.lat = str(lat)
        observer.lon = str(lon)
        
        # Calculate planetary positions
        sun = ephem.Sun(birth_date)
        moon = ephem.Moon(birth_date)
        mercury = ephem.Mercury(birth_date)
        venus = ephem.Venus(birth_date)
        mars = ephem.Mars(birth_date)
        jupiter = ephem.Jupiter(birth_date)
        saturn = ephem.Saturn(birth_date)
        uranus = ephem.Uranus(birth_date)
        neptune = ephem.Neptune(birth_date)
        pluto = ephem.Pluto(birth_date)
        
        # Store planetary positions in a dictionary
        planets = {
            "Sun": sun,
            "Moon": moon,
            "Mercury": mercury,
            "Venus": venus,
            "Mars": mars,
            "Jupiter": jupiter,
            "Saturn": saturn,
            "Uranus": uranus,
            "Neptune": neptune,
            "Pluto": pluto
        }
        
        # Prepare chart plotting
        plot_chart(planets, birth_date_time)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to plot the astrological chart
def plot_chart(planets, birth_date_time):
    # Create a new figure for the chart
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Set circular aspect
    ax.set_aspect('equal')
    
    # Draw the circle (astrological wheel)
    circle = plt.Circle((0, 0), 1, color='orange', fill=False, linewidth=2)
    ax.add_artist(circle)
    
    # Draw lines for houses (12 sectors)
    for i in range(12):
        angle = np.deg2rad(30 * i)
        ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color='black', lw=1)
    
    # Plot the planets
    planet_colors = {'Sun': 'yellow', 'Moon': 'silver', 'Mercury': 'gray', 'Venus': 'green', 'Mars': 'red',
                     'Jupiter': 'blue', 'Saturn': 'brown', 'Uranus': 'cyan', 'Neptune': 'indigo', 'Pluto': 'purple'}
    
    for planet_name, planet in planets.items():
        angle = np.deg2rad(planet.ra * 180 / np.pi)  # Convert Right Ascension to angle
        ax.plot(np.cos(angle), np.sin(angle), 'o', color=planet_colors[planet_name], label=planet_name, markersize=8)
    
    # Labels for planets
    for planet_name, planet in planets.items():
        angle = np.deg2rad(planet.ra * 180 / np.pi)
        ax.text(np.cos(angle) * 1.1, np.sin(angle) * 1.1, planet_name, color=planet_colors[planet_name], fontsize=10)
    
    # Add zodiac sign labels
    zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    for i, sign in enumerate(zodiac_signs):
        angle = np.deg2rad(30 * i)
        ax.text(np.cos(angle) * 1.2, np.sin(angle) * 1.2, sign, color='black', fontsize=12, ha='center')
    
    # Set title
    ax.set_title(f"Astrological Birth Chart: {birth_date_time.strftime('%Y-%m-%d %H:%M:%S')}", fontsize=14)
    
    # Remove the axes
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Display the plot in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the zodiac traits and constellation meanings
    traits_label.config(text="Zodiac Traits:")
    for i, planet in enumerate(planets.values()):
        # Getting the constellation based on RA and Dec
        constellation = ephem.constellation(planet)
        constellation_name = constellation[1]
        if constellation_name in constellations:
            planet_trait_label = tk.Label(window, text=f"{planet.name}: {constellations[constellation_name]}")
            planet_trait_label.pack()

# Function to play sound
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=-1, start=0.0)

# Creating the main window
window = tk.Tk()
window.title("Astrology Birth Chart Generator")
window.geometry("800x700")
window.configure(bg='#1E1E1E')

# Play background music
play_sound('Music Is Math.mp3')

# Font Style
title_font = ('Helvetica', 18, 'bold')
label_font = ('Arial', 14)
button_font = ('Courier', 12, 'bold')

# Labels and Inputs
tk.Label(window, text="Enter Date of Birth (YYYY-MM-DD)", font=label_font, bg='#1E1E1E', fg='white').pack(pady=10)
date_var = tk.StringVar()
date_entry = tk.Entry(window, textvariable=date_var, font=label_font)
date_entry.pack(pady=10)

tk.Label(window, text="Enter Time of Birth (HH:MM:SS)", font=label_font, bg='#1E1E1E', fg='white').pack(pady=10)
time_var = tk.StringVar()
time_entry = tk.Entry(window, textvariable=time_var, font=label_font)
time_entry.pack(pady=10)

tk.Label(window, text="Select City", font=label_font, bg='#1E1E1E', fg='white').pack(pady=10)
city_var = tk.StringVar(value=city_list[0])
city_dropdown = tk.OptionMenu(window, city_var, *city_list)
city_dropdown.config(font=label_font)
city_dropdown.pack(pady=10)

# Button to generate birth chart
generate_button = tk.Button(window, text="Generate Birth Chart", command=calculate_birth_chart, font=button_font, bg='blue', fg='white')
generate_button.pack(pady=20)

# Label for showing the zodiac traits
traits_label = tk.Label(window, text="Zodiac Traits will appear here.", font=label_font, bg='#1E1E1E', fg='white')
traits_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
