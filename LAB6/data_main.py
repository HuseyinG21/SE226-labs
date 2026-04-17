from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

def main():
    user_input = input(
        "Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): "
    )

    try:
        # Split and clean
        raw_list = user_input.split(",")
        cleaned_strings = strip_whitespaces(raw_list)

        # Convert to float
        numbers = [float(x) for x in cleaned_strings if x != ""]

        # Remove duplicates
        unique_numbers = remove_duplicates(numbers)

        print(f"Cleaned and unique data: {unique_numbers}")
        print("--------------------")

        print(f"Mean: {calculate_mean(unique_numbers):.2f}")
        print(f"Maximum: {find_maximum(unique_numbers)}")
        print(f"Minimum: {find_minimum(unique_numbers)}")

    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")

if __name__ == "__main__":
    main()