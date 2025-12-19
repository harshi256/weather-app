
import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "8ec73b180fe3c393c340185e0e92a0aa"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        messagebox.showerror("Error", "City not found")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"].title()

    result_label.config(
        text=f"🌍 City: {city}\n\n"
             f"🌡 Temperature: {temp} °C\n"
             f"💧 Humidity: {humidity}%\n"
             f"☁ Condition: {condition}"
    )

# ---------- GUI ----------
app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")
app.configure(bg="#1e1e2f")

title = tk.Label(app, text="Weather App", font=("Arial", 22, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=15)

city_entry = tk.Entry(app, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

search_btn = tk.Button(app, text="Get Weather", font=("Arial", 14), bg="#4CAF50", fg="white", command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(app, font=("Arial", 14), bg="#1e1e2f", fg="white", justify="center")
result_label.pack(pady=20)

app.mainloop()
