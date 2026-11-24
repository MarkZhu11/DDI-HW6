Yanhan Zhu yz11501

0. description

The bookstore database  has two tables, 'category'and 'book', with 4 categories and 12 books. The Python program lets the user view, search, add, update, and delete books from the command line.

1. to create database

```bash
sqlite3 bookstore.db < createTables.sql
sqlite3 bookstore.db < insertRows.sql
```

2. run python program

```bash
python3 bookstore_cli.py
```

3. the extra feature

I add the extra feature: search books by author (menu option 9).
