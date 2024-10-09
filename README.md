# TAPS-Parking

### Overview
The TAPS-Parking project automates the process of filling out a Google Form using Python and Selenium. This script allows users to efficiently submit information from a CSV/Excel file. The repo aims to automate the mundane task of filling a google form over 100 times in a single day.

### Prerequisites
- Python 3.x
- Selenium library
- Chrome Browser
- python-dotenv library for managing environment variables
- A CSV/Excel file formatted as specified below

### Installation
1. Clone the repo:
```bash
git clone https://github.com/dedsec995/TAPS-Parking.git
cd TAPS-Parking
```
2. install the required packages:
```bash
pip install requirements.txt
```
3. Set up the environment variables by creating a `.env` file in the root directory of the project:
```env
EMAIL=your_email@example.com
PASS=your_password
```
4. Ensure you have the appropriate WebDriver for chrome browser and it’s in your system’s PATH.

### CSV/Excel Format
The CSV/Excel file must contain the following columns in this exact order:
```mathematica
Lot, Open, Meter, S&S, ADA, Reserved, Loading, Event, Snow, Construction
```
Make sure that the Lot name matches the names used in the Google Form.
Each of the csv/excel can have 3 different shift times. E.g. `8-10`,`10-12`,`12-2`

### Usage
1. Ensure that your CSV/Excel file has correct name in python file and located in the project directory.
2. Update the selected_sheet variable in the script to reflect the correct sheet name
3. Run the script:
```bash
python final.py
```
Follow the prompt to complete two-factor authentication (2FA), type in any character and let the magic begin.

### Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or new features.