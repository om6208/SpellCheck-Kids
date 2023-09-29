from tkinter import *
from textblob import TextBlob
from PIL import ImageTk, Image  

def check_spelling():
    a=TextBlob(spell_check.get())
    spell=Label(window, text="The correct spelling is : ", font=("Arial", 30, "bold"), bg="gray")
    spell.pack()
    correct_text=Label(window, text=str(a.correct()), font=("Arial",45,"bold"), bg="lightpink")
    correct_text.pack()

window=Tk()
window.title("My spelling checker")
window.geometry("800x600")
# window.config(background="lightgreen")
img =Image.open('img-2.jpg')
bg = ImageTk.PhotoImage(img)

# app.geometry("650x450")

# Add image
label = Label(window, image=bg)
label.place(x = 0,y = 0)

text_heading=Label(window, text="Spelling Checker", font=("Arial", 50, "bold"),bg="#FFFFFF", fg="#8EC8DF")
text_heading.pack()

text_check=Label(window, text="Enter the spelling", font=("Arial", 35, "bold"), bg="#FFFFFF", fg="lightpink")
text_check.pack()

spell_check=Entry(window, font=("Arial", 45, "bold"),width=500, bg="lightblue")
spell_check.pack()

check_button=Button(window, text="Check!!", font=("Arial", 30, "bold") ,fg="white", bg="red", command=check_spelling)
check_button.pack()

window.mainloop()