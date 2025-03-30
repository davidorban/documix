"""
Tests for the Documix CLI
"""

import unittest
from unittest.mock import Mock, patch
from src.documix import DocumixCLI
from src.scrapers.firecrawl import FirecrawlScraper
from src.packager import ContentPackager

class TestDocumixCLI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.cli = DocumixCLI()
        self.mock_scraper = Mock(spec=FirecrawlScraper)
        self.mock_packager = Mock(spec=ContentPackager)
        self.cli.scraper = self.mock_scraper
        self.cli.packager = self.mock_packager
        
    def test_parse_arguments(self):
        """Test argument parsing"""
        args = self.cli.parse_arguments()
        self.assertEqual(args.command, 'package')
        self.assertEqual(args.scraper, 'firecrawl')
        self.assertEqual(args.format, 'txt')
        
    def test_setup_logging(self):
        """Test logging setup"""
        # Test verbose mode
        self.cli.setup_logging(True)
        self.assertEqual(self.cli.logger.level, 10)  # DEBUG level
        
        # Test non-verbose mode
        self.cli.setup_logging(False)
        self.assertEqual(self.cli.logger.level, 20)  # INFO level
        
    def test_validate_output_path(self):
        """Test output path validation"""
        # Test with no output path
        path = self.cli.validate_output_path('https://example.com', 'txt')
        self.assertEqual(path, 'documix_output.txt')
        
        # Test with custom output path
        custom_path = self.cli.validate_output_path(
            'https://example.com',
            'json',
            'custom_output.json'
        )
        self.assertEqual(custom_path, 'custom_output.json')
        
    @patch('builtins.print')
    def test_package_content(self, mock_print):
        """Test content packaging"""
        # Mock scraper response
        mock_content = {
            'base_url': 'https://example.com',
            'pages': [{'url': 'https://example.com/page1', 'content': 'content'}]
        }
        self.mock_scraper.scrape.return_value = mock_content
        
        # Test packaging
        self.cli.package_content(
            'https://example.com',
            'output.txt',
            ignore_patterns=['/ignore'],
            output_format='txt'
        )
        
        # Verify scraper was called
        self.mock_scraper.scrape.assert_called_once_with(
            'https://example.com',
            ['/ignore']
        )
        
        # Verify packager was called
        self.mock_packager.package.assert_called_once()
        
    def test_run(self):
        """Test CLI run method"""
        # Mock arguments
        with patch('argparse.ArgumentParser.parse_args') as mock_parse_args:
            mock_args = Mock()
            mock_args.command = 'package'
            mock_args.url = 'https://example.com'
            mock_args.output = None
            mock_args.ignore = ['/ignore']
            mock_args.scraper = 'firecrawl'
            mock_args.format = 'txt'
            mock_args.verbose = True
            mock_parse_args.return_value = mock_args
            
            # Run CLI
            self.cli.run()
            
            # Verify logging was set up
            self.assertEqual(self.cli.logger.level, 10)  # DEBUG level
            
            # Verify package_content was called
            self.mock_scraper.scrape.assert_called_once()
            self.mock_packager.package.assert_called_once()

if __name__ == '__main__':
    unittest.main()
