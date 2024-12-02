import logging
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

import os
os.chdir(os.getenv('WORKING_DIRECTORY'))


def checkReportValidity(report:list[int]) -> bool:
    '''
    Determines if a report of reactor levels is safe.

    A report is safe if:
    - All levels are either strictly increasing or strictly decreasing.
    - The difference between any two adjacent levels is at least 1 and at most 3.

    Parameters:
    levels (list[int]): A list of integers representing the reactor levels.

    Returns:
    bool: True if the report is safe, False otherwise.
    '''
    
    previousLevel = None
    reportValidity = True
    levelDirection = None

    for level in report:
        if previousLevel is not None:
            if abs(level - previousLevel) < 1 or abs(level - previousLevel) > 3:
                reportValidity = False
                break

            if levelDirection is None:
                if level > previousLevel:
                    levelDirection = 1
                else:
                    levelDirection = -1
            elif level > previousLevel:
                if levelDirection != 1:
                    reportValidity = False
                    break
            elif level < previousLevel:
                if levelDirection != -1:
                    reportValidity = False
                    break
        
        previousLevel = level
    
    return reportValidity


def main():
    '''
    Main function to process red-nosed reports from an input file, determining the number of valid reports based on certain validity criteria.

    
    Args:
        None

    Returns:
        None
    '''

    reports = []
    validReports = 0

    with open('2024/2 - Red-Nosed Reports/input.txt', 'r') as file:
        for line in file:
            reportLine = line.split(' ')
            reports.append([int(level) for level in reportLine])

    for report in reports:
        if checkReportValidity(report):
            validReports += 1
    
    print(f'Part 1 - Number of safe reports: {validReports}')

    validReportsDamper = 0

    for report in reports:
        if checkReportValidity(report):
            validReportsDamper += 1
        else:
            for levelPosition in range(len(report)):
                testCleanedReport = report.copy()
                testCleanedReport.pop(levelPosition)

                if checkReportValidity(testCleanedReport):
                    validReportsDamper += 1
                    break
    
    print(f'Part 2 - Number of safe reports with Problem Dampener: {validReportsDamper}')


if __name__ == '__main__':
    main()