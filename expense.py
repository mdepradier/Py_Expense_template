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


def chose_a_spender():
    users = get_user_list()
    user_choice = {
        "type": "list",
        "name": "chosen_user",
        "message": "Chose a spender:",
        "choices": users
    }
    option = prompt(user_choice)
    return option['chosen_user']


expense_report_file = "expense_report.csv"


def write_expense_in_expense_report(amount, label, spender):
    with open(expense_report_file, "a") as f:
        csv.writer(f, delimiter=",").writerow([amount, label, spender])


def new_expense(*args):
    infos = prompt(expense_questions)
    spender = chose_a_spender()
    amount = infos['amount']
    label = infos['label']
    write_expense_in_expense_report(amount, label, spender)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True
