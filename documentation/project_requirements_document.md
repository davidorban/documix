# Documix Product Requirements Document (PRD)

## 1. Project Overview

Documix is a command-line tool designed to scrape a complete documentation website and package its contents into a single, structured text file that is optimized for large language models. Inspired by Repomix—which condenses code repositories into one AI-friendly file—Documix adapts this idea specifically for web-based documentation. By aggregating content from multiple pages into one coherent file, the tool aims to simplify the ingestion process for AI models, saving developers, researchers, and technical writers time and reducing manual effort.

The project is being built to address the gap in tools that efficiently combine multi-page website documentation for analysis with AI tools. Key objectives include the ability to fetch various pages using popular scraping tools like Firecrawl, apply user-defined ignore rules (via CLI or .docignore file), and optionally include detailed metadata such as page titles. Success will be measured by ease-of-use, flexibility in output formatting (plain text and Markdown), and achieving acceptable performance even on moderately sized sites.

## 2. In-Scope vs. Out-of-Scope

**In-Scope Features and Functionality:**

*   **Website Scraping Integration:**

    *   Fetch content from a provided URL and all linked pages using a default scraper (Firecrawl) with options for Scrapy and wget as fallback.
    *   Support dynamic order configuration for scrapers via a CLI flag.

*   **Content Packaging:**

    *   Combine the scraped content into a single file using a Repomix-inspired structure which includes a header with the website name, generation date, and total pages processed.
    *   Allow customizable output naming conventions and support alternative formats such as Markdown.

*   **Ignore Patterns:**

    *   Allow specifying pages or sections to exclude through a dedicated .docignore file as well as via CLI flags.

*   **Optional Metadata Inclusion:**

    *   Optionally include metadata (like page titles and last modified dates) in the output file, based on a user flag.

*   **Concurrent/Multi-Threaded Scraping:**

    *   Support concurrent or multi-threaded requests to ensure efficient scraping of sites with many pages.

*   **Command-Line Interface (CLI):**

    *   A user-friendly CLI that handles commands, accepts additional flags (output file, ignore patterns, scraper preferences), and logs detailed progress and errors.

**Out-of-Scope Features and Functionality:**

*   **Real-Time Updates:**

    *   Documix will capture a static snapshot of the current site content and will not support real-time updates or auto-refresh of the output once created.

*   **Graphical User Interface (GUI):**

    *   The initial version is solely CLI-based; a GUI may be considered in future enhancements.

*   **PDF Extraction:**

    *   Extraction from PDF formats or other non-HTML content is not included in the initial release.

*   **User Role Differentiation:**

    *   The tool is built for universal CLI access with no role-based restrictions implemented in this version.

*   **Automatic LLM API Integration:**

    *   While designed for LLM ingestion, integrating directly with LLM APIs or auto-uploading files is not part of the initial MVP.

## 3. User Flow

When a user starts Documix from the command-line, they begin by entering the main command along with the target URL and optional flags. The user can specify the output file format (plain text or Markdown), decide whether to include page metadata, choose a preferred scraper, and set ignore patterns either via a CLI flag or a .docignore file. This initial step ensures that the tool can be tailored immediately to the user’s needs without any additional configuration.

Once the command is executed, Documix validates the URL and begins the scraping process. The tool concurrently fetches linked pages while respecting the ignore patterns and checking for any blocked pages (with notifications for pages restricted by robots.txt or authentication issues). After all content is gathered, the tool packages the data into a single output file with a structured header and detailed content blocks. Finally, Documix provides clear logging and notifications, informing the user about any skipped or blocked pages and confirming the successful generation of the final file.

## 4. Core Features

*   **Website Scraping Integration:**

    *   Utilize a default scraper (Firecrawl) with fallback options (Scrapy, wget).
    *   Dynamically allow users to configure the scraper order via a CLI flag (e.g., --scraper-order "scrapy,firecrawl,wget").

*   **Content Packaging:**

    *   Combine the fetched content into a single file with a structured header (website name, generation date, number of pages).
    *   Organize subsequent sections for each page with clear separation and optional metadata inclusion.

*   **Ignore Patterns:**

    *   Support the use of both a dedicated .docignore configuration file and CLI ignore flags to exclude specific pages or sections.

*   **Optional Metadata Inclusion:**

    *   Include page metadata (e.g., title, last modified date) above the content block if the user opts in via a flag.

*   **Output Customization:**

    *   Allow users to choose output formats (plain text, Markdown) and customize file naming conventions with prefixes, suffixes, or timestamps.

*   **Command-Line Interface (CLI):**

    *   Provide simple commands such as “documix package ” along with additional flags for output, ignore patterns, scraper selection, verbose logging, and override options for blocked pages.

*   **Concurrent/Multi-Threaded Scraping:**

    *   Implement parallel page fetching to meet performance requirements while maintaining respect for site rules.

*   **Logging and Verbose Mode:**

    *   Detailed logging of progress, errors, and ignored pages to aid troubleshooting.

## 5. Tech Stack & Tools

*   **Frontend/CLI:**

    *   Python 3.8+ is the language used to build the command-line tool.
    *   The CLI will be designed to parse user inputs, flags, and commands using Python libraries (e.g., argparse).

*   **Backend/Scraping Tools:**

    *   Primary scraper: Firecrawl (for its AI-friendly output).
    *   Alternate scrapers: Scrapy and wget (invoked as subprocess calls when needed).
    *   HTTP requests: Python’s “requests” library for initial URL checks and simple fetches.

*   **Tools & AI Models:**

    *   Windsurf (Modern IDE with integrated AI coding capabilities) for development.
    *   Claude 3.7 Sonnet, GPT 4o, and Gemini 2.5 Pro are mentioned as preferred models for future integration or testing use cases, ensuring the code and output are optimized for AI ingestion.

*   **Potential Plugins/Integrations:**

    *   Integration with IDE plugins like Cursor or Windsurf plugins may be explored to assist debugging and code generation in future iterations.

## 6. Non-Functional Requirements

*   **Performance:**

    *   The tool must process a website with approximately 50 pages (average 2KB per page) in under 5 minutes on a standard machine (e.g., 8GB RAM, 4-core CPU).

*   **Compatibility:**

    *   Must run on Python 3.8 and later.
    *   Integrate seamlessly with supported scraping tools (Firecrawl as primary, with Scrapy and wget as alternatives).

*   **Extensibility:**

    *   The architecture should allow adding new scraper modules via a plugin-like system.
    *   Future enhancements may include additional output formats or integration with third-party APIs.

*   **Security and Compliance:**

    *   Respect for robots.txt and site terms of service is a must, with robust warnings if site restrictions are detected.
    *   Provide an override option for advanced users while clearly communicating potential legal/ethical requirements.

*   **Usability:**

    *   A clean, straightforward CLI interface with detailed logging and a verbose mode to assist with troubleshooting and error reporting.

## 7. Constraints & Assumptions

*   **Dependencies:**

    *   The functioning of Documix relies on external scraping tools (e.g., Firecrawl, Scrapy, wget). Availability and API keys for these tools are a dependency.

*   **Design Assumptions:**

    *   The tool is assumed to be used in a command-line environment by developers, researchers, and technical writers.
    *   All configurations (e.g., ignore patterns) can be specified either via CLI flags or configuration files.

*   **Performance Constraints:**

    *   The output file’s size is maintained under a certain limit (e.g., <10MB), with performance potentially impacted by the number of pages scraped.

*   **Legal/Ethical Constraints:**

    *   The tool will not bypass robots.txt restrictions unless an explicit override is provided by the user, ensuring compliance with ethical scraping practices.

*   **Multi-threading:**

    *   Use of concurrent scraping might require additional handling to prevent overwhelming target websites, and is assumed to be implemented with respect to rate limits.

## 8. Known Issues & Potential Pitfalls

*   **Scraping Blocks and Rate Limits:**

    *   Some sites may block scraping activities due to strict robots.txt rules or rate limiting. The tool must notify the user about blocked pages and provide an override option while recommending caution.

*   **Dependency on External Tools:**

    *   If Firecrawl (or any other scraping tool) fails or is not available, there could be delays or errors. This risk is mitigated by allowing easy fallback to alternate tools like Scrapy and wget.

*   **Handling of Large Sites:**

    *   Large websites might produce output files that exceed the token limit of target AI models. Mitigation includes implementing robust ignore patterns and providing users with options to customize content aggregation.

*   **Error Handling and Logging:**

    *   Accurate detection and logging of errors (network issues, unsupported page formats, etc.) is crucial. Verbose mode must provide enough detail to troubleshoot potential scraping and packaging issues.

*   **Concurrent Processing Challenges:**

    *   While multi-threading aids performance, it may introduce race conditions or overload the target website’s server if not carefully managed. A balance must be maintained between performance gains and respectful use of target resources.

This document sets out all the necessary details for the AI model to generate further technical documents (Tech Stack, Frontend Guidelines, Backend Structure, etc.) without any ambiguity. The clear division between functional requirements, non-functional requirements, constraints, and known issues ensures that every aspect of Documix is precisely defined for a successful implementation.
