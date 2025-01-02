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


def get_budgets():
    """Fetch all budget and return them as a list."""
    budget_list = []
    # Fetch the budgets
    budgets_response = requests.get(
        f"{BASE_URL}/budgets", headers=headers, timeout=10)
    if budgets_response.status_code == 200:
        budgets = budgets_response.json()["data"]["budgets"]
        # Append budgets to list
        for budget in budgets:
            budget_list.append(budget['name'])
        return budget_list
    else:
        print(f"Failed to fetch budgets. Status Code: {
              budgets_response.status_code}")
        print(budgets_response.text)


# 2. get_categories(budget_id):
#     * Fetch category groups for the selected budget.
#     * Store the categories in a dictionary for easy lookups(e.g., category_id -> category_name).

# 3. get_transactions(budget_id, month):
#     * Fetch all transactions for the specified month and budget.

# 4. calculate_spending(transactions, categories):
#     * Group the transactions by category and calculate total spending per category.

# 5. display_summary(summary):
#     * Format and print the spending summary.


# Main program flow

budgets = get_budgets()

if budgets:
    print("Which budget would you like to see a monthly summary for?\n")
    for index, budget in enumerate(budgets):
        print(f"Enter {index+1} for '{budget}' budget.")
    user_input = int(input())
    print("you chose", user_input)
    budget_id = budgets[user_input-1]
    print("ID is,", budget_id)
else:
    print("No budgets available.")
