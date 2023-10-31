
def stringToMorseCode(givenText):
  morseCode = {
      'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
      'Y': '-.--', 'Z': '--..',
      '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
      "." : ".-.-.-","!" : "-.-.--","?": "..--.."
  }
  
  text = givenText
  solution = ''
  for x in range(len(text)):
    if text[x] == " ":
        solution += "/"
    elif text[x].capitalize() in morseCode: 
        solution += morseCode[text[x].capitalize()] + " "
    elif text[x] in morseCode:
        solution += morseCode[text[x]] + " "
  if solution.endswith(" "):
    solution = solution[:-1]
  return solution


print("Input any text here and it will be translated to morse code!")
print("Any space will be represented with a / and each letter is given a space")
userInput = input()
print(stringToMorseCode(userInput))