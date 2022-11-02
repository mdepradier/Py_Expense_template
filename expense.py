import ast
import copy
import csv

from PyInquirer import prompt

from user import get_user_list

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
]


def chose_a_spender(users):
    user_choice = {
        "type": "list",
        "name": "chosen_user",
        "message": "Chose a spender:",
        "choices": users
    }
    option = prompt(user_choice)
    return option['chosen_user']

# Get the list of participants among the users
def get_participants_list(spender, users):
    possible_participants = copy.deepcopy(users)
    possible_participants.remove(spender)

    select_participants_choice = {
        "type": "list",
        "name": "option",
        "message": "Select participants: ",
        "choices": ["All", "Select"]
    }

    option = prompt(select_participants_choice)
    if option['option'] == "All":
        return possible_participants

    user_choice = {
        "type": "checkbox",
        "name": "participants",
        "message": "Chose participants: ",
        "choices": [{"name": user} for user in possible_participants]
    }
    option = prompt(user_choice)
    return option['participants']



expense_report_file = "expense_report.csv"


def write_expense_in_expense_report(amount, label, spender, participants):
    with open(expense_report_file, "a") as f:
        csv.writer(f, delimiter=",").writerow([amount, label, spender, participants])


def new_expense(*args):
    infos = prompt(expense_questions)
    users = get_user_list()
    if len(users) == 0:
        print("No user found, please add one before adding an expense")
        return False

    spender = chose_a_spender(users)

    participants = get_participants_list(spender, users)

    amount = infos['amount']
    label = infos['label']

    write_expense_in_expense_report(amount, label, spender, participants)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True
