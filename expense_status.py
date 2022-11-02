import ast
import copy
import csv
import itertools

from expense import expense_report_file
from user import get_user_list


def show_transactions(transactions):
    for (debtor, creditor, value) in transactions:
        if value > 0:
            formatted_transaction = f"{debtor} owes {value}€ to {creditor}"
        else:
            formatted_transaction = f"{creditor} owes {-value}€ to {debtor}"
        print(formatted_transaction)


def find_zero_subset(balances):
    for i in range(1, len(balances)):
        for subset in itertools.combinations(balances.items(), i):
            if sum([balance[1] for balance in subset]) == 0:
                return [balance[0] for balance in subset]
    return None

def simplify_with_collector(balances):
    collector = next(iter(balances.keys()))
    return [(collector, person, balance) for (person, balance)
            in balances.items() if person != collector]

def compute_dept_simplification(remaining_set):
    balances = copy.deepcopy(remaining_set)
    for (user, balance) in balances.items():
        if balance == 0:
            print(f"{user} owes nothing")
    subsets = []
    while (subset := find_zero_subset(remaining_set)) is not None:
        subsets.append(subset)
        remaining_set = {x[0]: x[1] for x in remaining_set.items() if x[0] not in subset}
    subsets.append(list(remaining_set.keys()))

    optimal_transactions = []
    for subset in subsets:
        subset_balances = {person: balances[person] for person in subset}
        optimal_transactions.extend(simplify_with_collector(subset_balances))
    show_transactions(optimal_transactions)



def update_status(status, expense):
    amount = float(expense[0])
    spender = expense[2]
    participants = ast.literal_eval(expense[3])
    divided_amount = amount / (len(participants) + 1)

    status[spender] += amount - divided_amount
    for participant in participants:
        status[participant] -= divided_amount



def make_status_report():
    with open(expense_report_file, "r") as f:
        try:
            reader = csv.reader(f, delimiter=",")
            expense_list = [row for row in reader]
        except csv.Error:
            print("Error while reading expense report file")
            return False

    users = get_user_list()

    status = {}
    for user in users:
        status[user] = 0

    for expense in expense_list:
        update_status(status, expense)

    compute_dept_simplification(status)
