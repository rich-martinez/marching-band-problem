import os

minimumNumber = 64
arbitraryMaximumNumber = 10000
currentNumber = null

for baseNumber in range(minimumNumber, arbitraryMaximumNumber):
  factors = []
  minimumFactor = 2
  maximumFactor = (baseNumber / 2)

  for factorOfBaseNumber in range(minimumFactor, maximumFactor):
    if baseNumber % factorOfBaseNumber == 0:
      factors.append(factorOfBaseNumber)

  if factors.length == 64
    currentNumber = baseNumber
    break

os.system(currentNumber)