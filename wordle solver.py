import tkinter as tk
import tkinter.font as tkFont

HEIGHT = 700
WIDTH = 700

def input_manager(letter1, letter2, letter3, letter4, letter5, pos1, pos2, pos3, pos4, pos5, wrong, tk):
    file = open("dictionary.txt")
    words = []
    for line in file:
        line = line.rstrip("\n")
        words.append(line)
    letters = []
    tupl1 = tuple_maker(letter1, pos1)
    tupl2 = tuple_maker(letter2, pos2)
    tupl3 = tuple_maker(letter3, pos3)
    tupl4 = tuple_maker(letter4, pos4)
    tupl5 = tuple_maker(letter5, pos5)
    letters = array_maker(tupl1, letters)
    letters = array_maker(tupl2, letters)
    letters = array_maker(tupl3, letters)
    letters = array_maker(tupl4, letters)
    letters = array_maker(tupl5, letters)
    words = word_trimmer(wrong, words)
    for tupl in letters: 
        words = search(tupl, words)
    new_words = formatter(words)
    words_var = tk.StringVar(value=new_words)
    label = tk.Listbox(lower_frame, listvariable=words_var, font = 15, selectmode = 'extended')
    label.place(relwidth=1, relheight=1)

def formatter(words):
    new_arr = []
    str = ''
    for i in range(len(words)):
        str += words[i]
        str += ' '
        if i % 5 == 0 and i != 0:
            new_arr.append(str)
            str = ''
    return new_arr

def search(letters, words):
    words_new = []
    if len(letters) == 1:
        for line in words:
            if letters[0] in line:
                words_new.append(line)
    if len(letters) == 2:
        for line in words:
            if letters[0] in line:
                if line.index(letters[0]) == letters[1]:
                    words_new.append(line)
    return words_new

def tuple_maker(letter, position):
    if len(letter) == 1 and len(position) == 1:
        tupl = (letter, int(position) - 1)
    elif len(letter) == 1 and len(position) == 0:
        tupl = (letter)
    elif len(letter) == 0:
        return None
    return tupl

def array_maker(tupl, array):
    if tupl is not None:
        array.append(tupl)
    return array

def word_trimmer(not_in_word, words):
    not_included = list(not_in_word)
    new_list = []
    for line in words:
        checking = True
        for letter in not_included:
            if letter in line:
                checking = False
        if checking == True:
            new_list.append(line)
    return new_list

root = tk.Tk()
root.title("Wordle Solver")
icon = tk.PhotoImage(file = 'wordle_icon.png')
root.iconphoto(True, icon)

title_style = tkFont.Font(size=30, family = 'Helvetica')
inst_style = tkFont.Font(size=13, family = 'Helvetica', weight='bold')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg ='Green')

canvas.create_text(700/2, 50, fill="White", text="Wordle Solver", font=title_style)
canvas.create_text(650/7, 130, fill="White", text="Enter letters here: ", font=inst_style)
canvas.create_text(650/7, 200, fill="White", text="Enter position of\nletter above here\n(blank if unknown):", font=inst_style)
canvas.create_text(650/7, 270, fill="White", text="Enter letters that are\nNOT in the word here: ", font=inst_style)

frame1 = tk.Frame(root, bg='white', bd=5)
frame1.place(relx=0.3, rely=0.15, relwidth=0.075, relheight=0.075, anchor='n')

frame2 = tk.Frame(root, bg='white', bd=5)
frame2.place(relx=0.4, rely=0.15, relwidth=0.075, relheight=0.075, anchor='n')

frame3 = tk.Frame(root, bg='white', bd=5)
frame3.place(relx=0.5, rely=0.15, relwidth=0.075, relheight=0.075, anchor='n')

frame4 = tk.Frame(root, bg='white', bd=5)
frame4.place(relx=0.6, rely=0.15, relwidth=0.075, relheight=0.075, anchor='n')

frame5 = tk.Frame(root, bg='white', bd=5)
frame5.place(relx=0.7, rely=0.15, relwidth=0.075, relheight=0.075, anchor='n')

frame6 = tk.Frame(root, bg='white', bd=5)
frame6.place(relx=0.3, rely=0.25, relwidth=0.075, relheight=0.075, anchor='n')

frame7 = tk.Frame(root, bg='white', bd=5)
frame7.place(relx=0.4, rely=0.25, relwidth=0.075, relheight=0.075, anchor='n')

frame8 = tk.Frame(root, bg='white', bd=5)
frame8.place(relx=0.5, rely=0.25, relwidth=0.075, relheight=0.075, anchor='n')

frame9 = tk.Frame(root, bg='white', bd=5)
frame9.place(relx=0.6, rely=0.25, relwidth=0.075, relheight=0.075, anchor='n')

frame10 = tk.Frame(root, bg='white', bd=5)
frame10.place(relx=0.7, rely=0.25, relwidth=0.075, relheight=0.075, anchor='n')

frame11 = tk.Frame(root, bg='white', bd=5)
frame11.place(relx=0.5, rely=0.35, relwidth=0.47, relheight=0.075, anchor='n')

letter1 = tk.Entry(frame1, font=40)
letter1.place(relwidth=1, relheight=1)

letter2 = tk.Entry(frame2, font=40)
letter2.place(relwidth=1, relheight=1)

letter3 = tk.Entry(frame3, font=40)
letter3.place(relwidth=1, relheight=1)

letter4 = tk.Entry(frame4, font=40)
letter4.place(relwidth=1, relheight=1)

letter5 = tk.Entry(frame5, font=40)
letter5.place(relwidth=1, relheight=1)

pos1 = tk.Entry(frame6, font=40)
pos1.place(relwidth=1, relheight=1)

pos2 = tk.Entry(frame7, font=40)
pos2.place(relwidth=1, relheight=1)

pos3 = tk.Entry(frame8, font=40)
pos3.place(relwidth=1, relheight=1)

pos4 = tk.Entry(frame9, font=40)
pos4.place(relwidth=1, relheight=1)

pos5 = tk.Entry(frame10, font=40)
pos5.place(relwidth=1, relheight=1)

wrong = tk.Entry(frame11, font=40)
wrong.place(relwidth=1, relheight=1)

button = tk.Button(text="Show\n Words!", font=40, command=lambda: input_manager(letter1.get(), letter2.get(), letter3.get(), letter4.get(), letter5.get(), \
                    pos1.get(), pos2.get(), pos3.get(), pos4.get(), pos5.get(), wrong.get(), tk))
button.place(relx=0.8, rely=0.2, relheight=0.15, relwidth = 0.15)

lower_frame = tk.Frame(root, bg='white', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.45, anchor='n')
canvas.pack()

root.mainloop()


