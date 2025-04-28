# Structured Data Extraction and Verification System

## Overview

This system aims to **structure data from unstructured text** and integrate **scholarly verification** for accurate information extraction. It handles both **labeled** and **non-labeled books**, leveraging new technologies such as **LLMs** (e.g., **Ollama**) and **Regex** libraries for feature extraction.

## Key Example

Consider the sentence:

> **"Mohamed is born in Makkah"**

- **Challenge**: Who can confirm if "Mohamed" refers to the Prophet or someone else?
- If the name repeats, is it the same person or a different one?

**Experts** are needed to verify identities and gather accurate information.

## Current Approach

1. **Scrape Data**: Collect data from HTML sources where text and books are labeled correctly.
2. **Multiple Sources**: Combine information from various verified sources.

## Downsides of Current Approach

- Each source has its own **annotation system**, with both strengths and weaknesses.
- Sources often **lack clear explanations** for their labeling methods.
- **Reviewers and validators** are not consistently mentioned.
- **Data is often incomplete**.

## Additional Challenges

- **Non-labeled books**: A large portion of books and information are still not labeled.
- **Data Unification**: Our biggest challenge is unifying all data into one database.
- **Duplicates**: We need to remove duplicated data across sources.
- **Conflicting Information**: We must allow conflicting information while clearly mentioning the source for each.

## New Technologies and Solutions

- **Ollama** and other **Regex** libraries can now extract features and understand text.
- While these tools can help, **mistakes** can still occur.
- **Integrating newly labeled books** with the already labeled database remains a challenge.

## Proposed System

Our proposed system will:

- Use **LLMs** (e.g., **Ollama**) and existing libraries to:
  - **Extract features** from text.
  - **Establish relationships** between these features.
- Provide a **UI system** for scholars to:
  - **Review, correct, and verify** the extracted data.
  - **Connect verified data** directly to the unified labeled database.

## Steps to Achieve This

1. **Collect Existing Labeled Data**: Gather all existing labeled data into one unified database through scraping and other methods, following a unified schema.
2. **Prepare Non-Labeled Books**: Use **semantic chunking** to process non-labeled books, making them ready for scholar review in the UI system.

## Flowchart

```mermaid
flowchart TD
    subgraph Input
        A[Existing Labeled Data] -->|Scraping & Other Methods| B[Unified Schema]
        C[Non-Labeled Books] -->|Semantic Chunking| D[Chunked Text]
    end

    B --> E[LLM & Libraries (Ollama, Regex, etc.)]
    D --> E

    E --> F[Feature Extraction & Relationship Establishment]

    F --> G[Scholar UI System]
    G --> H[Scholar Review & Verification]

    H --> I[Unified Labeled Database]
