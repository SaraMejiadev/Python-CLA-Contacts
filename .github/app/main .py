# app/main.py
import argparse
from models import Contact

def add_contact(first_name, last_name):
    Contact.create(first_name=first_name, last_name=last_name)

def list_contacts():
    contacts = Contact.select()
    for contact in contacts:
        print(f"{contact.first_name} {contact.last_name}")

def find_contact(first_name):
    contacts = Contact.select().where(Contact.first_name == first_name)
    for contact in contacts:
        print(f"{contact.first_name} {contact.last_name}")

def main():
    parser = argparse.ArgumentParser(description='Contact Book CLI')
    parser.add_argument('command', choices=['add', 'list', 'find'], help='Command to execute')
    parser.add_argument('--first_name', help='First name of the contact')

    args = parser.parse_args()

    if args.command == 'add':
        add_contact(args.first_name, input('Enter last name: '))
    elif args.command == 'list':
        list_contacts()
    elif args.command == 'find':
        find_contact(args.first_name)

if __name__ == "__main__":
    main()
