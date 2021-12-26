import random
import os
import hangmanpics as pics

hangman = pics.HANGMANPICS

def read():
    with open('./data.txt','r',encoding="utf-8") as f:
        words = f.read().splitlines() #file's words into a list
        words = {k:v for k,v in enumerate(words)} # then to a dictionary
    return words

def random_word():
    words = read() # get dictionary of words
    rand = int(random.random() * len(words))#generate random number
    return rand
    
def printing(err_count, word):
    os.system('clear')
    print('\n********** Hangman **********\n')
    print('Guess the word!')
    print(hangman[err_count] + '\t' + word + '\n')

def check_win(word):
    win_flag = 1;
    for w in word:
        if w != '_ ':
            pass
        else:
            win_flag = 0
            break

    if win_flag == 1:
        return True
    else: return False

def main():
    err_count = 0

    words = read()
    rand = random_word()
    initial_word = words[rand]
    word = []

    for i in range(len(initial_word)):
        word.append('_ ')
     
    while err_count <= 5:
        index_coincidence = []
        print_word = ''
        
        for w in word:
            print_word = print_word + w

        if check_win(word) == True:
            printing(err_count, print_word)
            print('YOU WON!')
            break
        else: 
            printing(err_count, print_word)
            input_letter = input('\nEnter a letter: ')
        
        for i in range(len(initial_word)):
            if initial_word[i] == input_letter:
                index_coincidence.append(i)

        if index_coincidence == []:
            err_count += 1
        else:
            for i in index_coincidence:
                word[i] = str(input_letter + ' ')
        
    if err_count == 6:
        printing(err_count, print_word)
        print('YOU LOST!!')
    
    
        
        
    


if __name__ == "__main__":
    main()