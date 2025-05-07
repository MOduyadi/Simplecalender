# Simple Calendar

A Python script to generate a full year's calendar, save it to a file, and highlight custom event dates.

## Features

*   **Interactive Year Input:** Prompts the user to enter the desired year for the calendar.
*   **Console Output:** Prints the formatted calendar for the specified year directly to the console.
*   **File Output:** Saves the generated calendar to a text file (default: `calendar.txt`).
*   **Event Highlighting:** Marks dates with events using an asterisk (`*`) next to the day number.
*   **Customizable Events:** Allows users to define their own events within the script.
*   **Legend:** Includes a legend (`* : Indicates a day with an event`) at the end of the output.

## Usage

1.  Save the code as `simplecalendar.py`.
2.  Run the script from your terminal:
    ```bash
    python simplecalendar.py
    ```
3.  The script will prompt you to enter the year. Type the year and press Enter.
4.  The calendar for the entered year will be printed to the console and saved to `calendar.txt` in the same directory.

## Customizing Events

You can add your own events to be highlighted on the calendar:

1.  Open the `simplecalendar.py` script in a text editor.
2.  Locate the `if __name__ == "__main__":` block near the end of the file.
3.  Find the `events` dictionary definition.
4.  Add your events using the format `'YYYY-MM-DD': 'Your Event Description'`. You can use f-strings with the `year` variable if the event occurs annually, or use fixed dates.

    ```python
    # --- Define your events here ---
    # Add events to this dictionary with 'YYYY-MM-DD' as the key
    # and the event description as the value.
    events = {
        f"{year}-01-01": "New Year's Day",
        f"{year}-07-04": "Independence Day (US)", # Example using the input year
        "2024-12-25": "Example Fixed Date Event" # Example with a fixed date
        # Add your custom events here:
        # f"{year}-MM-DD": "My Birthday",
    }
    ```
5.  Save the script and run it as described in the Usage section. The dates you added will now be marked with an asterisk (`*`) in the output.
