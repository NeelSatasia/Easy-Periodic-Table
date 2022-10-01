from tkinter import *

window = Tk()
window.geometry("600x600")
window.title('Workout Planner')

add_workout_btn = Button(text='Add Workout', width=20, height=2)
add_workout_btn.grid(row=0, column=0)

remove_workout_btn = Button(text='Remove Workout', width=20, height=2)
remove_workout_btn.grid(row=1, column=0)

modify_workout_btn = Button(text='Modify Workout', width=20, height=2)
modify_workout_btn.grid(row=2, column=0)

history_workout_btn = Button(text='History', width=20, height=2)
history_workout_btn.grid(row=3, column=0)

window.mainloop()
