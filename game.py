from asciiart import TITLE, HANGMANASCII
import os
import string

# Paradox - How can the user select a valid index w/o knowing the total number of words (?)
# Solution - 'choose_word' replaced by 'get_words'
def get_words(file_path):
    # Protection 1
    if not os.path.exists(file_path):
        print('Invalid File (!)')
        return None
    with open(file_path, 'r') as file:
        return file.read().split(' ')

# 'valid_input' designed to validate user's input against given values
def valid_input(prompt, valid_values, cast_value_to_int=False):
    while True:
        value = input(prompt + ' (Type "EXIT" to Exit): ')
        if value.upper() == 'EXIT':
            print('[Gamebot] Exiting...')
            exit()
        elif cast_value_to_int:
            try:
                value = int(value)
            except:
                print('[Gamebot] Invalid Input Type - Expected an Integer (!)')
        if value not in valid_values:
            print('[Gamebot] Invalid Value (!)')
        else:
            return value

def reveal(corrupted_word, complete_word, char):
    updated_word = ''
    for index in range(len(complete_word)):
        if complete_word[index].upper() == char.upper():
            updated_word += char.upper()
        else:
            updated_word += corrupted_word[index]
    return updated_word

def prettify_corrupted_word(corrupted_word):
    pretty_corrupted_word = ''
    for char in corrupted_word:
        pretty_corrupted_word += char
        pretty_corrupted_word += ' '
    return pretty_corrupted_word[:-1]
        
if __name__ == '__main__':
    # Pre-Game
    total_words = get_words("<FILE>")
    len_total_words = len(total_words)
    total_strikes = 6
    strikes = 0
    used_characters = []
    
    # Game
    print(TITLE + '\n')
    chosen_index = valid_input('[Gamebot] Select a Number From 0 - %d' % (len_total_words - 1), range(1, len_total_words), cast_value_to_int=True)
    chosen_word = total_words[chosen_index].upper()
    corrupted_word = ('_' * len(chosen_word))
    print(HANGMANASCII[0].strip())
    print('[Gamebot] Corrupted Word: ' + prettify_corrupted_word(corrupted_word))
    print('[Gamebot] Good Luck シ')

    # Game Loop
    while True:
        if strikes == 6:
            print('[Gamebot] GAME OVER (!)')
            break
        char = valid_input('[Gamebot] Enter a Character', string.ascii_letters).upper()
        if char not in chosen_word.upper():
            strikes += 1
            print(HANGMANASCII[strikes].lstrip())
            print('[Gamebot] Wrong Guess (⌣́_⌣̀).. (Strikes %d/%d)' % (strikes, total_strikes))
        else:
            corrupted_word = reveal(corrupted_word, chosen_word, char)
            if corrupted_word == chosen_word.upper():
                print('[Gamebot] YOU WON (!) The Secret Word is "%s"' % chosen_word)
                break
            print(corrupted_word)

