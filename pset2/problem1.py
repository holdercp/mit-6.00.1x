balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
  balance -= balance * monthlyPaymentRate
  balance += (balance * (annualInterestRate / 12))

print("Remaining balance: " + str(round(balance, 2)))