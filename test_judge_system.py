import unittest


# Define the task function (the problem statement)
def task_run(input_data):
    """
    Processes the input data to calculate the total quantity of each product and the total number of products.

    Parameters:
    input_data (str): The input data containing product quantities and a termination line.

    Returns:
    str: A formatted string with product quantities, total product count, and total quantity.
    """
    products = {}
    for line in input_data.strip().split('\n'):
        if line == "statistics":
            break
        product, quantity = line.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    output = "Products in stock:\n"
    for product, quantity in products.items():
        output += f"- {product}: {quantity}\n"
    output += f"Total Products: {len(products)}\n"
    output += f"Total Quantity: {sum(products.values())}"
    return output


# User-provided solution (to be tested)
def user_solution_run(input_data):
    """
    Processes the input data in the same way as the task_run function.

    Parameters:
    input_data (str): The input data containing product quantities and a termination line.

    Returns:
    str: A formatted string with product quantities, total product count, and total quantity.
    """
    products = {}
    for line in input_data.strip().split('\n'):
        if line == "statistics":
            break
        product, quantity = line.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    output = "Products in stock:\n"
    for product, quantity in products.items():
        output += f"- {product}: {quantity}\n"
    output += f"Total Products: {len(products)}\n"
    output += f"Total Quantity: {sum(products.values())}"
    return output


# Define the test case for the task
class TestTask(unittest.TestCase):
    correct_tests = 0
    total_tests = 0

    @staticmethod
    def run_test(func, input_data, expected_output):
        """
        Runs a single test case and updates the total and correct test counts.

        Parameters:
        func (function): The function to be tested.
        input_data (str): The input data for the function.
        expected_output (str): The expected output from the function.
        """
        TestTask.total_tests += 1
        if func(input_data) == expected_output:
            TestTask.correct_tests += 1

    def test_task(self):
        """
        Test cases for the task_run function.
        """
        input_data = "bread: 4\ncheese: 2\nham: 1\nbread: 1\nstatistics"
        expected_output = """Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8"""
        self.run_test(task_run, input_data, expected_output)

    def test_user_solution(self):
        """
        Test cases for the user_solution_run function.
        """
        input_data = "bread: 4\ncheese: 2\nham: 1\nbread: 1\nstatistics"
        expected_output = """Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8"""
        self.run_test(user_solution_run, input_data, expected_output)


# Main judge function to run the tests
def judge():
    """
    Runs all test cases using unittest and calculates the success rate.
    """
    # Load the test cases from TestTask class
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask)
    runner = unittest.TextTestRunner()

    # Run the test suite
    runner.run(suite)

    # Retrieve the correct and total tests count
    total_tests = TestTask.total_tests
    correct_tests = TestTask.correct_tests

    # Calculate and print the success rate
    success_rate = (correct_tests / total_tests) * 100 if total_tests > 0 else 0
    print(f"Total Tests: {total_tests}")
    print(f"Correct Tests: {correct_tests}")
    print(f"Success Rate: {success_rate:.2f}%")


if __name__ == '__main__':
    judge()
