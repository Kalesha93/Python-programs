import time

questions = {
    "Capital of India?": "Delhi",
    "2+2*2?": "6",
    "Python is ___?": "programming language"
}
score = 0

for q,a in questions.items():
    print(q)
    start = time.time()
    ans = input("Answer: ")
    end = time.time()
    if end - start > 10:
        print("Time's up!")
        continue
    if ans.lower() == a.lower():
        score += 1

print("Your score:", score)
