import os
import json

from dotenv import load_dotenv
import requests


load_dotenv()  # Load the .env file
token = os.getenv("YNAB_API_TOKEN")
if token:
    print(f"Token: {token[:5]}...")  # Print the first 5 characters
else:
    print("Error: YNAB_API_TOKEN environment variable is not set.")

# Set the base URL and headers
BASE_URL = "https://api.ynab.com/v1"
headers = {
    "Authorization": f"Bearer {token}"
}

# 4. calculate_spending(transactions, categories):
#     * Group the transactions by category and calculate total spending per category.

# 5. display_summary(summary):
#     * Format and print the spending summary.


def get_budgets():
    """
    Processes the budgets response to return a dictionary of budget IDs and names.
    """

    budgets_response = fetch_budgets_response()

    if budgets_response.status_code == 200:
        budget_dict = {}
        budgets_data = budgets_response.json()["data"]["budgets"]

        # Add budgets and their ids to a new simplified dictionary
        for budget in budgets_data:
            budget_dict[budget['id']] = budget['name']

        return budget_dict
    else:
        print(f"Failed to fetch budgets. Status Code: {
              budgets_response.status_code}")
        print(budgets_response.text)
    return {}


def fetch_budgets_response():
    """
    Fetch the budgets from the API. Returns the response object.
    """
    return requests.get(f"{BASE_URL}/budgets", headers=headers, timeout=10)


def display_budgets(budget_list):
    """Display all available budgets"""
    # Display the options with indexes
    for index, (_, budget_name) in enumerate(budget_list):
        print(f"{index+1}. {budget_name.upper()}")


def get_valid_user_choice(budget_list):
    """Return the user's choice"""
    while True:
        user_input = int(input("Enter the number of your choice: "))
        if 1 <= user_input <= len(budget_list):
            return user_input
        else:
            print(f"Please enter a number between 1 and {len(budget_list)}.")


def get_budget_id(budget_list, choice):
    """
    Retrieve the budget ID for the user's selected budget.
    Parameters:
    - budget_list (list): A list of tuples containing budget IDs and names.
    - choice (int): The user's selection (1-based index) for the budget.
    Returns:
    - str: The budget ID corresponding to the user's choice.
    """

    # Retrieve the selected budget using the chosen index
    selected_budget = budget_list[choice-1]

    selected_budget_id, _ = selected_budget
    return selected_budget_id


def get_filtered_categories(budget_id):
    """
    This function filters out hidden category groups and hidden categories
    from the response, returning a dictionary where each category group
    id maps to another dictionary of categories.
    """

    # Fetch the categories for the given budget_id
    categories_response = fetch_categories_response(budget_id)

    if categories_response.status_code == 200:
        categories_data = categories_response.json()["data"]["category_groups"]

        print(json.dumps(categories_data[0:2], indent=4))

        filtered_categories_dict = {}

        # Iterate through the group categories
        for category_group in categories_data:
            # Skip the category group if it's hidden or an Internal Master Category
            if category_group.get('hidden') or category_group['name'] == 'Internal Master Category':
                continue

            # If category group is not hidden, filter the categories inside it
            filtered_categories = {}

            for category in category_group['categories']:
                # Skip the category group if it's hidden
                if category.get('hidden'):
                    continue

                filtered_categories_dict[category_group['id']] = {
                    'group_name': category_group['name'],
                }

                # print("category_group:",
                #       category_group['name'], "--", category['name'], "-", category['id'])

                # Add the category to the filtered_categories dictionary
                filtered_categories[category["id"]] = {
                    "name": category["name"],
                }
            # Only add to the main dictionary if there are valid categories
            if filtered_categories:
                filtered_categories_dict[category_group['name']
                                         ] = filtered_categories

        # print(json.dumps(filtered_categories_dict, indent=4))

        return filtered_categories_dict
    else:
        print(f"Failed to fetch categories. Status Code: {
              categories_response.status_code}")
        print(categories_response.text)
    return {}


def fetch_categories_response(budget_id):
    """
    Fetch the categories from the API. Returns the response object.
    """
    return requests.get(f"{BASE_URL}/budgets/{budget_id}/categories", headers=headers, timeout=10)


def get_monthly_transactions(budget_id, month='current'):
    """
    Fetch all transactions for the specified month and budget.
    """
    # Fetch the transactions for the given budget_id
    transactions_response = fetch_monthly_transactions_response(budget_id)

    if transactions_response.status_code == 200:
        transactions_dict = {}
        transactions_data = transactions_response.json()[
            "data"]["transactions"]

        # print(json.dumps(transactions_data[:], indent=4))

        # For each transaction id, add a dictionary of values
        for transaction in transactions_data:
            # Transfer transactions have an extra null transaction, so filter out null transactions
            if not transaction['category_id']:
                continue
            transactions_dict[transaction['id']] = {
                'amount': transaction['amount'],
                'category_id': transaction['category_id'],
                'category_name': transaction['category_name'],
            }

        # print(json.dumps(transactions_dict, indent=4))

        return transactions_dict
    else:
        print(f"Failed to fetch budgets. Status Code: {
              transactions_response.status_code}")
        print(transactions_response.text)
    return {}


def fetch_monthly_transactions_response(budget_id, month='current'):
    """
    Fetch the transactions for the specified month from the API.
    """
    return requests.get(f"{BASE_URL}/budgets/{budget_id}/months/{month}/transactions", headers=headers, timeout=10)

    ### Main program flow ###


def main():
    """
    Main program flow to interact with YNAB API and allow the user to select a budget.

    This function fetches all available budgets using the `get_budgets()` function,
    displays the budgets to the user with options to select a budget, and then retrieves
    the selected budget's ID. If no budgets are available, an appropriate message is shown.

    It calls the following functions:
    - `get_budgets()`: Fetches and returns the available budgets.
    - `display_budgets()`: Displays the available budgets to the user.
    - `get_valid_user_choice()`: Prompts the user to select a budget.
    - `get_budget_id()`: Retrieves the ID of the selected budget based on user input.
    """

    budget_dict = get_budgets()  # Fetch the budget data

    # Convert dictionary to list of tuples
    budget_list = list(budget_dict.items())

    if budget_dict:  # Ensure there are budgets available
        print("Which budget would you like to see a monthly summary for?\n")

        # Display the budgets
        display_budgets(budget_list)

        # Get valid user choice
        choice = get_valid_user_choice(budget_list)

        # Get the budget ID
        selected_budget_id = get_budget_id(budget_list, choice)

        print(f"\nYou selected the budget: {
              budget_dict[selected_budget_id].upper()}\n")

        print("Fetching categories...\n")

        get_filtered_categories(selected_budget_id)

        get_monthly_transactions(selected_budget_id)

    else:
        print("No budgets available.")


if __name__ == "__main__":
    main()
