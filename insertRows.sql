INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Science Fiction', 'science-fiction-category.jpg'),
(2, 'Fantasy', 'fantasy-category.jpg'),
(3, 'Mystery and Thriller', 'mystery-thriller-category.jpg'),
(4, 'Nonfiction', 'nonfiction-category.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Dune', 'Frank Herbert', '9780441013593', 18.00, 'dune.jpg', 1),
(2, 1, 'Neuromancer', 'William Gibson', '9780441569595', 11.99, 'neuromancer.jpg', 0),
(3, 1, 'The Left Hand of Darkness', 'Ursula K. Le Guin', '9780441478125', 10.99, 'left-hand-of-darkness.jpg', 0),
(4, 2, 'The Hobbit', 'J.R.R. Tolkien', '9780547928227', 18.99, 'hobbit.jpg', 1),
(5, 2, 'A Game of Thrones', 'George R.R. Martin', '9780553593716', 9.99, 'game-of-thrones.jpg', 0),
(6, 2, 'The Name of the Wind', 'Patrick Rothfuss', '9780756404741', 10.99, 'name-of-the-wind.jpg', 1),
(7, 3, 'Gone Girl', 'Gillian Flynn', '9780307588371', 18.00, 'gone-girl.jpg', 0),
(8, 3, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', '9780307454546', 16.00, 'dragon-tattoo.jpg', 0),
(9, 3, 'And Then There Were None', 'Agatha Christie', '9780062073488', 9.99, 'and-then-there-were-none.jpg', 1),
(10, 4, 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', '9780062316110', 27.99, 'sapiens.jpg', 1),
(11, 4, 'Educated', 'Tara Westover', '9780399590504', 30.00, 'educated.jpg', 0),
(12, 4, 'Cosmos', 'Carl Sagan', '9780345539434', 22.00, 'cosmos.jpg', 0);
