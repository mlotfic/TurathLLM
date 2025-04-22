# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:18:26 2025

@author: m.lotfi
"""

import os
import json
import pandas as pd
from pathlib import Path
from pprint import pprint
import glob
import shutil
import datetime
import re
import time

from camel_tools.utils.charmap import CharMapper
from camel_tools.utils.normalize import normalize_unicode

from typing import List, Dict, Tuple
from collections import defaultdict

from bs4 import BeautifulSoup


# # Unix timestamp
# timestamp = 1686325770

# # Convert to a datetime object
# date_time = datetime.datetime.fromtimestamp(timestamp)

# # Print the date in a readable format
# print(date_time.strftime('%Y-%m-%d'))

'''
volumes: 
    This key contains a list of volume identifiers. In this case, it has a single volume, '1', indicating that the document is a single-volume work.

headings: 
    This is a list of dictionaries, each representing a heading or section within the document. 
    Each dictionary contains:

        title: 
            The title of the section or heading, which is in Arabic.
        level: 
            The hierarchical level of the heading, indicating its depth in the document's structure (e.g., 1 for main sections, 2 for subsections, etc.).
        page: 
            The page number where the heading starts.
        print_pg_to_pg: 
            This dictionary maps printed page numbers to their corresponding logical page numbers. 
            The keys are strings in the format 'volume,page', and the values are the logical page numbers. 
            This mapping is useful for documents where the printed page numbers might differ from the logical sequence.

volume_bounds: 
    This dictionary defines the range of pages for each volume. 
    The key is the volume identifier, and the value is a list with two elements: 
        the starting and ending page numbers of the volume.

page_map: 
    This is a list of strings, each representing a page in the format 'volume,page'. 
    It provides a sequential list of all pages in the document.

page_headings: 
    This dictionary maps page numbers to a list of indices that correspond to the headings list. 
    It indicates which headings appear on each page.

non_author: 
    This key is an empty list, which might be intended to store information about non-author contributors or sections, but it currently contains no data.

'''

def read_json_file(file_path):
    """Read JSON file with proper encoding for Arabic text"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def to_csv(df, csv_path):
    """Save DF to file with proper encoding for Arabic text"""
    # Ensure directory exists
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)    
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    return csv_path

def walk_through_json_files(directory):
    """
    Walks through all json files in the specified directory and subdirectories.
    Returns a list of Path objects for the found JSON files.
    """
    try:
        directory_path = Path(directory)
        if not directory_path.exists():
            print(f"Directory {directory} does not exist!")
            return []  # Return an empty list if the directory doesn't exist

        json_files = list(directory_path.rglob("*.json"))  # Use "*.json" to match all JSON files

        if not json_files:
            print(f"No json files found in {directory}")
            return []  # Return an empty list if no files are found

        print(f"Found {len(json_files)} json files")
        return json_files

    except Exception as e:
        print(f"Error walking through directory: {str(e)}")
        return []  # Return an empty list on error


def parse_metadata(text, book_id_file, book_id):
    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize result dictionary
    metadata = {}
    
    # Regex pattern to match key-value pairs
    pattern = r'^(.*?)\s*:\s*(.+)$'
    
    for line in lines:
        # Strip whitespace
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Try to match the pattern
        match = re.match(pattern, line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            
            # Add to metadata dictionary
            metadata[key] = value
            
    metadata['book_id_file'] = book_id_file 
    metadata['book_id']      = book_id
    return metadata


def generate_arabic_slug(text: str) -> str:
    """Generate URL-friendly slug from Arabic text using camel-tools"""
    try:
        # Initialize Arabic to Buckwalter mapper
        ar2bw = CharMapper.builtin_mapper('ar2bw')
        
        # Normalize Unicode form and remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        text = normalize_unicode(text)
        
        # Remove special characters and tashkeel
        text = re.sub(r'[\u064B-\u065F\u0670]', '', text)  # Remove tashkeel
        text = re.sub(r'[^\w\s-]', '', text)
        
        # Replace spaces with hyphens
        text = re.sub(r'\s+', '-', text.strip())
        
        # Transliterate to Buckwalter
        slug = ar2bw.map_string(text)
        
        # Clean up slug
        slug = re.sub(r'[^\w-]', '', slug)
        slug = re.sub(r'-+', '-', slug)
        
        return slug.lower()
    except Exception as e:
        print(f"Error generating slug: {str(e)}")
        return ""

def generate_section_number(level: int, parent_number: str = None, counters: dict = None) -> Tuple[str, dict]:
    """Generate hierarchical section numbering"""
    if counters is None:
        counters = defaultdict(lambda: defaultdict(int))
    
    if level == 1:
        counters[1]['counter'] += 1
        return str(counters[1]['counter']), counters
    
    if parent_number:
        counters[level][parent_number] += 1
        return f"{parent_number}.{counters[level][parent_number]}", counters
    
    return "", counters

def find_parent_section(sections: List[Dict], current_level: int) -> Dict:
    """Find the parent section for the current level"""
    if not sections or current_level == 1:
        return None
    
    for section in reversed(sections):
        if section['level'] == current_level - 1:
            return section
    return None

def get_section_pages(sections: List[Dict], book_id) -> Dict[str, List[int]]:
    """
    Generate page ranges for each section based on hierarchy
    Returns dict of section numbers mapped to their page ranges
    """
    section_pages = {}
    
    for i, current_section in enumerate(sections):
        start_page = current_section['page']
        current_level = current_section['level']
        
        # Find the end page by looking at the next section at same or higher level
        end_page = start_page
        for next_section in sections[i + 1:]:
            if next_section['level'] <= current_level:
                end_page = next_section['page'] - 1
                break
        else:
            # If no next section found, use the start page as end page
            end_page = start_page
            
        # Ensure end_page is not less than start_page
        end_page = max(end_page, start_page)
        
        # Store page range
        section_pages[current_section['section_number']] = list(range(start_page, end_page + 1))
    
    return section_pages

def process_arabic_headings(content: List[Dict], book_id) -> Tuple[List[Dict], Dict[str, List[int]]]:
    """Process Arabic content and add slugs, section numbers, and page ranges"""
    processed_sections = []
    section_counters = defaultdict(lambda: defaultdict(int))
    
    for item in content:
        # Create basic section
        section = {
            'book_id'       : book_id,
            'header_id'     : len(processed_sections) + 1,
            'header'        : item['title'],
            'level'         : item['level'],
            'page'          : item['page'],
            'slug'          : generate_arabic_slug(item['title']),
            'section_number': '',
            'parent_id'     : None
        }
        
        # Find parent and generate section number
        parent = find_parent_section(processed_sections, section['level'])
        
        if parent:
            section['parent_id'] = parent['header_id']
            section_number, section_counters = generate_section_number(
                section['level'],
                parent['section_number'],
                section_counters
            )
        else:
            section_number, section_counters = generate_section_number(
                section['level'],
                None,
                section_counters
            )
            
        section['section_number'] = section_number
        processed_sections.append(section)
    
    # Second pass: Calculate page ranges
    section_pages = get_section_pages(processed_sections, book_id)
    
    # Add page ranges to sections
    for section in processed_sections:
        section['pages'] = section_pages.get(section['section_number'], [section['page']])
        
        # If pages list is empty, at least include the section's own page
        if not section['pages']:
            section['pages'] = [section['page']]
    
    section_pages_list =[]
    for key, value in section_pages.items():
        section_pages_list.append({
            "book_id"               : book_id,
            "section_number"        : key,
            'pages'                 : value
        })
        
    return processed_sections, section_pages_list

def get_footer(text, book_id, page_id):
    """
    Extract footer references from text that's split by a line of underscores
    
    Args:
        text (str): Input text containing main content and footer
        book_id: Identifier for the book
        page_id: Page number (default=2)
        
    Returns:
        tuple: (main_text, footer_references)
    """
    footer_ref = []
    # Pattern to capture reference number in parentheses and its content
    footer_pattern = r'\(\^([١٢٣٤٥٦٧٨٩٠]+)\)(.*?)(?=\(\^|$)'
    
    # Split text into main content and footer using underscore delimiter
    parts = text.split('_________\n')
    main_text = parts[0]
    footer = parts[1] if len(parts) > 1 else ''
    
    # Find all references in footer
    matches = re.findall(footer_pattern, footer, re.DOTALL)
    if matches:        
        for ref, content in matches:
            footer_ref.append({
                "book_id": book_id,
                "page_id": page_id,
                "ref:": f"(^{ref})",
                "Ref_context": content.strip()
            })
    else:
        footer_pattern = r'\(\^?([١٢٣٤٥٦٧٨٩٠]+)\)'
        # Find all references in footer
        matches = re.findall(footer_pattern, footer, re.DOTALL)        
        if matches: 
            # Split text by footer pattern
            parts1 = re.split(footer_pattern, footer)
            # Separate content and footers
            contents = parts1[::2]  # Even indices are content    
            # Clean up content
            contents = [content.strip() for content in contents if content.strip()]
            
            # Ensure we don't try to access more contents than available
            for x, ref in enumerate(matches):
                # Use the content if available, otherwise use an empty string
                content = contents[x] if x < len(contents) else ""
                footer_ref.append({
                    "book_id": book_id,
                    "page_id": page_id,
                    "ref:": f"(^{ref})",
                    "Ref_context": content
                })
                
    return main_text, footer_ref
  

def get_page_structure(text, book_id, page_id):
    """
    Parse Arabic text to extract headers, references, and footer structure
    
    Approach:
    1. Split text into main content and footer
    2. Extract headers from span tags
    3. Process text between headers
    4. Track references throughout the document
    
    Args:
        text (str): Input text with HTML span tags and references
        book_id: Book identifier
        page_id: Page number (default=2)
        
    Returns:
        list: [headers_titles, headers_text, ref_text, footer_ref]
    """
    
    # Pattern for references like (^١)
    ref_pattern = r'\(\^?([١٢٣٤٥٦٧٨٩٠]+)\)'

    # Pattern for headers in span tags with optional reference
    header_pattern = r'(<span[^>]*>(.*)</span>)(.*(\(\^[١٢٣٤٥٦٧٨٩٠]+\))?)'
    
    # header_pattern = r'(<span data-type="title" id=toc-\d+>([^<]+)</span>)(.*(\(\^[١٢٣٤٥٦٧٨٩٠]+\))?)'

    # Initialize storage lists
    headers_titles = []  # Store header titles
    headers_text = []    # Store text under each header
    ref_text = []        # Store reference information
    
    # Split and get footer references
    main_text, footer_ref = get_footer(text, book_id, page_id)

    # Find all header matches in main text
    matches = list(re.finditer(header_pattern, main_text))
    
    # i = 0
    # match = matches[i]
    if matches:
        # Iterate through headers in main text
        for i, match in enumerate(matches):
            # Extract header components
            header_tag = match.group(1)   # Full span tag
            header_title = match.group(2)   # Text inside span
            header_ref = match.group(4)   # Reference if present: (^١)
            
            # Parse span tag for header information
            soup = BeautifulSoup(header_tag, 'html.parser')       
            span_tag = soup.find("span")
            
            # Extract header title and ID
            if span_tag:
                header_title = span_tag.text.strip()
                match_id = re.search(r'\d+', str(span_tag.get('id', '')))
                header_id = match_id.group() if match_id else 0
            else:
                header_title = "" 
                header_id = 0
            
    
            # Handle text before first header
            if (i == 0) and len(main_text.split(header_tag)) > 1 :
                leftover = main_text.split(header_tag)[0].strip()            
                if leftover and not bool(BeautifulSoup(leftover, 'html.parser').find("span")):                
                    headers_text.append({
                        "book_id": book_id,
                        "page_id": page_id,
                        'header_id': int(header_id)-1,
                        'header_text': leftover,
                        'hasRef': bool(re.search(ref_pattern, leftover))
                    })
                    # Track references in leftover text
                    if bool(re.search(ref_pattern, leftover)):
                        for ref_id in re.findall(ref_pattern, leftover):
                            ref_text.append({
                                "book_id": book_id,
                                "page_id": page_id,
                                'header_id': int(header_id)-1,
                                "type": "in_header_text",
                                "ref_id": ref_id                        
                            })
                
            # Store header title information
            headers_titles.append({
                "book_id": book_id,
                "page_id": page_id,
                'header_id': int(header_id),
                'header_title': header_title,
                'hasRef': bool(re.search(ref_pattern, match.group(0)))
            })
            
            # Extract text between current and next header
            start = match.end()
            if i < len(matches) - 1:
                end = matches[i+1].start()
            else:
                # Last header - get text until end of main_text
                end = len(main_text)
                
            header_content = main_text[start:end].strip() if start < end else ""
            
            # Store header text information
            headers_text.append({
                "book_id": book_id,
                "page_id": page_id,
                'header_id': int(header_id),
                'header_text': header_content,
                'hasRef': bool(re.search(ref_pattern, header_content))
            })
            
            # Track references in header text and title
            if bool(re.search(ref_pattern, header_content)):
                for ref_id in re.findall(ref_pattern, header_content):
                    ref_text.append({
                        "book_id": book_id,
                        "page_id": page_id,
                        'header_id': int(header_id),
                        "type": "in_header_text",
                        "ref_id": ref_id                        
                    })
                    
            if bool(re.search(ref_pattern, match.group(0))):
                for ref_id in re.findall(ref_pattern, match.group(0)):
                    ref_text.append({
                        "book_id": book_id,
                        "page_id": page_id,
                        'header_id': int(header_id),
                        "type": "in_header_title",
                        "ref_id": ref_id                        
                    })
    elif main_text:
        headers_text.append({
            "book_id": book_id,
            "page_id": page_id,
            'header_id': -1,
            'header_text': main_text,
            'hasRef': bool(re.search(ref_pattern, main_text))
        })
        
        # Track references in main_text text
        if bool(re.search(ref_pattern, main_text)):
            for ref_id in re.findall(ref_pattern, main_text):
                ref_text.append({
                    "book_id": book_id,
                    "page_id": page_id,
                    'header_id': -1,
                    "type": "in_header_text",
                    "ref_id": ref_id                        
                })       

    return [headers_titles, headers_text, ref_text, footer_ref]

def get_structure_data_from_book_json(data, book_id_file):
    """
    Process a book's JSON data to extract structured information about pages, volumes, headers, and references.
    
    Approach:
    1. Extract metadata and book information
    2. Process book structure (volumes, headings)
    3. Process each page to extract headers, text sections, and references
    4. Organize all data into respective lists for further processing or database storage
    
    Args:
        data (dict): The complete book JSON data
        book_id_file (str): Identifier for the book file
        
    Returns:
        list: Collection of extracted data lists organized by category
    """
    
    # STEP 1: Initialize empty lists to store different types of structured data
    # These lists will hold data that can later be inserted into database tables
    
    # Basic page data
    pages_data = []
    
    # Book metadata
    meta = []
    author_page_start_data = []
    info_data = []
    info_long_data = []
    non_author_data = []
    
    # Volume structure data
    volume_bound_data = []  # Stores page ranges for each volume
    volume_pair_data = []   # Maps individual pages to volumes
    volume_data = []
    
    # Headings and sections data
    headings_processed_data = []
    section_pages_data = []
    
    # Headers and references data (extracted from page content)
    headers_titles_data = []  # Store header titles
    headers_text_data = []    # Store text under each header
    ref_text_data = []        # Store reference information
    footer_ref_data = []      # Store footnote references
    
    # STEP 2: Extract main data sections from the book JSON
    meta = data.get("meta", {})
    indexes = data.get("indexes", {})
    pages = data.get("pages", [])
    
    # STEP 3: Process book metadata
    # Extract basic book identification
    book_id = str(meta.get("id", ""))
    author_page_start = meta.get("author_page_start", "")
    
    # Store author page start information
    author_page_start_data.append({
        "book_id": book_id,
        "author_page_start": author_page_start
    })
    
    # Process and store book information metadata
    info_data.append(
        parse_metadata(meta.get("info", ""), book_id_file, book_id)
    )
    info_long_data.append(
        parse_metadata(meta.get("info_long", ""), book_id_file, book_id)
    )
    
    # STEP 4: Extract book structure indexes
    volumes = indexes.get("volumes", []) 
    headings = indexes.get("headings", [])
    # print_pg_to_pg = indexes.get("print_pg_to_pg", {})
    volume_bounds = indexes.get("volume_bounds", [])
    # page_map = indexes.get("page_map", {})
    # page_headings = indexes.get("page_headings", {})
    non_author = indexes.get("non_author", [])       
    
    # STEP 5: Process volume information
    # Store basic volume identifiers
    for volume_id in volumes:
        volume_data.append({
            "book_id": book_id,
            "volume_id": volume_id
        })
    
    # Store volume boundaries (start and end pages)
    for key, value in volume_bounds.items():
        volume_bound_data.append({
            "book_id": book_id,
            "volume_id": key,
            'start_page_id': value[0],
            'end_page_id': value[1]
        })
        
    # Create mapping between each page and its volume
    for key, value in volume_bounds.items():
        # For each page in the volume range
        for page_id in range(1, value[1]+1):
            volume_pair_data.append({
                "book_id": book_id,
                "volume_id": key,
                'page_id': page_id
            })
        
    # 
    if non_author and (len(non_author) >= 1) and isinstance(non_author, list):
        for non_authr in non_author:
            non_author_data.append({
                "book_id": book_id,
                "non_author": non_authr
                })
    else:
        non_author_data.append({
            "book_id": book_id,
            "non_author": ""
            })
        
    
    
    # STEP 6: Process section headings
    # Organize hierarchical section structure
    processed_sections, section_pages = process_arabic_headings(headings, book_id)  
    
    headings_processed_data.extend(processed_sections)
    section_pages_data.extend(section_pages)
    
    # STEP 7: Process each page's content
    # page = pages[14]
    # page = [item for item in pages if item['page'] == 4][0]
    for page in pages:
        
        # Extract basic page information
        page_id = page.get("page", "")
        text = page.get("text", "")
        
        # Store page data
        pages_data.append({       
            "book_id": book_id,
            'page': page_id,
            'text': text,
            'vol': page.get("vol", "")
        })
        
        # Extract structured content from page text
        # This separates headers, content text, and references
        page_structure = get_page_structure(text, book_id, page_id)
        
        # Accumulate page structure data from all pages
        # Each page can have multiple headers, text sections, and references
        headers_titles_data.extend(page_structure[0])  # Header titles
        headers_text_data.extend(page_structure[1])    # Text content under headers
        ref_text_data.extend(page_structure[2])        # References within content
        footer_ref_data.extend(page_structure[3])      # Footer references
    
    # STEP 8: Return all collected data for further processing or database insertion
    return [
        pages_data,  # Basic page information
        
        # Book metadata
        meta, author_page_start_data, info_data, info_long_data, non_author_data,
        
        # Volume structure
        volume_bound_data, volume_pair_data,
        
        # Section structure
        headings_processed_data, volume_data, section_pages_data,
        
        # Page content structure
        headers_titles_data, headers_text_data, ref_text_data, footer_ref_data            
    ]

# Usage example
if __name__ == "__main__":    
    # file_path = "./turath_books_json/2.json"
    directory = "./turath_books_json"
    json_files = walk_through_json_files(directory)

    # Initialize storage for all output entities
    pages_data_list                 = []
    meta_list                       = []
    author_page_start_data_list     = []
    info_data_list                  = []
    info_long_data_list             = []
    non_author_data_list            = []
    volume_bound_data_list          = []
    volume_pair_data_list           = []
    headings_processed_data_list    = []
    volume_data_list                = []
    section_pages_data_list         = []
    headers_titles_data_list        = []
    headers_text_data_list          = []
    ref_text_data_list              = []
    footer_ref_data_list            = []

    # Process each JSON file
    for file_path in json_files:
        start = time.time()
        
        filename = os.path.basename(file_path)
        book_id_file = os.path.splitext(filename)[0]
        print(f"Processing {book_id_file}")

        data = read_json_file(file_path)

        [pages_data, 
         meta, author_page_start_data, info_data, info_long_data, non_author_data,
         volume_bound_data, volume_pair_data,
         headings_processed_data, volume_data, section_pages_data,
         headers_titles_data, headers_text_data, ref_text_data, footer_ref_data] = get_structure_data_from_book_json(data, book_id_file)


        df = pd.DataFrame(pages_data)
        csv_path = f'./output/books/{book_id_file}/orignal_pages.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(volume_pair_data)
        csv_path = f'./output/books/{book_id_file}/volume_page_pair.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(headings_processed_data)
        csv_path = f'./output/books/{book_id_file}/headings.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(section_pages_data)
        csv_path = f'./output/books/{book_id_file}/sections.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(headers_titles_data)
        csv_path = f'./output/books/{book_id_file}/headings_titles.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(headers_text_data)
        csv_path = f'./output/books/{book_id_file}/headings_text.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(ref_text_data)
        csv_path = f'./output/books/{book_id_file}/text_citations.csv'
        to_csv(df, csv_path)
        
        df = pd.DataFrame(footer_ref_data)
        csv_path = f'./output/books/{book_id_file}/footer_citations_values.csv'
        to_csv(df, csv_path)
        
        # Extend master lists
        meta_list.extend(meta)
        author_page_start_data_list.extend(author_page_start_data)
        info_data_list.extend(info_data)
        info_long_data_list.extend(info_long_data)
        non_author_data_list.extend(non_author_data)
        volume_bound_data_list.extend(volume_bound_data)
        volume_data_list.extend(volume_data)
        
        print(f"⏱️ Duration for {book_id_file}: {round(time.time() - start, 2)} sec")

    
    # Create DataFrames  
    df_meta_list                    = pd.DataFrame(meta_list)
    df_author_page_start_data_list  = pd.DataFrame(author_page_start_data_list)
    df_info_data_list               = pd.DataFrame(info_data_list)
    df_info_long_data_list          = pd.DataFrame(info_long_data_list)
    df_non_author_data_list         = pd.DataFrame(non_author_data_list)
    df_volume_bound_data_list       = pd.DataFrame(volume_bound_data_list)
    df_volume_data_list             = pd.DataFrame(volume_data_list)
    
    
    # Final output directory
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # File names and data collection mapping
    file_names = [
        "meta.csv", "author_page_start.csv", "info.csv", "info_long.csv", "non_author.csv",
        "volume_bound.csv", "volumes.csv"
    ]

    data_list = [
        meta_list, author_page_start_data_list, info_data_list, info_long_data_list, non_author_data_list,
        volume_bound_data_list, volume_data_list
    ]

    # Save all data to CSVs
    for data, file_name in zip(data_list, file_names):
        if data:
            file_path = os.path.join(output_dir, file_name)
            try:
                df = pd.DataFrame(data)
                to_csv(df, file_path)
                print(f"✓ Saved {file_name} with {len(df)} records.")
            except Exception as e:
                print(f"✗ Failed to save {file_name}: {str(e)}")