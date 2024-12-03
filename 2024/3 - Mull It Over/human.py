import logging
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

import os
os.chdir(os.getenv('WORKING_DIRECTORY'))


def canBeInt(lst:list):
    '''
    Determine if all elements in a given list can be converted to integers.

    Args:
    - lst (list): A list of elements to be checked.

    Returns:
    - bool: True if all elements in the list can be converted to integers, and the list contains at least two elements; otherwise, False.
    
    Notes:
    - An empty list or a list with only one element will return False.
    - The function checks each element for a valid integer representation and uses a try-except block to handle potential ValueErrors that arise from attempting to convert non-integer values.
    '''

    if len(lst) < 2:
        return False
    
    for entry in lst:
        try:
            int(entry)
        except ValueError:
            return False
        
    return True


def getMulEntries(text:str) -> list:
    '''
    Extracts multiplication entries from a given string.

    This function searches for multiplication expressions of the format 'mul(a, b)' within the provided text. It looks specifically for entries where 'a' and 'b' are integers. It returns a list of tuples, where each tuple contains the two integers extracted from the multiplication expressions.

    Parameters:
    - text (str): A string containing multiple potential multiplication entries.

    Returns:
    - list: A list of lists, where each inner list contains two integers, extracted from the 'mul(a, b)' expressions found in the input text. Each tuple will have the format [a, b].
    '''

    potentialMulEntries = [potentialEntry[:8] for potentialEntry in text.split('mul(') if ')' in potentialEntry[:8]]
    potentialMulEntries = [potentialMulEntry.split(')')[0] for potentialMulEntry in potentialMulEntries if ',' in potentialMulEntry.split(')')[0]]
    mulEntries = [[int(potentialMulEntry.split(',')[0]), int(potentialMulEntry.split(',')[1])] for potentialMulEntry in potentialMulEntries if canBeInt(potentialMulEntry.split(','))]

    return mulEntries


def calculateMulsSum(fileName:str='2024/3 - Mull It Over/input.txt') -> None:
    '''
    This function calculates and prints the total sum of multiplication operations (muls) extracted from the provided text input. The input contains logical instructions and multiplication expressions, which the function parses and processes in two parts.

    Parameters:
    - fileName (str): The path to the input file containing a series of instructions and mathematical operations (default: '2024/3 - Mull It Over/input.txt').

    Output:
    - Total sum of all multiplication operations.
    - Total sum of multiplication operations, considering the toggle ("do()" / "don't()") logic.
    '''

    with open(fileName, 'r') as file:
        memory = file.read()
    
    totalMuls = 0

    mulEntries = getMulEntries(memory)
    mulsPerformed = [mulEntry[0] * mulEntry[1] for mulEntry in mulEntries]
    totalMuls += sum(mulsPerformed)

    print(f'Part 1 - The total sum of muls is:', totalMuls)

    enabled = True
    totalMuls = 0
    charPosition = 0

    while charPosition < len(memory):
        if memory[charPosition:charPosition+4] == 'do()':
            enabled = True
            charPosition += 4
            continue
        
        if memory[charPosition:charPosition+7] == "don't()":
            enabled = False
            charPosition += 7
            continue
        
        if memory[charPosition:charPosition+4] == 'mul(':
            endingIndex = charPosition + 4

            while endingIndex < len(memory) and memory[endingIndex] != ')':
                endingIndex += 1
            
            mulEntry = memory[charPosition:endingIndex + 1]
            entries = getMulEntries(mulEntry)
            
            if enabled and entries:
                for mulEntry in entries:
                    totalMuls += mulEntry[0] * mulEntry[1]
            
            charPosition = endingIndex + 1
            continue
        
        charPosition += 1

    print(f'Part 2 - The total sum of muls is:', totalMuls)


if __name__ == '__main__':
    calculateMulsSum()