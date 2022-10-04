from tkinter import *
import random
from tkinter import messagebox
from tkinter import constants

root=Tk()
root.title('Cricket')
root.geometry('862x580')
root.configure(background="green")
root.resizable(width=False, height=False)



inings=Entry(root,bg="black", font=("bold", 16), fg='green', width=10, justify=CENTER)
inings.grid(row=7,column=1,columnspan=2, pady=(50,0),)
OVER=Entry(root,bg="black", font=("bold", 16), fg='green', width=10, justify=CENTER)
OVER.grid(row=7,column=0,columnspan=1, pady=(50,0),)
BALL=Entry(root,bg="black", font=("bold", 16), fg='green', width=10, justify=CENTER)
BALL.grid(row=7,column=3,columnspan=1, pady=(50,0),)
OVER.insert(0,int(1))
BALL.insert(0, int(0))

#function

def new():
    ai_e.delete(0,END)
    u_e.delete(0,END)
    inings.delete(0,END)
    t_box.delete(0,END)
    s_box.delete(0,END)
    BALL.delete(0, END)
    BALL.insert(0, int(0))

def submit():
    totalover=((int(OVER.get())*6)+1)
    hit=u_e.get()
    if int(hit) == 0 or int(hit) == 1 or int(hit) == 2 or int(hit) == 3 or int(hit) == 4 or int(hit) == 5 or int(hit) == 6:
        ai_e.delete(0,END)
        totalball=int(BALL.get())
        BALL.delete(0, END)
        BALL.insert(0, int(totalball+1))
        totalball=int(BALL.get())
        value = random.randint(0,6)
        ai_e.insert(0, value)

        if int(totalover)==int(totalball):
            BALL.delete(0, END)
            BALL.insert(0, int(1))
            out=str(inings.get())+"OUT"
            inings.delete(0,END)
            inings.insert(0, out)
            s_box.insert(0, 0)
            target=(int(s_box.get())+1)
            t_box.delete(0,END)
            t_box.insert(0,target)
            s_box.delete(0,END)

        if int(hit) == int(ai_e.get()):
            BALL.delete(0, END)
            BALL.insert(0, int(0))
            out=str(inings.get())+"OUT"
            inings.delete(0,END)
            inings.insert(0, out)
            s_box.insert(0, 0)
            global scores
            global tergets
            scores =s_box.get()
            tergets = t_box.get()
            target=(int(s_box.get())+1)
            t_box.delete(0,END)
            t_box.insert(0,target)
            s_box.delete(0,END)

        if str(inings.get()) == "OUTOUT":
            win_by = (((int(tergets))-1) - (int(scores)))
            t_box.delete(0,END)
            t_box.insert(0,"You Win!")
            s_box.delete(0,END)
            s_box.insert(0,"You Win!")
            ai_e.insert(0,"You Win!")
            u_e.insert(0,"You Win!")
            box3=messagebox.askquestion("You Win!", f'Congratulation \nYou won by = {str(win_by)}runs\nDo you want to start another game?')

            if box3 == 'yes':
                ai_e.delete(0,END)
                u_e.delete(0,END)
                inings.delete(0,END)
                t_box.delete(0,END)
                s_box.delete(0,END)
                BALL.delete(0, END)
                BALL.insert(0, int(0))

            elif box3 == 'no':
                root.destroy()
                return

        if str(inings.get()) == "OUTOUTOUT":
            win_by = (((int(tergets))-1) - (int(scores)))
            t_box.delete(0,END)
            t_box.insert(0,"You Win!")
            s_box.delete(0,END)
            s_box.insert(0,"You Win!")
            ai_e.insert(0,"You Win!")
            u_e.insert(0,"You Win!")
            box3=messagebox.askquestion("You Win!", f'Congratulation \nYou won by = {str(win_by)}runs\nDo you want to start another game?')

            if box3 == 'yes':
                ai_e.delete(0,END)
                u_e.delete(0,END)
                inings.delete(0,END)
                t_box.delete(0,END)
                s_box.delete(0,END)
                BALL.delete(0, END)
                BALL.insert(0, int(0))

            elif box3 == 'no':
                root.destroy()
                return
            

        elif int(hit) != int(ai_e.get()):
            if str(inings.get()) == "OUT":
                s_box.insert(0, 0)
                score= int(s_box.get())+int(ai_e.get())
                s_box.delete(0,END)
                s_box.insert(0, score)
                if str(t_box.get()) != "" and str(s_box.get()) != "":
                    if int(s_box.get()) >= int(t_box.get()):
                        scores =s_box.get()
                        terget = t_box.get()
                        win_by = (int(scores)) - (int(terget))
                        s_box.delete(0,END)
                        t_box.delete(0, END)
                        t_box.insert(0, "You Lose!")
                        s_box.insert(0, "You Lose!")
                        ai_e.insert(0, "You Lose!")
                        u_e.insert(0, "You Lose!")
                        box3=messagebox.askquestion("You Lose", '\nopposition score= '+ str(score) +'\nDo you want to start a new game?')
                        if box3 == 'yes':
                            ai_e.delete(0,END)
                            u_e.delete(0,END)
                            inings.delete(0,END)
                            t_box.delete(0,END)
                            s_box.delete(0,END)
                            BALL.delete(0, END)
                            BALL.insert(0, int(0))
                        elif box3 == 'no':
                            root.destroy()
                            return


            elif str(inings.get()) == "":
                s_box.insert(0, 0)
                score= int(s_box.get())+int(hit)
                s_box.delete(0,END)
                s_box.insert(0, score)
            






    else:
        u_e.delete(0,END)
        u_e.insert(0,"--INVLAID NUMBER--")

            
                



#body
#title image and ai image
img_l=Label(root,font=("bold", 30), text='CRICKET', bg="green").grid(row=1,column=0,columnspan=4, pady=(30,0), padx=(342,342))
ai_l=Label(root, text="AI", bg="green",font=("bold",18)).grid(row=2,column=0,columnspan=4, pady=(40,0), padx=(342,342))
#ai input box
ai_e=Entry(root, bg="black", font=("bold", 16), fg='green', width=30, justify=CENTER)
ai_e.grid(row=3,column=0,columnspan=4, pady=(10,0), padx=(0,0), ipady=10)
#score bpx
s_box=Entry(root, bg="black", font=("bold", 16), fg='green', width=14, justify=CENTER)
s_box.grid(row=4,column=0, pady=(10,0), padx=(80,0), ipady=10)
s_l=Label(root,text=": SCORE", bg="black", fg="green", font="bold").grid(row=4,column=1, pady=(10,0), padx=(0,0), ipadx=5)
#total box
t_l=Label(root,text="TARGET :", bg="black", fg="green", font="bold").grid(row=4,column=2, pady=(10,0), padx=(0,0), ipadx=5)
t_box=Entry(root, bg="black", font=("bold", 16), fg='green', width=14, justify=CENTER)
t_box.grid(row=4,column=3, pady=(10,0), ipady=10, padx=(0,80))
#User input box and button
u_e=Entry(root, bg="black", font=("bold", 16), fg='green', width=30, justify=CENTER)
u_e.grid(row=5,column=0,columnspan=4, pady=(10,0), padx=(0,0), ipady=10)
u_b=Button(root,text="YOU", font = "bold", bg='green', fg='black', width=7, command=submit).grid(row=6,column=0,columnspan=4, pady=(10,0), padx=(342,342))
newgame=Button(root,text="NEW GAME", font = "bold", bg='green', fg='black', width=12, command=new).grid(row=8,column=1,columnspan=2, pady=(10,0), )
OVERBUTTON=Button(root,text="  OVER  ", font = "bold", bg='green', fg='black', width=12).grid(row=8,column=0,columnspan=1, pady=(10,0),)
BALLBUTTON=Button(root,text="TOTAL BALL", font = "bold", bg='green', fg='black', width=12).grid(row=8,column=3,columnspan=1, pady=(10,0),)

#runing mainloop
root.mainloop()
