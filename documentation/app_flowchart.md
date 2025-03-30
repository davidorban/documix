flowchart TD
    CLI_Input[CLI Input: URL and Flags]
    URL_Validation[Validate URL]
    Decide_Scraper{Select Scraper}
    Firecrawl[Firecrawl default]
    Fallback_Scraper[Fallback: Scrapy or wget]
    Concurrent_Scraping[Perform Concurrent Scraping]
    Blocked_Check{Check for Blocked Pages}
    Notify_Error[Notify User on Blocked Pages]
    Content_Aggregation[Aggregate Content and Apply Ignore Patterns]
    Metadata_Optional[Include Metadata if Flag Set]
    Package_Content[Package Content in Structured Format]
    Logging[Log Process Details and Errors]
    Write_Output[Write Output File in txt or md]
    Final_Review[Final User Review]

    CLI_Input --> URL_Validation
    URL_Validation --> Decide_Scraper
    Decide_Scraper -- Firecrawl --> Firecrawl
    Decide_Scraper -- Alternative --> Fallback_Scraper
    Firecrawl --> Concurrent_Scraping
    Fallback_Scraper --> Concurrent_Scraping
    Concurrent_Scraping --> Blocked_Check
    Blocked_Check -- Yes --> Notify_Error
    Blocked_Check -- No --> Content_Aggregation
    Notify_Error --> Content_Aggregation
    Content_Aggregation --> Metadata_Optional
    Metadata_Optional --> Package_Content
    Package_Content --> Logging
    Package_Content --> Write_Output
    Write_Output --> Final_Review
    Logging --> Final_Review