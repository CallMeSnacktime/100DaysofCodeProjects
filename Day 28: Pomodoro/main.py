from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global REPS

    REPS=0
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Title", fg=GREEN)
    tracker.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global REPS
    REPS +=1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    # Determine which countdown you're on
    if REPS%2 != 0:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)
    elif REPS % 8  == 0:
        countdown(long_sec)
        title.config(text="Break", fg=RED)
    elif REPS %2 ==0:
        countdown(short_sec)
        title.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec= "0"+ str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count-1)
    else:
        start_time()
        if REPS %2 ==0:
            tracker.config(text=tracker["text"]+"✓")

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# Canvas
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101,112,image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Label
title = Label(text="Timer",fg=GREEN , font=(FONT_NAME,40,"bold"), bg=YELLOW)
title.grid(column=1, row=0)

tracker = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,40,"bold"),)
tracker.grid(column=1, row=3)


# Buttons
start_button = Button(text="Start", bg=YELLOW, pady=10, highlightthickness=0, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, pady=10, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()