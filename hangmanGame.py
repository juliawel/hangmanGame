import random
from collections import Counter

if __name__ == '__main__':
    
    someWords = """apple banana mango strawberry 
    orange grape pineapple apricot lemon coconut watermelon
    cherry papaya berry peach lychee muskmelon"""

    someWords = someWords.split(' ')

    word = random.choice(someWords)

    print("Guess the word!\nHINT:it's the name of a fruit.")
    
    for i in word:
        print('_', end=' ')
    print()
        
    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1
            
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
        
            if not guess.isalpha():
                print('Enter only a LETTER!')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter!')
                continue
            elif guess in letterGuessed:
                print('You have already guesses that letter.')
                continue
            
            if guess in word:
                x = word.count(guess)
                
                for _ in range(x):
                    letterGuessed += guess
            
            for char in word:
                if char in letterGuessed and Counter(letterGuessed) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                elif Counter(letterGuessed) == Counter(word):
                    print(f'The word is: [{word}]', end=' ')
                    flag +=1
                    print('Congratulations, You won!')
                    break
                    break
                else:
                    print('_', end=' ')
            
            if chances == 0 and Counter(letterGuessed) != Counter(word):
                print(f'\nYou lost. Try again.\nThe word was [{word}]')
                    
    except KeyboardInterrupt:
        print('\nBye. Try again.')
        exit()
        
