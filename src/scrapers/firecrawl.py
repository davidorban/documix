"""
Firecrawl scraper integration module
"""

import os
from typing import Dict, List, Optional
import firecrawl

class FirecrawlScraper:
    """Scraper implementation using Firecrawl"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the scraper with optional API key"""
        self.api_key = api_key or os.getenv('FIRECRAWL_API_KEY')
        if not self.api_key:
            raise ValueError("Firecrawl API key must be provided or set in environment variable FIRECRAWL_API_KEY")
    
    def _matches_ignore_pattern(self, url: str, ignore_patterns: List[str]) -> bool:
        """
        Check if a URL matches any of the ignore patterns
        
        Args:
            url: The URL to check
            ignore_patterns: List of patterns to match against
            
        Returns:
            True if the URL should be ignored, False otherwise
        """
        import fnmatch
        from urllib.parse import urlparse
        
        # Parse the URL to get the path
        parsed_url = urlparse(url)
        path = parsed_url.path
        
        # Check each pattern
        for pattern in ignore_patterns:
            # Support both full URLs and path patterns
            if pattern.startswith('http'):
                if fnmatch.fnmatch(url, pattern):
                    return True
            else:
                if fnmatch.fnmatch(path, pattern):
                    return True
        
        return False
    
    def _filter_content(self, content: Dict, ignore_patterns: Optional[List[str]] = None) -> Dict:
        """
        Filter the scraped content based on ignore patterns
        
        Args:
            content: Dictionary containing the scraped content
            ignore_patterns: Optional list of patterns to ignore
            
        Returns:
            Filtered content dictionary
        """
        if not ignore_patterns:
            return content
            
        filtered_content = {
            'base_url': content.get('base_url', ''),
            'pages': []
        }
        
        for page in content.get('pages', []):
            page_url = page.get('url', '')
            if not self._matches_ignore_pattern(page_url, ignore_patterns):
                filtered_content['pages'].append(page)
                
        return filtered_content
    
    def scrape(self, url: str, ignore_patterns: Optional[List[str]] = None) -> Dict:
        """
        Scrape content from a URL using Firecrawl
        
        Args:
            url: The URL to scrape
            ignore_patterns: Optional list of patterns to ignore
            
        Returns:
            Dictionary containing the filtered scraped content
        """
        try:
            client = firecrawl.Client(api_key=self.api_key)
            result = client.scrape(url)
            
            if ignore_patterns:
                result = self._filter_content(result, ignore_patterns)
            
            return result
            
        except firecrawl.FirecrawlError as e:
            print(f"Error during scraping: {e}")
            raise

def main():
    """Main function for testing"""
    scraper = FirecrawlScraper()
    result = scraper.scrape("https://example.com")
    print(result)

if __name__ == "__main__":
    main()
