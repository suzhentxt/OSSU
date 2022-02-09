def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand = hand.copy()
    
    print("HAND, BEFORE REMOVING LETTERS:", hand)
    
    for letter in word:
        print("CURRENT VALUE OF LETTER " + str(letter) + ":", hand[letter])
        hand[letter] -= 1
        print("UPDATED VALUE OF LETTER " + str(letter) + ":", hand[letter], "\n")
    
    print("HAND, AFTER REMOVING LETTERS:", hand)
    
    return hand

# For testing purposes:    
hand = {'a':2, 'q':1, 'l':2, 'm':1, 'u':3, 'i':1}
word = 'quail'
print(updateHand(hand, word))