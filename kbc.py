questions=[
    [
        "what is your name?", "aditya","sagar","jaydeep","nota","a"
    ],
    [
        "which is your city?","mumbai","delhi","surat","pune","c"
    ],
    [
        "how is transe globe?","bad","very bad","worst","good","d"
    ]
]

levels=[1000,1200,1400,1600,1800,2000]
money=0

for i in range(0,len(questions)):
    question=questions[i]
    print(f"questions for rs.{levels[i]} is {questions [i][0]}")
    print(f"a.{questions[i][1]}     b.{questions[i][2]}")
    print(f"c.{questions[i][3]}     d.{questions[i][4]}")
    
    reply=str(input("enter your answer:"))
    if(reply==questions[i][5]):
     print(f"correct answer, you have win rs{levels[i]}")
    else:
     print("wrong answer|")
     break;