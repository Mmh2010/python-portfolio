import random

secret_number = random.randint(1,100)
print(f"the secret number is:{secret_number}")

def linear_search():
    global secret_number
    attempts=0
    for guess in range(1,101):
        attempts=attempts+1
        if guess == secret_number:
            print(f"You found the number. The number was {secret_number} and it took {attempts} attempts")

def bi_search():
    attempts=0
    low=1
    high=100
    found=False
    while found==False:
        attempts=attempts+1
        mid=(low+high)//2
        if mid== secret_number:
            print(f"You found the number. The number was {secret_number} and it took {attempts} attempts")
            found=True
        elif secret_number > mid:
             low=mid+1
        else:
              high=mid-1




