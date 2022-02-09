<<<<<<< HEAD
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   if aStr == '':
      return False

   if len(aStr) == 1:
      return aStr == char
      
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      return True
   elif char < midChar:
      return isIn(char, aStr[:midIndex])
   else:
=======
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   if aStr == '':
      return False

   if len(aStr) == 1:
      return aStr == char
      
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      return True
   elif char < midChar:
      return isIn(char, aStr[:midIndex])
   else:
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
      return isIn(char, aStr[midIndex+1:])