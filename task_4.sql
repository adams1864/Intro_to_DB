-- Query the column details of the Books table in alx_book_store
USE alx_book_store;

-- Retrieve column names and types for the Books table
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books';
