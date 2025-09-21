# BrowserAct + Make Webhook Integration

This project provides a simple Python script to send parsed data (JSON) from [BrowserAct](https://browseract.com) to a [Make.com](https://www.make.com) webhook.  
It allows you to easily connect web scraping workflows with apps like Google Sheets, Slack, or Email.

---

##Features
- Cleans JSON data (`null` → empty string).
- Sends each item to a Make webhook URL.
- Handles errors and retries.
- Supports batch sending with delays to avoid overload.

---
You need to replace the file in the script with your own when you have json, then run the script, and then get the link to your webhook in Make. 

## 📂 Project structure
