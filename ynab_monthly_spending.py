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

# 3. get_transactions(budget_id, month):
#     * Fetch all transactions for the specified month and budget.

# 4. calculate_spending(transactions, categories):
#     * Group the transactions by category and calculate total spending per category.

# 5. display_summary(summary):
#     * Format and print the spending summary.


def get_budgets():
    """Fetch all budget and return them as a list."""
    budget_dict = {}
    # Fetch the budgets
    budgets_response = requests.get(
        f"{BASE_URL}/budgets", headers=headers, timeout=10)
    if budgets_response.status_code == 200:
        budgets = budgets_response.json()["data"]["budgets"]
        # Add budgets and their ids to a new simplified dictionary
        for budget in budgets:
            budget_dict[budget['id']] = budget['name']
        return budget_dict
    else:
        print(f"Failed to fetch budgets. Status Code: {
              budgets_response.status_code}")
        print(budgets_response.text)
    return budget_dict


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
    # Retrieve the selected budget using the chosen index
    selected_budget = budget_list[choice-1]

    selected_budget_id, _ = selected_budget
    return selected_budget_id


def get_categories(budget_id):
    """Fetch category groups for the selected budget and store them in a dictionary for easy lookups."""
    category_dict = {}
    # Fetch the categories for the given budget_id
    categories_response = requests.get(
        f"{BASE_URL}/budgets/{budget_id}/categories", headers=headers, timeout=10)

    if categories_response.status_code == 200:
        categories_data = categories_response.json()["data"]["category_groups"]

        # Remove categories where 'hidden' is True
        filtered_categories_data = [
            category for category in categories_data if not category.get('hidden', False)]

        # Print the filtered data with indentation for clarity
        print(json.dumps(filtered_categories_data, indent=4))

        # Iterate over each category group and its categories
        for category_group in categories_data:
            for category in category_group["categories"]:
                category_dict[category['id']] = category['name']
        return category_dict
    else:
        print(f"Failed to fetch budgets. Status Code: {
              categories_response.status_code}")
        print(categories_response.text)
    return category_dict


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

        display_budgets(budget_list)  # Display the budgets

        choice = get_valid_user_choice(budget_list)  # Get valid user input

        selected_budget_id = get_budget_id(
            budget_list, choice)  # Get the budget ID

        get_categories(selected_budget_id)

    else:
        print("No budgets available.")


if __name__ == "__main__":
    main()
