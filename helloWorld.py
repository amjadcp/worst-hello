from random import choice
from colorama import Fore, Back
import colorama
import pyttsx3 # pip install pyttsx3

def main():
    colorama.init(autoreset=True)

    color = [Back.RED, Back.GREEN, Back.BLUE, Fore.RED, Fore.GREEN, Fore.BLUE]

    helloWorld = [
        f'''{choice(color)} HELLO WORLD''',
        f'''                              {choice(color)} HELLO WORLD''',
        f'''                                                              {choice(color)} HELLO WORLD''',
        f'''{choice(color)} HELLO WORLD    {choice(color)} HELLO WORLD    {choice(color)} HELLO WORLD''',
        f'''{choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D''',
        f'''                                                                                                                                                                                    {choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D''',
        f'''                                                                                                                                                                                                                                                                                                                                                                          {choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D''',
        f'''{choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D  {choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D  {choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D''',
                ]

    sound = pyttsx3.init()


    for i in range(2):
        print(choice(helloWorld))

        sound.say('hello world')
        sound.runAndWait()

        for j in range(4):
            for k in range(4):
                print(choice(helloWorld), end='')

        sound.say('hello world')
        sound.runAndWait()

        for j in range(4):
            for k in range(4-i):
                print(choice(helloWorld))
        sound.say('hello world')
        sound.runAndWait()

        for j in range(0, 4):
            for k in range(0, 4-j-1):
                print(end='')
            for k in (0, j+1):
                print(f'''                            {choice(color)} H {choice(color)} E {choice(color)} L {choice(color)} L {choice(color)} O {choice(color)} W {choice(color)} O {choice(color)} R {choice(color)} L {choice(color)} D''',end='')
            print()

        sound.say('hello world')
        sound.runAndWait()
    

        print(f'''

    {choice(color)}
    HELLO WORLD           HELLO WORLD   HELLO WORLDHELLO WORLD   HELLO WORLD             HELLO WORLD             HELLO WORLDHELLO WORLDHELLO WORLD   HELLO   HELLO  HELLO   
    HELLO WORLD           HELLO WORLD   HELLO WORLDHELLO WORLD   HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   WORLD   HELLO  WORLD
    HELLO WORLD           HELLO WORLD   HELLO WORLD              HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   HELLO   WORLD  HELLO
    HELLO WORLD           HELLO WORLD   HELLO WORLD              HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   WORLD   WORLD  WORLD
    HELLO WORLD           HELLO WORLD   HELLO WORLDHELLO         HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   HELLO   HELLO  HELLO
    HELLO WORLDHELLO WORLDHELLO WORLD   HELLO WORLDWORLD         HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   WORLD   WORLD  WORLD
    HELLO WORLDHELLO WORLDHELLO WORLD   HELLO WORLDHELLO         HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   HELLO   HELLO  HELLO
    HELLO WORLD           HELLO WORLD   HELLO WORLD              HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD   WORLD   WORLD  WORLD
    HELLO WORLD           HELLO WORLD   HELLO WORLD              HELLO WORLD             HELLO WORLD             HELLO WORLD           HELLO WORLD
    HELLO WORLD           HELLO WORLD   HELLO WORLDHELLO WORLD   HELLO WORLDHELLO WORLD  HELLO WORLDHELLO WORLD  HELLO WORLD           HELLO WORLD   HELLO   HELLO  HELLO      
    HELLO WORLD           HELLO WORLD   HELLO WORLDHELLO WORLD   HELLO WORLDHELLO WORLD  HELLO WORLDHELLO WORLD  HELLO WORLDHELLO WORLDHELLO WORLD   WORLD   WORLD  WORLD            

    ''')
    
    
        sound.say('hello!')
        sound.runAndWait()


if __name__ == '__main__':
    main()

'''
Need Packages
---------------

1. pyttsx3  - pip install pyttsx3
2. espeak   - sudo apt-get install espeak / sudo pacman -S espeak
3. colorama - pip install colorma

put terminal in full-screen !!!

'''