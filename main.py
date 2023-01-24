import json
from ui import UI


# flash_cards() tries to read from a previous file "words_to_learn". If found calls UI class with previous
# saved data. If not found, opens a fresh data of French words to learn
def flash_cards():
    try:
        with open('data/words_to_learn.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('data/french_words.json', 'r') as file:
            data = json.load(file)
    flash = UI(data)


if __name__ == "__main__":
    flash_cards()

