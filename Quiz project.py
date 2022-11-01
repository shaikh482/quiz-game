score=0
def abcd(a):
    
    if a!="yes":
        return("-----THANKS FOR PLAYING THE QUIZ GAME-----\n")
    else:
        return("NEXT QUIZ\n")
print("WELCOME TO QUIZ GAME\n")        
playing=input("Do you want to play the quiz.....\n ")
if  playing!="yes":
    quit()
else:
    print("LET'S PLAY THE QUIZ\n")
print("*****QUIZ NO. 1***********\n")

print("1) Who developed the python programming Language\n")
print("a)Wick van Rossum")
print("b)Ramus Lerdorf")
print("c)Gudio van Rossum")
print("d)Niene Stom\n")


ans=input("Enter the option : ")
if ans=="c":
    print("Answer is correct\n")
    score=score+1
else:
    print("Answer is wrong\n")
    print('----CORRECT ANSWER IS C:GUDIO VAN ROSSUM----\n')
    
    
print("*****QUIZ NO. 2***********\n")
print("2)In which year of First World War Germany declared war on Russia and France\n")
print("a)1914")
print("b)1915")
print("c)1916")
print("d)1917\n")


ans=input("Enter the option : ")
if ans=="a":
    print("Answer is correct\n")
    score=score+1
   
else:
    print("Answer is wrong\n")
    print('-----CORRECT ANSWER IS A:1914---\n')


print("*****QUIZ NO. 3***********\n")
print("3)ICO stands for\n")
print("a)International Civil Aviation Organization")
print("b)Indian Corporation of Agriculture Organization")
print("c)Institute of Company of Accounts Organization")
print("d)None of the above\n")


ans=input("Enter the option : ")
if ans=="a":
    print("Answer is correct\n")
    score=score+1
    
else:
    print("Answer is wrong\n")
    print('-----CORRECT ANSWER IS A:International Civil Aviation Organization---\n')
  
   
print("*****QUIZ NO. 4***********\n")
print("4)India has the largest deposite of___ in the world. \n")
print("a)gold")
print("b)copper")
print("c)mica")
print("d)None of the above\n")


ans=input("Enter the option : ")
if ans=="c":
    print("Answer is correct\n")
    score=score+1
else:
    print("Answer is wrong\n")
    print('-----CORRECT ANSWER IS C:mica---\n') 



print("*****QUIZ NO. 5***********\n")
print("5)How many Lok sabha seats belong to Rajhasthan\n")
print("a)32")
print("b)25")
print("c)30")
print("d)17\n")


ans=input("Enter the option :")
if ans=="b":
    print("Answer is correct\n")
    score=score+1
else:
    print("Answer is wrong")
    print('-----CORRECT ANSWER IS B:25-----\n')
    
print("*****QUIZ NO. 6***********\n")
print("6)India's first satellite is named after\n")
print("a)Aryabhatta")
print("b)Bhaskara II")
print("c)Bhaskara I")
print("d)Albert Einstein\n")


ans=input("Enter the option : ")
if ans=="a":
    print("Answer is correct\n")
    score=score+1
    
else:
    print("Answer is wrong")
    print('-----CORRECT ANSWER IS A:Aryabhatta---\n')
print("*********")    
print("YOUR TOTAL SCORE IS:\n","",score)
print("*********\n")
if score==6:
    print("EXCELLENT\n")
elif score==5:
    print("VERY GOOD\n")
elif score==4:
    print("GOOD\n")
else :
    print("BETTER LUCK NEXT TIME\n")
print("---------QUIZ COMPLETED------------ \n")
print("--------THANK FOR PLAYING QUIZ--------\n")