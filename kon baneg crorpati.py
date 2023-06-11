question = [
    ["1.Which lenguage was used to create fb ?","Python","French","Javascript","PHP","None",4],
            ["2.Which lenguage was used to create Google ?","Python","French","Javascript","PHP","None",4],
            ["3.Which lenguage was used to create Twitter ?","Python","French","Javascript","PHP","None",4],
            ["4.Which lenguage was used to create Yahoo ?","Python","French","Javascript","PHP","None",4],
            ["5.CMS stands for?","content management sysytem",'count memory system','confirmation memeory system','count manually']
]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,440000,1230000,2500000,5000000,10000000]
money=0
for i in range(0,len(question)):
    questions =question[i]
    print(f"\n\nQuestio for Rs. {levels[i]} \n{questions[0]}")
    print(f"a. {questions[1]}       b. {questions[2]}  ")
    print(f"c. {questions[3]}       d. {questions[4]}  ")
    reply=int(input("Enter your answer:(1-4) "))
    if(reply == questions[-1]):
        print(f"Correct answer!!! you have won Rs.{levels[i]}")
        if(i == 4):
            money = 20000
        elif( i == 9):
            money = 320000
        elif( i == 14):
            money = 10000000
    else:
        print("Wrong Answer!")
        break
print(f"Your take home money is {money}")
