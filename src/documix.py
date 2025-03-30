"""
Main entrypoint for the Documix CLI tool
"""

import argparse
import sys
from typing import List, Optional
import logging
from pathlib import Path
import json

from src.packager import ContentPackager
from src.scrapers.firecrawl import FirecrawlScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DocumixCLI:
    """
    Main CLI class for Documix
    """
    
    def __init__(self):
        """
        Initialize the CLI with default settings
        """
        self.scraper = FirecrawlScraper()
        self.packager = ContentPackager()
        
    def parse_arguments(self) -> argparse.Namespace:
        """
        Parse command line arguments
        
        Returns:
            Parsed arguments
        """
        parser = argparse.ArgumentParser(
            description="Documix - Website documentation and scraping tool"
        )
        
        # Subparsers for each command
        subparsers = parser.add_subparsers(dest='command', required=True)
        
        # Package command parser
        package_parser = subparsers.add_parser(
            'package',
            help='Package website content into a structured document'
        )
        package_parser.add_argument(
            'url',
            help='The URL to scrape and package'
        )
        package_parser.add_argument(
            '--output',
            help='Output file path (default: documix_output.txt for text, documix_output.json for JSON)'
        )
        package_parser.add_argument(
            '--ignore',
            nargs='*',
            help='Patterns to ignore during scraping'
        )
        package_parser.add_argument(
            '--scraper',
            choices=['firecrawl'],  # Only Firecrawl is currently supported
            default='firecrawl',
            help='Primary scraper to use'
        )
        package_parser.add_argument(
            '--format',
            choices=['txt', 'json'],
            default='txt',
            help='Output format (txt or json)'
        )
        package_parser.add_argument(
            '--verbose',
            action='store_true',
            help='Enable verbose logging'
        )
        
        return parser.parse_args()
    
    def setup_logging(self, verbose: bool) -> None:
        """
        Configure logging based on verbosity level
        
        Args:
            verbose: Whether to enable verbose logging
        """
        if verbose:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
    
    def validate_output_path(self, url: str, output_format: str, output_path: Optional[str] = None) -> str:
        """
        Validate and generate output path if not provided
        
        Args:
            url: The URL being processed
            output_format: The desired output format
            output_path: Optional user-provided output path
            
        Returns:
            Validated output path
        """
        if output_path:
            output_path = str(Path(output_path))
        else:
            base_name = Path(url).stem or 'documix_output'
            output_path = f"{base_name}.{output_format}"
        
        return output_path
    
    def package_content(self, url: str, output_path: str, ignore_patterns: Optional[List[str]] = None, 
                       output_format: str = 'txt', include_metadata: bool = True) -> None:
        """
        Package website content
        
        Args:
            url: The URL to scrape
            output_path: Path to save the output
            ignore_patterns: Patterns to ignore during scraping
            output_format: Output format (txt or json)
            include_metadata: Whether to include metadata
        """
        try:
            logger.info(f"Starting to scrape: {url}")
            
            # Scrape content
            content = self.scraper.scrape(url, ignore_patterns)
            
            logger.info(f"Successfully scraped {len(content.get('pages', []))} pages")
            
            # Package content
            self.packager = ContentPackager(output_format=output_format)
            self.packager.package(content, output_path, include_metadata=include_metadata)
            
            logger.info(f"Content packaged successfully to: {output_path}")
            
        except Exception as e:
            logger.error(f"Error during processing: {str(e)}")
            raise
    
    def run(self) -> None:
        """
        Main run method
        """
        try:
            args = self.parse_arguments()
            self.setup_logging(args.verbose)
            
            if args.command == 'package':
                logger.info("=== Documix Package Command ===")
                logger.info(f"URL: {args.url}")
                logger.info(f"Scraper: {args.scraper}")
                logger.info(f"Output format: {args.format}")
                
                output_path = self.validate_output_path(
                    args.url,
                    args.format,
                    args.output
                )
                
                self.package_content(
                    args.url,
                    output_path,
                    args.ignore,
                    args.format
                )
                
        except Exception as e:
            logger.error(f"Critical error: {str(e)}")
            sys.exit(1)

def main() -> None:
    """Main function"""
    cli = DocumixCLI()
    cli.run()

if __name__ == "__main__":
    main()
