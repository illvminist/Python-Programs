import nltk
from nltk.corpus import words
from colorama import Fore, Back, Style, init
import time
import sys

# Ensure you have the word list from some obscure dictionary shit called NLTK
nltk.download('words')
init(autoreset=True)  # Initialize colorama, which is how the text becomes coloured for the user

# introduces the program to the user upon launch

intro_title = """
GEMATRIA CALCULATOR 2077
"""

intro_paragraph = """
Greetings, traveler! Welcome to this arcane cipher, where ancient knowledge meets modern code. 
This program will unveil the secrets of the English language through the mystical art of Gematria, 
converting your words into their numerical equivalents. Behold the symbol of your chosen word, 
and once the art is revealed, you will be prompted to unlock the hidden meanings behind its numbers. 
Let the magic of numbers guide you through this journey!
"""

# ASCII Art Title 
ascii_art = '''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
'''

def calculateGematria(word): # the function which explains how to calculate gematria.
    """Calculate the gematria value of a word using the ordinal cipher (A=1, B=2, ..., Z=26)."""
    ordinal = {chr(i + 65): i + 1 for i in range(26)}  #65 represents the ASCII value for the letter 'A'.
    total = sum(ordinal[char] for char in word.upper() if char in ordinal)
    return total

def findMatchingWords(targetValue):
    """Find words in the NLTK word corpus with the same gematria value and filter out obscure ones."""
    matches = [word for word in words.words() if calculateGematria(word) == targetValue and 3 <= len(word) <= 10]
    return matches

def ordinalGematria(phrase):
    """Calculate gematria for a phrase and find matching words with the same value."""
    total = calculateGematria(phrase)
    breakdown = {char: ord(char.upper()) - 64 for char in phrase.upper() if char.isalpha()}

    # Display results for the input
  
    print(Fore.GREEN + f"Input Phrase: {Fore.YELLOW + phrase}")
    print(Fore.GREEN + f"Letter Values: {breakdown}")
    print(Fore.GREEN + f"Total Gematria Value: {total}")
    print(Fore.RED + "-" * 50)

    # Find matching words
    matches = findMatchingWords(total)

    # Display the matches
    print(Fore.GREEN + "Words with the same gematria value:")
    if len(matches) > 5:
        print(Fore.YELLOW + f"5 examples: {', '.join(matches[:5])}")
        more = input(Fore.MAGENTA + "Do you want to see all matches? (yes/no): ").strip().lower()
        if more == 'yes':
            printMatchesInChunks(matches)
    else:
        print(Fore.YELLOW + ", ".join(matches))

def printMatchesInChunks(matches, chunk_size=10):
    """Print the matching words in chunks of a specified size to prevent wrapping."""
    for i in range(0, len(matches), chunk_size):
        print(Fore.YELLOW + ", ".join(matches[i:i + chunk_size]))

print(Fore.LIGHTMAGENTA_EX + intro_title)
print(Fore.RED + ascii_art)
print(intro_paragraph)

# Main program loop
while True:
    inputPhrase = input(Fore.CYAN + "Enter a word or phrase (or type 'exit' to quit): ").strip()
    if inputPhrase.lower() == 'exit':
        print(Fore.RED + "Goodbye!")
        break
    ordinalGematria(inputPhrase)
