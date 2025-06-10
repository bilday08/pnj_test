DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    created_at TEXT
);

INSERT INTO customers (name, email, phone, created_at) VALUES
('Alice Tran', 'alice@example.com', '0909123456', '2023-11-01T10:00:00'),
('Bob Le', 'bob@example.com', '0933123456', '2023-12-01T12:00:00');
