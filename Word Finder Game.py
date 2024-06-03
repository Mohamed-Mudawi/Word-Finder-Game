# NY Times "Spelling Bee" inspired game, on Python Turtle
# Must make words from randomized list of letters. One letters in the center, the "golden letter" must be a part of every word

# Importing required modules and setting up turtle screen
import turtle
import random
turtle.setup(700,500)


# Defining functions that will draw every letter in the English alphabet, this will be used to draw letters inside the hexagons on the turtle screen
def A():
    turtle.pensize(2)
    turtle.left(75)
    turtle.forward(103.5/4)
    
    turtle.right(150)
    turtle.forward(103.5/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(52/4)
    turtle.left(75)
    turtle.pendown()
    turtle.forward(26.65/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(26.65/4)
    turtle.right(75)
    turtle.forward(52/4)
    turtle.left(75)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
    
def B():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.right(90)
    turtle.forward(25/4)
    
    turtle.circle(-25/4, 180)
    turtle.forward(25/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25/4)
    turtle.pendown()
    turtle.circle(-25/4,180)
    turtle.forward(25/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def C():
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(75/4)
    turtle.pendown()
    
    turtle.circle(25/4,180)
    turtle.forward(50/4)
    turtle.circle(25/4,180)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25/4)
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def D():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    turtle.right(90)
    turtle.forward(10/4)
    turtle.circle(-50/4,180)
    turtle.forward(10/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(60/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def E():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.right(90)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.pendown()
    
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(50/4)
    turtle.pendown()
    
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def F():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.right(90)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def G():
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(75/4)
    turtle.pendown()
    
    turtle.circle(25/4,180)
    turtle.forward(50/4)
    turtle.circle(25/4,180)
    
    turtle.left(90)
    turtle.forward(25/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25/4)
    turtle.pendown()
    
    turtle.right(90)
    turtle.forward(25/4)
    
    turtle.penup()
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def H():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(50/4)
    
    turtle.left(90)
    turtle.forward(50/4)
    turtle.left(180)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def I():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(100/4)
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def J():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.right(90)
    turtle.forward(50/4)
    turtle.right(90)
    turtle.forward(75/4)
    turtle.circle(-25/4,180)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25/4)
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def K():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(50/4)
    turtle.pendown()
    
    turtle.left(135)
    turtle.forward(70.71/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(70.71/4)
    turtle.pendown()
    
    turtle.left(90)
    turtle.forward(70.71/4)
    
    turtle.penup()
    turtle.left(45)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def L():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
    
def M():
    turtle.pensize(2)
    turtle.left(75)
    turtle.forward(103.5/4)
    
    turtle.right(150)
    turtle.forward(103.5/4)
    
    
    turtle.left(150)
    turtle.forward(103.5/4)
    
    turtle.right(150)
    turtle.forward(103.5/4)
    
    turtle.penup()
    turtle.left(75)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def N():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.right(150)
    turtle.forward(115.47/4)
    
    turtle.left(150)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(100/4)
    
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
    
def O():
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(75/4)
    turtle.pendown()
    
    turtle.circle(25/4,180)
    turtle.forward(50/4)
    turtle.circle(25/4,180)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(75/4)
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def P():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.right(90)
    turtle.forward(25/4)
    
    turtle.circle(-25/4, 180)
    turtle.forward(25/4)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def Q():
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(75/4)
    turtle.pendown()
    
    turtle.circle(25/4,180)
    turtle.forward(50/4)
    turtle.circle(25/4,180)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(75/4)
    
    
    turtle.left(225)
    turtle.forward(25/4)
    turtle.pendown()
    
    turtle.left(180)
    turtle.forward(25/4)
    
    turtle.penup()
    turtle.left(45)
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def R():
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.right(90)
    turtle.forward(25/4)
    
    turtle.circle(-25/4, 180)
    turtle.forward(25/4)
    
    turtle.left(135)
    turtle.forward(70.71/4)
    
    turtle.penup()
    turtle.left(45)
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def S():
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(50/4)
    turtle.left(90)
    turtle.forward(75/4)
    turtle.pendown()
    
    turtle.circle(25/4,180)
    turtle.left(45)
    turtle.forward(70.71/4)
    turtle.right(45)
    turtle.circle(-25/4,180)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25/4)
    turtle.left(90)
    turtle.forward(50/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def T():
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(25/4)
    turtle.left(90)
    turtle.forward(100/4)
    turtle.left(90)
    turtle.forward(25/4)
    turtle.left(180)
    turtle.pendown()
    
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25/4)
    turtle.pendown()
    
    turtle.left(90)
    turtle.forward(100/4)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(25/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
  
def U():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.left(180)
    turtle.forward(75/4)
    turtle.circle(25/4,180)
    turtle.forward(75/4)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(100/4)
    turtle.left(90)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def V():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.right(165)
    turtle.forward(103.5/4)
    turtle.left(150)
    turtle.forward(103.5/4)
    
    turtle.penup()
    turtle.right(165)
    turtle.forward(100/4)
    turtle.left(90)
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def W():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.right(165)
    turtle.forward(103.5/4)
    turtle.left(150)
    turtle.forward(103.5/4)
    
    turtle.right(150)
    turtle.forward(103.5/4)
    turtle.left(150)
    turtle.forward(103.5/4)
    
    turtle.penup()
    turtle.right(165)
    turtle.forward(100/4)
    turtle.left(90)
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def X():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.right(90)
    turtle.right(63.435)
    turtle.forward(111.8/4)
    
    turtle.penup()
    turtle.left(63.435)
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.left(90)
    turtle.left(63.435)
    turtle.forward(111.8/4)
    
    turtle.penup()
    turtle.right(63.435)
    turtle.right(180)
    turtle.forward(50/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def Y():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.right(90)
    turtle.right(63.435)
    turtle.forward(55.902/4)
    
    turtle.penup()
    turtle.left(63.435)
    turtle.left(63.435)
    turtle.forward(55.902/4)
    turtle.pendown()
    
    turtle.left(180)
    turtle.forward(55.902/4)
    
    turtle.left(90-63.435)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(25/4)
    
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)
def Z():
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100/4)
    turtle.pendown()
    
    turtle.right(90)
    turtle.forward(50/4)
    turtle.right(90+90-63.435)
    turtle.forward(111.8/4)
    
    turtle.left(90+90-63.435)
    turtle.forward(50/4)
    
    turtle.penup()
    turtle.forward(10/4)
    turtle.pendown()
    turtle.pensize(1)


# Defining a function that will take an input letter, draw that letter on the turtle screen, and return a string value of that letter
def word_picker(letters):
    
    
    if letters == 'a':
        A()
        return('a')
    if letters == 'b':
        B()
        return('b')
    if letters == 'c':
        C()
        return('c')
    if letters == 'd':
        D()
        return('d')
    if letters == 'e':
        E()
        return('e')
    if letters == 'f':
        F()
        return('f')
    if letters == 'g':
        G()
        return('g')
    if letters == 'h':
        H()
        return('h')
    if letters == 'i':
        I()
        return('i')
    if letters == 'j':
        J()
        return('j')
    if letters == 'k':
        K()
        return('k')
    if letters == 'l':
        L()
        return('l')
    if letters == 'm':
        M()
        return('m')
    if letters == 'n':
        N()
        return('n')
    if letters == 'o':
        O()
        return('o')
    if letters == 'p':
        P()
        return('p')
    if letters == 'q':
        Q()
        return('q')
    if letters == 'r':
        R()
        return('r')
    if letters == 's':
        S()
        return('s')
    if letters == 't':
        T()
        return('t')
    if letters == 'u':
        U()
        return('u')
    if letters == 'v':
        V()
        return('v')
    if letters == 'w':
        W()
        return('w')
    if letters == 'x':
        X()
        return('x')
    if letters == 'y':
        Y()
        return('y')
    if letters == 'z':
        Z()
        return('z')


# Hiding the turtle cursor
turtle.hideturtle()

# Creating colors for both grey and gold
gold = (1,0.85,0)
grey = (0.87,0.87,0.87)

# Creating 7 different positions for the hexagons
positions = {'top':(0,100*2-62),'topleft':(-33*2,81*2-62),'topright':(33*2,81*2-62),'bottomright':(33*2,43*2-62),'bottomleft':(-33*2,43*2-62),'bottom':(0,24*2-62),'middle':(0,62*2-62)}


# Defining a function that will draw a hexagon. It will take the position of where the hexagon should be, the color that will fill it,
# and the letter inside of it
def hexagon(position,color,letter):
    turtle.pu()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.goto(position)
    turtle.pd()
    turtle.setheading(0)
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(20*2)
        turtle.right(60)
    turtle.end_fill()
    turtle.pu()
    turtle.right(55)
    turtle.fd(20)
    turtle.pd()
    turtle.setheading(270)
    turtle.fd(30)
    turtle.setheading(0)
    turtle.pencolor('Black')
    character = word_picker(letter)
    return character


# Defining a function that will set up the turtle screen with all the appropriate hexagons, and their randomized letters
def set_up_screen():
    turtle.tracer(0)
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    vowels = ['a','e','i','o','u','y']
    random.shuffle(consonants)
    random.shuffle(vowels)
    letters = []
    letters.extend(vowels[:3])
    letters.extend(consonants[:4])
    random.shuffle(letters)
    letter1 = hexagon(positions['top'],grey,letters[0])
    letter2 = hexagon(positions['topleft'],grey,letters[1])
    letter3 = hexagon(positions['topright'],grey,letters[2])
    letter4 = hexagon(positions['bottomright'],grey,letters[3])
    letter5 = hexagon(positions['bottomleft'],grey,letters[4])
    letter6 = hexagon(positions['bottom'],grey,letters[5])
    letter7 = hexagon(positions['middle'],gold,letters[6])
    turtle.update()
    return [letter1,letter2,letter3,letter4,letter5,letter6,letter7.upper()] # Letter 7 is upper cased because it is the golden letter, which will make it easier to detect


# Retrieving the golden letter, which is the only letter that is upper cased
letters = set_up_screen()
for letter in letters:
    if letter.isupper():
        golden_letter = letter
        
        
# Defining a function that will shuffle the hexagons on the screen, but not the golden letter, it will stay in the same space
# Shuffling doesn't provide any advantage, except for a different/better perspective
def shuffle_letters():
    random.shuffle(letters)
    temp_letters = []
    for letter in letters:
        temp_letters.append(letter)
    temp_letters.remove(golden_letter)

    turtle.tracer(0)

    hexagon(positions['middle'],gold,golden_letter.lower())
            
    hexagon(positions['top'],grey,temp_letters[0])
    hexagon(positions['topleft'],grey,temp_letters[1])
    hexagon(positions['topright'],grey,temp_letters[2])
    hexagon(positions['bottomright'],grey,temp_letters[3])
    hexagon(positions['bottomleft'],grey,temp_letters[4])
    hexagon(positions['bottom'],grey,temp_letters[5])
    
    turtle.update()


# Getting a list of 10,000 words from 'https://www.mit.edu/~ecprice/wordlist.10000'
import requests
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
text = requests.get(url)

full_text = text.text

full_text = full_text.split('\n')

# Removing words that are shorter than 4 characters, or longer than 7
copy_text = full_text[:]
for word in copy_text:
    if len(word) > 7 or len(word) < 4:
        full_text.remove(word)

# Defining a function that will run the game
def play_game():
    print('Welcome to spelling be. "End" to end the game, "Shuffle board" to shuffle letters')
    correct_words = []
    
    while True:

        # If the user found more than 4 words, for every time they have an odd number of words found,
        # notify the user and show them the words they found
        if len(correct_words) > 4 and len(correct_words)%2 != 0:
            print('Congratulations! You have found {} correct words.'.format(len(correct_words)))
            print(correct_words)
        
        restart_loop = False
        user_input = input()
        if user_input.lower() == 'end': # If the user inputs end, end the game
            print('Thank you for playing')
            break
        if user_input.lower() == 'shuffle board': # If the user inputs shuffle board, call the shuffle_letters function to shuffle the hexagons
            shuffle_letters()
            continue
            
        if len(user_input) < 4: # If the length of the word the user inputted is less than 4 characters, it's invalid
            print('Too short!')
            continue

        # If the user used any letters not in the randomized list of letters, it's invalid
        for letter in user_input:
            if letter.lower() not in letters:
                if letter.upper() not in letters:
                    print('Bad letters!')
                    restart_loop = True
                    break
        if restart_loop == True:
            continue

        # If the user didn't user the golden letter in the word, restart the loop
        golden_letter_found = False
        for letter in user_input:
            if letter.lower() == golden_letter.lower():
                golden_letter_found = True

        if not golden_letter_found:
            print('Word must contain golden letter.')
            continue

        # If the word the user inputted is in the large word list, it's correct
        if user_input in full_text:

            print('Good!')
            correct_words.append(user_input)


        # Other wise, the user inputted a word not in the word list, so it's invalid
        else:

            print('Not in word list!')
            continue
            
# Game will only execute if script is run directly
if __name__ == '__main__':
    
    play_game()
















