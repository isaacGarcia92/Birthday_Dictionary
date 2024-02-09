import json
import datetime
from collections import Counter
from bokeh.plotting import figure, show, output_file


months_dict = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def parse_string(string):
    try:
        return str(string)
    except ValueError:
        return None


def parse_date(string):
    try:
        return datetime.datetime.strptime(string, '%d-%m-%Y')
    except ValueError:
        return None


def validate_names():
    while True:
        str_input = input('Who is the birthday you want to look up? Write first and last name: ')
        parsed_str = parse_string(str_input)

        if parsed_str:
            words = parsed_str.split()

            for i in range(0, len(words)):
                words[i] = words[i].capitalize()

            new_str = ' '.join(words)

            return new_str
        else:
            print('Invalid Input!')
        print()


def initial_greeting():
    print('Welcome to the birthday dictionary!')
    print()


def goodbye_greeting():
    print('Thank for using our program!')


def choose_option():
    while True:
        print('Please choose from the following options:')
        print("1.- Look for someone's birthday")
        print("2.- Add someone's name and birthday")
        print('3.- See the list of names on the directory')
        print('4.- See how many birthdays are on each month')
        print('5.- Plot histogram of each month')
        print('6.- Exit program')
        print()
        int_input = input('Type number option: ')
        parsed_int = parse_int(int_input)

        if parsed_int:
            if parsed_int < 1 or parsed_int > 6:
                print('Choose between numbers 1 and 6')
            else:
                return parsed_int
        else:
            print('Invalid Input!')
        print()


def print_names(dic):
    print()
    for name in dict(dic).keys():
        print(name)
    print()


def add_full_name():
    while True:
        first_name_input = input('Type first name: ').capitalize().strip()
        parsed_first_name = parse_string(first_name_input)

        if parsed_first_name.isalpha():
            if len(parsed_first_name) < 2:
                print('Type a first name with at least 2 characters')
            else:
                break
        else:
            print('Invalid Input!')

    while True:
        last_name_input = input('Type last name: ').capitalize().strip()
        parsed_last_name = parse_string(last_name_input)

        if parsed_last_name.isalpha():
            if len(parsed_last_name) < 2:
                print('Type a last name with at least 2 characters')
            else:
                break
        else:
            print('Invalid Input')

    full_name_array = [parsed_first_name, parsed_last_name]
    full_name_string = ' '.join(full_name_array)
    return full_name_string


def add_date():
    while True:
        date_input = input('Type birthday date in format dd-mm-yyyy: ')
        parsed_date = parse_date(date_input)

        if parsed_date is None:
            print('Invalid Input!')
        else:
            return parsed_date


def update_json_file(dic):
    with open('birthdays.json', 'w') as file:
        json.dump(dic, file, default=str)

    print('This name was added to the birthday dictionary!')
    print()


def check_name_in_dict(name, dic):
    if name in dict(dic).keys():
        print(f"{name}'s birthday is on {dict(dic)[name]}")
    else:
        print('This name does not exist in the dictionary!')
    print()


def no_birthdays_yet():
    print('Birthdays have not been recorded yet!')


def count_birthday_month(json_dict, month_dict):
    months = []
    for names, string in dict(json_dict).items():
        month_num = int(str(string).split('-')[1])
        months.append(dict(month_dict)[month_num])
    count = Counter(months)
    return count


def print_counted_months(counter_dict):
    for month in dict(counter_dict).keys():
        print(f'There are {dict(counter_dict)[month]} birthday(s) on {month}')
    print()


def plot_histogram(counter_dict, month_dict):
    output_file('plot.html')

    x_categories = [dict(month_dict)[month] for month in dict(month_dict).keys()]
    x_axis = [names for names in dict(counter_dict).keys()]
    y_axis = [dict(counter_dict)[number] for number in dict(counter_dict).keys()]

    plot = figure(x_range=x_categories)
    plot.vbar(x=x_axis, top=y_axis, width=0.5)
    show(plot)
