# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 08:55:58 2025

@author: m.lotfi
"""
import os
import json
import pandas as pd

# data_normalized = data
def get_source_relational_db(data_normalized, language = "Arabic", Diacritics = True):
        
    # Initialize empty lists to store data for different tables 
    collection_data = []
    
    for book, book_data in data_normalized.items():
        book_fullname  = book_data.get("name", "")
        collections    = book_data.get("collection", [])
        
        for collection in collections:
            collection_data.append({
                "book_shortname"    : book,
                "book"              : book_fullname,
                "book_filename"     : collection.get("name", ""),
                "author"            : collection.get("author", ""),
                "language"          : collection.get("language", ""),
				"has_sections"      : collection.get("has_sections", ""),
				"direction"         : collection.get("direction", ""),
				"source"            : collection.get("source", ""),
				"comments"          : collection.get("comments", ""),
				"link"              : collection.get("link", ""),
				"linkmin"           : collection.get("linkmin", "")
			})
      
    return collection_data

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
    
   
# Usage example
if __name__ == "__main__":
    
    file_path = "editions.json"
    
    # Read the JSON file    
    data = read_json_file(file_path)
    len(data)
    
    editions_data = get_source_relational_db(data, language = "", Diacritics = "")

    # Create DataFrames   
    editions_df   = pd.DataFrame(editions_data)
    
    # Save to CSV        
    csv_path = "output/info/info_editions.csv"
    to_csv(editions_df, csv_path)
    