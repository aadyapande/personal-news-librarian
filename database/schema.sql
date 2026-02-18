CREATE TABLE articles (
    article_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    source TEXT NOT NULL,
    section TEXT NOT NULL,
    published_date TEXT NOT NULL,
    author TEXT,
    url TEXT UNIQUE NOT NULL,

    -- TEMPORARY (to be dropped later)
    content TEXT,

    -- PERMANENT
    gist TEXT NOT NULL,
    raw_excerpt TEXT,

    ingested_at TEXT NOT NULL
);
