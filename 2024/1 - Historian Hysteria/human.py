import logging
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

import os
os.chdir(os.getenv('WORKING_DIRECTORY'))


def main():
    '''
    Main function to execute the reading of input, calculation of total distance, and similarity score, and print the results.
    
    Args:
        None

    Returns:
        None
    '''

    inputListRight = []
    inputListLeft = []

    with open('2024/1 - Historian Hysteria/input.txt', 'r') as file:
        for line in file:
            splitInputLine = line.split('   ')
            inputListLeft.append(int(splitInputLine[0]))
            inputListRight.append(int(splitInputLine[1]))

        inputListRight.sort()
        inputListLeft.sort()

    totalDistance = 0

    for entryNumber in range(len(inputListRight)):
        totalDistance += abs(inputListRight[entryNumber] - inputListLeft[entryNumber])

    print(f'Part 1 - The total distance between the lists is: {totalDistance}')

    similarityScore = 0

    for liftEntryNumber in inputListLeft:
        if liftEntryNumber in inputListRight:
            similarityScore += liftEntryNumber * inputListRight.count(liftEntryNumber)

    print(f'Part 2 - The total similarity score is: {similarityScore}')


if __name__ == '__main__':
    main()