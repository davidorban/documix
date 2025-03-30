# Documix

A powerful tool for scraping and documenting websites.

## Features

- Website scraping using multiple tools (Firecrawl, wget, scrapy)
- Content packaging into structured documents
- Ignore patterns for excluding specific content
- Metadata inclusion for detailed documentation
- Command-line interface for easy usage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/davidorban/documix.git
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
documix package <url> [options]
```

Options:
- `--output <file>`: Specify output file (default: documix_output.txt)
- `--ignore <patterns>`: List of patterns to ignore
- `--scraper <tool>`: Choose scraper (firecrawl, wget, scrapy)
- `--scraper-order <tool,tool,tool>`: Define scraper order
- `--verbose`: Enable detailed logging

## Project Structure

```
documix/
├── src/
│   ├── documix.py          # Main CLI entrypoint
│   ├── scrapers/           # Scraper implementations
│   │   └── firecrawl.py    # Firecrawl scraper
│   └── packager.py         # Content packaging
├── tests/                  # Test files
├── docs/                   # Documentation
├── venv/                   # Virtual environment
└── requirements.txt        # Project dependencies
```

## Development

To run tests:
```bash
python -m pytest tests/
```

## License

MIT License
