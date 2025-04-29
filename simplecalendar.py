# Calendar Generator for a Given Year
# Coded by: Moduyadi

import calendar

class Coder:
    def __init__(self, year):
        self.year = year

    def generate_calendar(self, filename="calendar.txt"):
        header = f"Calendar for the Year {self.year}"
        separator = "=" * len(header)

        # Write to file and print to screen
        with open(filename, "w") as file:
            print(header)
            print(separator)
            file.write(header + "\n" + separator + "\n")

            for month in range(1, 13):
                month_title = f"{calendar.month_name[month]} {self.year}".center(28, "-")
                month_output = calendar.month(self.year, month)

                print("\n" + month_title)
                print(month_output)

                file.write("\n" + month_title + "\n")
                file.write(month_output + "\n")

        print(f"\nFull calendar saved to '{filename}'.")

# Example usage
my_calendar = Coder(2025)
my_calendar.generate_calendar()