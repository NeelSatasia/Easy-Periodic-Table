from tkinter import *

window = Tk()
window.geometry("600x600")
window.title('Workout Planner')

main_frame = Frame(window)
main_frame.pack()

def goToAddWorkout():
    exercises = []

    add_workout_frame = Frame(main_frame)
    add_workout_frame.grid(row=0, column=1, padx=10)

    new_workout_canvas = Canvas(add_workout_frame)
    new_workout_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrllBar = Scrollbar(add_workout_frame, orient='vertical', command=new_workout_canvas.yview)
    scrllBar.pack(side='right', fill='y')

    new_workout_canvas.configure(yscrollcommand=scrllBar.set)
    new_workout_canvas.bind('<Configure>', lambda e: new_workout_canvas.configure(scrollregion=new_workout_canvas.bbox('all')))

    add_workout_frame_2 = Frame(new_workout_canvas)

    new_workout_canvas.create_window((0, 0), window=add_workout_frame_2, anchor='nw')

    workout_name_label = Label(master=add_workout_frame_2, text='Workout Name: ')
    workout_name_label.grid(row=0, column=0, columnspan=1)

    workout_name_entry = Entry(master=add_workout_frame_2, width=20)
    workout_name_entry.grid(row=0, column=1, columnspan=2)

    def add_exercise():
        exercise_name_entry = Entry(master=add_workout_frame_2, width=10)
        exercise_name_entry.grid(row=len(exercises) + 4, column=0, columnspan=1)

        reps_entry = Entry(master=add_workout_frame_2, width=5)
        reps_entry.grid(row=len(exercises) + 4, column=1, columnspan=1)

        sets_entry = Entry(master=add_workout_frame_2, width=5)
        sets_entry.grid(row=len(exercises) + 4, column=2, columnspan=1)

        exercises.append([])


    add_exercise_btn = Button(master=add_workout_frame_2, text='Add Exercise', command=add_exercise)
    add_exercise_btn.grid(row=1, column=0, columnspan=3, pady=5)

    save_workout_btn = Button(master=add_workout_frame_2, text='Save Workout')
    save_workout_btn.grid(row=2, column=0, columnspan=3, pady=2)

    exercise_name = Label(master=add_workout_frame_2, text='Exercises')
    exercise_name.grid(row=3, column=0, columnspan=1)

    reps = Label(master=add_workout_frame_2, text='Reps')
    reps.grid(row=3, column=1, columnspan=1)

    sets = Label(master=add_workout_frame_2, text='Sets')
    sets.grid(row=3, column=2, columnspan=1)

workout_btns_frame = Frame(main_frame)
workout_btns_frame.grid(row=0, column=0, sticky="N", pady=50)

add_workout_btn = Button(master=workout_btns_frame, text='Add Workout', width=20, height=2, command=goToAddWorkout)
add_workout_btn.grid(row=0, column=0)

remove_workout_btn = Button(master=workout_btns_frame, text='Remove Workout', width=20, height=2)
remove_workout_btn.grid(row=1, column=0)

modify_workout_btn = Button(master=workout_btns_frame, text='Modify Workout', width=20, height=2)
modify_workout_btn.grid(row=2, column=0)

history_workout_btn = Button(master=workout_btns_frame, text='History', width=20, height=2)
history_workout_btn.grid(row=3, column=0)

window.mainloop()
