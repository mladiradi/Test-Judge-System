# Test-Judge-System

The goal of this project is to build a system that automatically tests a user-provided solution against a predefined task and calculates the success rate of the tests. This project involves creating a testing framework using Python's unittest module, defining a task function, a user solution function, and a judge function to evaluate the solutions.


# Explanation:

    task_run Function:
        Processes the input data to compute product quantities and the total number of products.

    user_solution_run Function:
        Mimics the behavior of task_run for user testing.

    TestTask Class:
        Contains methods to test task_run and user_solution_run.
        Uses run_test to execute a test case and update the count of correct and total tests.

    judge Function:
        Loads and runs the test cases.
        Calculates the success rate and prints the results.


1. Imports and Function Definitions

    Purpose: The unittest module is imported to create and run test cases. This module provides a framework for writing and running tests.

2. Task Function

    Purpose: This function processes a given input string, which contains product quantities followed by a termination line. It calculates and returns the total quantity of each product, the total number of products, and the total quantity in a formatted string.
    How It Works:
        The input string is split into lines.
        Each line is processed to extract product names and quantities.
        Quantities are accumulated in a dictionary.
        The function then builds and returns a string that lists each product with its total quantity, the total number of products, and the overall quantity.

3. User Solution Function

    Purpose: This function is meant to be the user’s implementation. It performs the same task as the primary task function and should produce the same results for given inputs.
    How It Works:
        Similar to the task function, it processes the input string in the same manner, accumulates quantities, and returns a formatted output string.

4. Test Case Class

    Purpose: This class defines tests for both the task function and the user solution function. It uses the unittest framework to verify that the functions produce the correct outputs.
    How It Works:
        The class tracks the number of total tests and the number of correct tests.
        It includes a method for running individual test cases, checking if the output of a function matches the expected result.
        Specific test methods are provided for testing the task function and the user solution function.

5. Judge Function

    Purpose: This function runs all the defined test cases and calculates the success rate of the user’s solution.
    How It Works:
        It creates a test suite from the test case class.
        Executes the tests and collects results.
        Calculates the success rate based on how many tests passed out of the total number of tests.
        Prints the total number of tests, the number of correct tests, and the success rate.

6. Main Execution

    Purpose: This ensures that the judge() function is executed when the script is run directly. It prevents the function from running if the script is imported as a module in another script.
   
