"""
Tests for the ContentPackager
"""

import unittest
from unittest.mock import Mock, patch
from src.packager import ContentPackager, ContentMetadata
from pathlib import Path
import json

class TestContentMetadata(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://example.com"
        self.scrape_time = datetime.datetime(2025, 3, 30, 18, 0, 0)
        self.metadata = ContentMetadata(self.base_url, self.scrape_time)
        
    def test_add_page(self):
        """Test adding page metadata"""
        page_data = {
            'url': 'https://example.com/page1',
            'title': 'Page 1',
            'content': 'Content of page 1'
        }
        
        self.metadata.add_page(page_data)
        
        self.assertEqual(len(self.metadata.pages), 1)
        self.assertEqual(self.metadata.total_pages, 1)
        self.assertEqual(self.metadata.total_content_size, len(page_data['content']))
        
    def test_to_dict(self):
        """Test converting metadata to dictionary"""
        self.metadata.add_page({
            'url': 'https://example.com/page1',
            'title': 'Page 1',
            'content': 'Content of page 1'
        })
        
        metadata_dict = self.metadata.to_dict()
        
        self.assertEqual(metadata_dict['base_url'], self.base_url)
        self.assertEqual(metadata_dict['scrape_time'], self.scrape_time.isoformat())
        self.assertEqual(len(metadata_dict['pages']), 1)
        
    def test_to_json(self):
        """Test converting metadata to JSON"""
        self.metadata.add_page({
            'url': 'https://example.com/page1',
            'title': 'Page 1',
            'content': 'Content of page 1'
        })
        
        json_str = self.metadata.to_json()
        self.assertTrue(json_str.startswith("{\"base_url\":\""))
        self.assertTrue(json_str.endswith("}"))

class TestContentPackager(unittest.TestCase):
    def setUp(self):
        self.packager = ContentPackager(output_format='txt')
        self.sample_content = {
            'base_url': 'https://example.com',
            'pages': [
                {
                    'title': 'Home',
                    'url': 'https://example.com',
                    'content': 'Sample content...'
                }
            ]
        }
        
    def test_format_content(self):
        """Test content formatting"""
        formatted = self.packager.format_content(self.sample_content, include_metadata=True)
        self.assertIn("--- Page Metadata ---", formatted)
        self.assertIn("--- Page Content ---", formatted)
        
    def test_package_txt(self):
        """Test packaging in text format"""
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            self.packager.package(self.sample_content, 'output.txt', include_metadata=True)
            mock_open.assert_called_once_with('output.txt', 'w', encoding='utf-8')
        
    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.write_text')
    def test_package_json(self, mock_write_text, mock_mkdir):
        """Test packaging in JSON format"""
        packager = ContentPackager(output_format='json')
        packager.package(self.sample_content, 'output.json', include_metadata=True)
        
        # Verify directory creation
        mock_mkdir.assert_called()
        
        # Verify metadata file creation
        self.assertTrue(mock_write_text.call_count > 0)

if __name__ == '__main__':
    unittest.main()
