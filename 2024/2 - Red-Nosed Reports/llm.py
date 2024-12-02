import logging
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

import os
os.chdir(os.getenv('WORKING_DIRECTORY'))


def is_safe_report(levels):
    """
    Determines if a report of reactor levels is safe.

    A report is safe if:
    - All levels are either strictly increasing or strictly decreasing.
    - The difference between any two adjacent levels is at least 1 and at most 3.

    Parameters:
    levels (list[int]): A list of integers representing the reactor levels.

    Returns:
    bool: True if the report is safe, False otherwise.
    """
    n = len(levels)
    
    if n < 2:
        return False  # Reports with fewer than 2 levels can't be evaluated.

    all_increasing = all(levels[i] < levels[i + 1] for i in range(n - 1))
    all_decreasing = all(levels[i] > levels[i + 1] for i in range(n - 1))

    # Check if the sequence is either all increasing or all decreasing
    if not (all_increasing or all_decreasing):
        return False

    # Check the difference between adjacent levels
    for i in range(n - 1):
        difference = abs(levels[i + 1] - levels[i])
        if difference < 1 or difference > 3:
            return False
    
    return True


def report_with_one_removal_is_safe(levels):
    """
    Checks if a report can become safe by removing a single level.

    Parameters:
    levels (list[int]): A list of integers representing the reactor levels.

    Returns:
    bool: True if the report can become safe after removing one level, False otherwise.
    """
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(modified_levels):
            return True
    return False


def count_safe_reports(file_path, use_dampener=False):
    """
    Counts the number of safe reports in a given input file.

    A report is considered safe if it is safe by itself, or it can become safe
    by removing a single level if `use_dampener` is True.

    Parameters:
    file_path (str): The path to the input file containing the reports.
    use_dampener (bool): Whether to apply the Problem Dampener logic.

    Returns:
    int: The count of safe reports.
    """
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            report = line.strip()
            levels = list(map(int, report.split()))
            if is_safe_report(levels) or (use_dampener and report_with_one_removal_is_safe(levels)):
                safe_count += 1

    return safe_count


if __name__ == "__main__":
    # Update the file path below to the location of your input file
    file_path = '2024/2 - Red-Nosed Reports/input.txt'
    
    # Count reports without Problem Dampener
    safe_reports_without_dampener = count_safe_reports(file_path)
    print(f"Part 1 - Number of safe reports without Problem Dampener: {safe_reports_without_dampener}")
    
    # Count reports with Problem Dampener
    safe_reports_with_dampener = count_safe_reports(file_path, use_dampener=True)
    print(f"Part 2 - Number of safe reports with Problem Dampener: {safe_reports_with_dampener}")
