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

BUDGET = "Davis Family"


# 1. get_budgets():
#     * Fetch all budgets and return them as a list.
#     * Optionally, let the user select one by name or ID.
def get_budgets():
    """Fetch all budget and return them as a list."""
    budget_list = []
    # Fetch the budgets
    budgets_response = requests.get(f"{BASE_URL}/budgets", headers=headers)
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


# # Fetch the budgets
# budgets_response = requests.get(f"{base_url}/budgets", headers=headers)
# if budgets_response.status_code == 200:
#     budgets = budgets_response.json()["data"]["budgets"]

#     # Loop through each budget
#     for budget in budgets:
#         budget_id = budget["id"]
#         budget_name = budget["name"]
#         print(f"Budget: {budget_name}")

#         # Fetch accounts for the budget
#         accounts_response = requests.get(
#             f"{base_url}/budgets/{budget_id}/accounts", headers=headers)
#         if accounts_response.status_code == 200:
#             accounts = accounts_response.json()["data"]["accounts"]
#             for account in accounts:
#                 print(f"\tAccount: {account['name']}")
#         else:
#             print(f"\tCould not fetch accounts for budget {budget_name}")
# else:
#     print("Failed to fetch budgets")

print(get_budgets())
