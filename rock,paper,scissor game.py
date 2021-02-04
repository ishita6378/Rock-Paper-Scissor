from tkinter import *
import random

root = Tk()
computer_input = random.choice(["rock","paper","scissor"])
root.geometry("659x499")
user=[]
computer=[]
f1 = Frame(root,bg="Yellow",borderwidth=10)
f1.grid()
instruction_img = PhotoImage(file = r"C:\desktop folders\stone.png")
instruction_img_main = instruction_img.subsample(2,2)
instruction_label = Label(f1,image=instruction_img_main)
instruction_label.grid(row=1,column=1)

def rock():
    user_input="rock"
    computer_input = random.choice(["rock", "paper", "scissor"])
    if computer_input == "paper":
        a.set(f"you loose and computer choose {computer_input}")
        s1.update()
        computer.append(1)
        c_score.set(f"computer score - {str(sum(computer))}")
        s3.update()

    elif computer_input == "scissor":
        a.set(f"you win and computer choose {computer_input}")
        s1.update()
        user.append(1)
        u_score.set(f"user score - {str(sum(user))}")
        s2.update()
    else:
        a.set(f"equal and computer choose {computer_input}")
        s1.update()
def paper():
    user_input ="paper"
    computer_input = random.choice(["rock", "paper", "scissor"])
    if computer_input == "scissor":
        a.set(f"you loose and computer choose {computer_input}")
        s1.update()
        computer.append(1)
        c_score.set(f"computer score - {str(sum(computer))}")
        s3.update()
    elif computer_input == "rock":
        a.set(f"you win and computer choose {computer_input}")
        s1.update()
        user.append(1)
        u_score.set(f"user score - {str(sum(user))}")
        s2.update()
    else:
        a.set(f"equal and computer choose {computer_input}")
        s1.update()
def scissor():
    user_input="scissor"
    computer_input = random.choice(["rock", "paper", "scissor"])
    if computer_input == "paper":
        a.set(f"you win and computer choose {computer_input}")
        s1.update()
        user.append(1)
        u_score.set(f"user score - {str(sum(user))}")
        s2.update()
    elif computer_input == "rock":
        a.set(f"you loose and computer choose {computer_input}")
        s1.update()
        computer.append(1)
        c_score.set(f"computer score - {str(sum(computer))}")
        s3.update()
    else:
        a.set(f"equal and computer choose {computer_input}")
        s1.update()
L4=Label(f1,text="ROCK  PAPER  SCISSOR",fg="Black",bg="Yellow",font="Times 30 bold")
L4.grid(row=0,column=1)
img_rock = PhotoImage(file=r"C:\Users\ishit\Pictures\wallpapers\rock.png")
img_rock_main = img_rock.subsample(5,5)
b1 = Button(f1,text = "rock",command = rock,image=img_rock_main)
b1.grid(row=2,column=0)
img_paper = PhotoImage(file=r"C:\Users\ishit\Pictures\wallpapers\paper.png")
img_paper_main = img_paper.subsample(5,5)
b2 = Button(f1,text = "paper",command = paper,image=img_paper_main)
b2.grid(row=2,column=1)
img_scissor = PhotoImage(file=r"C:\Users\ishit\Pictures\wallpapers\scissor.png")
img_scissor_main = img_scissor.subsample(5,5)
b3 = Button(f1,text = "scissor",command = scissor,image=img_scissor_main)
b3.grid(row=2,column=2)
L1=Label(f1,text="RESULT",fg="Black")
L1.grid(row=4,column=0)
L2=Label(f1,text="USER SCORE",fg="Black")
L2.grid(row=5,column=0)
L3=Label(f1,text="COMPUTER SCORE",fg="Black")
L3.grid(row=6,column=0)
img_rock = PhotoImage(file=r"C:\Users\ishit\Pictures\wallpapers\rock.png")
img_rock_main = img_rock.subsample(5,5)
b1 = Button(f1,text = "rock",command = rock,image=img_rock_main)
b1.grid(row=2,column=0)
img_paper = PhotoImage(file=r"C:\Users\ishit\Pictures\wallpapers\paper.png")
img_paper_main = img_paper.subsample(5,5)
b2 = Button(f1,text = "paper",command = paper,image=img_paper_main)
b2.grid(row=2,column=1)
a=StringVar()
a.set("")
s1=Entry(f1,textvariable=a)
s1.grid(row=4,column=1,ipadx=100)
u_score=StringVar()
u_score.set(f"user score -{str(sum(user))}")
s2 = Entry(f1,textvariable = u_score)
s2.grid(row=5,column=1,ipadx=100)
s2.update()
c_score=StringVar()
c_score.set(f"computer score -{str(sum(computer))}")
s3 = Entry(f1,textvariable = c_score)
s3.grid(row=6,column=1,ipadx=100)
s3.update()
root.mainloop()