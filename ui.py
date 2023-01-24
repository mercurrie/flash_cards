import random
from tkinter import *
import json
BACKGROUND_COLOR = "#B1DDC6"


class UI:

    # initializes class with starting UI
    def __init__(self, data: list):
        self.current_word = {}
        self.window = Tk()
        self.canvas = Canvas(width=800, height=526)
        self.card_front = PhotoImage(file="images/card_front.png")
        self.card_back = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
        self.word_list = data
        self.flip_timer = self.window.after(3000, func=self.flip_card)
        self.display()

    # update_card() refreshes flash card with new French word and resets flip_card timer
    def update_card(self):
        self.window.after_cancel(self.flip_timer)
        self.current_word = random.choice(self.word_list)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_word["French"], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.card_front)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    # flip_card() refreshes canvas to show back of card containing English translation
    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_word["English"], fill="white")
        self.canvas.itemconfig(self.card_background, image=self.card_back)

    # display() configures window and canvas, refreshes flip_card timer, and adds buttons to UI
    def display(self):
        self.window.title("Flash Cards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=2)

        x_image = PhotoImage(file="images/wrong.png")
        unknown_button = Button(image=x_image, highlightthickness=0, command=self.update_card)
        unknown_button.grid(column=0, row=1)

        check_image = PhotoImage(file="images/right.png")
        known_button = Button(image=check_image, highlightthickness=0, command=self.is_known)
        known_button.grid(column=1, row=1)

        self.update_card()

        self.window.mainloop()

    # is_known() removes word from dictionary and creates new json file for unknown words when checkmark is clicked
    def is_known(self):
        self.word_list.remove(self.current_word)
        with open("data/words_to_learn.json", 'w') as json_file:
            json.dump(self.word_list, json_file)
        self.update_card()
