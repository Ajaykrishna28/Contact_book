# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:31:03 2024

@author: Ajaykrishna28
"""

import json

# File to store contact information
CONTACTS_FILE = 'contacts.json'

# Global variable to store contacts
contacts = {}
2

# To load contacts from file
def load_contacts():
    global contacts
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

# To save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# To add a new contact
def add_contact():
    global contacts
    name = input(" Enter Name: ")
    phone = input(" Enter Phone number: ")
    email = input(" Enter Email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f" Contact {name} added. ")

# To view all contacts
def view_contacts():
    global contacts
    if not contacts:
        print(" No contacts found. ")
    else:
        print(" Contact List: ")
        for name, info in contacts.items():
            print(f" Name: {name}, Phone: {info['phone']}, Email: {info['email']} ")

# To edit an existing contact
def edit_contact():
    global contacts
    name = input(" Enter the name of the contact to edit: ")
    if name in contacts:
        print(f" Editing contact {name} ")
        phone = input(f" Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f" Enter new email address (current: {contacts[name]['email']}): ")
        contacts[name] = {' phone ': phone, ' email ': email}
        print(f" Contact {name} updated. ")
    else:
        print(f" Contact {name} not found. ")

# To delete a contact
def delete_contact():
    global contacts
    name = input(" Enter the name of the contact to delete : ")
    if name in contacts:
        del contacts[name]
        print(f" Contact {name} deleted. ")
    else: 
        print(f" Contact {name} not found. ")


load_contacts()  # Load contacts when the program starts

while True:
    print("\n Contact Manager ")
    print(" 1. Add new Contact ")
    print(" 2. View your Contacts ")
    print(" 3. Edit Contact ")
    print(" 4. Delete Contact ")
    print(" 5. Save Contacts ")
    print(" 6. Exit ")
    choice = input(" Enter your Choice : ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        save_contacts()
        print(" Contacts saved. ")
    elif choice == '6':
        save_contacts()
        print(" Exiting the program. ")
        break
    else:
        print(" Invalid choice. Please try again. ")
