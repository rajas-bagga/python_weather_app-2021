import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_key = os.getenv("API_KEY")

def getWeather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        print(json)
        city = json["name"]
        country = json["sys"]["country"]

        temp = json["main"]["temp"] - 273.15
        format_temp = "{:.2f}".format(temp)
        format_temp = str(format_temp)
        icon = json["weather"][0]["icon"]
        weather = json["weather"][0]["main"]
        dis_weather = json["weather"][0]["description"]
        pressure = json["main"]["pressure"]


        return [city, country, format_temp, icon, weather, dis_weather, pressure]

    else:
        return False

def search(*args):
    city = entry_1.get()
    city = getWeather(city)

    if city == False:
        messagebox.showerror("Error", "No Such City")

    else:

        img = PhotoImage(file=f"icons\\{city[3]}.png")

        label_1.configure(text=f"Location: {city[0]}, {city[1]}")
        label_2.configure(text=f"Temperature: {city[2]} °C")
        label_3.configure(text=f"Weather: {city[4]}")
        label_4.configure(text=f"Description: {city[5]}")
        label_5.configure(text=f"Pressure: {city[6]}")
        label_6.configure(image=img, bg="#87CEEB")
        label_6.image = img




getWeather("Allahabad")


# img = ImageTk.PhotoImage(Image.open("icons\\01d.png"))

root = Tk()
root.title("Krishna's Weather App")
root.resizable(False, False)
# root.iconbitmap("C:\\Users\\91731\\Desktop\\projects\\weather.ico")

img = None
# PhotoImage(file="01d.png")

label = Label(text="Weather App", font="Consolas 35 bold", fg="blue").pack()

entry_1 = Entry(root, width=40, font="Consolas 20")
entry_1.pack(padx=20, pady=20)

imgage = PhotoImage(file=f"icons\\09d.png")

label_1 = Label(text="Location:", font="Calibiri 25")
label_2 = Label(text="Temperature:", font="Calibiri 25")
label_3 = Label(text="Weather:", font="Calibiri 25")
label_4 = Label(text="Discription:", font="Calibiri 25")
label_5 = Label(text="Pressure:", font="Calibiri 25")
label_6 = Label(root, image=None)

label_6.pack(padx=20, pady=(5, 10), expand="yes", fill="both")
label_1.pack(anchor=W, padx=20, pady=10)
label_2.pack(anchor=W, padx=20, pady=10)
label_3.pack(anchor=W, padx=20, pady=10)
label_4.pack(anchor=W, padx=20, pady=10)
label_5.pack(anchor=W, padx=20, pady=10)

style = ttk.Style()


style.configure('W.TButton', font=('Calibri', 20, 'bold'))

button = ttk.Button(text="Check Weather!", command=search, style="W.TButton").pack(padx=20, pady=10)

root.bind("<Return>", search)
root.mainloop()
