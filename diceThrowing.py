import diceModule
import random

VALID_DIE = ["D4","D6","D8","D10","D12","D20","D100"]
first_check = True
second_check = True

while first_check:
    print("Dice available are: D4, D6, D8, D10, D12, D20, D100")    
    dice_chosen = str(input("Choose a type of dice to roll: "))
    dice_chosen = dice_chosen.upper()
    if dice_chosen not in VALID_DIE:
        print( f"That's not a valid die, try a {random.choice(VALID_DIE)}?")
        continue
    else:        
        while second_check:
            try:
                n_dice = int(input("How many dice would you like to roll? "))
            except: 
                print("Please enter an integer")
                continue
            if dice_chosen == "D4":
                diceModule.throwD4(n_dice)
                print ("you rolled: ", diceModule.D4List, "totalling: ", sum(diceModule.D4List))
                diceModule.D4List.clear()
            elif dice_chosen == "D6":
                diceModule.throwD6(n_dice)
                print ("you rolled: ", diceModule.D6List, "totalling: ", sum(diceModule.D6List))
                diceModule.D6List.clear()
            elif dice_chosen == "D8":
                diceModule.throwD8(n_dice)
                print ("you rolled: ", diceModule.D8List, "totalling: ", sum(diceModule.D8List))
                diceModule.D8List.clear()
            elif dice_chosen == "D10":
                diceModule.throwD10(n_dice)
                print ("you rolled: ", diceModule.D10List, "totalling: ", sum(diceModule.D10List))
                diceModule.D10List.clear()
            elif dice_chosen == "D12":
                diceModule.throwD12(n_dice)
                print ("you rolled: ", diceModule.D12List, "totalling: ", sum(diceModule.D12List))
                diceModule.D12List.clear()
            elif dice_chosen == "D20":
                diceModule.throwD20(n_dice)
                print ("you rolled: ", diceModule.D20List, "totalling: ", sum(diceModule.D20List))
                diceModule.D20List.clear()
            elif dice_chosen == "D100":
                diceModule.throwD100(n_dice)
                print ("you rolled: ", diceModule.D100List, "totalling: ", sum(diceModule.D100List))
                diceModule.D100List.clear()
            
            
            askYesNo = str(input("Would you like to roll more dice? Y/N: "))
            askYesNo = askYesNo.upper()
            if askYesNo == "N" or "NO":
                first_check = False
                second_check = False
                break
            else:
                continue
                
            
        