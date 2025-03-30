"""
Tests for the Firecrawl scraper
"""

import unittest
from unittest.mock import Mock, patch
from src.scrapers.firecrawl import FirecrawlScraper

class TestFirecrawlScraper(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.scraper = FirecrawlScraper(api_key=self.api_key)
        
    def test_matches_ignore_pattern_full_url(self):
        """Test matching full URL patterns"""
        patterns = ["https://example.com/path/*"]
        self.assertTrue(self.scraper._matches_ignore_pattern("https://example.com/path/to/page", patterns))
        self.assertFalse(self.scraper._matches_ignore_pattern("https://example.com/other/path", patterns))
        
    def test_matches_ignore_pattern_path(self):
        """Test matching path patterns"""
        patterns = ["/path/*"]
        self.assertTrue(self.scraper._matches_ignore_pattern("https://example.com/path/to/page", patterns))
        self.assertFalse(self.scraper._matches_ignore_pattern("https://example.com/other/path", patterns))
        
    def test_filter_content(self):
        """Test content filtering"""
        content = {
            'base_url': 'https://example.com',
            'pages': [
                {'url': 'https://example.com/page1', 'content': 'content1'},
                {'url': 'https://example.com/page2', 'content': 'content2'},
                {'url': 'https://example.com/ignore', 'content': 'ignore_content'}
            ]
        }
        
        patterns = ["/ignore"]
        filtered = self.scraper._filter_content(content, patterns)
        
        self.assertEqual(len(filtered['pages']), 2)
        self.assertTrue(all('ignore' not in page['url'] for page in filtered['pages']))
        
    @patch('src.scrapers.firecrawl.firecrawl.Client')
    def test_scrape(self, mock_client):
        """Test the scrape method"""
        mock_client.return_value.scrape.return_value = {
            'base_url': 'https://example.com',
            'pages': [
                {'url': 'https://example.com/page1', 'content': 'content1'},
                {'url': 'https://example.com/page2', 'content': 'content2'}
            ]
        }
        
        result = self.scraper.scrape("https://example.com", ignore_patterns=["/page2"])
        
        self.assertEqual(len(result['pages']), 1)
        self.assertEqual(result['pages'][0]['url'], 'https://example.com/page1')

if __name__ == '__main__':
    unittest.main()
