# Design a simple quiz game using a while loop. The program asks a series of multiple-choice questions to the user. For each correct answer, the user gets +1 point.
# The quiz ends either when all questions are answered or the user types 'exit'.
# After the quiz ends, show the total score.
# Handle invalid inputs (options not A/B/C/D or empty).

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

# quiz loop
while i< len(questions):
    
    q = questions[i]
    print(q["question"])
    
    # display options
    for key , value in q["options"].items():
        print(key,value)
    
    response = input("enter your option:").upper().strip() 
    
    if(response == "exit"):
        exit()
     
    if(response not in ["A","B","C","D"]):
        print("Enter valid output")
        continue
        
    if(response == q["answer"]):
        point = point +1
    else:
        print("Incorrect ansewer")
    
    i = i+1

print("Quiz is finishied")
print(f"your score is {point}/5. Thanks for playing")