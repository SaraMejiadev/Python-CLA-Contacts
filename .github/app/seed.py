# app/seed.py
from models import Contact

# Seed data
contacts_data = [
    {"first_name": "John", "last_name": "Doe"},
    {"first_name": "Jane", "last_name": "Doe"},
    # Add more contacts as needed
]

# Seed the database
Contact.insert_many(contacts_data).execute()
