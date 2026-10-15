# FrontierGraph System Architecture

## 1. Overview

FrontierGraph consists of a research data pipeline, a production database, a backend API, and an interactive analytics application.

A separate experimental database engine will be developed to understand database internals and evaluate different storage and indexing strategies.

The architecture prioritizes modularity, maintainability, reliable data processing, and low-cost development.

## 2. Technology Stack and Responsibilities

| Component | Technology | Responsibility |
|---|---|---|
| Research data source | OpenAlex API | Provide publication metadata, author information, research topics, and available citation data |
| Data ingestion pipeline | Python, HTTPX, Pandas | Fetch research records, normalize fields, validate data, remove duplicates, and update the production database |
| Production database | PostgreSQL | Reliably store research papers, authors, topics, relationships, and application data |
| Backend API | FastAPI, Pydantic | Handle application requests, validate inputs, execute research queries, and expose analytics functionality |
| Frontend | Streamlit, Plotly | Provide interactive search, filtering, dashboards, research summaries, and visualizations |
| Experimental database | Python, binary file I/O | Implement storage, persistence, indexing, and querying mechanisms for educational experimentation and benchmarking |
| Machine learning | scikit-learn, Sentence Transformers | Analyze topic relationships, compute semantic representations, and identify emerging research patterns |
| AI research agent | LLM API and Python tools | Retrieve evidence, analyze research records, and generate source-grounded summaries and reports |
| Testing | pytest | Verify database behavior, API functionality, and data processing correctness |
| Version control | Git, GitHub | Track changes, document decisions, and maintain the project's source code |

## 3. Data Flow

**Research collection**

OpenAlex API → Python ingestion pipeline → PostgreSQL

**User interaction**

Streamlit frontend → FastAPI backend → PostgreSQL → FastAPI → Streamlit

**Research analysis**

PostgreSQL → Python analytics and ML → Stored results → FastAPI → Streamlit

## 4. Experimental Database Isolation

The custom database engine is independent of the production application's primary storage.

It will begin as a simple append-only key-value store and progressively introduce on-disk persistence, disk pages, indexing, B+ trees, query parsing, and durability mechanisms.

Its purpose is to study database implementation and benchmark performance, not to replace PostgreSQL.

Failures in the experimental database should not prevent users from accessing FrontierGraph.

## 5. Initial Development Principles

- Build locally using free and open-source tools wherever practical.
- Introduce additional infrastructure only when justified by a concrete requirement.
- Keep research ingestion independent of user-facing search requests.
- Test core functionality and validate research data before presenting it.
- Provide links to original research sources and communicate uncertainty in automated findings.
- Keep experimental components isolated from production-critical systems.