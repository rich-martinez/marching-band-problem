import os

minimumNumber = 64
arbitraryMaximumNumber = 100000

for baseNumber in range(minimumNumber, arbitraryMaximumNumber):
  factors = []
  minimumFactor = 2
  maximumFactor = int(baseNumber / 2)

  for factorOfBaseNumber in range(minimumFactor, maximumFactor):
    if baseNumber % factorOfBaseNumber == 0:
      factors.append(factorOfBaseNumber)

  if len(factors) == 64:
    print(baseNumber)
    break
  