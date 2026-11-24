PRAGMA foreign_keys = ON;

CREATE TABLE category (
    categoryId INTEGER PRIMARY KEY,
    categoryName TEXT NOT NULL,
    categoryImage TEXT
);

CREATE TABLE book (
    bookId INTEGER PRIMARY KEY,
    categoryId INTEGER NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT,
    readNow INTEGER,
    FOREIGN KEY (categoryId) REFERENCES category(categoryId)
);
