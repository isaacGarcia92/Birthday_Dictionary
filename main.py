import functions
import json


def main():
    functions.initial_greeting()

    while True:
        with open('birthdays.json', 'r') as file:
            birthdays = json.load(file)

        user_option = functions.choose_option()

        if user_option == 1:
            if len(birthdays) == 0:
                functions.no_birthdays_yet()
            else:
                user_name = functions.validate_names()
                functions.check_name_in_dict(user_name, birthdays)

        elif user_option == 2:
            full_name = functions.add_full_name()
            date = functions.add_date()
            birthdays[full_name] = date
            functions.update_json_file(birthdays)

        elif user_option == 3:
            if len(birthdays) == 0:
                functions.no_birthdays_yet()
            else:
                functions.print_names(birthdays)

        elif user_option == 4:
            if len(birthdays) == 0:
                functions.no_birthdays_yet()
            else:
                counted_months = functions.count_birthday_month(birthdays, functions.months_dict)
                functions.print_counted_months(counted_months)

        elif user_option == 5:
            if len(birthdays) == 0:
                functions.no_birthdays_yet()
            else:
                counted_months = functions.count_birthday_month(birthdays, functions.months_dict)
                functions.plot_histogram(counted_months, functions.months_dict)

        else:
            functions.goodbye_greeting()
            break


if __name__ == '__main__':
    main()
