cost = raw_input ('An egg will be point one dollars, how much do you want?')
pay = raw_input ('We only take cash, please pay your eggs in dollars. Change is acceptable')
change = float (pay) - 0.1 * float (cost)
print " Here's your change, ", change, "dollars."
