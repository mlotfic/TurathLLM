# Unstructured to Structured Schema

**Database Schema Design for Structuring Unstructured Data for AI, LLMs, RDB, GDB, and RAG Applications**

---

## 📌 Overview

This project presents a modular and extensible database schema to transform and organize unstructured data for:

- **AI & LLMs (Large Language Models)** – for information extraction, NER, and semantic enrichment  
- **RDB (Relational Databases)** – for structured tabular storage and analytical querying  
- **GDB (Graph Databases)** – for representing entities and their complex interrelations  
- **RAG (Retrieval-Augmented Generation)** – for hybrid systems that combine LLMs with contextual data retrieval

Whether you're working with historical texts, invoices, academic corpora, or complex narrative chains like Hadith, this schema helps you **extract**, **structure**, and **link** data across multiple formats and paradigms.

---

## 🧱 Project Structure

```css
├── schemas/
│   ├── books/                            # General schema for structuring book data
│   │   ├── rdb_schema.sql                # Relational DB schema (PostgreSQL / SQLite)
│   │   ├── gdb_schema.cypher             # Graph DB schema (Neo4j / GDB compatible)
│   │   ├── entity_definitions.yaml       # YAML description of entities and relationships
│
│   ├── scraping/
│   │   ├── islamicurdubooks/
│   │   ├── islamweb/
│   │   ├── hadith-api-1/
│   │   ├── alminasadata/
│   │       ├── rdb_schema.sql
│   │       ├── gdb_schema.cypher
│   │       ├── entity_definitions.yaml
│   │       ├── examples/
│   │       │   ├── hadith_chain_example.json
│   │       │   ├── invoice_layout.json
│   │       ├── pipelines/
│   │       │   └── ETL.md
│   │       ├── scripts/
│   │       │   └── ETL.md
│   │       └── docs/
│   │           └── architecture_diagram.png
│
├── examples/                             # Reusable cross-domain example inputs
│   ├── hadith_chain_example.json
│   ├── invoice_layout.json
│
├── pipelines/                            # ETL process explanations
│   └── ETL.md
│
├── scripts/                              # Supporting scripts (e.g., extraction, conversion)
│   └── ETL.md
│
├── docs/                                 # Architecture, diagrams, and developer notes
│   └── architecture_diagram.png
│
├── README.md
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
  A valuable reference project that explores structuring public talks and events into rich, queryable data using schema design. Inspired parts of the modular schema design and entity modeling used in this repository.
