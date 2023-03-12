from tkinter import *
import requests
import json
from datetime import datetime
import pandas as pd
 
 
root =Tk()
root.geometry("800x500") 
root.resizable(0,0) 
root.title("Vreme")

datum = StringVar()
ura = StringVar()

 
def showWeather():

    df = pd.read_csv("data/processed/obdelani.csv", sep=",", header=0)
    df = df.drop(['pm10'], axis=1)
    df = df.drop(['Unnamed: 0'], axis=1)

    datum_izb=datum.get()+" "+ura.get()+":00:00"

    df = df.loc[df['date'] == datum_izb]


    if(len(df.index)==1):

        df = df.drop(['date'], axis=1)

        zadnji = df.iloc[-1].to_dict()

        zadnji["pm25"] = zadnji["pm2.5"]
        del zadnji["pm2.5"]

        tfield1.delete("1.0", "end")   #to clear the text field for every new output
        tfield1.tag_configure("tag_name", justify='center')
        tfield1.insert(INSERT, zadnji["pm25"])   #to insert or send value in our Text Field to display output
        tfield1.tag_add("tag_name", "1.0", "end")

        tfield2.delete("1.0", "end")   #to clear the text field for every new output
        tfield2.tag_configure("tag_name", justify='center')
        tfield2.insert(INSERT, zadnji["o3"])   #to insert or send value in our Text Field to display output
        tfield2.tag_add("tag_name", "1.0", "end")

        tfield3.delete("1.0", "end")   #to clear the text field for every new output
        tfield3.tag_configure("tag_name", justify='center')
        tfield3.insert(INSERT, zadnji["co"])   #to insert or send value in our Text Field to display output
        tfield3.tag_add("tag_name", "1.0", "end")

        tfield4.delete("1.0", "end")   #to clear the text field for every new output
        tfield4.tag_configure("tag_name", justify='center')
        tfield4.insert(INSERT, zadnji["no2"])   #to insert or send value in our Text Field to display output
        tfield4.tag_add("tag_name", "1.0", "end")

        tfield5.delete("1.0", "end")   #to clear the text field for every new output
        tfield5.tag_configure("tag_name", justify='center')
        tfield5.insert(INSERT, zadnji["temp"])   #to insert or send value in our Text Field to display output
        tfield5.tag_add("tag_name", "1.0", "end")

        tfield6.delete("1.0", "end")   #to clear the text field for every new output
        tfield6.tag_configure("tag_name", justify='center')
        tfield6.insert(INSERT, zadnji["dwpt"])   #to insert or send value in our Text Field to display output
        tfield6.tag_add("tag_name", "1.0", "end")

        tfield7.delete("1.0", "end")   #to clear the text field for every new output
        tfield7.tag_configure("tag_name", justify='center')
        tfield7.insert(INSERT, zadnji["rhum"])   #to insert or send value in our Text Field to display output
        tfield7.tag_add("tag_name", "1.0", "end")

        tfield8.delete("1.0", "end")   #to clear the text field for every new output
        tfield8.tag_configure("tag_name", justify='center')
        tfield8.insert(INSERT, zadnji["prcp"])   #to insert or send value in our Text Field to display output
        tfield8.tag_add("tag_name", "1.0", "end")

        tfield21.delete("1.0", "end")   #to clear the text field for every new output
        tfield21.tag_configure("tag_name", justify='center')
        tfield21.insert(INSERT, zadnji["snow"])   #to insert or send value in our Text Field to display output
        tfield21.tag_add("tag_name", "1.0", "end")

        tfield22.delete("1.0", "end")   #to clear the text field for every new output
        tfield22.tag_configure("tag_name", justify='center')
        tfield22.insert(INSERT, zadnji["wdir"])   #to insert or send value in our Text Field to display output
        tfield22.tag_add("tag_name", "1.0", "end")

        tfield23.delete("1.0", "end")   #to clear the text field for every new output
        tfield23.tag_configure("tag_name", justify='center')
        tfield23.insert(INSERT, zadnji["wspd"])   #to insert or send value in our Text Field to display output
        tfield23.tag_add("tag_name", "1.0", "end")

        tfield24.delete("1.0", "end")   #to clear the text field for every new output
        tfield24.tag_configure("tag_name", justify='center')
        tfield24.insert(INSERT, zadnji["wpgt"])   #to insert or send value in our Text Field to display output
        tfield24.tag_add("tag_name", "1.0", "end")

        tfield25.delete("1.0", "end")   #to clear the text field for every new output
        tfield25.tag_configure("tag_name", justify='center')
        tfield25.insert(INSERT, zadnji["pres"])   #to insert or send value in our Text Field to display output
        tfield25.tag_add("tag_name", "1.0", "end")

        tfield26.delete("1.0", "end")   #to clear the text field for every new output
        tfield26.tag_configure("tag_name", justify='center')
        tfield26.insert(INSERT, zadnji["tsun"])   #to insert or send value in our Text Field to display output
        tfield26.tag_add("tag_name", "1.0", "end")

        tfield27.delete("1.0", "end")   #to clear the text field for every new output
        tfield27.tag_configure("tag_name", justify='center')
        tfield27.insert(INSERT, zadnji["coco"])   #to insert or send value in our Text Field to display output
        tfield27.tag_add("tag_name", "1.0", "end")

    
        # API url
        weather_url = 'http://0.0.0.0:8085/air/predict'
    
        # Get the response from fetched url
        response = requests.post(weather_url, json=zadnji)
    
        # changing response from json to python readable 
        pm10 = response.json()["prediction"]
        pm10 = round(pm10, 2)

    
    
        tfield28.delete("1.0", "end")   #to clear the text field for every new output
        tfield28.tag_configure("tag_name", justify='center')
        tfield28.insert(INSERT, pm10)   #to insert or send value in our Text Field to display output
        tfield28.tag_add("tag_name", "1.0", "end")
    
    else:
        tfield1.delete("1.0", "end")
        tfield2.delete("1.0", "end")
        tfield3.delete("1.0", "end")
        tfield4.delete("1.0", "end")
        tfield5.delete("1.0", "end")
        tfield6.delete("1.0", "end")
        tfield7.delete("1.0", "end")
        tfield8.delete("1.0", "end")
        tfield21.delete("1.0", "end")
        tfield22.delete("1.0", "end")
        tfield23.delete("1.0", "end")
        tfield24.delete("1.0", "end")
        tfield25.delete("1.0", "end")
        tfield26.delete("1.0", "end")
        tfield27.delete("1.0", "end")
        tfield28.delete("1.0", "end")
        inp_datum.delete(0, END)
        inp_ura.delete(0, END)
        inp_datum.insert(END, 'Datum ni na voljo')
 
 
city_head= Label(root, text = 'Ljubljana Bežigrad', font = 'Arial 20 bold').pack(pady=10) #to generate label heading


frame3  =  Frame(root,  width=600,  height=  400, pady=10)
frame3.pack()

izbiraD= Label(frame3, text = 'Datum (YYYY-MM-DD):', font = 'Arial 14').grid(row=0,  column=0,  padx=5,  pady=5) 
izbiraU= Label(frame3, text = 'Ura (HH):', font = 'Arial 14').grid(row=0,  column=1,  padx=5,  pady=5) 

inp_datum = Entry(frame3, textvariable = datum,  width = 24, font='Arial 14 bold')
inp_datum.grid(row=1,  column=0,  padx=5,  pady=5)
inp_datum.insert(END, '2023-03-03')
inp_ura = Entry(frame3, textvariable = ura,  width = 24, font='Arial 14 bold')
inp_ura.grid(row=1,  column=1,  padx=5,  pady=5) 
inp_ura.insert(END, '14')

 
Button(root, command = showWeather, text = "Pridobi podatke", font="Arial 12 bold", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

frame  =  Frame(root,  width=600,  height=  400,  bg='dark green', pady=10)
frame.pack()

spacer1 = Label(root, text="")
spacer1.pack()

frame2  =  Frame(root,  width=600,  height=  400,  bg='dark green', pady=10)
frame2.pack()

 
info25 = Label(frame, text = "PM 2.5", font = 'arial 12 bold').grid(row=0,  column=0,  padx=5,  pady=5)
infoO3 = Label(frame, text = "O3", font = 'arial 12 bold').grid(row=0,  column=1,  padx=5,  pady=5)
infoCO = Label(frame, text = "CO", font = 'arial 12 bold').grid(row=0,  column=2,  padx=5,  pady=5)
infoNO2 = Label(frame, text = "NO2", font = 'arial 12 bold').grid(row=0,  column=3,  padx=5,  pady=5)
infoT = Label(frame, text = "Temp", font = 'arial 12 bold').grid(row=0,  column=4,  padx=5,  pady=5)
infoDWPT = Label(frame, text = "DWPT", font = 'arial 12 bold').grid(row=0,  column=5,  padx=5,  pady=5)
infoRHUM = Label(frame, text = "RHUM", font = 'arial 12 bold').grid(row=0,  column=6,  padx=5,  pady=5)
infoPRCP = Label(frame, text = "PRCP", font = 'arial 12 bold').grid(row=0,  column=7,  padx=5,  pady=5)

infoSNOW = Label(frame2, text = "SNOW", font = 'arial 12 bold').grid(row=0,  column=0,  padx=5,  pady=5)
infoWDIR = Label(frame2, text = "WDIR", font = 'arial 12 bold').grid(row=0,  column=1,  padx=5,  pady=5)
infoWSPD = Label(frame2, text = "WSPD", font = 'arial 12 bold').grid(row=0,  column=2,  padx=5,  pady=5)
infoWPGT = Label(frame2, text = "WPGT", font = 'arial 12 bold').grid(row=0,  column=3,  padx=5,  pady=5)
infoPRES = Label(frame2, text = "PRES", font = 'arial 12 bold').grid(row=0,  column=4,  padx=5,  pady=5)
infoTSUN = Label(frame2, text = "TSUN", font = 'arial 12 bold').grid(row=0,  column=5,  padx=5,  pady=5)
infoCOCO = Label(frame2, text = "COCO", font = 'arial 12 bold').grid(row=0,  column=6,  padx=5,  pady=5)
info10 = Label(frame2, text = "PM 10", font = 'arial 12 bold', fg='dark red').grid(row=0,  column=7,  padx=5,  pady=5)

print(frame.winfo_width)
 
tfield1 = Text(frame, width=10, height=2)
tfield1.grid(row=1,  column=0,  padx=5,  pady=5)
tfield2 = Text(frame, width=10, height=2)
tfield2.grid(row=1,  column=1,  padx=5,  pady=5)
tfield3 = Text(frame, width=10, height=2)
tfield3.grid(row=1,  column=2,  padx=5,  pady=5)
tfield4 = Text(frame, width=10, height=2)
tfield4.grid(row=1,  column=3,  padx=5,  pady=5)
tfield5 = Text(frame, width=10, height=2)
tfield5.grid(row=1,  column=4,  padx=5,  pady=5)
tfield6 = Text(frame, width=10, height=2)
tfield6.grid(row=1,  column=5,  padx=5,  pady=5)
tfield7 = Text(frame, width=10, height=2)
tfield7.grid(row=1,  column=6,  padx=5,  pady=5)
tfield8 = Text(frame, width=10, height=2)
tfield8.grid(row=1,  column=7,  padx=5,  pady=5)

tfield21 = Text(frame2, width=10, height=2)
tfield21.grid(row=1,  column=0,  padx=5,  pady=5)
tfield22 = Text(frame2, width=10, height=2)
tfield22.grid(row=1,  column=1,  padx=5,  pady=5)
tfield23 = Text(frame2, width=10, height=2)
tfield23.grid(row=1,  column=2,  padx=5,  pady=5)
tfield24 = Text(frame2, width=10, height=2)
tfield24.grid(row=1,  column=3,  padx=5,  pady=5)
tfield25 = Text(frame2, width=10, height=2)
tfield25.grid(row=1,  column=4,  padx=5,  pady=5)
tfield26 = Text(frame2, width=10, height=2)
tfield26.grid(row=1,  column=5,  padx=5,  pady=5)
tfield27 = Text(frame2, width=10, height=2)
tfield27.grid(row=1,  column=6,  padx=5,  pady=5)
tfield28 = Text(frame2, width=10, height=2)
tfield28.grid(row=1,  column=7,  padx=5,  pady=5)

root.mainloop()