import logging
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

import os
os.chdir(os.getenv('WORKING_DIRECTORY'))

from collections import Counter


def read_input(file_path):
    """
    Reads the input from a specified text file and separates the location IDs into two lists.

    Args:
        file_path (str): The path to the text file containing pairs of location IDs.

    Returns:
        tuple: Two lists (left_list, right_list) containing the location IDs from the file.
    """
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left_id, right_id = map(int, line.split())
            left_list.append(left_id)
            right_list.append(right_id)
    
    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between two lists of location IDs by pairing the 
    sorted elements and summing the absolute differences.

    Args:
        left_list (list of int): A list of location IDs from the left group.
        right_list (list of int): A list of location IDs from the right group.

    Returns:
        int: The total distance calculated from the differences of paired elements.
    """
    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance


def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score based on how many times each number in the 
    left list appears in the right list.

    Args:
        left_list (list of int): A list of location IDs from the left group.
        right_list (list of int): A list of location IDs from the right group.

    Returns:
        int: The total similarity score calculated by summing the products of 
              left_list numbers and their occurrences in the right_list.
    """
    right_count = Counter(right_list)
    
    similarity_score = sum(left_number * right_count[left_number] for left_number in left_list)
    
    return similarity_score


def main():
    """
    Main function to execute the reading of input, calculation of total distance, 
    and similarity score, and print the results.
    
    Args:
        None

    Returns:
        None
    """
    input_file = '2024/1 - Historian Hysteria/input.txt'  # File name with the input data
    left_list, right_list = read_input(input_file)
    
    # Calculate and print total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print("The total distance between the lists is:", total_distance)
    
    # Calculate and print similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("The total similarity score is:", similarity_score)


if __name__ == "__main__":
    main()