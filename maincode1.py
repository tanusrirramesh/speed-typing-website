import time
import random

easy=["The sun shines brightly","Python is fun to learn.","I opened the door."]
medium=["The doctor advised the man to give up smoking.","She completed the assignment before the deadline.","Me and my brother don't see each other often."]
hard=["The number of people who smoke is increasing, so cancer will soon be the most common cause of death.","The old man sat on the park bench, watching children play as the sun set.","Despite repeated warnings, people continue to ignore the harmful effects of pollution."]
    

print("  TYPING SPEED TEST  \n")
print("  Choose Difficulty:")
print("1. Easy \n 2. Medium \n 3. Hard")
diff=int(input("Enter your choice (1-3): "))
paragraph=""
if diff==1:
    paragraph=random.choice(easy)
elif diff==2:
    paragraph=random.choice(medium)
elif diff==3:
    paragraph=random.choice(hard)
else:
    print("Invalid")
    exit()


print("  Choose Test Duration: \n")
print("1. 30 seconds \n 2. 1 minute \n 3. 2 minutes")
timechoice=int(input("Enter your choice (1-3): \n"))
if timechoice==1:
    timelimit=30
elif timechoice==2:
    timelimit=60
elif timechoice==3:
    timelimit=120
else:
    print("Invalid")
    exit()

print("     START TYPING    \n")
print("Type the paragraph below continuously.\n")
print(paragraph)
print("Press ENTER to start  \n")
input()


start=time.time()
typedtext=input("Start typing:  \n")
end=time.time()
timetaken=end-start


if timetaken>timelimit:
    print("Time limit exceeded! \n")
    timetaken=time_limit


typedwords=typedtext.split()          
totalwords=len(typedwords)            
original=paragraph.split()        
correct=0


for i in range(min(totalwords, len(original))):
    if typedwords[i]==original[i]:
        correct+=1


timemin=timetaken/60
if timemin>0:
    wpm = round(totalwords/timemin)
else:
    wpm=0
if totalwords>0:
    acc=(correct/totalwords)*100
else:
    acc=0



print("    RESULTS    \n")
print("Time :", round(timetaken,2), "seconds")
print("Words typed:",totalwords)
print("WPM:",wpm)
print("Accuracy:",round(acc,2),"%")
