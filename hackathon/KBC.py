# KBC
q=[
      "1.who invented python language?",
      "2.what is the National sports of India?",
      "3.which bollywood movie got highest box office collections  in 2020?",
      "4.How many times can a person run for President of the USA?",
      "5.who won the Bharat Ratna award in 2015?"
]
o=[
    ["charles babbage","dennis ritchie","guido van rossum","james gosling"],
    ["hockey","cricket","kabaddi","football"],
    ["tanhaji","baaghi","street dancer3","bahubali2"],
    ["3","2","1","none of these"],
    ["sachin tendulkar","amitabh bachhan","sunil chetri","madan mohan malviya"]
]
a=[3,1,1,2,4]
ff=[["1.charles babbage\n","3.guido van rossum"],
    ["1.hockey\n","4.football"],
    ["1.tanhaji\n","4.bahubali2"],
    ["2.2\n","3.1"],
    ["3.sunil chetri\n","4.maddan mohan malviya"]
    ]
print("------------WELCOME TO KBC---------------")
name=input("enter your name:")
print("Good Luck------>>>>",name)
i=sum=count=0
while i<len(q):
    j=0
    print(q[i])
    while j<len(o[i]):
        print(j+1,".",o[i][j])
        j+=1
    ans=int(input("Enter your answer or you can use 5050 lifeline:-"))
    if ans==a[i]:
        sum+=2000000
        print("Congratulations you have won:-",sum)
    elif ans==5050:
        if count==1:
             print("Sorry you have already used 5050 Lifeline")
             ans1=int(input("Enter your answer:-"))
        if count<1:
            count+=1
            print(ff[i][0])
            print(ff[i][1])
            ans1=int(input("you have two options now, choose one:-"))
        if ans1==a[i]:
            sum+=2000000
            print("Congratultions you have won:-",sum)
        else:
            print("your answer is wrong and you won:-",sum)
            print("game over")
            print("Answer was:",a[i])
            break
    else:
        print("your answer is wrong and you won:-",sum)
        print("game over")
        print("Answers was:",a[i])
        break
    i+=1
    print()