import csv
import re
from collections import defaultdict

# === Step 1: Load contact details from CSV ===
def load_contacts(csv_path):
    contacts = {}

    # Open the CSV file that contains the contact list
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Combine first, middle, and last name into full name
            name_parts = [row.get('First Name', ''), row.get('Middle Name', ''), row.get('Last Name', '')]
            name = ' '.join(part for part in name_parts if part).strip()

            # Get phone number
            phone = row.get('Phone 1 - Value')

            if name and phone:
                # Remove non-digit characters from phone number
                digits = re.sub(r'\D', '', phone)

                # Standardize to format like '919876543210' (India)
                if digits.startswith('91') and len(digits) > 10:
                    digits = digits[-10:]  # Keep last 10 digits
                    digits = '91' + digits

                # Add to dictionary: phone -> name
                contacts[digits] = name

    return contacts

# === Step 2: Extract birthday messages from WhatsApp chat ===
def extract_birthdays(chat_path):
    # Regular expression to find lines with "Happy birthday @<number>"
    # Also captures the date of the message
    bday_pattern = re.compile(r'^(\d{1,2}/\d{1,2}/\d{2}),\s+\d{1,2}:\d{2}.*?@(\d+)', re.IGNORECASE)

    birthday_mentions = defaultdict(list)  # phone -> list of birthday messages
    birthday_dates = {}                   # phone -> first date mentioned

    # Open the WhatsApp chat file line by line
    with open(chat_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = bday_pattern.search(line)
            if match:
                date, phone = match.groups()
                birthday_mentions[phone].append(line.strip())

                # Only keep the first detected birthday date
                if phone not in birthday_dates:
                    birthday_dates[phone] = date

    return birthday_mentions, birthday_dates

# === Step 3: Combine everything and save to CSV ===
def save_birthdays_to_csv(chat_path, contacts_path, output_path):
    # Load contact mapping from CSV
    contacts = load_contacts(contacts_path)

    # Extract birthday wishes and dates from WhatsApp chat
    mentions, mention_dates = extract_birthdays(chat_path)

    # Open output CSV file to write the results
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write column headers
        writer.writerow(['Name', 'Phone', 'Wishes', 'Birthday Date'])

        # Write one row per person with birthday mentions
        for phone, lines in mentions.items():
            name = contacts.get(phone, f"Unknown")               # Get name from contacts
            date = mention_dates.get(phone, "Unknown")           # Get date of birthday wish
            writer.writerow([name, phone, len(lines), date])     # Write to file

# === Step 4: Run everything ===

# Input paths
chat_file = "WhatsApp Chat with Synchronoise.txt"  # exported WhatsApp chat
contacts_file = "contacts.csv"                     # exported Google contacts
output_file = "birthday_summary_with_dates.csv"    # where results will be saved

# Run the program
save_birthdays_to_csv(chat_file, contacts_file, output_file)

print(f"Birthday summary saved to: {output_file}")
