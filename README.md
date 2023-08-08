# Firebase Firestore Data Fetcher

A simple Python script to fetch documents from a Firebase Firestore collection and save them to a local `.json` file. Helpful when your project is on the free tier and you don't want to enable billing on your account.

## Prerequisites

- Python 3.6+
- Firebase project with Firestore enabled

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/bijx/Firestore-Data-Fetcher.git
   ```

2. Navigate to the project directory:
   ```
   cd Firestore-Data-Fetcher
   ```

3. Install the required packages:
   ```
   pip install firebase-admin
   ```

4. Obtain your Firebase service account key:
   - Go to the Firebase Console.
   - Navigate to your project.
   - Click on "Project settings".
   - Click on the "Service accounts" tab.
   - Generate a new private key.
   - Save the `.json` file with your credentials to the project directory.

## Usage

1. Open the script and replace `'collection_name'` with the name of the Firestore collection you want to fetch.
2. Run the script:
   ```
   python script.py
   ```

3. The data will be saved in a file named `output.json`.

## Notes

- Just a word of caution: Always keep your Firebase service account key secure and never expose it in public locations.
