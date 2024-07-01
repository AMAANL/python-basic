import pyttsx3
import random
def func(message):
    engine.say(message)
    engine.runAndWait()
engine = pyttsx3.init()
engine.say("A wild caterpie has appeared,     what you want to do? ")
engine.runAndWait()
choice1=input("run/fight:   ").lower()

if choice1=="run":
    func("You have successfully escaped")
    
elif choice1=="fight":
    engine.say("Go Pikaachu")
    engine.runAndWait()
    print("Go Pikachu!!!")
    print()
   
    
    php= 80
    chp= 100
    double_team = False
    while php > 0 and chp > 0:
     
        
            
        engine.say("caterpie used stringshot")
        engine.runAndWait()
        print("caterpie used String Shot")
        print()
        engine.say(f"Your pokemon's Hp reduced to {php}") 
        engine.runAndWait() 
        engine.say(" Which move you want to choose")           
        print(f"Your pokemon's Hp reduced to {php}")
        engine.runAndWait()
        choice2=input('''Which move you want to choose 
        *tackle=10 HP     *double team=reduces damage by half
        *iron tail=20 HP  *thunder=25 HP \n''').lower()
        print()
       
        if choice2 == "tackle":
            chp -= 10
            engine.say("Pikachu used Tackle!")
            engine.runAndWait()
            print("Pikachu used Tackle!")
        elif choice2 == "double team":
            double_team = True
            engine.say("Pikachu used double team!Caterpie's attacks will now do half damage")
            engine.runAndWait()
            print("Pikachu used Double Team! Caterpie's attacks will now do half damage.")
        elif choice2 == "iron tail":
            chp -= 20
            engine.say("Pikachu used Iron Tail!")
            engine.runAndWait()
            print("Pikachu used Iron Tail!")
        elif choice2 == "thunder":
            chp -= 25
            engine.say("Pikachu used Thunder!")
            engine.runAndWait()
            print("Pikachu used Thunder!")
        else:
            engine.say("Invalid move. Pikachu missed the turn!")
            engine.runAndWait()
            print("Invalid move. Pikachu missed the turn!")
        print()
        if chp <= 0:
            chp = 0
            engine.say("Caterpie fainted. You won!")
            engine.runAndWait()
            print("Caterpie fainted. You won!")
            break
        
        if double_team:
              php -=10
        else:
            php -=20
        print()
        print()
        
        print("catterpie hp",chp)
        if php <= 0:
            php = 0
            print()
            engine.say("pikachu fainted. You lost!")
            engine.runAndWait()
            print("Pikachu fainted. You lost!!")
            break
    