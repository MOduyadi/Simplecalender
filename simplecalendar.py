# Calendar Generator for a Given Year
# Coded by: Moduyadi

import calendar

class Coder:
    def __init__(self, year):
        self.year = year

    def generate_calendar(self, filename="calendar.txt", events=None):
        if events is None:
            events = {}
        header = f"Calendar for the Year {self.year}"
        separator = "=" * len(header)

        # Write to file and print to screen
        with open(filename, "w") as file:
            print(header)
            print(separator)
            file.write(header + "\n" + separator + "\n")

            cal = calendar.Calendar()
            for month in range(1, 13):
                month_title = f"{calendar.month_name[month]} {self.year}".center(28, "-")
                month_output = calendar.month(self.year, month)

                # --- Event Highlighting Logic ---
                dates_with_events = []
                for date_obj in cal.itermonthdates(self.year, month):
                    # Process only dates belonging to the current month
                    if date_obj.year == self.year and date_obj.month == month:
                        formatted_date = date_obj.strftime('%Y-%m-%d')
                        if formatted_date in events:
                            dates_with_events.append(date_obj.day)

                # Modify month_output string to add '*'
                if dates_with_events:
                    lines = month_output.split('\n')
                    header_line = lines[0] # Weekday names (Mo Tu We Th Fr Sa Su)
                    day_lines = lines[1:]
                    modified_lines = [header_line]

                    for line in day_lines:
                        new_line = line
                        for day in dates_with_events:
                            # Need to handle spacing carefully: day could be ' 5' or '15'
                            # Try replacing space-padded day followed by space or newline
                            day_str_pad_space = f"{day: >2} "
                            day_str_pad_event = f"{day: >2}*" # Note: Adds *, might slightly misalign
                            
                            # If the day string is exactly 2 chars (e.g., ' 5', '15')
                            if day_str_pad_space in new_line:
                                new_line = new_line.replace(day_str_pad_space, day_str_pad_event)
                                # Check if it was at the end of the line (no trailing space)
                            elif new_line.endswith(f"{day: >2}"):
                                new_line = new_line[:-len(f"{day: >2}")] + day_str_pad_event
                                
                        modified_lines.append(new_line)
                    month_output = "\n".join(modified_lines)
                # --- End Event Highlighting ---


                print("\n" + month_title)
                print(month_output)

                file.write("\n" + month_title + "\n")
                file.write(month_output + "\n")

            # Add legend
            legend = "\n* : Indicates a day with an event"
            print(legend)
            file.write(legend + "\n")

        print(f"\nFull calendar saved to '{filename}'.")

if __name__ == "__main__":
    # Get year input from user with validation
    while True:
        try:
            year_input = input("Enter the year for the calendar: ")
            year = int(year_input)
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a valid integer year.")

    # --- Define your events here ---
    # Add events to this dictionary with 'YYYY-MM-DD' as the key
    # and the event description as the value.
    # You can use f-strings to include the user's input year,
    # or use fixed dates. Modify this section before running the script.
    events = {
        f"{year}-01-01": "New Year's Day",  # Example using the input year
        f"{year}-10-31": "Halloween",        # Example using the input year
        # "2024-12-25": "Example Christmas (fixed date)" # Example with a fixed date
    }

    # Instantiate the calendar generator with the user's year
    my_calendar = Coder(year)

    # Generate the calendar, passing the events dictionary
    my_calendar.generate_calendar(events=events)