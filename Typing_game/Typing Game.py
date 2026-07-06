import tkinter as tk
import tkinter.ttk as ttk 
import random
import csv

def start_game():
    global username
    username = username_entry.get()
    if username:
        username_frame.pack_forget()  
        start_button.pack_forget()    
        score_label.pack()            
        lives_label.pack()            
        canvas.pack()                 
        new_letter()

def new_letter():
    global lives, letter
    if lives == 0:
        game_over()
        return

    alpha = random.choice("abcdefghijklmnopqrstuvwxyz")
    x = random.randint(60, 660)
    canvas.coords(letter, x, 10)
    canvas.itemconfig(letter, text=alpha, fill="white", font=("Copperplate Gothic Light", 24, "bold"))
    move_letter()

def move_letter():
    global lives
    if lives == 0:
        return

    canvas.move(letter, 0, 10)
    x, y = canvas.coords(letter)
    if y >= 710:
        lives -= 1
        lives_label.config(text="Lives: {}".format(lives))
        canvas.config(bg="#f72119")  
        screen.after(300, reset_canvas_color) 
        if lives == 0:
            game_over()
            return
        new_letter()
    else:
        screen.after(speed, move_letter)

def reset_canvas_color():
    canvas.config(bg="#1c1c1c")#Neon Red BG  

def check_input(event):
    global score
    if lives == 0:
        return

    typed_letter = event.char.lower() 
    falling_letter = canvas.itemcget(letter, "text") 
    if typed_letter == falling_letter:
        score += 10
        score_label.config(text="Score: {}".format(score))
        new_letter()

def game_over():
    canvas.delete("all")
    save_score(username, score)
    display_scoreboard()

def save_score(username, score):
    try: 
        with open('scores.csv', 'r') as file:
            pass
    except FileNotFoundError:
        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file) 
            writer.writerow(['Username', 'Score']) 
    
    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

def display_scoreboard():
    scoreboard_window = tk.Toplevel(screen) 
    scoreboard_window.title("Type Rush - Scoreboard") 

    #Label for scoreboard title
    title_label = tk.Label(scoreboard_window, text="Scoreboard", font=("Arial", 22))
    title_label.pack(pady=5)

    #Headings and rows of table
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 16))
    style.configure("Treeview", font=("Arial", 12), rowheight=50)

    # Frame for Treeview and scrollbar
    tree_frame = tk.Frame(scoreboard_window)
    tree_frame.pack(fill="both", expand=True) 

    # Creating  scrollbar
    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side="right", fill="y") 

    # Creating Treeview widget
    tree = ttk.Treeview(tree_frame, columns=("Username", "Score"), show="headings", yscrollcommand=tree_scroll.set) 
    tree_scroll.config(command=tree.yview) 

    # Column headings and alignments
    tree.heading("Username", text="Username")
    tree.heading("Score", text="Score")

    # Column details
    tree.column("Username", anchor=tk.CENTER, width=150)  
    tree.column("Score", anchor=tk.CENTER,width=100)     

    tree.pack(fill="both", expand=True) 

    with open('scores.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        scores = sorted(reader, key=lambda x: int(x[1]), reverse=True)  
        for user, score in scores:
            tree.insert("", "end", values=(user, score))

screen = tk.Tk()
screen.title("Type Rush")
screen.geometry("720x720")

username = ""
score = 0
lives = 3
speed = 500 #500 milliseconds

canvas = tk.Canvas(screen, bg="#1c1c1c", width=720, height=720) #Black BG
letter = canvas.create_text(200, 10, text="", font=("Copperplate Gothic Light", 24, "bold"), fill="white")#White text

score_label = tk.Label(screen, text="Score: 0", font=("Times New Roman", 16), fg="#0f52ba") #Blue fill
lives_label = tk.Label(screen, text="Lives: 3", font=("Times New Roman", 16), fg="#0f52ba") #Blue fill

username_frame = tk.Frame(screen) 
username_frame.pack(expand=True) 

username_sentence = tk.Label(username_frame, text="Enter Username", font=("Times New Roman", 14))
username_sentence.pack(pady=5) 

username_entry = tk.Entry(username_frame, font=("Times New Roman", 14))
username_entry.pack(pady=5)

start_button = tk.Button(username_frame, text="Start Game", command=start_game, font=("Times New Roman", 14))
start_button.pack(pady=5)

screen.bind("<Key>", check_input) 
screen.mainloop() 
