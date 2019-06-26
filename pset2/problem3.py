balance = 320000
annualInterestRate = 0.2

def payDebt(payment, monthlyIntRate):
  balanceCopy = balance

  for month in range(12):
    balanceCopy -= payment
    balanceCopy += balanceCopy * monthlyIntRate

  if balanceCopy > .01:
    return 1
  elif balanceCopy < -.01:
    return -1
  else:
    return 0

monthlyIntRate = annualInterestRate / 12
lowPayment = balance / 12
highPayment = (balance * (1 + monthlyIntRate) ** 12) / 12

while True:
  avgPayment = (lowPayment + highPayment) / 2
  result = payDebt(avgPayment, monthlyIntRate)
  if result == 1:
    lowPayment = avgPayment
  elif result == -1:
    highPayment = avgPayment
  else:
    break

print("Lowest Payment: " + str(round(avgPayment, 2)))
