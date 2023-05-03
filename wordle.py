import sys          # GETTİNG WoD AS COMMAND-LİNE ARGUMENT
WoD = (sys.argv[1])
WoD = WoD.upper()  # TO AVOİD SOME İNPUT MİSTAKES
if len(WoD) != 5:
    print("The length of WoD must be five!")
    sys.exit()


def lettercheck(word):
    # FUNCTİON FOR COMPARE ALL LETTER İN word WİTH LETTERS İN WoD
    counter_letter = 0     # TO İDENTİFY THE ORDER OF LETTER
    index_number = 0  # TO İDENTİFY İNDEX OF LETTERS İN WoD
    if word == WoD:
        return
    for letter in range(len(word)):
        counter_letter += 1
        letter_control = any([word[letter] == i for i in WoD])  # İF ANY LETTER MATCHES WİTH word[letter],TURN TRUE
        if letter_control is True:
            if word[letter] == WoD[index_number]:
                print(f"{counter_letter}. letter exists and located in right position.")
            else:
                print(f"{counter_letter}. letter exists but located in wrong position.")
        else:
            print(f"{counter_letter}. letter does not exist.")
        index_number += 1


indicator = ["st", "nd", "rd", "th", "th", "th"]
counterTry = 0   # TO İDENTİFY NUMBER OF TRIES
for repeat in range(6):
    word = input("WoD is:")
    word = word.upper()  # TO AVOİD SOME İNPUT MİSTAKES
    counterTry += 1
    if len(word) != 5:
        print(f"Try{counterTry} ({word}): The length of word must be five!")
        continue
    if word == WoD:
        print(f"Try{counterTry}({word}):Congratulations!You guess right in {counterTry}{indicator[counterTry-1]} shot!")
        break
    print(f"Try{counterTry} ({word}):")
    lettercheck(word)
if word != WoD:
    print("You are failed!")
