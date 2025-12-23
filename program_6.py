questions = [
    {
        "question": "Who is known as the destroyer in the Hindu Trinity?",
        "options": {"A": "Brahma", "B": "Vishnu", "C": "Shiva", "D": "Indra"},
        "answer": "C"
    },
    {
        "question": "What was the name of Lord Rama's wife?",
        "options": {"A": "Radha", "B": "Sita", "C": "Draupadi", "D": "Kunti"},
        "answer": "B"
    },
    {
        "question": "Who was the author of the epic Mahabharata?",
        "options": {"A": "Valmiki", "B": "Veda Vyasa", "C": "Tulsidas", "D": "Kalidasa"},
        "answer": "B"
    },
    {
        "question": "What was the name of Arjuna's son who died in the Kurukshetra war?",
        "options": {"A": "Abhimanyu", "B": "Lakshmana", "C": "Nakul", "D": "Ekalavya"},
        "answer": "A"
    },
    {
        "question": "Who killed the demon Mahishasura?",
        "options": {"A": "Durga", "B": "Lakshmi", "C": "Kali", "D": "Parvati"},
        "answer": "A"
    }
]

point = 0 
i = 0 

while i< len(questions):
    
    q = questions[i]
    print(q["question"])
    
    for key , value in q["options"].items():
        print(key,value)
    
    response = input("enter your option").upper()
    
    if(response == exit):
        exit()
     
    if(response not in ["A","B","C","D" ,"a", "b", "c" , "d"] or response == " "):
        print("Enter valid output")
        continue
        
    if(response == q["answer"]):
        point = point +1
    else:
        print("Incorrect ansewer")
    
    i = i+1
print("Quiz is finishied")
print(f"your score is {point}/5. Thanks for playing")