# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 10:51:59 2025

@author: m.lotfi
"""

import codecs
import json
import os
from datetime import datetime

def convert_to_serializable(obj):
    """
    Recursively convert BeautifulSoup Tags and complex objects to serializable format
    
    Strategies:
    1. Convert BeautifulSoup Tags to text
    2. Handle datetime objects
    3. Convert complex objects to strings
    4. Recursively process nested structures
    """
    if hasattr(obj, 'get_text'):
        # BeautifulSoup Tag conversion
        return obj.get_text()
    elif isinstance(obj, datetime):
        # Datetime serialization
        return obj.isoformat()
    elif isinstance(obj, dict):
        # Recursively process dictionary
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # Recursively process list
        return [convert_to_serializable(item) for item in obj]
    elif hasattr(obj, '__dict__'):
        # Convert object with __dict__ to dictionary
        return convert_to_serializable(obj.__dict__)
    else:
        # Try to serialize, if fails convert to string
        try:
            json.dumps(obj)
            return obj
        except TypeError:
            return str(obj)
        
def to_json_with_arabic(data, base_folder, filename, overwrite = True, **kwargs):

    file_path = os.path.join(base_folder, filename)
    
    # Check if the specified HTML file exists.
    if os.path.exists(file_path) and (overwrite == False):
        print(f"The file '{filename}' exists.")
        # File exists. Return None.
        return None
    else:
        # File does not exist. Create the necessary directory if it doesn't exist.
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        # Preprocess data to make it JSON serializable
        try:
            serializable_data = convert_to_serializable(data)
        except Exception as conversion_error:
            print(f"Data conversion error: {conversion_error}")
            serializable_data = str(data)

        # Default JSON saving configurations
        default_config = {
            'ensure_ascii': False,  # Critical for Arabic text
            'indent': 4,            # Readable formatting
            'sort_keys': False      # Preserve original order
        }

        # Merge default config with user-provided kwargs
        json_config = {**default_config, **kwargs}

        try:
            # Method 1: Using codecs (Recommended for Arabic)
            with codecs.open(file_path, 'w', encoding='utf-8') as f:
                json.dump(serializable_data, f, **json_config)

            print(f"JSON saved successfully: {file_path}")
            return file_path

        except Exception as e:
            print(f"Error saving JSON: {e}")

            # Fallback method
            try:
                # Method 2: Standard JSON dump with UTF-8
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(serializable_data, f, **json_config)

                print(f"Fallback JSON save successful: {file_path}")
                return file_path

            except Exception as fallback_error:
                print(f"Fallback JSON save failed: {fallback_error}")

        return None
    
# Define the directory containing JSON files
directory_path = '.'

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a JSON file
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)
        
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                # Print the data or process it as needed
                print(f"Contents of {filename}:")
                #print(data)
                to_json_with_arabic(data, "base_folder", filename)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from file {filename}: {e}")