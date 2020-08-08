import sys
import time
import argparse

parser = argparse.ArgumentParser(description='Find a number between a range of a starting number and ending number that has a specific number of factors. *This has only been tested with positive numbers.')
parser.add_argument('-s', '--startNum', nargs='?', type=int, help='First number in range to check against a specific number of factors.')
parser.add_argument('-e', '--endNum', required=True, nargs='?', type=int, help='Last number in range to check number against a specific number of factors.')
parser.add_argument('-f', '--numberOfFactors', required=True, nargs='?', type=int, help='The number of factors required.')
args = parser.parse_args()

firstNumberInRange = args.startNum or args.numberOfFactors
if (firstNumberInRange < args.numberOfFactors):
  raise Exception('The startNum must be >= numberOfFactors')

lastNumberInRange = args.endNum
requiredNumberOfFactors = args.numberOfFactors
initialTime = time.time()

for currentNumberInRange in range(firstNumberInRange, lastNumberInRange):
  factors = [1, currentNumberInRange]
  minimumFactor = 2
  maximumFactor = int(currentNumberInRange / 2)
  currentTime = time.time()
  elapsedSeconds = (currentTime - initialTime)

  print(f"Elapsed Time in Seconds: {elapsedSeconds}", end='\r')
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
