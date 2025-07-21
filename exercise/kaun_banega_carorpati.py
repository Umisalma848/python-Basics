question=[["Which country invented paper?", "Egypt", "Greece", "China", "India"],
    ["What was the first video ever uploaded to YouTube?", "Me at the Zoo", "First Video Ever", "Space Oddity", "Hello World"],
    ["What animal can hold its breath the longest underwater?", "Elephant", "Sea Turtle", "Dolphin", "Sperm Whale"],
    ["What year did the first manned space flight happen?", "1960", "1961", "1962", "1963"],
    ["What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Perth"],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus"],
    ["What famous structure in Paris was completed in 1889 for a world fair?", "Eiffel Tower", "Louvre Museum", "Notre-Dame", "Arc de Triomphe"],
    ["What famous scientist developed the theory of relativity?", "Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei"],
    ["What is the largest country by land area?", "USA", "Canada", "Russia", "China"],
    ["What is the tallest mountain in the world?", "K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
    ["What is the capital city of Canada?", "Toronto", "Vancouver", "Ottawa", "Montreal"]

]   


price=[1000,2000,4000,5000,6000,10000,12000,24000,32000,150000,320000]
answers = ['c', 'a', 'd', 'b', 'c', 'b', 'a', 'b', 'c', 'c', 'c']
money=0
for i in range(0,len(question)):
    print(f"\n\n\nquestion for rs:,{price[i]}")
    print(f" a. {question[i][1]}   b. {question[i][2]}")
    print(f" c. {question[i][3]}   d . {question[i][4]}")
    reply=(input("enter answer:,"))

    if reply==answers[i]:
        print(f"answer:, you won {price[i]}")
    else:
         print("wrong answer")
         break
print(f"total price money is:{price[i]}")        