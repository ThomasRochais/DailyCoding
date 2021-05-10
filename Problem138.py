S = [1, 5, 10, 25] # Set of coins
n = 16 # Target number
sol = {}
numCoins = 0 # Number of coins needed to reach target (initialized to 0)
list.sort(S, reverse = True) # Sort the list of coins from highest to lowest values
r = n # Residual to match
for s in S:
    q = r // s # Multiplicity
    r = r % s # Reminder
    sol[s] = q # Map the coin value to its multiplicity
    numCoins += q # Add the number of coins used
if r != 0:
    print("Impossible:", r, "is left to pay")
else:
    print("The number of coins used is", numCoins)
print(sol)
