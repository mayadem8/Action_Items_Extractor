import PyPDF2
import openai
from datetime import datetime
import sqlite3


with open("API_KEY.txt", "r") as file:
    api_key = file.read().strip()

openai.api_key = api_key
today_date = datetime.now()

all_text = ""


with open(
    "C:\\Users\\Maya\\Desktop\\Python\\Microsoft To Do List\\OneSource Consulting Client.pdf",
    "rb",
) as file:
    reader = PyPDF2.PdfReader(file)

    num_pages = len(reader.pages)

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        all_text += text + "\n"

prompt = f""""
          Here is a text:\n\n{all_text}\n\nExtract only the action items from the following text. 
          Do not include any headings or names. If an action item has a specific date, include it. 
          Format all possible dates in the format 'YYYY-MM-DD' (for example, 25th October 2024 should be written as '2024-10-25'). 
          If the date is mentioned as a relative term (like 'next week' or 'in two weeks'), calculate and display the exact 
          date based on {today_date} in the same 'YYYY-MM-DD' format. 
          If the date is unknown (like 'TBD' or 'as soon as possible'), write 'null' but still display this action item. 
          Please ensure to include any action items listed. Separate action item and (date or 'null') with a percentage symbol. 
          Example: ' Action item description % 2024-10-25'
          """

response = openai.ChatCompletion.create(
    model="gpt-4", messages=[{"role": "user", "content": prompt}], max_tokens=500
)


response_text = response["choices"][0]["message"]["content"].strip()
print(response_text)


conn = sqlite3.connect("action_items.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS action_items")


cursor.execute(
    """
CREATE TABLE IF NOT EXISTS action_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    due_date DATE
)
"""
)


action_items = response_text.split("\n")

for item in action_items:
    description_date_split = item.split(" % ")
    description = description_date_split[0].strip()
    due_date = description_date_split[1].strip()

    cursor.execute(
        """
        INSERT INTO action_items (description, due_date)
        VALUES (?, ?)
        """,
        (description, due_date if due_date != "null" else None),
    )

conn.commit()
conn.close()
