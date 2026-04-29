import tkinter as tk
# tkinter is a free GUI toolkit built into Python, we use it to make windows and buttons

import json
# json lets us save and load our flashcards from a file

import os
# os lets us check if a file exists before we try to open it

import random
# random lets us shuffle the flashcard order so questions aren't always the same


window = tk.Tk()
# creates the main app window

window.title("Rozoom")
# sets the text shown in the title bar

window.geometry("400x520")
# sets the window size to 400 pixels wide and 520 pixels tall

title = tk.Label(window, text="Rozoom", font=("Arial", 18))
# creates a heading label with the app name in large text

title.pack(pady=20)
# places the heading on screen with a gap above and below it

status_label = tk.Label(window, text="", font=("Arial", 10), wraplength=350)
# creates a message label that shows feedback like "Correct!" or "Wrong."
# wraplength=350 makes long messages wrap onto a new line instead of going off screen

status_label.pack(pady=5)
# places the status label on screen


selected_category = None
# stores whichever category the user picks, starts as None meaning nothing chosen yet

current_answer = ""
# stores the correct answer for whatever question is currently showing

score = 0
# counts how many questions the user got right

question_index = 0
# tracks which question we are on, 0 means the first one

filtered_questions = []
# holds the list of flashcards that match the chosen category

FLASHCARDS_FILE = "flashcards.json"
# the filename where all our flashcard data is saved


# these are functions that handle loading and saving the flashcard file

def load_flashcards():
    if not os.path.exists(FLASHCARDS_FILE):
        # checks if the file exists before trying to open it, avoids a crash
        return []
    try:
        with open(FLASHCARDS_FILE, "r") as f:
            # opens the file in read mode
            data = json.load(f)
            # converts the JSON text in the file into a Python list
            return data if isinstance(data, list) else []
            # returns the list only if it really is a list, otherwise returns empty
    except (json.JSONDecodeError, IOError):
        return []
        # if the file is broken or unreadable, return an empty list instead of crashing

def save_flashcards(cards):
    with open(FLASHCARDS_FILE, "w") as f:
        # opens the file in write mode, this overwrites whatever was there before
        json.dump(cards, f, indent=4)
        # converts the Python list into JSON and writes it neatly to the file


# this function opens a popup so the user can pick which category to study

def choose_category():
    cards = load_flashcards()
    # loads all flashcards from the file

    if not cards:
        status_label.config(text="No flashcards found! Add some first.")
        return
        # stops here if there are no flashcards at all

    seen = []
    # will hold the list of unique categories found in the flashcards

    for card in cards:
        cat = card.get("category", "")
        # reads the category field from each flashcard

        if cat and cat not in seen:
            seen.append(cat)
            # only adds the category if we haven't seen it before, no duplicates

    popup = tk.Toplevel(window)
    # creates a new popup window on top of the main window

    popup.title("Select Category")
    popup.geometry("280x250")
    popup.resizable(False, False)
    # locks the popup size so it can't be resized

    popup.grab_set()
    # keeps focus locked to the popup until it is closed

    tk.Label(popup, text="Choose a category:", font=("Arial", 12)).pack(pady=12)
    # adds a heading inside the popup

    def select(cat):
        global selected_category
        selected_category = cat
        # saves whichever category the user clicked as the selected one

        status_label.config(text=f"Category: {cat}  ")
        # updates the main window status to show which category was chosen

        popup.destroy()
        # closes the popup after a selection is made

    for cat in seen:
        tk.Button(popup, text=cat, width=22, command=lambda c=cat: select(c)).pack(pady=4)
        # creates one button per category
        # lambda c=cat makes sure each button remembers its own category value


# these functions handle quiz logic - starting the quiz, showing questions, checking answers, and moving on

def start_quiz():
    global filtered_questions, question_index, score

    if selected_category is None:
        status_label.config(text="Please choose a category first.")
        return
        # stops here if the user hasn't picked a category yet

    cards = load_flashcards()
    # loads all flashcards from the file

    filtered_questions = [
        c for c in cards
        if c.get("category", "").lower() == selected_category.lower()
    ]
    # keeps only the cards that belong to the chosen category, comparison is case-insensitive

    if not filtered_questions:
        status_label.config(text="No flashcards in this category.")
        return
        # stops here if the chosen category has no cards in it

    random.shuffle(filtered_questions)
    # randomises the question order so it's different every time

    question_index = 0
    # resets back to the first question

    score = 0
    # resets the score to zero for a fresh quiz

    show_question()
    # displays the first question

    for w in [quiz_button, category_button, add_button, manage_button]:
        w.pack_forget()
        # hides all four menu buttons while the quiz is running

    for w in [quiz_question_label, quiz_answer_entry, check_button, next_button, back_button]:
        w.pack(pady=8)
        # shows the quiz screen widgets


def show_question():
    global current_answer
    card = filtered_questions[question_index]
    # gets the flashcard at the current position in the list

    quiz_question_label.config(
        text=f"Q {question_index + 1}/{len(filtered_questions)}: {card['question']}"
    )
    # updates the question label to show the question number and text

    current_answer = card["answer"]
    # saves the correct answer so we can compare it when the user submits

    quiz_answer_entry.delete(0, tk.END)
    # clears the answer input box ready for a new answer

    status_label.config(text="")
    # clears any previous correct/wrong message


def check_answer():
    global score
    user_answer = quiz_answer_entry.get().strip()
    # reads what the user typed and removes any accidental spaces at the edges

    if not user_answer:
        status_label.config(text="Type an answer first.")
        return
        # stops here if the box is empty

    if user_answer.lower() == current_answer.lower():
        status_label.config(text="Correct! ✓")
        score += 1
        # if the answers match (ignoring capitalisation), mark it correct and add a point
    else:
        status_label.config(text=f"Wrong. Answer was: {current_answer}")
        # if wrong, show what the correct answer was


def next_question():
    global question_index
    question_index += 1
    # moves forward to the next question

    if question_index >= len(filtered_questions):
        status_label.config(text=f"Done! Score: {score}/{len(filtered_questions)}")
        quiz_question_label.config(text="Quiz complete!")
        quiz_answer_entry.delete(0, tk.END)
        return
        # if we've gone past the last question, show the final score and stop

    show_question()
    # otherwise show the next question


# this function hides the quiz screen and brings the main menu back

def go_back():
    for w in [quiz_question_label, quiz_answer_entry, check_button, next_button, back_button]:
        w.pack_forget()
        # hides all the quiz widgets

    for w in [quiz_button, category_button, add_button, manage_button]:
        w.pack(pady=10)
        # shows all four menu buttons again

    status_label.config(text="")
    # clears the status message


# this function opens a form popup so the user can create a new flashcard

def add_flashcard():
    popup = tk.Toplevel(window)
    # creates a new popup window

    popup.title("Add Flashcard")
    popup.geometry("320x280")
    popup.resizable(False, False)
    popup.grab_set()
    # locks focus to the popup until it is closed

    tk.Label(popup, text="Category:").pack(pady=(14, 0))
    cat_entry = tk.Entry(popup, width=35)
    cat_entry.pack()
    # label and input box for the category field

    tk.Label(popup, text="Question:").pack(pady=(10, 0))
    q_entry = tk.Entry(popup, width=35)
    q_entry.pack()
    # label and input box for the question field

    tk.Label(popup, text="Answer:").pack(pady=(10, 0))
    a_entry = tk.Entry(popup, width=35)
    a_entry.pack()
    # label and input box for the answer field

    result_label = tk.Label(popup, text="", font=("Arial", 10))
    result_label.pack(pady=6)
    # small label inside the popup that shows success or error messages

    def save():
        cat = cat_entry.get().strip()
        question = q_entry.get().strip()
        answer = a_entry.get().strip()
        # reads and trims the text from all three input boxes

        if not cat or not question or not answer:
            result_label.config(text="Please fill in all fields.")
            return
            # stops here if any field is empty

        cards = load_flashcards()
        # loads the existing flashcards so we can add to them

        cards.append({"category": cat, "question": question, "answer": answer})
        # adds the new flashcard as a dictionary to the list

        save_flashcards(cards)
        # saves the updated list back to the file

        result_label.config(text="Saved! Add another or close.")
        cat_entry.delete(0, tk.END)
        q_entry.delete(0, tk.END)
        a_entry.delete(0, tk.END)
        # clears all three boxes so the user can add another card straight away

        status_label.config(text=f"Flashcard added to '{cat}'")
        # updates the main window to confirm the card was saved

    tk.Button(popup, text="Save Flashcard", width=20, command=save).pack(pady=6)
    # button that triggers the save function when clicked


# this function opens a scrollable list of all flashcards so the user can edit or delete them

def manage_flashcards():
    cards = load_flashcards()
    # loads all flashcards from the file

    if not cards:
        status_label.config(text="No flashcards to manage! Add some first.")
        return
        # stops here if there are no flashcards yet

    popup = tk.Toplevel(window)
    popup.title("Manage Flashcards")
    popup.geometry("500x450")
    popup.resizable(False, False)
    popup.grab_set()
    # creates the manage popup and locks focus to it

    tk.Label(popup, text="Your Flashcards", font=("Arial", 13, "bold")).pack(pady=10)
    # bold heading at the top of the manage window

    frame_container = tk.Frame(popup)
    frame_container.pack(fill="both", expand=True, padx=10)
    # a container frame that holds the scrollable area

    scrollbar = tk.Scrollbar(frame_container)
    scrollbar.pack(side="right", fill="y")
    # vertical scrollbar on the right side

    canvas = tk.Canvas(frame_container, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    # canvas is needed to make scrolling work in tkinter

    scrollbar.config(command=canvas.yview)
    # links the scrollbar to the canvas so they move together

    cards_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=cards_frame, anchor="nw")
    # places the actual card rows inside the canvas

    def refresh_list():
        for widget in cards_frame.winfo_children():
            widget.destroy()
            # removes every existing row so we can redraw from scratch

        current_cards = load_flashcards()
        # reloads the latest data from the file

        if not current_cards:
            tk.Label(cards_frame, text="No flashcards left!", font=("Arial", 10)).pack(pady=20)
            return
            # shows a message if every card has been deleted

        for i, card in enumerate(current_cards):
            row = tk.Frame(cards_frame, pady=4)
            row.pack(fill="x", padx=5)
            # creates one horizontal row for each flashcard

            summary = f"{card.get('category', '')} | {card.get('question', '')}"
            if len(summary) > 45:
                summary = summary[:45] + "..."
            # builds a short preview text, cuts it off at 45 characters if too long

            tk.Label(row, text=summary, width=38, anchor="w", font=("Arial", 9)).pack(side="left")
            # displays the preview text on the left side of the row

            def open_edit(idx=i, c=card):
                # idx=i and c=card make sure each button remembers which card it belongs to

                edit_popup = tk.Toplevel(popup)
                edit_popup.title("Edit Flashcard")
                edit_popup.geometry("320x260")
                edit_popup.resizable(False, False)
                edit_popup.grab_set()
                # creates the edit popup and locks focus to it

                tk.Label(edit_popup, text="Category:").pack(pady=(12, 0))
                cat_var = tk.Entry(edit_popup, width=35)
                cat_var.insert(0, c.get("category", ""))
                cat_var.pack()
                # pre-fills the category box with the card's existing category

                tk.Label(edit_popup, text="Question:").pack(pady=(8, 0))
                q_var = tk.Entry(edit_popup, width=35)
                q_var.insert(0, c.get("question", ""))
                q_var.pack()
                # pre-fills the question box with the card's existing question

                tk.Label(edit_popup, text="Answer:").pack(pady=(8, 0))
                a_var = tk.Entry(edit_popup, width=35)
                a_var.insert(0, c.get("answer", ""))
                a_var.pack()
                # pre-fills the answer box with the card's existing answer

                edit_msg = tk.Label(edit_popup, text="", font=("Arial", 9))
                edit_msg.pack(pady=4)
                # small label inside the edit popup for showing save confirmation

                def save_edit():
                    new_cat = cat_var.get().strip()
                    new_q = q_var.get().strip()
                    new_a = a_var.get().strip()
                    # reads the updated values from all three boxes

                    if not new_cat or not new_q or not new_a:
                        edit_msg.config(text="Please fill in all fields.")
                        return
                        # stops here if any field was left empty

                    all_cards = load_flashcards()
                    all_cards[idx] = {"category": new_cat, "question": new_q, "answer": new_a}
                    # replaces the old card at position idx with the updated version

                    save_flashcards(all_cards)
                    # saves the whole updated list back to the file

                    status_label.config(text="Flashcard updated!")
                    edit_popup.destroy()
                    # closes the edit popup

                    refresh_list()
                    # redraws the list so the change shows immediately

                tk.Button(edit_popup, text="Save Changes", width=20, command=save_edit).pack(pady=8)
                # button that triggers the save_edit function

            tk.Button(row, text="Edit", width=6, command=open_edit).pack(side="left", padx=3)
            # Edit button placed next to the card summary

            def delete_card(idx=i):
                all_cards = load_flashcards()
                all_cards.pop(idx)
                # pop() removes the card at position idx from the list

                save_flashcards(all_cards)
                # saves the updated list with that card removed

                status_label.config(text="Flashcard deleted.")
                refresh_list()
                # redraws the list so the deleted card disappears immediately

            tk.Button(row, text="Delete", width=6, fg="red", command=delete_card).pack(side="left", padx=3)
            # Delete button in red text to make clear it's a destructive action

        cards_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        # tells the canvas how tall all the content is so the scrollbar works correctly

    refresh_list()
    # draws the full list as soon as the popup opens

    def on_frame_configure(event):
        canvas.config(scrollregion=canvas.bbox("all"))
        # updates the scroll region whenever the frame changes size

    cards_frame.bind("<Configure>", on_frame_configure)
    # binds the above function so it runs automatically when needed


# these are the quiz screen widgets - they are hidden at the start and only shown during a quiz

quiz_question_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350)
# label that displays the current question

quiz_answer_entry = tk.Entry(window, width=38)
# input box where the user types their answer

check_button = tk.Button(window, text="Check Answer", width=20, command=check_answer)
# button that triggers the check_answer function

next_button = tk.Button(window, text="Next Question", width=20, command=next_question)
# button that moves to the next question

back_button = tk.Button(window, text="← Back to Menu", width=20, command=go_back)
# button that exits the quiz and returns to the main menu


# these are the four main menu buttons shown when the app first opens

quiz_button = tk.Button(window, text="Start Quiz", width=22, command=start_quiz)
quiz_button.pack(pady=10)
# starts the quiz when clicked

category_button = tk.Button(window, text="Choose Category", width=22, command=choose_category)
category_button.pack(pady=10)
# opens the category selection popup

add_button = tk.Button(window, text="Add Flashcard", width=22, command=add_flashcard)
add_button.pack(pady=10)
# opens the add flashcard form

manage_button = tk.Button(window, text="Manage Flashcards", width=22, command=manage_flashcards)
manage_button.pack(pady=10)
# opens the manage flashcards popup


window.mainloop()
# starts the app and keeps the window open, listens for any clicks or key presses and responds to them
