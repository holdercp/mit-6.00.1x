balance = 3329
annualInterestRate = 0.2

def payDebt(payment):
  balanceCopy = balance
  monthlyIntRate = annualInterestRate / 12

  for month in range(12):
    balanceCopy -= payment
    balanceCopy += balanceCopy * monthlyIntRate

  return balanceCopy <= 0

payment = 10
debtPaid = False
while not debtPaid:
  debtPaid = payDebt(payment)
  if not debtPaid:
    payment += 10

print("Lowest Payment: " + str(payment))