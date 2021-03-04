"""
This program will prompt the user to enter an amount in EUROS and it will print that amount in as few coins as possible.
"""

amount = float(raw_input("Enter an amount in EUROS: "))

print amount, "stands for:"

coin_list = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

coin_list_res = []

for coin in coin_list:
    res_coin_amount = amount//coin
    coin_list_res.append(res_coin_amount)
    amount -= res_coin_amount * coin
    

for i in range(len(coin_list_res)):
    print int(coin_list_res[i]), "coins of", coin_list[i]


"""
Explanation of the code steps:

First I created a variable called amount that promps the user to enter an amount in EUROS. That amount is a float.
The goal of the exercise is to print to the user the minimun number of coins to which we can divid the amount given as input. To do so, I created a coin_list that takes every coin that there is in EUROS. I also created an empty list called coin_list_res that will save the result of the amount divided by the coin. This result will be an integer because I did the integer division with //. 
Afterwards, I update the amount by decrementing it with the value of the amount of coins used in that particular iteration.
Finally I loop over the coin_list_res and print to the user the amount of each coin.
 
"""
