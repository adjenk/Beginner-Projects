# coin weight in grams
pennyWeight = 2.5
nickelWeight = 5.0
dimeWeight = 2.268
quarterWeight = 5.670

# amount of coins that fit in each type of wrapper
pennyWrapper = 50
nickelWrapper = 40
dimeWrapper = 50
quarterWrapper = 40

print("Welcome to the Coin Estimator!")
print("Please enter the weight of your: ")

pennies = float(input("Pennies: "))
nickels = float(input("Nickels:" ))
dimes = float(input("Dimes: "))
quarters = float(input("Quarters: "))

estimatedPennies = pennies / pennyWeight
estimatedNickels = nickels / nickelWeight
estimatedDimes = dimes / dimeWeight
estimatedQuarters = quarters / quarterWeight

print("Pennies: ", int(estimatedPennies))
print("Nickels: ", int(estimatedNickels))
print("Dimes: ", int(estimatedDimes))
print("Quarters: ", int(estimatedQuarters))
