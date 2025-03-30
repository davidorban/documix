"""
Module for packaging scraped content into structured documents
"""

from typing import Dict, List, Optional
import datetime
import json
from pathlib import Path

class ContentMetadata:
    """
    Class for managing content metadata
    """
    
    def __init__(self, base_url: str, scrape_time: datetime.datetime):
        """
        Initialize metadata
        
        Args:
            base_url: The base URL that was scraped
            scrape_time: The time when scraping occurred
        """
        self.base_url = base_url
        self.scrape_time = scrape_time
        self.pages: List[Dict] = []
        self.total_pages = 0
        self.total_content_size = 0
        
    def add_page(self, page_data: Dict) -> None:
        """
        Add page metadata
        
        Args:
            page_data: Dictionary containing page information
        """
        url = page_data.get('url', '')
        title = page_data.get('title', 'Untitled')
        content = page_data.get('content', '')
        
        page_metadata = {
            'url': url,
            'title': title,
            'content_size': len(content),
            'scrape_time': self.scrape_time.isoformat(),
            'relative_path': self._get_relative_path(url)
        }
        
        self.pages.append(page_metadata)
        self.total_pages += 1
        self.total_content_size += len(content)
        
    def _get_relative_path(self, url: str) -> str:
        """
        Get the relative path from the base URL
        
        Args:
            url: The URL to get relative path for
            
        Returns:
            Relative path string
        """
        from urllib.parse import urlparse
        base_path = urlparse(self.base_url).path
        page_path = urlparse(url).path
        
        if page_path.startswith(base_path):
            return page_path[len(base_path):].lstrip('/')
        return page_path
    
    def to_dict(self) -> Dict:
        """
        Convert metadata to dictionary
        
        Returns:
            Dictionary containing all metadata
        """
        return {
            'base_url': self.base_url,
            'scrape_time': self.scrape_time.isoformat(),
            'total_pages': self.total_pages,
            'total_content_size': self.total_content_size,
            'pages': self.pages
        }
    
    def to_json(self) -> str:
        """
        Convert metadata to JSON string
        
        Returns:
            JSON string representation of metadata
        """
        return json.dumps(self.to_dict(), indent=2)

class ContentPackager:
    """
    Class for packaging scraped content
    """
    
    def __init__(self, output_format: str = 'txt'):
        """
        Initialize the packager with output format
        
        Args:
            output_format: The format to output the content ('txt' or 'json')
        """
        self.output_format = output_format.lower()
        self.supported_formats = ['txt', 'json']
        
        if self.output_format not in self.supported_formats:
            raise ValueError(f"Unsupported format: {output_format}. Supported formats: {self.supported_formats}")
    
    def create_header(self, url: str, page_count: int) -> str:
        """
        Create a structured header for the output document
        
        Args:
            url: The URL that was scraped
            page_count: Number of pages scraped
            
        Returns:
            Formatted header string
        """
        now = datetime.datetime.now()
        header = f"""
=== Website Documentation ===

URL: {url}
Generation Date: {now.strftime('%Y-%m-%d %H:%M:%S')}
Page Count: {page_count}

=== Content ===
"""
        return header
    
    def format_content(self, content: Dict, include_metadata: bool = False) -> str:
        """
        Format the scraped content into a structured format
        
        Args:
            content: Dictionary containing scraped content
            include_metadata: Whether to include page metadata
            
        Returns:
            Formatted content string
        """
        formatted_content = ""
        
        for page in content.get('pages', []):
            if include_metadata:
                formatted_content += f"\n--- Page Metadata ---\n"
                formatted_content += f"Title: {page.get('title', 'N/A')}\n"
                formatted_content += f"URL: {page.get('url', 'N/A')}\n"
                formatted_content += f"Content Size: {len(page.get('content', ''))} bytes\n"
            
            formatted_content += f"\n--- Page Content ---\n{page.get('content', '')}\n"
        
        return formatted_content
    
    def package(self, content: Dict, output_path: str, include_metadata: bool = False) -> None:
        """
        Package the content into a file
        
        Args:
            content: Dictionary containing scraped content
            output_path: Path to save the output file
            include_metadata: Whether to include page metadata
        """
        try:
            output_path = Path(output_path)
            
            if self.output_format == 'json':
                # For JSON output, create a directory structure
                output_dir = output_path.parent / 'documix_output'
                output_dir.mkdir(parents=True, exist_ok=True)
                
                # Create metadata file
                metadata = ContentMetadata(
                    content.get('base_url', ''),
                    datetime.datetime.now()
                )
                
                for page in content.get('pages', []):
                    metadata.add_page(page)
                    
                    # Create page content files
                    relative_path = metadata.pages[-1]['relative_path']
                    page_dir = output_dir / Path(relative_path).parent
                    page_dir.mkdir(parents=True, exist_ok=True)
                    
                    page_file = page_dir / f"{Path(relative_path).stem}.txt"
                    page_file.write_text(page.get('content', ''), encoding='utf-8')
                
                # Write metadata
                metadata_file = output_dir / 'metadata.json'
                metadata_file.write_text(metadata.to_json(), encoding='utf-8')
                
                print(f"Content packaged successfully to: {output_dir}")
                print(f"Metadata written to: {metadata_file}")
                
            else:  # txt format
                with open(output_path, 'w', encoding='utf-8') as f:
                    header = self.create_header(
                        content.get('base_url', ''),
                        len(content.get('pages', []))
                    )
                    formatted_content = self.format_content(content, include_metadata)
                    f.write(header + formatted_content)
                    
                print(f"Content packaged successfully to: {output_path}")
                
        except Exception as e:
            print(f"Error packaging content: {e}")
            raise

def main():
    """Main function for testing"""
    packager = ContentPackager(output_format='json')
    sample_content = {
        'base_url': 'https://example.com',
        'pages': [
            {
                'title': 'Home',
                'url': 'https://example.com',
                'content': 'Sample content...'
            },
            {
                'title': 'About',
                'url': 'https://example.com/about',
                'content': 'About page content...'
            }
        ]
    }
    packager.package(sample_content, 'output.json', include_metadata=True)

if __name__ == "__main__":
    main()
