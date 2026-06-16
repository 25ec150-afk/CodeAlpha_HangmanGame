import random

words=["python","apple","cloud","laptop","ocean"]
word=random.choice(words)
guessed=[]
wrong=0
limit=6
while wrong<limit:
    display=" ".join(c if c in guessed else "_" for c in word)
    print("\nWord:",display)
    if "_" not in display:
        print("You won!")
        break
    ch=input("Enter a letter: ").lower()
    if len(ch)!=1 or not ch.isalpha():
        print("Enter one letter.")
        continue
    if ch in guessed:
        print("Already guessed.")
        continue
    guessed.append(ch)
    if ch not in word:
        wrong+=1
        print(f"Wrong! {limit-wrong} chances left.")
else:
    print("Game Over! Word was:",word)
