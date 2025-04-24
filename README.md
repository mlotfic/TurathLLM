## Project: unstructured-to-structured-ai-schema (Main Project)

### Core Goal (from main README)

*   To provide **database schema designs** (blueprints) for transforming unstructured data into structured formats.
*   Target applications include:
    *   **AI & LLMs:** For training, information extraction (NER), semantic enrichment.
    *   **Relational Databases (RDB):** For standard tabular storage (e.g., PostgreSQL, SQLite) and analytical querying.
    *   **Graph Databases (GDB):** For representing complex entities and relationships (e.g., Neo4j).
    *   **Retrieval-Augmented Generation (RAG):** To feed structured, contextual data to LLMs.
*   Focuses on complex data like historical texts (including Islamic sources like Hadith, books), invoices, etc.
*   Aims to bridge relational and graph data models.

### Key Components & Structure (from main README)

*   **`schemas/` directory:** Contains schema definitions for different data sources/types (e.g., `books`, `scraping/alminasadata`).
*   **Schema Files within each sub-directory:**
    *   `rdb_schema.sql`: SQL schema for relational databases.
    *   `gdb_schema.cypher`: Cypher schema for graph databases.
    *   `entity_definitions.yaml`: A crucial human/machine-readable file defining entities and their relationships. This can be used to drive other tools (like dbt, Airbyte).
*   **`examples/`:** Sample input data (e.g., `hadith_chain_example.json`).
*   **`pipelines/`, `scripts/`, `docs/`:** Supporting materials for ETL processes, helper scripts, and documentation.

### Data Sources Explored (from main README)

*   **Books:** OpenITI Corpus, **Turath Platform**, Islamweb Library, Islamic Urdu Books.
*   **Narrators:** MuslimScholars.info, Islamic Urdu Books Rawy List, AlMinasa AI.
*   **APIs:** Hadith API (fawazahmed0).

---

## Component Example: Turath Books Pipeline (`turath_books/README.md`)

This specific component focuses on processing **Turath heritage book data (JSON format)**. It acts as a concrete ETL (Extract, Transform, Load) pipeline within the broader project framework.

### Goal (from turath_books README)

*   To provide a pipeline that converts Turath JSON book data into structured **CSV files**.
*   These CSVs are designed for downstream use in:
    *   Database ingestion (RDB/GDB)
    *   Knowledge graph construction
    *   NLP processing
    *   RAG systems
    *   **dbt** data modeling
    *   **Airbyte** data pipelines

### Approach (from turath_books README)

1.  **Input:** Reads `.json` files from a specified directory (`./turath_books_json`).
2.  **Parsing:** Extracts book metadata, volume/section structures, page content, headers, and references (inline/footer).
3.  **Normalization:** Creates slugs, section numbers, and maps relationships between pages, headings, and volumes.
4.  **Output:** Saves extracted entities into multiple distinct CSV files (e.g., `pages.csv`, `meta.csv`, `headings.csv`, `volume.csv`, `ref_text.csv`, etc.) under an `output` directory. Each CSV includes a `book_id` for traceability.

### Integration (from turath_books README)

*   Explicitly leverages the `entity_definitions.yaml` (likely defined within or aligned with the main project's schema structure) to:
    *   Generate `catalog.json` for **Airbyte** data ingestion pipelines.
    *   Generate `schema.yml` for **dbt** data modeling, testing, and documentation.

### Example Use Cases (from turath_books README)

*   Building Islamic knowledge graphs (narrators, books, references).
*   Training LLMs with fine-tuned book metadata.
*   Searching and referencing Arabic heritage texts.
*   Generating semantic embeddings and document chunking.
*   Ingesting into SQL or graph databases for scholarly research.

### Dependencies (from turath_books README)

*   Python 3.8+
*   `pandas`
*   `beautifulsoup4`
*   `camel-tools` (likely for Arabic text processing)

---

## Overall Summary & Relationship

*   The main `unstructured-to-structured-ai-schema` project defines standardized **schemas** (RDB, GDB) and **entity definitions** (`entity_definitions.yaml`) for organizing complex unstructured data, particularly historical/Islamic texts.
*   The `turath_books` component is a practical **ETL pipeline implementation** within this framework.
*   It takes a specific data source (Turath JSON) and processes it into structured **CSVs**.
*   Crucially, it uses the `entity_definitions.yaml` concept from the main project to facilitate integration with data tools like **Airbyte** and **dbt**.
*   The structured CSV output from `turath_books` is intended to be loadable into databases conforming to the schemas defined in the main project, making it suitable for AI/LLM fine-tuning, knowledge graph population, and RAG applications.

---

## 🧱 Project Structure

```css
turath_books/
            ├── input/                                # Directory for raw Turath JSON files
            │   ├── example_book.json                 # Example input file
            │
            ├── output/                               # Directory for generated CSV files
            │   ├── pages.csv                         # Extracted page-level data
            │   ├── meta.csv                          # Metadata about books
            │   ├── headings.csv                      # Extracted headings/sections
            │   ├── volume.csv                        # Volume-level data
            │   ├── ref_text.csv                      # Inline/footer references
            │
            ├── schemas/                              # Schema definitions for Turath books
            │   ├── rdb_schema.sql                    # Relational DB schema
            │   ├── gdb_schema.cypher                 # Graph DB schema
            │   ├── entity_definitions.yaml           # Entity and relationship definitions
            │
            ├── scripts/                              # Helper scripts for ETL processing
            │   ├── parse_json.py                     # Script to parse Turath JSON files
            │   ├── normalize_data.py                 # Script to normalize and clean data
            │   ├── export_csv.py                     # Script to export data to CSV
            │
            ├── docs/                                 # Documentation for the pipeline
            │   ├── README.md                         # Overview of the Turath Books pipeline
            │   ├── architecture_diagram.png          # Diagram of the ETL process
            │
            ├── tests/                                # Unit tests for the pipeline
            │   ├── test_parse_json.py                # Tests for JSON parsing
            │   ├── test_normalize_data.py            # Tests for data normalization
            │   ├── test_export_csv.py                # Tests for CSV export
            │
            └── README.md                             # Main README for the `turath_books` component
            └── LICENSE
```

Each subfolder (e.g., `islamicurdubooks`, `islamweb`, `hadith-api-1`) includes:

- `rdb_schema.sql` – PostgreSQL/SQLite compatible schema
- `gdb_schema.cypher` – Neo4j schema for graph modeling
- `entity_definitions.yaml` – Describes data entities and relationships
- Example data and diagrams for reference

---

## 📚 Data Sources

Here are the sources being explored for schema extraction and dataset creation:

### 📖 Book Sources
- [OpenITI GitHub Corpus](https://github.com/OpenITI/RELEASE/tree/v2023.1.8)
- [Turath Platform](https://app.turath.io/)
- [Islamweb Library](https://www.islamweb.net/ar/library/index.php?page=bookslist)
- [Islamic Urdu Books](https://islamicurdubooks.com/index.php)

### 👤 Narrator Information
- [MuslimScholars.info](https://muslimscholars.info/manage.php?submit=scholar&ID=3)
- [Islamic Urdu Books Rawy List](https://islamicurdubooks.com/hadith/rawylistcomplete.php?bookid=1&LFirstChar=%d8%a8)
- [AlMinasa AI Project](https://alminasa.ai/)

### 🔗 API & Miscellaneous
- [Hadith API (FawazAhmed)](https://github.com/fawazahmed0/hadith-api/)

These sources are used to derive schemas, sample datasets, and entity relationship models.

---

## 📌 Goal

To enable developers, researchers, and scholars to:

- Rapidly structure unstructured Islamic or historical data
- Build LLM-based applications with integrated knowledge graphs
- Enable RAG pipelines with rich, contextual structured sources
- Connect relational and graph-based knowledge systems

---

## 🔗 Related Projects & References

- [**Bespoke Public Talks**](https://github.com/bespoke-inc/bespoke-public-talks):  
  A full code repo for the tutorial that walks through building AI-powered chatbots, covering foundational concepts to advanced deployment techniques.

- [**Quran Detector (Annotator)**](https://github.com/SElBeltagy/Quran_Detector):  
  A full code repo that capable of identifying any Quranic verse or verse fragment that is equal to or greater than 3 words, in any piece of text.
  The tool is capable of detecting minor typos and even missing words, but it is most efficient when carrying out exact matching.
  Error detection and missing word detection can be enabled and disabled by the programmer using the code provided here..

## 🎥 Video References

- [**Arabic Text Handling**](https://youtu.be/tA7Fv2Xf9gg):  
  A comprehensive walkthrough on transforming and handling Arabic text 

- [**How to Build AI Chatbots: Full Guide from Beginner to Pro (Latest Update)**](https://www.youtube.com/watch?v=SWP3k-24jT4):  
  A full tutorial that walks through building AI-powered chatbots, covering foundational concepts to advanced deployment techniques.

