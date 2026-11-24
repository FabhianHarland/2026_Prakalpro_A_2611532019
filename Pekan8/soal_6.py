LAST_DIGIT = 9 # chage to the last digit of your nim
daily_limit = 30000 + LAST_DIGIT*1000
expenses = [20000,35000,15000,28000,40000,22000,31000]
#Write your code below
total = 0
highest = expenses[0]
day_above_limit = 0
for i in range (len(expenses)):
    total = total + expenses[i]
    print(f"Day {i+1}:",expenses[i])
    if highest < expenses[i] :
        highest = expenses[i]
    if expenses[i] > daily_limit:
        day_above_limit += 1


print("Daily limit: ",daily_limit)
print("Total:",total)
print("Avarage : ",total/(len(expenses)))
print(f"Highest: day ",highest)
print("Daily limit: ",day_above_limit)