Webpage Content Automation with Selenium
This Python Selenium script automates the process of logging into SauceDemo and extracting key details like the webpage title, current URL, and its entire content. The content is saved to a text file for further analysis or record-keeping.

Features
Login Automation:

Logs into SauceDemo using provided credentials.
Information Extraction:

Fetches and prints:
Title of the webpage.
Current URL.
Saves the webpage's entire HTML source code to a file named Webpage_task_11.txt.
Automated File Saving:

The webpage content is stored locally in a text file for later use.
Requirements
Python 3.8 or later.
Google Chrome Browser.
Python Libraries:
Selenium: For browser automation.
Webdriver-Manager: For automatic ChromeDriver installation.
Install the required Python libraries:

bash
Copy code
pip install selenium webdriver-manager
Setup and Execution
Clone or Download the Repository:

Download this project and navigate to the directory.
Run the Script:

Execute the script using Python:
bash
Copy code
python script_name.py
Output:

The script will log into SauceDemo and display:
Webpage title.
Current URL.
Saves the full HTML source of the webpage to a file named Webpage_task_11.txt.
Expected Output
Console Output:
arduino
Copy code
Webpage Title: Swag Labs
Current URL: https://www.saucedemo.com/inventory.html
Webpage content saved to 'Webpage_task_11.txt'
Generated File:
Filename: Webpage_task_11.txt
Location: Script's directory.
Content: The full HTML source of the webpage after login.
Code Workflow
Setup WebDriver:
Uses webdriver_manager to configure ChromeDriver automatically.
Access SauceDemo:
Navigates to the SauceDemo website and logs in using provided credentials.
Extract Details:
Fetches the webpage title, URL, and HTML source code.
Save File:
Writes the HTML source to Webpage_task_11.txt.
Cleanup:
Ensures the browser is closed after execution.
Troubleshooting
Driver Issues:

If ChromeDriver fails, ensure your Chrome browser is up-to-date.
Dependencies Not Installed:

Run:
bash
Copy code
pip install selenium webdriver-manager
File Save Errors:

Ensure you have write permissions in the directory.
Enhancements
Add error handling for incorrect login credentials.
Extract specific data (e.g., product names, prices) instead of the entire webpage content.
License
This project is for educational purposes and is free to use. Contributions and enhancements are welcome!

Author
This script is a demonstration of Selenium automation for web scraping and interaction. Feel free to contact me for questions or suggestions!
