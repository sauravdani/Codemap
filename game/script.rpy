# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mc = Character(["mc"],
                     who_color="#c8ffc8")

define d = Character("Daisy",who_color = "#c56fe5")
define e = Character("Eric Buggerman",who_color = "#ecce5b")
define c = Character("Carl Patt",who_color = "#665599")
define p = Character("Dev Patt",who_color = "#32b4a9")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

python:
    mc = renpy.input("What is your name?", length=32)
    mc = mc.strip()

    if not mc:
         mc = "Frank Smith"

"Hello [mc]! Let me assist you with the basics. Press enter to continue."

"This is a visual-novel based game aimed to give you vibrant gaming experience while testing your coding skills too.\n\n(You either can use the touchpad or enter key to continue...)"

"You can navigate through the options given below to understand more about them." 

"Remember one thing the game requires manual saving, so don't forget to do that after each play."

"(Right click or press Esc to open the menu prompt.)"

"Enjoy!!!"

with fade 

mc "Hello World! There you go. Succesfully compiled"

with dissolve 

mc "\"What is happening here? Ah! I am getting pulled into the system!! NO wait!!!\""

mc "This is a strange world! More of like..."

mc "Wait no, I am in the world of numbers!\n\n(Your heart starts beating fast with anxiety around this unknown world folding many dangers)."

d "Look who's here! Another one from the human world. The luring of programming holds the potential enough to pull anyone here."

d "Hey! What's your Name?"

menu:
    "Lie to her!":
        mc "My name is Jarret."
        d "(In mind) {i}Why does he have to lie to me. I can clearly see his name "
        d "Oh! Nice to meet you. I should take my leave now. You better prepare yourself for the fight!"
        mc "Wait! Which fight....?"
        "She leaves the place with unanswered questions."
        jump nextStory
    
    "Say the truth!":
        jump choiceTruth


label choiceTruth:

mc "My name is [mc]."

d "Oh! Nice to meet you. I am Daisy."

menu:
    "Ask about her":
        jump herInfo
    "Ask about the place":
        jump placeInfo   
    "No conversation":
        jump nextStory

label herInfo:

mc "Tell me about you!" 

d "You already know my name but people here are always elevated by my presence."

d "You too deserve a good time but first I need to tell you something about this place."

mc "About this place?"


label placeInfo:
    
d "This place is full of dangers."

d "Tonight is the inaugral party of the coding pits."

d "It's a boring contest where players come and try hands on various coding problems."

d "Doesn't it sound dumb right?" 

d "Don't worry! you stay with me and we will bypass that much efforts."

d "I have the answers to most of the questions already with me"

d "Join me! Maybe then we can sneak out and have good time."

menu:
    "Join her!":
        "You both reach at the coding venue. There are many teams ready with their mentors."

        d "This is Carl Patt, He's best at solving the most complex problems and knows how to find shorcuts."

        d "Dev Patt, brother to Carl the best mentor anyone can ever have. He knows how to win from scratch."

        d "Eric Buggerman is the toughest mentor one can have. His teachings are way too much based on punishments and harsh lessons. Oh! poor lad"
        
        jump dPit
    "No! This doesn't sound good":
        jump nextStory






label nextStory:

mc "She seems weird. I need to know more about this party."

mc "The gate is locked. To explore more about the party I need to find a way to unlock it!"

mc "Let's see what is has to say!"

"BE CAUTIOUS!! This house is belongs to the Patt brothers who rule this world."

"If you fail in unlocking it, you may have to face the consequences too."


menu:
    "Give it a try": 
        jump pattStory
    "Nah! Look for someone else": 
        jump ericStory
    

"You click on the door knob and flames of color hinder your vision."

"To unlock this lock you need to choose the correct option"

# #include <iostream> 
# #include <string>
# using namespace std; 
# int main(int argc, char const *argv[])
# {
# 	char s1[6] = "Code";
# 	char s2[6] = "Map";
# 	char s3[12] = s1 + " " + s2;
# 	cout<<s3;
# 	return 0;
# } 

# a) Hello
# b) World
# c) Error
# d) Hello World

label ericStory:

"You walk across the area and come across a shady place"

"A big man was sitting there with an eye on the mansion you came from."

mc "Hey! Can you guide me about this coding pits and the venue?"

"The gignatic man rose from his seat and stood tall in front of you"

e "You dare to come into my area. Let's see what you have"

e "Answer me!"

python:
    ans = renpy.input("Which bug in programming was responsible to cause computer pandemonium", length=32)
    ans = ans.strip()

if (ans != "Y2K Bug"):
    e "Dare not to talk with Buggerman when you can't answer me on bugs! Leave the place before you die."
    return
else:    
    jump codingRoundE


label pattStory:
    
menu:
    "Code":
        "Wrong Choice!!"
        "Suddenly you see a big man coming out from the house and stabs you for breaching the house rules."
        return
        
    "Map":
        "Wrong Choice!!"
        "Suddenly you see a big man coming out from the house and stabs you for breaching the house rules."
        return

    "Error":
        "Right Choice!!"
        jump pattStoryContinue
        
    "Code Map":
        "Wrong Choice!!"
        "Suddenly you see a big man coming out from the house and stabs you for breaching the house rules."
        return


label dPit:
    d "There's time in the competitions, why not we hangout together till that time in the fountain park!"
    
    menu:
        "Hell yeah!":
            "You reach fountain park and sit there talking for a few minutes"
            "The time kept passing and in the heat of the moment you missed the reporting time of the competition."
            "You go back to the venue but of no use."
            return
        "NO! I need to prepare myself":
            jump codingRoundD

label pattStoryContinue:

c "So you're the one who came from earth this time."

c "Every year many people come to us but only a few of them win, the one who have the dedication."

p "Tonight is the inaugral party of the coding pits."

p "It's a contest where players come from earth and try hands on various coding problems."

p "If you manage to win, you'll find your way home, else would always stay here."

p "Now we too give you a choice! Carl or Me."

"This is Carl Patt, He's best at solving the most complex problems and knows how to find shorcuts."

"Dev Patt, brother to Carl the best mentor anyone can ever have. He knows how to win from scratch."       

menu:
    "Carl Patt":
        jump codingRoundC
    "Dev Patt":
        jump codingRoundP
   
     
label codingRoundD:

"The compeition begins"

mc "Hey! Tell me the question. Only mentors have access to it."

d "Wait, I am trying to figure it out. I can't understand it."

d "I know the answer though, here the answer is Compilation Error"

"You enter the answer in the console, and......"

with fade

"Failed! There are no shortcuts to programming. It's all practise. "

"Next time don't let distractions ruin your game!"

return


label codingRoundP:

"The compeition begins"

p "The question is : "

# Which of the following C++ code will give error on compilation?

# ================code 1=================
# #include <iostream>
# using namespace std;
# int main(int argc, char const *argv[])
# {
# 	cout<<"Hello World";
# 	return 0;
# }
# ========================================
# ================code 2=================
# #include <iostream>
# int main(int argc, char const *argv[])
# {
# 	std::cout<<"Hello World";
# 	return 0;
# }
# ========================================
# a) Code 1 only
# b) Neither code 1 nor code 2
# c) Both code 1 and code 2
# d) Code 2 only

menu:
    "Code 1":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "Neither code 1 nor code 2":
        "Congratulations! You won the game"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "Both code 1 and code 2":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "Code 2 only":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    
    
label codingRoundC:  #Ismein ek timer add hona hai

"The compeition begins"

menu:
    
    "Code 1":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "Neither code 1 nor code 2":
        "Congratulations! You won the game"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "Both code 1 and code 2":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "Code 2 only":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return 


label codingRoundE:

e "Hah! Right Answer"

e "Tonight is the inaugral party of the coding pits."

e "It's a contest where players come from earth and try hands on various coding problems."

e "If you manage to win, you'll find your way home, else would always stay here."

"The compeition begins"

# if n == 0
#    print ("zero") 
# elif : n == 1     
#    print ("one")  
# elif             
#    n == 2:        
#    print ("two") 
# else n == 3:      
#    print ("three")

e "The question says: Count the number of errors in the code"

menu:
    "1":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "4":
        "Congratulations! You won the game"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "3":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return
    "2":
        "Sorry, Wrong Choice"
        "If you have just begin your coding journey, keep in mind only consistency can take you to the victory."
        return 
        
# This ends the game.
return