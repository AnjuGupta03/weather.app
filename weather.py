import tkinter as tk
from tkinter import ttk,Button
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9866db48289acc6e57daa46ae07aa8c5").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])






win = tk.Tk()
win.title("WA")
win.config(bg="blue")
win.geometry("500x570")

name_label = tk.Label(win, text="WA Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

list_name = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
             "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
             "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
             "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
             "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
             "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
             "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
             "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]


city_name = tk.StringVar()
comm = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20, "bold"),textvariable=city_name)
comm.place(x=25, y=120, height=50, width=450)



w_label = tk.Label(win, text="Weather Climate", font=("Times New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = tk.Label(win, text="t", font=("Times New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)


wb_label = tk.Label(win, text="Weather Description", font=("Times New Roman", 20))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = tk.Label(win, text="", font=("Times New Roman", 20))
wb_label1.place(x=250, y=330, height=50, width=210)



temp_label = tk.Label(win, text="Temperature", font=("Times New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = tk.Label(win, text="", font=("Times New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)


per_label = tk.Label(win, text="Pressure", font=("Times New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = tk.Label(win, text="", font=("Times New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("Times New Roman", 30, "bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


win.mainloop()
