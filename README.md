WhatsApp Birthday Extractor

A lightning-fast mini-project (vibed out in 15 mins 😎) to help club coordinators like me remember birthdays — without ever setting a reminder.

As the coordinator of our club, I kept forgetting people’s birthdays. Thankfully, everyone says “Happy birthday @phone-number” in our WhatsApp group chats — so I automated it!
 What It Does

    Parses a WhatsApp chat export to detect birthday wishes.

    Identifies phone numbers from those wishes.

    Maps phone numbers to names using your exported contacts.

    Saves a clean birthday list in CSV format.

 How to Use

    Clone this repository

git clone https://github.com/your-username/whatsapp-birthday-extractor.git
cd whatsapp-birthday-extractor

Export your WhatsApp chat

    On WhatsApp → Open Group → "More" → "Export chat" → Without media

    Save the .txt file in this project directory.

Export your contacts

    From Google Contacts or your phone

    Save it as a .csv (make sure it includes names and phone numbers)

    Place it in the same directory.

Update the script if needed

    Make sure the filenames in the script match your .txt and .csv file names.

Run the script

    python birthday_extractor.py

    Check your output

        You'll get a birthdays.csv file with all detected birthdays and mapped names 🎂

🛠 Example Output

Phone Number, Name, Birthday Date (First Mention)
+919000271882, Krish Singhvi, 19/12/2024
+917218347988, Soham Walimbe, 15/10/2024
...

 Notes

    It assumes people write “Happy birthday @...” in their wishes.

    If a phone number appears multiple times, the first mention date is used.

    You can easily extend it to include all wishers, count, etc.

 Future Ideas

    Set up a birthday calendar (Google Calendar integration?)

    Slack/Discord bot for birthday reminders

    GUI for non-coders

 Contribute

Got a better regex or idea? PRs welcome.
