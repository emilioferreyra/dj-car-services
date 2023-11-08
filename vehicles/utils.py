import datetime


def select_vehicle_year():
    # Get the current year
    current_year = datetime.datetime.now().year

    # Calculate the range of available years from 1970 to the next year
    available_years = list(range(1970, current_year + 1))

    # Display the available years to the user
    print("Available years to choose from:")
    for year in available_years:
        print(year)

    while True:
        try:
            # Ask the user to enter the vehicle year
            chosen_year = int(input("Select the vehicle year: "))

            # Check if the entered year is in the list of available years
            if chosen_year in available_years:
                return chosen_year
            else:
                print("Invalid year. Please enter a year within the available range.")
        except ValueError:
            print("Please enter a valid year (integer).")
