# 🕌 TurathLLM

**Turn raw Islamic heritage texts into structured, searchable databases.**

TurathLLM is a data pipeline designed to extract structured information from unstructured Islamic books, especially classical texts. It uses rule-based logic, small AI models, and regex to prepare datasets for scholarly review, research, or application development.

---

## ✨ What It Does

- 🔍 Collects and parses classical Islamic texts (Hadith, Fiqh, Tafsir, etc.)
- 🧠 Uses regex + small language models to extract named entities, chains, and references
- 🗃️ Builds structured outputs in SQL-ready formats
- 🏷️ Labels and annotates data for easier scholarly validation

---

## 📌 Who It's For

### 🔧 **Developers & Data Engineers**

**TurathLLM** is an open-source pipeline that transforms unstructured Islamic heritage texts into structured SQL databases. It uses regex, lightweight AI models, and data-cleaning tools to parse classical books, extract metadata, and build review-ready datasets. Ideal for devs building tools around knowledge graphs, search systems, or scholarly annotation platforms.

> Automate the process of turning messy text into normalized, queryable databases — perfect for building knowledge graphs, semantic search, and annotation tools.

### 📊 **Data Scientists & NLP Folks**

**TurathLLM** is a hybrid rule-based + AI pipeline that turns classical Islamic texts into structured data. Designed for Arabic NLP tasks, it combines regex-driven tagging with small LLMs to extract entities, relationships, and schema-ready metadata from complex heritage content. It’s a starting point for downstream tasks like NER, chain validation, and scholarly review support.

> Train/test Arabic NLP models using structured ground truth from real Islamic text. Perform entity linking, isnad classification, matn defect analysis, and more.

### 📚 **Islamic Scholars & Researchers**

**TurathLLM** is a tool that helps prepare classical Islamic texts for scholarly review. It collects and organizes raw book content, then labels and structures the data — including narrators, chains, references, and metadata — using AI and rules. The result is a searchable, structured format that simplifies the task of verifying, analyzing, and studying traditional knowledge.

> Get book content that’s pre-organized for review: chains, narrators, sources, topics, references — all clearly labeled and ready to verify.

---

### 🪄 Bonus: Short 1-Liner for GitHub / Tags / Indexing 
* `From raw Islamic text to SQL — powered by AI and regex`
*  `Structured Islamic knowledge from classical books`
* `Parse, label, and structure Turath texts for modern tools`

---

## ⚙️ Tech Stack

| Layer        | Tools & Libraries                                |
|--------------|--------------------------------------------------|
| Language     | Python                                           |
| NLP          | CAMeL Tools, regex, local LLM (via Ollama)      |
| DB           | SQLite / PostgreSQL                              |
| ETL          | Custom pipelines, Pandas, DuckDB, FastAPI        |
| Graph (opt)  | Neo4j for narrator/chain relationships           |
| Deployment   | CLI + Jupyter + API-ready (FastAPI/Uvicorn)     |

---

## 📁 Project Structure

```css
turathstruct/
            ├── data/
            │         ├── raw/ # Unprocessed book texts (JSON, TXT, HTML, etc.)
            │         ├── processed/ # Cleaned and normalized outputs
            │         └── schemas/ # YAMLs for grading, metadata mapping, etc.
            ├── src/
            │         ├── extraction/ # Regex, NER, LLM integration
            │         ├── labeling/ # Tagging narrators, chain roles, references
            │         ├── db/ # SQLite/PostgreSQL export scripts
            │         └── utils/ # Helper functions, config loaders
            ├── notebooks/ # Jupyter experiments and visualizations
            ├── configs/ # YAML/JSON configs for pipeline control
            ├── main.py # Main CLI entrypoint
            └── README.md
```

---


# 📚 Project: 

> unstructured-to-structured-ai-schema (Main Page)

## 📌 Table of Contents

1. [Project Goal](#📌-goal)
2. [Example Use Cases](#example-use-cases)
3. [Project Approach](./docs/approach.md)
4. [Key Components & Structure](#key-components--structure)
5. [Data Sources Collections](./docs/data_sources.md)
6. Entity Extraction 
    - (I) [Book Structuring](#)
    - (II) [Rgex Extraction](#)
    - (III) [LLM Relationship Extraction](#)
7. Flask App UI/UX Design and Implementation for review the annotation Entity Extraction 
---

## 📌 Goal

To enable developers, researchers, and scholars to:

- Rapidly structure unstructured Islamic or historical data
- Build LLM-based applications with integrated knowledge graphs
- Enable RAG pipelines with rich, contextual structured sources
- Connect relational and graph-based knowledge systems

### 📌 Core Goal

*   To provide **database schema designs** (blueprints) for transforming unstructured data into structured formats.
*   Target applications include:
    *   **AI & LLMs:** For training, information extraction (NER), semantic enrichment.
    *   **Relational Databases (RDB):** For standard tabular storage (e.g., PostgreSQL, SQLite) and analytical querying.
    *   **Graph Databases (GDB):** For representing complex entities and relationships (e.g., Neo4j).
    *   **Retrieval-Augmented Generation (RAG):** To feed structured, contextual data to LLMs.
*   Focuses on complex data like historical texts (including Islamic sources like Hadith, books), invoices, etc.
*   Aims to bridge relational and graph data models.

[(Back to top)](#📌-table-of-contents)

---

## 📎 Example Use Cases 

* 📚 Building Islamic knowledge graphs (narrators, books, references) 
* 🤖 Training LLMs with fine-tuned book metadata 
* 🔍 Searching and referencing Arabic heritage texts 
* 🧩 Generating semantic embeddings and document chunking 
* 🗃️ Ingesting into SQL or graph databases for scholarly research

[(Back to top)](#📌-table-of-contents)

---

## Key Components & Structure

###   **`schemas/` directory:** 
*   Contains schema definitions for different data sources/types.
*   `rdb_schema.sql`: SQL schema for relational databases.
*   `gdb_schema.cypher`: Cypher schema for graph databases.
*   `entity_definitions.yaml`: A crucial human/machine-readable file defining entities and their relationships. This can be used to drive other tools (like dbt, Airbyte).

### **`input/`:** 
- Sample input data (e.g., `hadith_chain_example.json`).

### **`output/`:** 
- Sample output data (e.g., `hadith_chain_example.csv`).

### **`pipelines/`, `scripts/`, `docs/`:** 
- Supporting materials for ETL processes, helper scripts, and documentation.

[(Back to top)](#📌-table-of-contents)

---

### Dependencies (from turath_books README)

*   `Python 3.8.2+`
*   `pandas`
*   `beautifulsoup4`
*   `re`
*   `camel-tools` (likely for Arabic text processing)
*   `pyarabic` (likely for Arabic numeric text processing and detection)
*   `dateparser` (likely for Arabic date detection)
*   `spacy` (likely for Arabic NPL)
*   `difflib` (likely for text similarity)
*   `hydra` (Configuration Management Framework)

[(Back to top)](#📌-table-of-contents)

---

## Overall Summary & Relationship

*   The main `unstructured-to-structured-ai-schema` project defines standardized **schemas** (RDB, GDB) and **entity definitions** (`entity_definitions.yaml`) for organizing complex unstructured data, particularly historical/Islamic texts.
*   The `turath_books` component is a practical **ETL pipeline implementation** within this framework.
*   It takes a specific data source (Turath JSON) and processes it into structured **CSVs**.
*   Crucially, it uses the `entity_definitions.yaml` concept from the main project to facilitate integration with data tools like **Airbyte** and **dbt**.
*   The structured CSV output from `turath_books` is intended to be loadable into databases conforming to the schemas defined in the main project, making it suitable for AI/LLM fine-tuning, knowledge graph population, and RAG applications.

[(Back to top)](#📌-table-of-contents)

---

## 🔗 Related Datasets Projects & References

- [**Sanadset 650K: Data on Hadith Narrators**](https://data.mendeley.com/datasets/5xth87zwb5/4):  
  Sanadset is a full hadith dataset that contains over 650,986 records collected from 926 historical Arabic books of hadith. This dataset can be used for further investigation and classification of hadiths (Strong/Weak), and narrators (trustworthy/not) using AI techniques, and also it can be used as a linguistic resource tool for Arabic Natural Language Processing.

- [**Multi-IsnadSet MIS for Sahih Muslim Hadith with chain of narrators, based on multiple ISNAD**](https://www.sciencedirect.com/science/article/pii/S2352340924004086?ssrnid=4726768&dgcid=SSRN_redirect_SD):  
  - `Specific`:	Islamic Hadith corpus, Multi-Isnad of Hadith Narrators, Social Network 
  - `subject area`:	Analysis (SNA), Graph Neural Network (GNN). Neo4j Graph Database
  - `Keywords`: Multi-Isnad of Hadith Narrators datasetChain of narrators; Machine learning; Graph database; Spatial–Temporal data; Social-Network Analysis (SNA); Graph Neural Networks (GNN) 
  - `Data Format	Raw`: NetworkX Python Library dump
    `Raw`: Different Visualization & Exploration softwares (Gephi, Cytoscape, and Social Network Visualizer) dump
    `Raw`: Neo4J database dump
    Geography Markup Language format (.gml), XML-based graph format (.graphml)

- [**OpenITI**](https://alraqmiyyat.github.io/OpenITI/):

  > ⚠️ **Caution:** This collection may include work from non-Sunni 🕌 (*mosque*) and non-Muslim ✡️ (*Jewish*) ✝️ (*Christian*) sources. Please handle and interpret the texts with care. 📚 (*texts*)

  OpenITI is a corpus of digital Islamicate texts. It is primarily intended as a foundation for new forms of macro textual analysis and digital scholarship. It is **not** (currently) a digital library with a user interface, reading environment, or search functions.

  - 📂 (*GitHub Repo*) [OpenITI Annotation](https://github.com/OpenITI/Annotation)
  - 📘 (*Guide*) [OpenITI mARkdown Format](https://maximromanov.github.io/mARkdown/)
  - 🐍 (*Python Library*) [OpenITI Python Lib](https://github.com/OpenITI/openiti)
  - 📄 (*Docs*) [OpenITI Python Lib Docs](https://openiti.readthedocs.io/en/latest/source/usermanual.html)
  - 📦 (*Corpus*) [OpenITI Corpus](https://github.com/OpenITI/RELEASE/tree/v2023.1.8)

- [**Quran-DB**](https://github.com/youzarsiph/quran-db):  
  Quran-DB is a sophisticated and comprehensive database of the Quran, available in both SQLite3 and JSON formats.
  Designed for optimal data organization and retrieval, it provides robust and efficient access to Quranic content and metadata.
  The database is meticulously structured to support various applications, including scholarly research, educational tools, and digital Quranic resources. 

[(Back to top)](#📌-table-of-contents)

---

## 🔗 Related Projects & References

- [**Quran Detector (Annotator)**](https://github.com/SElBeltagy/Quran_Detector):  
  A full code repo that capable of identifying any Quranic verse or verse fragment that is equal to or greater than 3 words, in any piece of text.
  The tool is capable of detecting minor typos and even missing words, but it is most efficient when carrying out exact matching.
  Error detection and missing word detection can be enabled and disabled by the programmer using the code provided here.

- [**Arabic NLP (camel_tools)**](https://github.com/CAMeL-Lab/camel_tools):  
  CAMeL Tools is suite of Arabic natural language processing tools developed by the CAMeL Lab at New York University Abu Dhabi.

- [**Arabic NLP (pyarabic)**](https://github.com/linuxscout/pyarabic):  
  A specific Arabic language library for Python, provides basic functions to manipulate Arabic letters and text, like detecting Arabic letters, Arabic letters groups and characteristics, remove diacritics etc.

- [**Arabic NLP (pyarabic)**](https://github.com/linuxscout/pyarabic):  
  A specific Arabic language library for Python, provides basic functions to manipulate Arabic letters and text, like detecting Arabic letters, Arabic letters groups and characteristics, remove diacritics etc.
  
- [**Bespoke Public Talks**](https://github.com/bespoke-inc/bespoke-public-talks):  
  A full code repo for the tutorial that walks through building AI-powered chatbots, covering foundational concepts to advanced deployment techniques.

[(Back to top)](#📌-table-of-contents)

---

## 🎥 Video References

- [**Arabic Text Handling**](https://youtu.be/tA7Fv2Xf9gg):  
  A comprehensive walkthrough on transforming and handling Arabic text 

- [**Ollama Course – Build AI Apps Locally**](https://youtu.be/GWB9ApTPTv4?si=W1tpOioEwqqpBQgc):  
  Learn how to set up and use Ollama to build powerful AI applications locally. This hands-on course covers pulling and customizing models, REST APIs, Python integrations, and real-world projects like a Grocery List Organizer, RAG System, and an AI Recruiter Agency. Perfect for developers and AI enthusiasts ready to bring their ideas to life with local LLMs. Don’t miss the exclusive BONUS project at the end! 

- [**Full Flask Course For Python - From Basics To Deployment**](https://www.youtube.com/watch?v=oQ5UfJqW5Jo):  
  This is a full Flask course for Python. It goes from the very basics like templates and POST requests, to more advanced stuff like sessions and database connections up until blueprints and deployment with Docker.

- [**How to Build AI Chatbots: Full Guide from Beginner to Pro (Latest Update)**](https://www.youtube.com/watch?v=SWP3k-24jT4):  
  A full tutorial that walks through building AI-powered chatbots, covering foundational concepts to advanced deployment techniques.

[(Back to top)](#📌-table-of-contents)

---

## 📚 Books
