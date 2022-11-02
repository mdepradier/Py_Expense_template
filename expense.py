import csv

from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]

expense_report_file = "expense_report.csv"
def write_expense_in_expense_report(amount, label, spender):
    with open(expense_report_file, "a") as f:
        csv.writer(f, delimiter=",").writerow([amount, label, spender])



def new_expense(*args):
    infos = prompt(expense_questions)
    amount = infos['amount']
    label = infos['label']
    spender = infos['spender']
    write_expense_in_expense_report(amount, label, spender)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


