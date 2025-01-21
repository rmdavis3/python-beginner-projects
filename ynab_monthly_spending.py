import os
import json

from dotenv import load_dotenv
import requests

# Load the .env file for environment variables
load_dotenv()
token = os.getenv("YNAB_API_TOKEN")

# Check if token is available
if token:
    print(f"Token: {token[:5]}...")  # Print the first 5 characters
else:
    print("Error: YNAB_API_TOKEN environment variable is not set.")

# Set the base URL and headers for YNAB API requests
BASE_URL = "https://api.ynab.com/v1"
headers = {
    "Authorization": f"Bearer {token}"
}


def get_budgets():
    """
    Fetches the list of available budgets from the YNAB API.

    Returns:
        dict: A dictionary where the key is the budget ID and the value is the budget name.
    """

    budgets_response = fetch_budgets_response()

    if budgets_response.status_code == 200:
        budget_dict = {}
        budgets_data = budgets_response.json()["data"]["budgets"]

        # Add budget IDs and names to the dictionary
        for budget in budgets_data:
            budget_dict[budget['id']] = budget['name']

        return budget_dict
    else:
        print(
            f"Failed to fetch budgets. Status Code: {budgets_response.status_code}")
        print(budgets_response.text)
    return {}


def fetch_budgets_response():
    """
    Sends a GET request to fetch budgets from the YNAB API.

    Returns:
        Response: The response object from the YNAB API.
    """
    return requests.get(f"{BASE_URL}/budgets", headers=headers, timeout=10)


def display_budgets(budget_list):
    """
    Displays a list of available budgets for the user to choose from.

    Args:
        budget_list (list): A list of tuples containing budget IDs and names.
    """
    # Display available budgets with indexes
    for index, (_, budget_name) in enumerate(budget_list):
        print(f"{index+1}. {budget_name.upper()}")


def get_valid_user_choice(budget_list):
    """
    Prompts the user to choose a budget by entering a valid number.

    Args:
        budget_list (list): A list of available budgets.

    Returns:
        int: The user's valid choice (1-based index).
    """
    while True:
        user_input = int(input("Enter the number of your choice: "))
        if 1 <= user_input <= len(budget_list):
            return user_input
        else:
            print(f"Please enter a number between 1 and {len(budget_list)}.")


def get_budget_id(budget_list, choice):
    """
    Retrieves the budget ID based on the user's selected budget.

    Args:
        budget_list (list): A list of tuples containing budget IDs and names.
        choice (int): The user's selection (1-based index) for the budget.

    Returns:
        str: The budget ID corresponding to the selected budget.
    """
    selected_budget = budget_list[choice-1]
    selected_budget_id, _ = selected_budget
    return selected_budget_id


def get_filtered_categories(budget_id):
    """
    Fetches and filters out hidden or internal categories from the YNAB API response.

    Args:
        budget_id (str): The budget ID for which categories are being fetched.

    Returns:
        dict: A dictionary of category groups with their respective categories.
    """
    categories_response = fetch_categories_response(budget_id)

    if categories_response.status_code == 200:
        categories_data = categories_response.json()["data"]["category_groups"]

        filtered_categories_dict = {}

        # Iterate through the group categories
        for category_group in categories_data:
            # Skip the category group if it's hidden or an Internal Master Category
            if category_group.get('hidden') or category_group['name'] == 'Internal Master Category':
                continue

            filtered_categories = {}

            # Filter categories within the group
            for category in category_group['categories']:
                # Skip hidden categories
                if category.get('hidden'):
                    continue

                filtered_categories[category["id"]] = {
                    "name": category["name"]}

            # Only add valid categories to the dictionary
            if filtered_categories:
                filtered_categories_dict[category_group['name']
                                         ] = filtered_categories

        return filtered_categories_dict
    else:
        print(
            f"Failed to fetch categories. Status Code: {categories_response.status_code}")
        print(categories_response.text)
    return {}


def fetch_categories_response(budget_id):
    """
    Sends a GET request to fetch categories for a given budget ID.

    Args:
        budget_id (str): The ID of the selected budget.

    Returns:
        Response: The response object from the YNAB API.
    """
    return requests.get(f"{BASE_URL}/budgets/{budget_id}/categories", headers=headers, timeout=10)


def get_monthly_transactions(budget_id, month='current'):
    """
    Fetches all transactions for a specified month and budget.

    Args:
        budget_id (str): The ID of the selected budget.
        month (str): The month for which transactions are being fetched (default is 'current').

    Returns:
        dict: A dictionary where transaction IDs are keys and transaction details are values.
    """
    transactions_response = fetch_monthly_transactions_response(
        budget_id, month)

    if transactions_response.status_code == 200:
        transactions_dict = {}
        transactions_data = transactions_response.json()[
            "data"]["transactions"]

        for transaction in transactions_data:
            # Transfer transactions have an extra null transaction, so filter out null transactions
            if not transaction['category_id']:
                continue
            transactions_dict[transaction['id']] = {
                'amount': transaction['amount'],
                'category_id': transaction['category_id'],
                'category_name': transaction['category_name'],
            }

        return transactions_dict
    else:
        print(
            f"Failed to fetch transactions. Status Code: {transactions_response.status_code}")
        print(transactions_response.text)
    return {}


def fetch_monthly_transactions_response(budget_id, month='current'):
    """
    Sends a GET request to fetch transactions for the specified month and budget ID.

    Args:
        budget_id (str): The ID of the selected budget.
        month (str): The month for which transactions are being fetched (default is 'current').

    Returns:
        Response: The response object from the YNAB API.
    """
    return requests.get(f"{BASE_URL}/budgets/{budget_id}/months/{month}/transactions", headers=headers, timeout=10)


def calculate_spending(transactions, categories):
    """
    Calculates the total spending per category, grouped by category group.

    Args:
        transactions (dict): A dictionary of transactions.
        categories (dict): A dictionary of category groups with categories.

    Returns:
        dict: A dictionary where category groups map to category spending totals.
    """
    results_dict = {}

    # Outer loop: Iterate over category groups
    for category_group_name, category_group_categories in categories.items():
        results_dict[category_group_name] = {}

        # Inner loop: Iterate over categories in the group
        for category_id, category_info in category_group_categories.items():
            total_spending = 0

            # Loop through transactions and sum the amounts for matching categories
            for transaction_id, transaction_info in transactions.items():
                # Check if the transaction belongs to the current category
                if transaction_info["category_id"] == category_id:
                    total_spending += transaction_info["amount"]

            # Add category spending to the results
            results_dict[category_group_name][category_info["name"]
                                              ] = total_spending

    return results_dict


def display_summary(results):
    """
    Displays the formatted spending summary, including totals for each category group 
    and overall spending.

    Args:
        results (dict): The spending results per category group.
    """
    print("Spending Summary:")
    print("-----------------")

    overall_total = 0  # Track overall total spending

    # Iterate through category groups
    for category_group_name, categories in results.items():
        group_total = sum(categories.values())
        overall_total += group_total  # Update overall total

        # Display category group total
        print(f"{category_group_name}: ${group_total /1000:,.2f}")

        # Display individual categories within the group
        for category_name, amount in categories.items():
            print(f"  - {category_name}: ${amount / 1000:,.2f}")

        print()  # Add a blank line for readability

    print("-----------------")
    print(f"Total Spending: ${overall_total / 1000:,.2f}")


def main():
    """
    Main program flow to interact with YNAB API and allow the user to select a budget.

    This function:
    - Fetches all available budgets.
    - Displays them to the user with options.
    - Retrieves the selected budget's ID.
    - Fetches categories and transactions.
    - Calculates and displays a spending summary.
    """
    budget_dict = get_budgets()  # Fetch available budgets

    # Convert dictionary to list of tuples
    budget_list = list(budget_dict.items())

    if budget_dict:  # Ensure there are budgets available
        print("Which budget would you like to see a monthly summary for?\n")

        display_budgets(budget_list)  # Display available budgets

        choice = get_valid_user_choice(budget_list)  # Get valid user choice

        selected_budget_id = get_budget_id(
            budget_list, choice)  # Get selected budget ID

        print(
            f"\nYou selected the budget: {budget_dict[selected_budget_id].upper()}\n")

        print("Fetching categories...\n")

        categories = get_filtered_categories(
            selected_budget_id)  # Fetch filtered categories
        transactions = get_monthly_transactions(
            selected_budget_id)  # Fetch transactions

        # Calculate spending totals
        results = calculate_spending(transactions, categories)

        display_summary(results)  # Display formatted summary

    else:
        print("No budgets available.")


if __name__ == "__main__":
    main()
