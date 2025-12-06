# Simple Contact Book Manager

A console-based application to manage contacts, demonstrating fundamental Data Structures and Algorithms (DSA) in Python.

## 📌 Overview

This project is a simple Contact Book Manager that allows users to perform basic operations such as adding, deleting, viewing, and searching for contacts. It is designed to showcase the usage of:
- **Lists**: To store the collection of contacts.
- **Dictionaries**: To represent individual contact details (Name, Phone).
- **Linear Search**: To find a specific contact by name.
- **Sorting**: To display contacts in alphabetical order.

## 🚀 Features

- **Add Contact**: Store a new contact's name and phone number.
- **Delete Contact**: Remove a contact by their name.
- **View Contacts**: See a list of all contacts, automatically sorted alphabetically by name.
- **Search Contact**: Find a contact's details by entering their name.
- **Input Validation**: Basic checks to ensure names and phone numbers are not empty.

## 🛠️ Prerequisites

- **Python 3.x**: Ensure you have Python installed on your system. You can check by running:
  ```bash
  python --version
  ```

## 📂 Project Structure

```
Simple-Contact-Book-Manager/
│
├── contact_manager.py       # Main application script
├── test_contact_manager.py  # Unit tests for the application
├── demo_input.txt           # Sample input for demonstration
└── README.md                # Project documentation
```

## 💻 How to Run

1.  **Navigate to the project directory**:
    ```bash
    cd Simple-Contact-Book-Manager
    ```

2.  **Run the application**:
    ```bash
    python contact_manager.py
    ```

3.  **Follow the on-screen menu**:
    ```text
    === Simple Contact Book Manager ===
    1. Add Contact
    2. Delete Contact
    3. View Contacts (Sorted)
    4. Search Contact
    5. Exit
    ===================================
    Enter your choice (1-5):
    ```

## 🧪 Running Tests

This project includes a unit test suite to verify functionality. To run the tests:

```bash
python test_contact_manager.py
```

## 🔍 Implementation Details

### Data Structures
- **Global List (`contacts`)**: Acts as the main database in memory.
- **Dictionary**: Each contact is stored as `{'name': '...', 'phone': '...'}`.

### Algorithms
- **Sorting**: The `view_contacts` function uses Python's built-in `sorted()` function with a lambda key to sort by name:
  ```python
  sorted(contacts, key=lambda x: x["name"].lower())
  ```
- **Searching**: The `search_contact` function iterates through the list one by one (Linear Search) to find a match.

## 📝 Example Usage

```text
Enter your choice (1-5): 1
Enter Name: Alice
Enter Phone Number: 555-0100
Contact 'Alice' added successfully.

Enter your choice (1-5): 3

--- Contact List (Sorted) ---
Name: Alice, Phone: 555-0100
-----------------------------
```

## ⚠️ Note
This application stores data in **memory (RAM)**. All contacts will be lost when the program is exited. This is by design to keep the implementation simple and focused on in-memory data structures.
