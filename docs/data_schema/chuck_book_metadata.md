“Here’s a **Recommended Semantic Chunk Schema for book metadata** in Markdown — useful for pairing with your `book_chunks` table and ensuring clean, structured book-level data.”


# 📦 Recommended Semantic Chunk Schema for Book Metadata

**Table name:** `book_metadata`

| 📌 Field        | 💬 Description                                                | 🔑 Example                                      |
|-----------------|-------------------------------------------------------------|------------------------------------------------|
| `book_id`      | Unique book identifier (primary key, referenced in chunks)  | `book-001`                                    |
| `title`        | Full title of the book                                      | `The Book of Knowledge`                       |
| `author`       | Author or authors                                           | `Imam al-Ghazali`                            |
| `translator`   | Translator (if applicable)                                  | `Muhammad Nur`                               |
| `editor`       | Editor (if applicable)                                      | `Ali Ahmad`                                  |
| `publisher`    | Publishing house                                            | `Dar al-Minhaj`                              |
| `edition`      | Edition or version                                          | `2nd edition`                                |
| `isbn`         | ISBN number (if available)                                  | `978-1234567890`                             |
| `language`     | Language code                                               | `ar` / `en`                                  |
| `publication_year` | Year of publication                                     | `2001`                                       |
| `pages`        | Total number of pages                                       | `350`                                        |
| `subject`      | Main subject or genre                                       | `Islamic jurisprudence`                      |
| `keywords`     | Keywords or tags                                            | `[“fiqh”, “knowledge”, “ethics”]`           |
| `summary`      | Short summary or abstract                                   | `A foundational text on seeking knowledge...`|
| `metadata`     | Extra metadata (as JSON)                                    | `{“series”: “Ihya Ulum al-Din”}`            |

“✅ Example JSON Record --------------------- json CopyEdit `{ "book_id": "book-001", "title": "The Book of Knowledge", "author": "Imam al-Ghazali", "translator": "Muhammad Nur", "editor": "Ali Ahmad", "publisher": "Dar al-Minhaj", "edition": "2nd edition", "isbn": "978-1234567890", "language": "ar", "publication_year": 2001, "pages": 350, "subject": "Islamic jurisprudence", "keywords": ["fiqh", "knowledge", "ethics"], "summary": "A foundational text on seeking knowledge...", "metadata": { "series": "Ihya Ulum al-Din" } }` 

* * * 

### ✅ SQL `CREATE TABLE` statement 

```sql
CREATE TABLE book_metadata ( book_id VARCHAR(255) PRIMARY KEY, title TEXT NOT NULL, author TEXT, translator TEXT, editor TEXT, publisher TEXT, edition TEXT, isbn VARCHAR(20), language VARCHAR(10), publication_year INT, pages INT, subject TEXT, keywords JSON, summary TEXT, metadata JSON, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP );`”

