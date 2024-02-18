import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QLineEdit, QListWidget, QMessageBox, QDialog
)
from qdarkstyle import load_stylesheet

class FindBookDialog(QDialog):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Find a Book')
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        self.titleInput = QLineEdit()
        self.titleInput.setPlaceholderText("Enter book title")
        layout.addWidget(self.titleInput)

        self.searchButton = QPushButton('Search')
        self.searchButton.clicked.connect(self.searchBook)
        layout.addWidget(self.searchButton)

        self.setLayout(layout)

    def searchBook(self):
        title_to_find = self.titleInput.text()
        self.library.file.seek(0)
        books = self.library.file.read().splitlines()
        found_book = next((book for book in books if book.startswith(title_to_find)), None)
        if found_book:
            book_info = found_book.split(',')
            QMessageBox.information(self, "Book Found", f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Pages: {book_info[3]}")
        else:
            QMessageBox.information(self, "Book Not Found", "The book you searched for could not be found.")
        self.close()

class Library(QMainWindow):
    def __init__(self, filename='books.txt'):
        super().__init__()
        self.filename = filename
        self.file = open(self.filename, 'a+')  # Open the file in append mode, create if not exists
        self.initUI()

    def __del__(self):
        self.file.close()  # Close the file when the object is destroyed

    def initUI(self):
        self.setWindowTitle('Library Management System')
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout()

        self.bookListWidget = QListWidget()
        layout.addWidget(self.bookListWidget)

        self.addButton = QPushButton('Add Book')
        self.addButton.clicked.connect(self.addBook)
        layout.addWidget(self.addButton)

        self.removeButton = QPushButton('Remove Book')
        self.removeButton.clicked.connect(self.removeBook)
        layout.addWidget(self.removeButton)

        self.listButton = QPushButton('List Books')
        self.listButton.clicked.connect(self.listBooks)
        layout.addWidget(self.listButton)

        self.findButton = QPushButton('Find Book')
        self.findButton.clicked.connect(self.showFindBookDialog)
        layout.addWidget(self.findButton)

        self.titleInput = QLineEdit()
        self.titleInput.setPlaceholderText("Enter book title")
        layout.addWidget(self.titleInput)

        self.authorInput = QLineEdit()
        self.authorInput.setPlaceholderText("Enter author name")
        layout.addWidget(self.authorInput)

        self.yearInput = QLineEdit()
        self.yearInput.setPlaceholderText("Enter release year")
        layout.addWidget(self.yearInput)

        self.pagesInput = QLineEdit()
        self.pagesInput.setPlaceholderText("Enter number of pages")
        layout.addWidget(self.pagesInput)

        self.centralWidget.setLayout(layout)

    def listBooks(self):
        self.bookListWidget.clear()
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            self.bookListWidget.addItem(book)

    def addBook(self):
        title = self.titleInput.text()
        author = self.authorInput.text()
        year = self.yearInput.text()
        pages = self.pagesInput.text()
        if all([title, author, year, pages]):
            book_info = f"{title},{author},{year},{pages}\n"
            self.file.write(book_info)
            self.file.flush()
            self.titleInput.clear()
            self.authorInput.clear()
            self.yearInput.clear()
            self.pagesInput.clear()
            self.listBooks()
        else:
            QMessageBox.warning(self, "Incomplete Details", "Please enter all details for the book.")

    def removeBook(self):
        selected_items = self.bookListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Needed", "Please select a book to remove.")
            return
        selected_item = selected_items[0]
        title_to_remove = selected_item.text().split(',')[0]

        self.file.seek(0)
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            if not book.startswith(title_to_remove):
                self.file.write(book)
        self.listBooks()

    def showFindBookDialog(self):
        self.findBookDialog = FindBookDialog(self)
        self.findBookDialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())
    libApp = Library()
    libApp.show()
    sys.exit(app.exec())
