<<<<<<< HEAD
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp
=======
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
