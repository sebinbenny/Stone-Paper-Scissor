from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("300x230")
root.iconbitmap('D:/Programing/PYTHON/GUI/Images/sps.ico')
root.title("Stone-Paper-Scissor")
root.configure(background="cornsilk3")


def mach_counter_check(mach_counter, user_counter):
    if mach_counter == 5 and user_counter < 5:
        machine_score = Label(root, text=mach_counter, bg="cornsilk3", fg="red3")
        machine_score.place(x=255, y=180)
        messagebox.showinfo("OOPS!!", "Machine Won. Better Luck next time. \U0001F62A")
        exit()


def user_counter_check(mach_counter, user_counter):
    if mach_counter < 5 and user_counter == 5:
        user_score = Label(root, text=user_counter, bg="cornsilk3", fg="red3")
        user_score.place(x=70, y=180)
        messagebox.showinfo("WINNER", "Winner winner, Chicken dinner!! \U0001F917")
        exit()


def refresh_com_Entry():
    com_Entry.configure(text="The Machine made its choice.")


def play():
    user_op = user_option_combo.get()
    if user_op == '--Select--':
        messagebox.showinfo("Warning", "You should select a valid option.")
    else:
        machine_op = random.choice(["Stone", "Paper", "Scissor"])
        global mach_counter, user_counter, machine_score, user_score, com_Entry
        if user_op == "Stone" and machine_op == "Paper":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op +
                                    ". Machine Wins.")
            mach_counter += 1
            mach_counter_check(mach_counter, user_counter)
            machine_score = Label(root, text=mach_counter, bg="cornsilk3", fg="red3")
            machine_score.place(x=255, y=180)
            com_Entry.configure(text="The Machine is thinking.")
            com_Entry.after(1000, refresh_com_Entry)
        elif user_op == "Stone" and machine_op == "Scissor":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op + ". You Won.")
            user_counter += 1
            user_counter_check(mach_counter, user_counter)
            user_score = Label(root, text=user_counter, bg="cornsilk3", fg="red3")
            user_score.place(x=70, y=180)
            com_Entry.configure(text="The Machine is thinking.")
            com_Entry.after(1000, refresh_com_Entry)
        elif user_op == "Stone" and machine_op == "Stone":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op + ". Stalemate.")
        elif user_op == "Paper" and machine_op == "Paper":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op + ". Stalemate.")
        elif user_op == "Paper" and machine_op == "Scissor":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op +
                                    ". Machine Wins.")
            mach_counter += 1
            mach_counter_check(mach_counter, user_counter)
            machine_score = Label(root, text=mach_counter, bg="cornsilk3", fg="red3")
            machine_score.place(x=255, y=180)
            com_Entry.configure(text="The Machine is thinking.")
            com_Entry.after(1000, refresh_com_Entry)
        elif user_op == "Paper" and machine_op == "Stone":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op + ". You Won.")
            user_counter += 1
            user_counter_check(mach_counter, user_counter)
            user_score = Label(root, text=user_counter, bg="cornsilk3", fg="red3")
            user_score.place(x=70, y=180)
            com_Entry.configure(text="The Machine is thinking.")
            com_Entry.after(1000, refresh_com_Entry)
        elif user_op == "Scissor" and machine_op == "Scissor":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op + ". Stalemate.")
        elif user_op == "Scissor" and machine_op == "Paper":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op + ". You Won.")
            user_counter += 1
            user_counter_check(mach_counter, user_counter)
            user_score = Label(root, text=user_counter, bg="cornsilk3", fg="red3")
            user_score.place(x=70, y=180)
            com_Entry.configure(text="The Machine is thinking.")
            com_Entry.after(1000, refresh_com_Entry)
        elif user_op == "Scissor" and machine_op == "Stone":
            messagebox.showinfo("Round Result", "Machine chose " + machine_op + " and you choose " + user_op +
                                    ". Machine Wins.")
            mach_counter += 1
            mach_counter_check(mach_counter, user_counter)
            machine_score = Label(root, text=mach_counter, bg="cornsilk3", fg="red3")
            machine_score.place(x=255, y=180)
            com_Entry.configure(text="The Machine is thinking.")
            com_Entry.after(1000, refresh_com_Entry)


mach_counter, user_counter = 0, 0
head = Label(root, text="STONE-PAPER-SCISSOR GAME", width=29, font=('Helvetica 13 bold'),
             bg="cornsilk3", fg="blue4")
com_Entry = Label(root, text="The Machine is thinking.", bg="cornsilk3", fg="purple", font=('Helvetica 10'))
com_Entry.after(1000, refresh_com_Entry)
user_Entry = Label(root, text="Choose your entry :", bg="cornsilk3", fg="medium blue", font=('Helvetica 9'))
user_option_combo = ttk.Combobox(root, values=["--Select--", "Stone", "Paper", "Scissor"])
user_option_combo.current(0)
play = Button(root, text="Play", command=play, bg="cornsilk3", borderwidth=3, relief="sunken", fg="Black")
user = Label(root, text="USER : ", bg="cornsilk3", fg="medium blue")
user_score = Label(root, text=user_counter, bg="cornsilk3", fg="red3")
machine = Label(root, text="COMPUTER : ", bg="cornsilk3", fg="medium blue")
machine_score = Label(root, text=mach_counter, bg="cornsilk3", fg="red3")


head.grid(row=0, column=1, pady=10)
com_Entry.grid(row=1, column=1, pady=10)
user_Entry.place(x=20, y=90)
user_option_combo.place(x=130, y=90)
play.place(x=130, y=130)
user.place(x=30, y=180)
user_score.place(x=70, y=180)
machine.place(x=180, y=180)
machine_score.place(x=255, y=180)


mainloop()
