---

# .windsurfrules

## Project Overview
- **Type:** Command-Line Tool
- **Description:** Documix is a CLI tool that scrapes and packages website documentation into a single AI-friendly text file, inspired by Repomix.
- **Primary Goal:** Simplify the process of feeding website documentation to LLMs for efficient analysis.

## Project Structure
### Framework-Specific Routing
- **Directory Rules:**
  - Since Documix is a Python CLI application without a web routing framework, routing is managed via CLI command parsing (e.g., using argparse or click).
  - Example: The command "documix package <url>" routes to the scraping and packaging logic within the CLI module.

### Core Directories
- **Versioned Structure:**
  - `documix/`: Contains the core modules for scraping, packaging, and CLI interface.
    - Example: `documix/cli.py` handles command-line parsing and dispatching commands.
  - `documix/scrapers/`: Houses integrations with scraping tools like Firecrawl, Scrapy, or wget.
  - `tests/`: Contains unit and integration tests for all functional components.

### Key Files
- **Stack-Versioned Patterns:**
  - `documix/__main__.py`: Entry point for the application, enabling execution via `python -m documix`.
  - `documix/cli.py`: Implements CLI commands including `package`, with support for flags such as `--output`, `--ignore`, and `--scraper-order`.

## Tech Stack Rules
- **Version Enforcement:**
  - `python@3.8+`: Ensure compatibility with Python 3.8 or newer; enforces usage of modern Python features and dependency compatibility (e.g., Firecrawl, Requests).
  - `firecrawl`: Primary scraper tool integrated directly into the scraping module.
  - Optional tools (Scrapy, wget) are invoked via subprocess for fallback scenarios.

## PRD Compliance
- **Non-Negotiable:**
  - "Documix must support both a `.docignore` file and CLI flag for ignore patterns, ensuring developers can exclude specified pages or sections." Enforces version-specific constraints on input sanitation and command behavior.

## App Flow Integration
- **Stack-Aligned Flow:**
  - Example: "Documix CLI flow → `documix/cli.py` parses the command `package <url>`, triggers concurrent scraping in `documix/scrapers/`, and then assembles output in a single file (either `.txt` or `.md`) with optional metadata inclusion."

---