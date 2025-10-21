"""

LEARNING OBJECTIVES:
- Practice CRUD operations with REST APIs
- Implement filtering and searching
- Handle query parameters for sorting and pagination
- Generate summaries and reports
- Work with enumerations and validation

PROJECT OVERVIEW:
Build a REST API to manage a library of books with categories, authors, and reporting features.

INSTRUCTIONS:
Complete the TODO sections below to build a fully functional Book Library AP
Note: Containerize your App
"""

""" Model"""
from enum import Enum
from pydantic import BaseModel
from datetime import date
from typing import List, Optional, Dict

class BookCategory(str, Enum):
    """Enum for book categories"""
    FICTION = "fiction"
    NONFICTION = "nonfiction"
    SCIENCE = "science"
    HISTORY = "history"
    BIOGRAPHY = "biography"
    TECHNOLOGY = "technology"
    OTHER = "other"

class BookCreate(BaseModel):
    title: str
    author: str
    category: BookCategory
    published_date: date

class Book(BookCreate):
    id: int

class AuthorSummary(BaseModel):
    author: str
    book_count: int


class CategorySummary(BaseModel):
    category: str
    book_count: int


""" Databasemodel"""

from typing import List, Optional

class Database:
    """In-memory database template for books"""

    def __init__(self):
        self._books: List[Book] = []
        self._current_id = 1

    def generate_id(self) -> int:
        """Generate next book ID"""
        # TODO: Implement ID generation
        new_id = self._current_id
        self._current_id += 1
        return new_id
          
    def add_book(self, book: BookCreate) -> Book:
        """Add a new book to the database"""
        # TODO: Implement adding a book
        new_book = Book (
            id = self.generate_id(),
            title = book.title,
            author = book.author,
            category = book.category,
            published_date = book.published_date
        )
        self._books.append(new_book)
        return {"data" : new_book,
                "message": "Addded successfuly"}

    def get_all_books(self) -> List[Book]:
        """Return all books"""
        # TODO: Implement retrieving all books
        return self._books

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Find a book by ID"""
        # TODO: Implement lookup by ID
        for book in self._books:
            if book_id == book.id:
                return book
            return "not found"

    def update_book(self, book_id: int, updates: dict) -> Optional[Book]:
        """Update book details by ID"""
        # TODO: Implement update
        for book in self._books:
            if book_id == book.id:
                book.title = updates.title
                book.author = updates.author
                book.category = updates.category
                book.published_date = updates.published_date
                return {
                    "data": book,
                    "message": "updated successful"
                }

    def delete_book(self, book_id: int) -> bool:
        """Delete a book by ID"""
        # TODO: Implement delete
        for book in self._books:
            if book.id == book_id:
                self._books.remove(book)
                return {
                    "data":book,
                    "message": "Deleted successfully"
                }

    def get_books_by_category(self, category: BookCategory) -> List[Book]:
        """Retrieve all books in a given category"""
        # TODO: Implement category filter
        for book in self._books:
            if book.category == category:
                return book

    def get_author_summary(self) -> List[AuthorSummary]:
        """Return count of books per author"""
        # TODO: Implement author summary
        count = {}
        for book in self._books:
            if book.author in count:
                pass
                count[book.author] += 1
            else:
                count[book.author] = 1
        return count

    def get_category_summary(self) -> List[CategorySummary]:
        """Return count of books per category"""
        # TODO: Implement category summary
        count = {}
        for book in self._books:
            if book.category in count:
                count[book.category] += 1
            else:
                count[book.category] = 1
        return count

# dd = Database()
# dd.get_category_summary()
# dd.get_author_summary()
# dd.add_book(BookCreate(title="python",author="ben",category="fiction",published_date="2025-10-19"))
# dd.add_book(BookCreate(title="c",author="com",category="nonfiction",published_date="2025-10-19"))
# dd.add_book(BookCreate(title="c",author="com",category="nonfiction",published_date="2025-10-19"))
# print(dd.get_all_books())
# #print(dd.get_book_by_id(1))
# #print(dd.delete_book(1))
# #print(dd.get_all_books())
# #print(dd.get_books_by_category("fiction"))
# print(dd.get_author_summary())
# print(dd.get_category_summary())

"""
API ENDPOINT
"""

from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

app = FastAPI(title="Book Library API")

db = Database()  # in-memory database instance

@app.post("/books")
def create_book(book: BookCreate):
    """Add a new book"""
    # TODO: Call db.add_book and return the new book
    return db.add_book(book)

@app.get("/books")
def list_books(category: Optional[BookCategory] = None) -> List[Book]:
    """List all books or filter by category"""
    # TODO: Return db.get_all_books or db.get_books_by_category
    if category:
        return db.get_books_by_category(category)
    return db.get_all_books()

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Retrieve a book by ID"""
    # TODO: Return db.get_book_by_id or raise 404
    book = db.get_book_by_id(book_id)
    if not book_id:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updates: BookCreate):
    """Update a book by ID"""
    # TODO: Call db.update_book and return updated book
    updated = db.update_book(book_id,updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """Delete a book by ID"""
    # TODO: Call db.delete_book or raise 404
    deleted = db.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted

@app.get("/summary/authors")
def author_summary():
    """Return summary of books per author"""
    # TODO: Call db.get_author_summary
    return db.get_author_summary()

@app.get("/summary/categories")
def category_summary():
    """Return summary of books per category"""
    # TODO: Call db.get_category_summary
    return db.get_category_summary()
