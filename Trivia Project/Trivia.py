import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import pandas as pd

script_dir = Path(__file__).parent  

os.chdir(script_dir)

# Load the Excel file 
question_bank = Path("question_bank.xlsx")
dataframe = pd.read_excel(question_bank)

# Create a list of available categories
category_list = dataframe['Category'].unique()

# Create the root window
root = tk.Tk()
root.title("Trivia!")
root.geometry("600x500")

# Initialize the ttk button style 
style = ttk.Style()
style.configure("TButton",
                font=("Times New Roman", 14),
                background="lightblue",  
                foreground="black")

style.map("TButton",
          background=[("active", "lightblue")], 
          foreground=[("active", "darkblue")])


# Load and resize background image
image_path = "darkblue_lights.png"
image = Image.open(image_path)

background_image = ImageTk.PhotoImage(image.resize((600, 500))) 


# Create canvas to place the background image on root window
canvas = tk.Canvas(root, width=600, height=500)
canvas.place(x=0, y=0)  

canvas.create_image(0, 0, image=background_image, anchor="nw") 


# Initialize global variables
score = 0
current_question = 0
questions = []
category = None
category_selected=False 



# Function to clear all non-canvas widgets in the root window
def clear_widgets():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Widget) and widget != canvas:  
            widget.destroy()



# Function to exit and show the final score
def exit_and_show_score():
    global score 
    
    clear_widgets()

    ended_label=tk.Label(root, text="You have ended the quiz!", font=("Times New Roman", 14), fg="black")
    ended_label.pack(pady=20)

    score_label = tk.Label(root, text=f"Your final score is {score}/{len(questions)}", font=("Times New Roman", 14), fg="black")
    score_label.pack(pady=20)
    
    retake_button = ttk.Button(root, text="Retake Quiz", style="TButton", command=start_quiz)
    retake_button.pack(pady=10)
    
    exit_button = ttk.Button(root, text="Exit", style="TButton", command=root.quit)
    exit_button.pack(pady=10) 


#Function to confirm exit
def confirmation():

    clear_widgets()

    confirm=tk.Label(root, text="Are you sure you want to quit?", font=("Times New Roman", 14), fg="black")
    confirm.pack(pady=10)

    yes_button=ttk.Button(root, text="Yes", style="TButton", command=exit_and_show_score)
    yes_button.pack(pady=10)

    no_button=ttk.Button(root, text="No", style="TButton", command=continuing)
    no_button.pack(pady=10)


#Function that resumes the quiz
def continuing():

    if category_selected:
        ask_question()
    else:
        start_quiz()



# Function that starts the quiz
def start_quiz():
 
    global score, current_question, questions, category, category_selected
    
    clear_widgets()

    # Ask the user to select a category
    welcome_label=tk.Label(root, text='Welcome!', font=("Georgia", 20), fg="black")
    welcome_label.pack(pady=10) 

    category_label = tk.Label(root, text="Choose a category:", font=("Times New Roman", 18), fg="black")
    category_label.pack(pady=(10, 30))

    for cat in category_list:
        button = ttk.Button(root, text=cat, style="TButton", command=lambda c=cat: select_category(c))
        button.pack(pady=5)

        
    exit_button = ttk.Button(root, text="Exit", style="TButton", command=confirmation)
    exit_button.pack(pady=40)



# Function to handle category selection
def select_category(selected_category): 
    global category, category_selected, questions

    print(f"You have selected {selected_category}")
    category = selected_category
    category_selected=True
    clear_widgets()
    
    # Filter out questions based on selected category
    category_data = dataframe[dataframe['Category'] == category]
    questions = category_data.to_dict(orient='records')
    random.shuffle(questions)
 
    ask_question()


# Function to display question and options
def ask_question():
    global current_question

    if current_question >= len(questions):
        exit_and_show_score()
        return
    
    question = questions[current_question]
    clear_widgets()
    
    # Display the question
    question_label = tk.Label(root, text=question['Question'], font=("Times New Roman", 16), wraplength=500, fg="black")
    question_label.pack(pady=20)

    # Display the options
    options = [f"A. {question['Option A']}",
               f"B. {question['Option B']}",
               f"C. {question['Option C']}",
               f"D. {question['Option D']}"]

    
    # Create buttons for the options
    for option in options:
        option_button = ttk.Button(root, text=option, style="TButton",
                                  command=lambda o=option: check_answer(o))
        option_button.pack(pady=5)

    
    #Exit button to prematurely exit the quiz
    exit_button=ttk.Button (root, text="Exit quiz", style="TButton",
                           command=confirmation)
    exit_button.pack(pady=(40, 5))


# Function to check user's answer against correct answer
def check_answer(selected_option):
    global current_question, score

    question = questions[current_question]
    correct_answer = question['Correct Answer']
    
    if selected_option[0] == correct_answer:
        score += 1 
        feedback = "Correct!"
        feedback_color="green"
    else:
        feedback = f"Incorrect. You chose {selected_option[0]}. The correct answer was {correct_answer}."
        feedback_color="red"
    
    show_feedback(feedback, feedback_color)


    next_button = ttk.Button(root, text="Next Question", style="TButton", command=next_question)
    next_button.pack(pady=(20, 5)) 
   

# Function to display feedback after an answer
def show_feedback(feedback_text, feedback_color):
    feedback_label = tk.Label(root, text=feedback_text, font=("Times New Roman", 14), fg=feedback_color, bg="lightblue")
    feedback_label.pack(pady=10)
    

# Function to move on to the next question
def next_question():
    global current_question

    current_question += 1
    ask_question()
    

# Start the quiz when the program is run
start_quiz()

# Run the Tkinter event loop
root.mainloop()