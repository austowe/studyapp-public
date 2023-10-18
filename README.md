# studyapp-public

StudyApp is a Python tool designed to assist students in preparing for tests using AI. This project is in its early stages and has the potential for a lot of growth. Included in this repository is a scraper script that parses Learning Suite practice tests/quizzes, saving the questions to the `questions.json` question bank. The practice script allows users to take console-based practice tests and provides AI-powered insights when mistakes are made.

## Dependencies

- `scraper.py` - Beautiful Soup
- `practice.py` - OpenAI

## Instructions

1. Create a `keys.py` file in the project directory with your own OpenAI credentials:

   ```python
   openai_org = 'YOUR_ORG_ID'
   openai_api_key = 'YOUR_API_KEY'
   ```

2. Run the scraper to collect practice test data:

   ```
   python scraper.py
   ```

3. Start the practice test:

   ```
   python practice.py
   ```

The scraper should only be run when new questions are ready to be added. HTML from the target page needs to be acquired separately. In the case of Learning Suite, this can be achieved with a Selenium scraper.
