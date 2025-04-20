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
