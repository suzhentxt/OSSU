def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    import ps4a
    print("IMPORTING 'SCRABBLE_LETTER_VALUES': \n'", ps4a.SCRABBLE_LETTER_VALUES)
    print('')
    
    print("HAND LENGTH:", n)
    print('')
    
    wordLength = len(word)
    print("WORD LENGTH DETECTED:", wordLength)
    print('')
    wordValue = 0
    
    for letter in word:
        if letter in ps4a.SCRABBLE_LETTER_VALUES.keys():
            print("LETTER DETECTED:", letter)
            wordValue += ps4a.SCRABBLE_LETTER_VALUES[letter]
            print("INCREASING WORDVALUE BY:", ps4a.SCRABBLE_LETTER_VALUES[letter])
            print("NEW WORDVALUE VALUE:", wordValue)
            print('')
    
    wordValue = wordValue * wordLength
    print("WORDVALUE MULTIPLIED BY LENGTH (" + str(wordLength) + "):", wordValue)
    print('')
    
    if wordLength == n:
        wordValue += 50
        print("ADDITIONAL 50 POINTS ADDED FOR USING ALL LETTERS")
        print("BONUS WORD VALUE:", wordValue)
        print('')
    
    print("FINAL WORDVALUE:", wordValue)
    print('')
    return wordValue
    