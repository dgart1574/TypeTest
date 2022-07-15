import random
import time
SentenceList = [   
]
i = 0
while i < 1000000:
    Sentence = random.choice(SentenceList)
    print(Sentence)
    begin = time.time()
    Typeresult = str(input())
    if len(Sentence) == len(Typeresult):
        if Typeresult == Sentence:
            print('Correct!')
        else:
            print('Incorrect!')
    end = time.time()
    stopwatch = end - begin
    print (len(Typeresult) / stopwatch * 60) 
    i = i + 1
