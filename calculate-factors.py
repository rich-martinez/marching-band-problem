import sys
import time
import argparse

parser = argparse.ArgumentParser(description='Find a number between a range of a starting number and ending number that has a specific number of factors.')
parser.add_argument('--startNum', required=True, nargs='?', type=int, help='First number in range to check against a specific number of factors.')
parser.add_argument('--endNum', required=True, nargs='?', type=int, help='Last number in range to check number against a specific number of factors.')
parser.add_argument('--numberOfFactors', required=True, nargs='?', type=int, help='The number of factors required.')
args = parser.parse_args()

if (args.startNum < args.numberOfFactors):
  raise Exception('The startNum must be >= numberOfFactors')

firstNumberInRange = args.startNum
lastNumberInRange = args.endNum
requiredNumberOfFactors = args.numberOfFactors
initialTime = time.time()

for currentNumberInRange in range(firstNumberInRange, lastNumberInRange):
  factors = [1, currentNumberInRange]
  minimumFactor = 2
  maximumFactor = int(currentNumberInRange / 2)
  currentTime = time.time()
  elapsedSeconds = (currentTime - initialTime)

  print(f"Elapsed Seconds: {elapsedSeconds}", end='\r')
  sys.stdout.flush()

  # make max factor range inclusive by adding one
  for factorOfCurrentNumberInRange in range(minimumFactor, maximumFactor+1):
    if currentNumberInRange % factorOfCurrentNumberInRange == 0:
      factors.append(factorOfCurrentNumberInRange)

  numberOfFactors = len(factors)
  if numberOfFactors == requiredNumberOfFactors:
    print()
    print(f"The number {currentNumberInRange} has exactly {numberOfFactors} factors.")
    print()
    break
