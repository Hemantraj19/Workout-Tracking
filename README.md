# Exercise Tracker

This Python script allows you to track your exercises using the Nutritionix API and store the data in a Google Sheets document using the Sheety API.

## Setup

1. **Nutritionix API:**
    - Obtain your Nutritionix API credentials by signing up on their [website](https://www.nutritionix.com/business/api).
    - Replace `"your app id"` and `"your api key"` in the code with your actual App ID and API Key.

2. **Sheety API:**
    - Set up a Google Sheets document and integrate it with Sheety. Follow the instructions on the [Sheety website](https://sheety.co/) to create an endpoint for your Google Sheets document.
    - Replace `"your sheet endpoint"` in the code with your actual Sheety endpoint.
    - Replace `"your bearer token"` with your actual Bearer Token.

3. **Dependencies:**
    - Ensure you have the `requests` library installed. If not, you can install it using `pip install requests`.

## Usage

1. Run the script, and it will prompt you to input details about the exercise you did (For eg: I ran for 20 minutes and cycled for 30 minutes).

2. The script will use the Nutritionix API to analyze the exercise input and retrieve relevant data, it will also calculate calories burned on its own.

3. The obtained exercise data will be formatted and sent to your Google Sheets document via the Sheety API.

## Code Explanation

- The script starts by importing the necessary libraries (`requests` and `datetime`) and setting up API credentials and endpoints.

- It prompts the user to input details about the exercise and sends the input to the Nutritionix API using a POST request.

- The response from Nutritionix is processed, and the relevant exercise data is extracted.

- The current date and time are obtained using the `datetime` module.

- The formatted exercise data is sent to the Sheety API, updating the Google Sheets document.

- The script prints the response from Sheety, indicating the success or failure of the data update.

Feel free to customize the script according to your specific requirements.
