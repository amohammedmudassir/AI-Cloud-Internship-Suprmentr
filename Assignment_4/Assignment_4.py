n=50
fizz=0
buzz=0
fizzbuzz=0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
        fizzbuzz+=1
    if i%3==0:
        print("Fizz")
        fizz+=1
    elif i%5==0:
        print("Buzz")
        buzz+=1
    else:
        print(i)
print(f"Fizz: {fizz}, Buzz: {buzz}, FizzBuzz: {fizzbuzz}")