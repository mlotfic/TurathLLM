# 📚 Project: 

> unstructured-to-structured-ai-schema (Main Page)

## 📌 Table of Contents

1. [Project Goal](#goal)
2. [Example Use Cases](#--example-use-cases)
3. [Project Approach](./docs/approach.md)
3. [Key Components & Structure](./docs/approach.md)
4. [Data Sources Collections](./docs/data_sources.md)

---

## 📌 Goal

To enable developers, researchers, and scholars to:

- Rapidly structure unstructured Islamic or historical data
- Build LLM-based applications with integrated knowledge graphs
- Enable RAG pipelines with rich, contextual structured sources
- Connect relational and graph-based knowledge systems

---

## 📌 Core Goal

*   To provide **database schema designs** (blueprints) for transforming unstructured data into structured formats.
*   Target applications include:
    *   **AI & LLMs:** For training, information extraction (NER), semantic enrichment.
    *   **Relational Databases (RDB):** For standard tabular storage (e.g., PostgreSQL, SQLite) and analytical querying.
    *   **Graph Databases (GDB):** For representing complex entities and relationships (e.g., Neo4j).
    *   **Retrieval-Augmented Generation (RAG):** To feed structured, contextual data to LLMs.
*   Focuses on complex data like historical texts (including Islamic sources like Hadith, books), invoices, etc.
*   Aims to bridge relational and graph data models.

---

## 📎 Example Use Cases 

* 📚 Building Islamic knowledge graphs (narrators, books, references) 
* 🤖 Training LLMs with fine-tuned book metadata 
* 🔍 Searching and referencing Arabic heritage texts 
* 🧩 Generating semantic embeddings and document chunking 
* 🗃️ Ingesting into SQL or graph databases for scholarly research

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

---

## Overall Summary & Relationship

*   The main `unstructured-to-structured-ai-schema` project defines standardized **schemas** (RDB, GDB) and **entity definitions** (`entity_definitions.yaml`) for organizing complex unstructured data, particularly historical/Islamic texts.
*   The `turath_books` component is a practical **ETL pipeline implementation** within this framework.
*   It takes a specific data source (Turath JSON) and processes it into structured **CSVs**.
*   Crucially, it uses the `entity_definitions.yaml` concept from the main project to facilitate integration with data tools like **Airbyte** and **dbt**.
*   The structured CSV output from `turath_books` is intended to be loadable into databases conforming to the schemas defined in the main project, making it suitable for AI/LLM fine-tuning, knowledge graph population, and RAG applications.

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
  

- [**Quran-DB**](https://github.com/youzarsiph/quran-db):  
  Quran-DB is a sophisticated and comprehensive database of the Quran, available in both SQLite3 and JSON formats.
  Designed for optimal data organization and retrieval, it provides robust and efficient access to Quranic content and metadata.
  The database is meticulously structured to support various applications, including scholarly research, educational tools, and digital Quranic resources. 

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
  
- [**Bespoke Public Talks**](https://github.com/bespoke-inc/bespoke-public-talks):  
  A full code repo for the tutorial that walks through building AI-powered chatbots, covering foundational concepts to advanced deployment techniques.


## 🎥 Video References

- [**Arabic Text Handling**](https://youtu.be/tA7Fv2Xf9gg):  
  A comprehensive walkthrough on transforming and handling Arabic text 

- [**Ollama Course – Build AI Apps Locally**](https://youtu.be/GWB9ApTPTv4?si=W1tpOioEwqqpBQgc):  
  Learn how to set up and use Ollama to build powerful AI applications locally. This hands-on course covers pulling and customizing models, REST APIs, Python integrations, and real-world projects like a Grocery List Organizer, RAG System, and an AI Recruiter Agency. Perfect for developers and AI enthusiasts ready to bring their ideas to life with local LLMs. Don’t miss the exclusive BONUS project at the end! 

- [**Full Flask Course For Python - From Basics To Deployment**](https://www.youtube.com/watch?v=oQ5UfJqW5Jo):  
  This is a full Flask course for Python. It goes from the very basics like templates and POST requests, to more advanced stuff like sessions and database connections up until blueprints and deployment with Docker.

- [**How to Build AI Chatbots: Full Guide from Beginner to Pro (Latest Update)**](https://www.youtube.com/watch?v=SWP3k-24jT4):  
  A full tutorial that walks through building AI-powered chatbots, covering foundational concepts to advanced deployment techniques.

