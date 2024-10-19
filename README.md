Project Title: Action Item Extractor with AI
Overview
This Python project automates the process of extracting action items from PDF meeting minutes using OpenAI's GPT-4 API. It formats the dates in a standard format and stores the extracted action items in an SQLite database, making it easier to track and manage tasks, particularly when integrating with task management tools like Microsoft To Do.

Features
PDF Text Extraction: Uses PyPDF2 to extract text from meeting minutes stored in a PDF file.
AI-Powered Action Item Extraction: Utilizes OpenAI's GPT-4 to identify and extract action items from the text.
Date Formatting: Automatically detects dates within the action items and formats them in YYYY-MM-DD format. Relative date phrases (e.g., "next week") are also resolved.
SQLite Database Integration: The extracted action items and their corresponding dates are stored in an SQLite database.
Null Handling: Action items without a clear due date are assigned a null value in the database.
Prerequisites
Python 3.x
PyPDF2
OpenAI Python Client
SQLite3 (part of Python’s standard library)
