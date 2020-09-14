#Claudel Saintilien
#November 28,2014 
#Demonstrates if,elif, and else Statements
#Date Modified December 1,2014
#Saintilien_Claudel_a8.py



print("Welcome to a Fruitful Discovery")
print("Join us as we discover what kind of Fruit are you?")

print("Be sure to use capital letters when answering")

Apple=0
Banana=0
Grape=0
Orange=0

countA=Apple
countB=Banana
countC=Grape
countD=Orange

print("1.Which kind of Climate do you prefer ?")
print("C)Hot")
print("B)Warm")
print("A)Cold")
print("D)Both A and C")
    
Answer=input("Enter Answer")

if Answer == "C":
     print("Burnt rubber")
     countA+=1
elif Answer=="B": 
     print("Quality Heat")
     countB+=1 
elif Answer=="A":
     print("Cold Sleep ")
     countC+=1
elif Answer=="D":
     print("Best of both Temperatures")
     countD+=1

print("2.If you could visit your favorite island what would it be?")
print("A)Bahamas")
print("B)Hawaii")
print("C)Universal Orlando Studios")
print("D)Atlantic City")

Answer=input("Enter Answer")

if Answer=="D":
    print("Nice Choice")
    countD+=1
elif Answer=="B":
    print("Even better")
    countB+=1
elif Answer=="C":
    print("Super")
    countC+=1 
elif Answer=="A":
    print("Fantastic")
    countA+=1

      

print("3.How you would you describe yourself as a person?")
print("A)Aggressive")
print("B)Numb")
print("C)Cheerful")
print("D)Gloomy")

Answer=input("Enter Answer")

if Answer=="D":
    print("Rough")
    countD+=1
elif Answer=="B":
    print("Why The Silent Type")
    countB+=1
elif Answer=="A":
     print("Yay!A hype type")
     countA+=1
elif Answer=="C":
     print("Depressed much")
     countC+=1 


print("4.Do you eat Sunflower Seeds?")
print("A)Maybe")
print("B)No")
print("C)Yes")
print("D)Depends")

Answer=input("Enter Answer")


if Answer=="C":
   print("Nothing to be ashamed of")
   countC+=1
elif Answer=="A":
     print("Good. They're bad for you.")
     countA+=1
elif Answer=="D":
     print("Cool")
     countD+=1
elif Answer=="B":
     print("On what grounds?")
     countB+=1

         


print("5.If you can wish for a tree to hang out in your backyard,what tree would it be?")
print("B)Banana Tree")             
print("C)Grape Tree")
print("A)Apple Tree")
print("D)Orange Tree")

Answer=input("Enter Answer")


if Answer=="B":
     print("Nice")
     countB+=1
elif Answer=="C":
     print("Cool")
     countC+=1
elif Answer=="A":
     print("Superb Choice!")
     countA+=1
elif Answer=="D":
     print("You Orangehead")
     countD+=1


print("6.Are you a Summer Person?")
print("A)Absolutely. Who isn't?!")
print("D)Nope,I'm an inside person!")
print("C)Nope,Just Because")
print("B)Nope,I hate the Sun!")

Answer==input("Enter Answer")

if Answer=="A":
     print("Right!Except for maybe people who like Grapes.")
     countA+=1
elif Answer=="D":
     print("Hey, No judgement")
     countD+=1
elif Answer=="C":      
     print("Very unclear, but I'll take your word for it")
     countC+=1
elif Answer=="B":
     print("You're not the first")
     countB+=1
   
     

print("7.What's your favorite Color?")
print("D)Orange")
print("A)Red")
print("B)Yellow")
print("C)Purple")      

Answer=input("Enter Answer")

if Answer=="D":
     print("Good Choice")
     countD+=1 
elif Answer=="B":
     print("Mine too.")
     countB+=1
elif Answer=="C":
     print("Good Choice!")
     countC+=1
elif Answer=="A":
     print("That's new")
     countA+=1


print("8.How do you like your fruit?")
print("D)Cut in 4 slices")
print("B)Cut in 8 Slices")
print("A)Cut in Half")
print("C)No cuts necessary")

Answer=input("Enter Answer")

if Answer=="D":
     print("Nice")
     countD+=1
elif Answer=="B":
     print("Well, aren't you precise")
     countB+=1
elif Answer=="A":
     print("Mine too!")
     countA+=1
elif Answer=="C":
     print("You think you're too good for cut fruit.")
     countC+=1

print("9.If you were Stranded on an island and had to take only one kind of fruit with you, what kind of fruit would you take?")
print("A)Apples, because they're nature's candy")
print("D)Orange, because I like Orange Juice.")
print("B)Bananas, because I can befriend monkeys with them.")
print("C)Grapes, because I like small fruits.")

Answer=input("Enter Answer")

if Answer=="A":
     print("Agreed, 100%")
     countA+=1
elif Answer=="D":
     print("Interesting.")
     countD+=1
elif Answer=="B":
     print("Clever")
     countB+=1
elif Answer=="C":
     print("They like you too.")
     countC+=1

print("10.Which fruit would you most likely turn to to start your day?")
print("A)Apples,because they're sportscandy")
print("B)Bananas,because they have that Potassium man")
print("D)Oranges, because they're juicy.")
print("C)Grapes, because they're small and tasty.")

Answer=input("Enter Answer")

if Answer=="A":
     print("That's true")
     countA+=1
elif Answer=="B":
     print("True")
     countB+=1
elif Answer=="D":
     print("Like Juicy Fruit")
     countD+=1
elif Answer=="C":
     print("Like Potato chips on a Saturday afternoon")
     countC+=1
     

if countA>=countB and countA>=countC and countA>=countD:
     print("Congratulations you are an Apple.")
else:
     print("So Sad.You are not an Apple.")
if countB>=countA and countB>=countC and countB>=countD:
     print("Congratulations you are a Banana.")
else:
     print("So sad you are not a Banana.")    
if countC>=countA and countC>=countB and countC>=countD: 
    print("Congratulations you are a Grape.")
else:
    print("So sad.You are not a Grape.")     
if countD>=countA and countD>=countB and countD>=countC:
     print("Congratulations you are an Orange.")
else:
     print("So sad. You are not an Orange.")
     
          
     

     


     
     
           
          




