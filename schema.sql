CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL,
    gst REAL,
    total REAL,
    payment TEXT,
    date TEXT
);
