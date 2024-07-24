## Library Management System

### Prerequisites

- Python 3.10+

### Description

The Library Management System is a console-based Python application that helps users manage a collection of books. The application allows users to add, remove, search, display, and update the status of books. Each book is represented by its title, author, publication year, and current status (available or issued).

### Features

- **Add a Book**: Users can add new books to the library by providing the title, author, and year of publication. Each book is assigned a unique ID and marked as "available" by default.
- **Remove a Book**: Users can remove books from the library using the book's ID.
- **Search for Books**: Users can search for books by title, author, or publication year.
- **Display All Books**: The system displays a list of all books, including their ID, title, author, year of publication, and status.
- **Update Book Status**: Users can update the status of a book (e.g., mark it as "issued" or "available").

### Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/erastoff/mylibManager.git
   cd mylibManager

2. Install dependencies: This project has no external dependencies, just for lintering

3. Run the application:

   ```bash
   python main.py
   ```
4. Follow the on-screen instructions to manage your library, including adding, removing, and updating books.

### Testing

- The project includes tests to ensure functionality works as expected.

   ```bash
   python test_main.py
   ```