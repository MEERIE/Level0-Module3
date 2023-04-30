from tkinter import Tk, simpledialog, messagebox
if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    happy = simpledialog.askstring(title=None, prompt="Are You Happy!?")
    if happy == "yes":
        messagebox.showinfo(Title=None, message="GREAT, KEEP DOING WHAT YOU ARE DOING!")
    elif happy == "no":
        messagebox.showinfo(Title=None, message="not good")
    pass
