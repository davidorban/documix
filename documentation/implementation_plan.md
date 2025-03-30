# Implementation plan

## Phase 1: Environment Setup

1. **Prevalidation**: Check if the current directory already contains project files (e.g., `setup.py`, `pyproject.toml`, or a `venv` folder). If found, skip project initialization. *(Reference: Project Overview, Key Considerations)*
2. Verify that Python 3.8+ is installed by running `python --version`. *(Reference: Tech Stack: Language)
3. Create the base project directory structure if it doesn’t already exist:
   - Create `/src` for source code
   - Create `/tests` for test scripts
   - Create `/docs` for documentation *(Reference: Project Overview, Tech Stack)*
4. Create and activate a Python virtual environment using:
   - Command: `python -m venv venv` then activate with `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows). *(Reference: Tech Stack: Language)
5. Install initial dependencies using pip:
   - Install `requests` and `firecrawl` as primary libraries.
   - (Optional) Ensure that `scrapy` and `wget` are available for fallback, even if not installed by default—they can be invoked via subprocess.
   - Command: `pip install requests firecrawl` *(Reference: Tech Stack: Dependencies)*
6. **Validation**: Run `python --version` and `pip freeze` to confirm the correct setup.

## Phase 2: Command-Line Interface (CLI) Development

7. Create the CLI entrypoint file at `/src/documix.py`. *(Reference: Core Functionality: Command-Line Interface (CLI))*
8. Set up Python’s `argparse` module to handle the primary command `documix package <url>` and additional CLI flags:
   - `--output <file>` for specifying the output file
   - `--ignore <patterns>` for list of ignore patterns
   - `--scraper <tool>` to choose a scraper (options: firecrawl, wget, scrapy)
   - `--scraper-order <tool,tool,tool>` to define the scraper order
   - `--verbose` for detailed logging
   *(Reference: Core Functionality: Command-Line Interface (CLI))*
9. Add command handler functions that will route the user’s input to the appropriate scraping and packaging functionalities. *(Reference: Core Functionality: Command-Line Interface (CLI))*
10. **Validation**: Run `python src/documix.py --help` to verify that help information displays all commands and flags correctly.

## Phase 3: Scraper Integration

11. Create a module at `/src/scrapers/firecrawl.py` to integrate the primary scraping tool, Firecrawl. Code the function to accept a starting URL and perform scraping using Firecrawl’s API (ensure API key is managed via environment variable or configuration). *(Reference: Core Functionality: Website Scraping)*
12. Create a fallback scraping module at `/src/scrapers/fallback.py` which implements scraper integrations with Scrapy and wget using subprocess calls.
13. In the main CLI command, implement logic to read the `--scraper` and `--scraper-order` flags so that if the primary scraper fails or is not selected, the program falls back to secondary options in the configured order. *(Reference: Core Functionality: Website Scraping, Scraper Integration)*
14. **Validation**: Write and run a unit test to simulate a scrape from a sample URL using both Firecrawl and one fallback option, verifying that content is returned or appropriate errors are handled.

## Phase 4: Content Packaging

15. Create a module `/src/packager.py` that defines the content packaging functionality.
16. Implement the logic to combine scraped content into a single `.txt` file with a structured header that includes:
    - Website name
    - Generation date
    - Page count
   and individual page-wise content blocks. *(Reference: Core Functionality: Content Packaging)*
17. Add support for outputting Markdown by checking the file extension (if `.md` is specified) and formatting the output accordingly. *(Reference: Core Functionality: Content Packaging)
18. Allow for customizable output file naming conventions using prefixes, suffixes, and timestamps by parsing the corresponding CLI flags if provided. *(Reference: Core Functionality: Content Packaging)*
19. **Validation**: Execute the packaging module with dummy content to verify that the header and content blocks are correctly structured and that the output file adheres to the specified format.

## Phase 5: Ignore Patterns & Metadata Inclusion

20. Create a configuration module `/src/config.py` to handle user configuration options, including reading a `.docignore` file if it exists.
21. Implement logic to parse the `.docignore` file and the `--ignore` flag; ensure that any pages matching the specified patterns are excluded from the output. *(Reference: Core Functionality: Ignore Patterns)*
22. Add a CLI flag (e.g., `--include-metadata`) to allow users to optionally add page metadata (such as title and last modified date) above the content for each page. *(Reference: Core Functionality: Metadata Inclusion)*
23. **Validation**: Test the ignore functionality by supplying URLs or patterns that should be skipped, and run the CLI with and without the metadata flag to confirm behavior.

## Phase 6: Concurrency & Performance

24. Develop a concurrent scraping module at `/src/scraper_concurrent.py` to enhance performance via multi-threading or multi-processing. *(Reference: Core Functionality: Website Scraping, Performance)*
25. Integrate the concurrent module into the main scraping workflow so that pages are scraped in parallel, targeting the performance requirement of processing 50 pages (2KB/page) in under 5 minutes.
26. **Validation**: Run a performance test using a simulated website with 50 pages; measure execution time and adjust thread/process counts as needed.

## Phase 7: Logging & Error Handling

27. Integrate the Python `logging` module across all modules to provide debug and error logs. Ensure the logs are detailed when the `--verbose` flag is active. *(Reference: Core Functionality: Error Handling & Logging)*
28. Implement proper error handling for network issues, scraping errors, and respect for `robots.txt`. If a page is blocked by `robots.txt`, notify the user and provide an option to override the block. *(Reference: Core Functionality: Website Scraping, Error Handling)*
29. **Validation**: Simulate failure conditions (e.g., blocked pages, network errors) and verify that errors are logged and communicated to the user with the possibility to override when appropriate.

## Phase 8: Packaging & Distribution Setup

30. Create a `setup.py` (or `pyproject.toml`) in the project root to configure the package for PyPI distribution. Include metadata such as project version, description, and dependencies. *(Reference: Tech Stack: Packaging)*
31. Configure console scripts entry point so that after installation, the CLI command `documix` is available. *(Reference: Core Functionality: Command-Line Interface (CLI))*
32. **Validation**: Run `pip install -e .` and test that the command `documix package <url>` runs as expected.

## Phase 9: Integration & Testing

33. Create unit tests in `/tests` for each module (scraping, packaging, configuration, concurrent execution). *(Reference: Key Considerations: Testing)
34. Develop integration tests in `/tests/test_documix.py` to simulate full command-line operations including scraping, packaging, and error handling.
35. **Validation**: Run all tests using `pytest` ensuring high test coverage and proper functionality across different modules.

## Phase 10: Documentation & Final Checks

36. Write a detailed `README.md` documenting the usage of the Documix CLI tool, configuration options, installation instructions, and examples of commands. *(Reference: Project Overview, Core Functionality: Command-Line Interface (CLI))*
37. Create or update developer documentation in `/docs` including module descriptions, API endpoints (if any), and design decisions.
38. Review and update code comments and inline documentation for clarity.
39. **Validation**: Perform a final review by running the CLI tool end-to-end using sample inputs and reading through the logs/output to ensure complete and correct behavior.

# Final Note

Ensure that each implementation step is validated in your development environment before proceeding to the next phase. The above plan provides a structured roadmap to build the Documix command-line tool that meets user requirements and performance targets.