# 📚 Turath JSON to CSV Converter

This project provides a full pipeline to process structured Arabic heritage book data (Turath) in JSON format and convert it into structured CSV outputs for further use in:

- Database ingestion
- Knowledge graph construction
- NLP processing
- RAG (Retrieval-Augmented Generation)
- dbt data modeling
- Airbyte pipelines

---

## 🧠 Approach

The script performs the following major steps:

### 1. Walk Through JSON Files
It recursively searches through a given directory (`./turath_books_json`) to find `.json` files representing books.

### 2. Parse Book-Level Metadata
Extracts:
- Author's starting page
- Short/long metadata sections
- Optional non-author contributors

### 3. Process Volume & Section Indexes
Extracts:
- Volume IDs and page bounds
- Headings and section hierarchy
- Page-to-heading and heading-to-page mappings

### 4. Extract and Normalize Content Per Page
- Splits content into header sections using `<span>` tags
- Maps inline and footer references
- Generates `slug` and `section_number` per heading
- Extracts hierarchical structure of content

### 5. Consolidate and Save as CSV
All extracted entities are stored in dedicated CSVs under the output directory:

---

## 🗃️ Output Structure

| File | Description |
|------|-------------|
| `pages.csv` | Raw page content (text, volume, page ID) |
| `meta.csv`, `info.csv`, `info_long.csv` | Book-level metadata |
| `volume.csv`, `volume_bound.csv`, `volume_pair.csv` | Volume structure and page mapping |
| `headings.csv`, `headings_processed.csv` | Hierarchical section info |
| `headers_titles.csv`, `headers_text.csv` | Header parsing from page content |
| `ref_text.csv`, `footer_ref.csv` | Inline and footer references |
| `section_pages.csv`, `page_headings.csv` | Mappings of pages to sections/headings |

Each file includes `book_id` to preserve origin.

---

## 🛠️ Usage

```bash
python turath_json_to_csv.py
```

---

## 🧩 Integration 

### 🔁 With Airbyte 
- Convert the `entity_definitions.yaml` to `catalog.json` for Airbyte ingestion. 
- Load CSVs into any destination (e.g. PostgreSQL, BigQuery) using the schema. 

### 🧱 With dbt * Use the `entity_definitions.yaml` to create `schema.yml`. 

* Add tests like `not_null`, `unique`, and relationships. 
* Build transformations or docs in dbt using the generated structured data. 

---

## ✅ Requirements 
* Python 3.8+ * Dependencies: 
* `pandas` 
* `beautifulsoup4` 
* `camel-tools` 

Install: 
```bash 
pip install pandas beautifulsoup4 camel-tools

``` 

---

## 📂 Project Structure 

```bash
turath_json_to_csv.py 
```
---

## It includes: 
* `turath_json_to_csv.py` (placeholder) 
* `README.md` (placeholder) 
* `schema.yml` (for dbt) 
* `catalog.json` (for Airbyte) 
* `entity_definitions.yaml` 
* Folder structure for `turath_books_json/` and `output`

---

## 👨‍💻 Author 

Created by \[m.lotfi\] — for processing classical Islamic and Arabic texts using modern data engineering pipelines. 

---

## 📬 Contributions 
PRs, issues, and feedback welcome!

Open to improvements in: 
* Multi-volume processing 
* Graph-based relation extraction 
* Language model enrichment”

