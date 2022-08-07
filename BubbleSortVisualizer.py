from tkinter import *  # graphic library
import random  # random library
import time  # time library

win = Tk()
win.geometry("1500x1000")  # window size
c = Canvas(win, width=1500, height=1000, bg="black")  # canvas settings
c.pack()

lst = []  # values list
linelst = []  # graphic lines list

for i in range(0, 300):  # list definition
    lst.append(i)  # list[i] = i

random.shuffle(lst)  # shuffle the list
size = 2  # size of rectangle
for i in range(0,
               len(lst)):  # graphing the list, win.winfo_screenheight() is to flip the object on screen so 0 is bottom
    linelst.append(c.create_rectangle(i * size, win.winfo_screenheight() - 0, i * size + size,
                                      win.winfo_screenheight() - lst[i] * size, fill="white"))

b = 0
a = len(lst) - 1


def sort():  # sorting function
    global a, b, lst, linelst
    if a > 0:  # check if we got to end of list
        c.itemconfig(linelst[b], fill="white")  # change color of rec[b] to white
        c.itemconfig(linelst[b + 1], fill="white")
        if lst[b] > lst[b + 1]:  # check if we need to flip values
            save_num = lst[b + 1]  # so we can then set lst[b]
            lst[b + 1] = lst[b]
            lst[b] = save_num

            c.move(linelst[b], size, 0)  # move the line on canvas (object, x movement, y movement)
            c.move(linelst[b + 1], -size, 0)

            save_line = linelst[b + 1]  # same as we did for the values list
            linelst[b + 1] = linelst[b]
            linelst[b] = save_line

        if b < a - 1:
            b += 1  # increment 'b': so we can check the next pair
        elif b == a - 1:  # decrement 'a': an iteration of 'a' assures the biggest value is sorted
            a -= 1
            b = 0

        c.itemconfig(linelst[b], fill="red")  # change color of rec[b] to red
        c.itemconfig(linelst[b + 1], fill="red")
        win.after(1, sort)  # recall sort again for the next frame with delay of 1 millisecond


sort()  # call the sort() function

win.mainloop()
