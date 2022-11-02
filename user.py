import csv

from PyInquirer import prompt

user_questions = [
    {
        "type": "input",
        "name": "Name",
        "message": "Name: ",
    },
]

user_csv_file = "users.csv"


def add_user_to_csv_file(name):
    with open(user_csv_file, "a") as f:
        csv.writer(f, delimiter=",").writerow([name])


# Read the csv file and return a list of users
def get_user_list():
    with open(user_csv_file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        user_list = [row[0] for row in reader]
    return user_list


def verify_user_name(name):
    if name == "":
        print("Name cannot be empty")
        return False

    if not(name.isalpha()):
        print("Name must contain only letters")
        return False

    if name in get_user_list():
        print("Name already taken")
        return False
    return True


def add_user():
    infos = prompt(user_questions)

    name = infos['Name']
    if not verify_user_name(name):
        return False

    add_user_to_csv_file(name)

    print("User Added !")
    return True
