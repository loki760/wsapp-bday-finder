# WhatsApp Birthday Extractor

A lightning-fast mini-project (vibed coded in 15 mins 😎) to help club coordinators like me remember birthdays — without ever setting a reminder.

As the coordinator of our club, I kept forgetting people’s birthdays. Thankfully, everyone says *“Happy birthday @phone-number”* in our WhatsApp group chats — so I automated it!

---

## What It Does

- Parses a WhatsApp chat export to detect birthday wishes.
- Identifies phone numbers from those wishes.
- Maps phone numbers to names using your exported contacts.
- Saves a clean birthday list in CSV format.

---

## How to Use

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/whatsapp-birthday-extractor.git
   cd whatsapp-birthday-extractor
   
2. **Export your WhatsApp chat**
   - On WhatsApp → Open the group → Tap menu (⋮) → More → Export chat → Without media
   - Save the exported .txt file in the project directory.
     
3. **Export your contacts**
   - From Google Contacts or your phone
   - Save them as a .csv file (must include at least Name and Phone Number)
   - Place the .csv in the same directory as the script.

4. **Update filenames in the script (if needed)**
   - Make sure the script refers to the correct .txt and .csv filenames.

5. **Run the script**
```bash
   python3 script.py

   


