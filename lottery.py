# Lottery of the second price auction with costly signals

import random

random.seed(120719)


### Sum of all lottery tickets

# Parameters
n = 88 # number of participants
a = 1 # initial number
d = 1 # step

def sumAS(a, d, n):
    sum = (n / 2) * (2 * a + (n - 1) * d)
    return sum

total_tickets = int(sumAS(a, d, n))
print("The total number of tickets is:", total_tickets)


### Once I have the total number of tickets, I randomly choose a number, assuming that the first "n" tickets are
# owned by the winner (highest total payoff), "n-1" tickets are owned by the second player, and so on...

winning_ticket = random.randint(1, total_tickets)
print("The winning ticket is:", winning_ticket)


### Lottery winner is the number times that the difference between the total number of tickets and the winning ticket
# must be substracted by the "n" tickets of the winner, "n-1" tickets of the second player... till it is equal or below 0.

diff = total_tickets - winning_ticket
print("Difference:", diff)

for count, i in enumerate(range(n, 0, -1)):
    print("Substract to difference:", i)
    diff -= i
    print("New difference:", diff)
    print("Individual's ranking:", count+1)
    if diff <= 0:
        break

print("The lottery winner is:", count+1, "rd player")
