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

# 2. get_categories(budget_id):
#     * Fetch category groups for the selected budget.
#     * Store the categories in a dictionary for easy lookups(e.g., category_id -> category_name).

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


def display_budgets():
    """Display all available budgets"""
    # Convert the dictionary to a list of tuples (budget_id, budget_name)
    budget_list = list(budget_dict.items())

    # Display the options with indexes
    for index, (_, budget_name) in enumerate(budget_list):
        print(f"{index+1}. {budget_name.upper()}")

    choice = get_valid_user_choice(budget_list)

    # Retrieve the selected budget using the chosen index
    selected_budget = budget_list[choice-1]

    selected_budget_id, _ = selected_budget
    print("ID is,", selected_budget_id)


def get_valid_user_choice(budget_list):
    """Return the user's choice"""
    while True:
        user_input = int(input("Enter the number of your choice: "))
        if 1 <= user_input <= len(budget_list):
            return user_input
        else:
            print(f"Please enter a number between 1 and {len(budget_list)}.")


# Main program flow
budget_dict = get_budgets()

if budget_dict:

    print("Which budget would you like to see a monthly summary for?\n")
    display_budgets()
    # budget_id = get_budget_id()


else:
    print("No budgets available.")
