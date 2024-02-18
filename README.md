### README for Library Management System

This Python script implements a basic Library Management System using PyQt6 for the graphical user interface (GUI) and QDarkStyle for styling. The application allows users to add, remove, list, and search for books in a library. Each book's information includes its title, author, release year, and number of pages. The data is stored in a text file named `books.txt`.

#### Features

- **Add a Book**: Users can enter the details of a book (title, author, release year, and pages) and add it to the library.
- **Remove a Book**: Users can select a book from the list and remove it.
- **List Books**: Displays all the books currently in the library.
- **Find a Book**: Users can search for a book by its title. If the book is found, its details are displayed.

#### Dependencies

- Python 3.x
- PyQt6
- QDarkStyle

#### Installation

1. Ensure Python 3.x is installed on your system.
2. Install PyQt6 and QDarkStyle using pip:

   ```bash
   pip install PyQt6 qdarkstyle
   ```

#### Usage

1. Run the script:

   ```bash
   python library_management_system.py
   ```

2. The application window will open with the title "Library Management System". From here, you can interact with the system to manage your library.

#### Application Structure

- **Main Window (`Library` class)**: The primary interface where users can add, remove, list, and find books.
- **Find Book Dialog (`FindBookDialog` class)**: A pop-up dialog that allows users to search for a book by title.

#### Adding a Book

Fill in the book's title, author, release year, and number of pages in the provided text fields, and click "Add Book" to add the book to the library.

#### Removing a Book

Select a book from the list and click "Remove Book" to remove it from the library.

#### Listing Books

Click "List Books" to refresh and display the current list of books in the library.

#### Finding a Book

Click "Find Book" to open the Find Book Dialog, where you can search for a book by its title.

#### Notes

- The application uses a text file (`books.txt`) to store and manage book data. Ensure this file is in the same directory as the script or update the script with the correct path to the file.
- The QDarkStyle stylesheet enhances the GUI appearance, providing a dark theme for better readability and a modern look.

### Conclusion

This Library Management System is a simple yet effective tool for managing a collection of books. It demonstrates the use of PyQt6 for creating desktop applications with Python. Customizations and extensions can be made to incorporate more complex functionalities as needed.
