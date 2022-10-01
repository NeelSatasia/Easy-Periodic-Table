from tkinter import *

def initializeWindow():
    global window
    global history_labelFrame
    global scrollBar
    global canvas
    global secondFrame
    
    window = Tk()
    window.geometry("600x400")
    window.title("Workout Planner")
    
    history_labelFrame = LabelFrame(window, text="Workout History")
    history_labelFrame.pack(padx=8, pady=8, expand=True, fill=BOTH)
    
    canvas = Canvas(history_labelFrame)
    canvas.pack(side = LEFT, fill = BOTH, expand = True)
    
    scrollBar = Scrollbar(history_labelFrame, orient=VERTICAL, command=canvas.yview)
    scrollBar.pack(side = RIGHT, fill = Y)
    
    canvas.configure(yscrollcommand = scrollBar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    
    secondFrame = Frame(canvas)
    canvas.create_window((0,0), window=secondFrame, anchor="nw")

def populateHistory():
    workout_history = [ 
        {"exercises": [ ["Push Ups", 10, 3], ["1-Minute Plank", 5, 2]], "duration": 20, "date": "September 30, 2022"},
        {"exercises": [ ["Push Ups", 10, 5] ], "duration": 10, "date": "October 1, 2022"},
        {"exercises": [ ["Crunches", 20, 5], ["Crunches", 10, 5] ], "duration": 40, "date": "October 2, 2022"} 
        ]

    secondFrame.columnconfigure(0, weight=1)
    secondFrame.columnconfigure(1, weight=1)
    secondFrame.columnconfigure(2, weight=1)
    
    Label(secondFrame, text="Date").grid(row=0, column=0, sticky="EW")
    Label(secondFrame, text="Duration").grid(row=0, column=1, sticky="EW")
    Label(secondFrame, text="Exercises").grid(row=0, column=2, sticky="EW")
    
    i = 1
    for workout in workout_history:
        Label(secondFrame, text=workout["date"]).grid(row=i, column=0, padx=5, pady=5)
        Label(secondFrame, text=f"{workout['duration']} minutes").grid(row=i, column=1, padx=5, pady=5)
        
        exercises = ""
        for exercise in workout["exercises"]:
            exercises += f"{exercise[0]} (Reps: {exercise[1]}, Sets: {exercise[2]})\n"
        else:
            exercises = exercises[0:-1]

        exercisesLabel = Label(secondFrame, text=exercises)
        exercisesLabel.grid(row=i, column=2, padx=5)
        
        i += 1
    
    
initializeWindow()
populateHistory()
window.mainloop()
