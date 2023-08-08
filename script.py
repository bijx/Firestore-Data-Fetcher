import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from google.cloud.firestore_v1 import _helpers

class FirestoreEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, _helpers.DatetimeWithNanoseconds):
            return obj.rfc3339()
        return super().default(obj)

def fetch_firestore_data(collection_name, credential_path, output_path):
    # Initialize the SDK
    cred = credentials.Certificate(credential_path)
    firebase_admin.initialize_app(cred)

    # Get a reference to the Firestore service
    db = firestore.client()

    # Fetch all documents from the specified collection
    docs = db.collection(collection_name).stream()

    # Convert the documents to a dictionary format
    data = {doc.id: doc.to_dict() for doc in docs}

    # Save the data to a .json file using the custom encoder
    with open(output_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, cls=FirestoreEncoder)

    print(f"Data saved to {output_path}")

# Usage:
fetch_firestore_data('collection_name', 'path_to_your_credentials.json', 'output.json')
