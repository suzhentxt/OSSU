<<<<<<< HEAD
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += "_"
=======
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += "_"
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
    return string