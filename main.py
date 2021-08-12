# It's a simple typing speed testing Gui app made by me with Love and Power of coffee.
# Go ahead and execute this code...Timer will start as soon as you start typing.

import math
from tkinter import *
import random
from threading import Timer
from timeit import default_timer as timer

COUNTDOWN_TIME = 1
FONT_NAME = "Courier"

text_paras = [
    "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They can also"
    " be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where"
    " the audio is difficult to hear or is intentionally muted.",

    "Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature mind,"
    " reading is the greatest source of pleasure and solace to distressed minds. The study of good books ennobles us"
    " and broadens our outlook.",

    "this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods"
    " or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of"
    " run on sentences this should help you get faster at typing."
]

random_text = random.choice(text_paras)
random_text_list = random_text.split()


def get_input():
    global starting_time, label

    end_timer = timer()
    total_time = round((end_timer - starting_time - 4), 2) / 60

    user_text = input_box.get('1.0', 'end-1c')
    user_text_list = user_text.split()

    comparing_list = random_text_list[: len(user_text_list)]

    errors_list = [error for error in user_text_list if error not in comparing_list]
    errors_count = len(errors_list)

    wpm = round((len(user_text)/5 - errors_count) / total_time)
    results = f"Congratulations\n Wpm: {wpm}\n Errors: {errors_count}"

    label.config(fg="red", text=results)
    label.pack()


def start_timer(event):
    threading_timer = Timer(60.0, get_input)
    threading_timer.start()
    count_down(1*60)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)


# Configuring GUI
window = Tk()
window.title('Typing Speed Meter')
window.config(bg="#334756", width=1000, height=600, padx=30, pady=30)

canvas = Canvas()
canvas.config(bg="#2C394B", highlightthickness=0, width=900, height=500)
canvas.create_text((450, 130), width=880, text=random_text, font=(FONT_NAME, 20, "bold"), fill="#FDEFEF")

input_box = Text(height=5, width=60, font=(FONT_NAME, 15, "bold"))
canvas.create_window((450, 350), window=input_box)
input_box.bind("<Button-1>", start_timer)

timer_text = canvas.create_text(50, 20, text="00:00", fill="#FF4848", font=(FONT_NAME, 20, "bold"))
canvas.pack()

submit_button = Button(text="Submit", bg="#FFF338", fg="#003638", height=2, width=7, highlightthickness=0, command=get_input)
submit_button.pack(pady=(15, 0))

label = Label(fg="red", text="", font=(FONT_NAME, 20, "bold"))

starting_time = timer()

window.mainloop()
