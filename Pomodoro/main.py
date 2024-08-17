from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    sart_label.config(text="Timer")
    check_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = 10
    short_break = 5
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break)
        sart_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

    elif REPS % 2 == 0:
        count_down(short_break)
        sart_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

    else:
        count_down(work_sec)
        sart_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec} ")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ""
        session = math.floor(REPS / 2)
        for _ in range(session):
            mark += "✔"

        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Focus Timer")
window.config(padx=100, pady=50, bg=YELLOW)

sart_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
sart_label.grid(column=1, row=0)

start_butt = Button(text="Start", command=start_timer, highlightthickness=0)
start_butt.grid(column=0, row=3)

check_label = Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=4)

reset_butt = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_butt.grid(column=2, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
