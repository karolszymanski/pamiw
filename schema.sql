DROP TABLE IF EXISTS packages;

CREATE TABLE packages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status TEXT NOT NULL,
    package_id TEXT NOT NULL
);