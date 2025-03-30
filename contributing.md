**Contributing to Documix**

Thank you for your interest in contributing to **Documix**\! We’re building a tool to scrape and package website documentation for AI use, inspired by Repomix, and we welcome help from the community to make it better. Whether you’re fixing bugs, adding features, or improving docs, your contributions are valuable.

**How to Contribute**

**1\. Get Started**

1. **Fork the Repository**:  
   * Go to [github.com/davidorban/documix](https://github.com/davidorban/documix) and click "Fork".  
2. **Clone Your Fork**:  
3. bash

git clone https://github.com/\<your-username\>/documix.git

4. cd documix  
5. **Install Dependencies**:  
6. bash  
7. pip install \-r requirements.txt  
8. For development, also install:  
9. bash  
10. pip install \-r requirements-dev.txt  
11. *Note*: Requires Python 3.8+. See README.md (README.md\#dependencies) for details.  
12. **Set Up Scraper**:  
    * Default is Firecrawl. Get an API key from [firecrawl.dev](https://firecrawl.dev/) and set it:  
    * bash  
    * export FIRECRAWL\_API\_KEY="your-api-key"

**2\. Find Something to Work On**

* **Issues**: Check the [Issues tab](https://github.com/davidorban/documix/issues) for bugs, feature requests, or tasks labeled good first issue.  
* **Roadmap**: See README.md (README.md\#roadmap) for MVP priorities (due May 15, 2025\) and future ideas (e.g., PDF support, GUI).  
* **Ideas**: Have a suggestion? Open a new issue with details\!

**3\. Make Changes**

1. **Create a Branch**:  
2. bash  
3. git checkout \-b \<branch-name\>  
   * Use descriptive names (e.g., feature/add-metadata, bugfix/ignore-patterns).  
4. **Code**:  
   * Follow Python PEP 8 style (use flake8 for linting if installed via requirements-dev.txt).  
   * Keep changes focused—one feature or fix per PR.  
5. **Test**:  
   * Run the tool manually: python documix.py package \<test-url\>.  
   * Add unit tests in tests/ if applicable (MVP tests TBD).  
6. **Commit**:  
   * Use clear messages (e.g., "Add metadata support to output", "Fix ignore pattern parsing").  
7. bash

git add .

8. git commit \-m "\<your-message\>"

**4\. Submit a Pull Request (PR)**

1. **Push to Your Fork**:  
2. bash  
3. git push origin \<branch-name\>  
4. **Open a PR**:  
   * Go to [github.com/davidorban/documix](https://github.com/davidorban/documix) and click "New Pull Request".  
   * Base branch: main.  
   * Compare: Your branch.  
5. **Describe Your Changes**:  
   * Explain what you did, why, and how to test it.  
   * Link to related issues (e.g., "Fixes \#12").  
6. **Review Process**:  
   * Maintainers will review your PR. Be open to feedback or requests for changes.

**5\. Sync Your Fork**

Keep your fork up-to-date with the main repo:  
bash  
git remote add upstream https://github.com/davidorban/documix.git  
git fetch upstream  
git checkout main  
git merge upstream/main  
git push origin main

**Contribution Guidelines**

**Code Style**

* **Python**: Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/). Use tools like flake8 or black (optional).  
* **Comments**: Add docstrings for functions and inline comments for complex logic.  
* **Structure**: Keep the codebase modular (e.g., separate scraping, processing, CLI logic).

**Scope**

* **MVP Focus (Q2 2025\)**: Core scraping (Firecrawl), packaging, ignore patterns, metadata support.  
* **Future Ideas**: Welcome, but prioritize MVP completion unless marked urgent.

**Testing**

* Manual testing is fine for now (e.g., run on a sample site like https://docs.windsurf.com/windsurf/).  
* Unit tests are encouraged—add to tests/ if you’re tackling a complex feature.

**Issues and Features**

* **Bug Reports**: Include steps to reproduce, expected vs. actual behavior, and environment details.  
* **Feature Requests**: Describe the use case and how it benefits Documix users.

**Development Environment**

* **Python**: 3.8+  
* **Dependencies**: Listed in requirements.txt and requirements-dev.txt.  
* **Optional Tools**: flake8 (linting), pytest (testing, TBD).

**Current Priorities**

* MVP (May 15, 2025):  
  * Robust scraping with Firecrawl.  
  * Packaging logic with metadata.  
  * CLI polish and ignore patterns.  
* See README.md (README.md\#roadmap) for details.

**Questions?**

* Open an issue with \[Question\] in the title.  
* Reach out via GitHub Discussions (if enabled later).

**Acknowledgments**

Every contributor helps shape Documix. Your name will be added to a future CONTRIBUTORS.md file (post-MVP)\!
