from tkinter import * 
from tkinter import filedialog 
import datetime as dt  
import time  
from playsound import playsound  

  
def alarm(setAlarmTimer,path):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        #currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:
            print("playing sound")  
            playsound(path)  
            break  
  
def getAlarmTime():  
    
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime,path)  

def browse_sound_file():
    global path 
    path = filedialog.askopenfilename(filetypes=[("Sound files", ".mp3;.wav")])
     
guiWindow = Tk()  
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("364x250")  
guiWindow.config(bg = "#87BDD8")  
guiWindow.resizable(width = False, height = False)  

timeFormat = Label(  
    guiWindow,  
    text = "Remember to set time in 24-hour format!",  
    fg = "white",  
    bg = "#36486B",  
    font = ("Arial", 15)  
    ).place(  
        x = 0,  
        y = 210   
        )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour   Min    Sec",  
    font = 60,  
    fg = "white",  
    bg = "#87BDD8"  
    ).place(  
        x = 180,  
        y = 10  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#034F84",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 5,  
        y = 50  
        )
label_sound = Label(guiWindow, text="Choose Sound File:").place(
    x=0,
    y=100
)

entry_sound = Entry(guiWindow, width=25).place(
    x=120,
    y=100
)

button_browse = Button(guiWindow, text="Browse", command=browse_sound_file).place(
    x=290,
    y=98
)
frame = Frame(guiWindow)
frame.place(x=180,y=47)

hour = StringVar(guiWindow)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(guiWindow)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(guiWindow)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
   

   
submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 110,  
        y = 150  
        )  
guiWindow.mainloop()