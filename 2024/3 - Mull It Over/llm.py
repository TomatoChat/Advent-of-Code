import logging
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

import os
os.chdir(os.getenv('WORKING_DIRECTORY'))

import re


def calculateMuls(fileName:str='2024/3 - Mull It Over/input.txt') -> None:
    '''
    Calculate the total sum of valid multiplication results from a specified input file.
    
    This function reads an input file containing multiplication instructions formatted 
    as 'mul(X,Y)' where X and Y are integers. It evaluates these instructions and 
    prints the sum of the results.

    Parameters:
    - fileName (str): The name of the input file containing multiplication instructions.

    Returns:
    - None: The function prints the total sum of valid multiplication results.
    '''

    with open(fileName, 'r') as file:
        data = file.read()

    pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    matches = re.findall(pattern, data)
    totalSum = sum(int(x) * int(y) for x, y in matches)

    print(f'Part 1 - The total sum of the multiplication results is: {totalSum}')

    return None


def calculateSumFromCorruptedMemory(fileName:str='2024/3 - Mull It Over/input.txt') -> None:
    '''
    Calculate the total sum of multiplication results from potentially corrupted memory.
    
    This function scans through the input data from a specified file to identify valid 
    multiplication instructions in the form 'mul(X,Y)' where X and Y are integers. It 
    also recognizes 'do()' and 'don't()' instructions which enable or disable the 
    execution of future multiplication instructions, respectively.

    Parameters:
    - fileName (str): The name of the input file containing the corrupted memory data.

    Returns:
    - None: The function prints the total sum of valid multiplication results.
    '''

    with open(fileName, 'r') as file:
        data = file.read()

    totalSum = 0
    enabled = True
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)|do\(\)|don't\(\)"

    for match in re.finditer(pattern, data):
        instruction = match.group(0)
        
        if instruction.startswith('mul'):
            if enabled:
                x, y = re.findall(r'\d+', instruction)
                result = int(x) * int(y)
                totalSum += result
        elif instruction == 'do()':
            enabled = True
        elif instruction == "don't()":
            enabled = False

    print(f'Part 2 - The total sum of the multiplication results is:', totalSum)


if __name__ == '__main__':
    calculateMuls()
    calculateSumFromCorruptedMemory()