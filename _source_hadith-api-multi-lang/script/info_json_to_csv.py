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
    
    hadith_data = []
    sections_data = []
    section_details_data = []
    for book, book_data in data_normalized.items():
        
        metadata      = book_data.get("metadata", {})
        
        book_fullname       = metadata.get("name", "")
        last_hadithnumber   = metadata.get("last_hadithnumber", "")
        
        sections        = metadata.get("sections", {})
        section_details = metadata.get("section_details", {})
        
        
        for idx, section in sections.items():
            sections_data.append({
                "book_shortname"    : book,
                "book"              : book_fullname,
                "last_hadithnumber" : last_hadithnumber,
                "idx"               : idx,
                "section"           : section,
                                
                })
            
        
        for idx, section_detail in section_details.items():
            section_details_data.append({
                "book_shortname"        : book,
                "book"                  : book_fullname,
                "last_hadithnumber"     : last_hadithnumber,
                "idx"                   : idx,
                "hadithnumber_first"    : section_detail.get("hadithnumber_first", ""),
                "hadithnumber_last"     : section_detail.get("hadithnumber_last", ""),
                "arabicnumber_first"    : section_detail.get("arabicnumber_first", ""),
                "arabicnumber_last"     : section_detail.get("arabicnumber_last", ""),                
                })            
        
        
        hadiths  = book_data.get("hadiths", [])
        
        
        for hadith in hadiths:
            hadithnumber =  hadith.get("hadithnumber", "")
            arabicnumber =  hadith.get("arabicnumber", "")
            grades       =  hadith.get("grades", "")
            reference    =  hadith.get("reference", {})
            for grade in grades:                 
                hadith_data.append({
                    "book_shortname"    : book,
                    "book"              : book_fullname,
                    "last_hadithnumber" : last_hadithnumber,
    				"hadithnumber"      : hadithnumber,
    				"arabicnumber"      : arabicnumber,
    				"ruler"             : grade.get("name", ""),
    				"grade"             : grade.get("grade", ""),
    				"reference_book"    : reference.get("book", ""),
                    "reference_hadith"  : reference.get("hadith", "")
    			})
      
    return sections_data, section_details_data, hadith_data

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
    
    file_path = "info.json"
    
    # Read the JSON file    
    data = read_json_file(file_path)
    len(data)
    
    sections_data, section_details_data, hadith_data = get_source_relational_db(data, language = "", Diacritics = "")

    # Create DataFrames   
    sections_df         = pd.DataFrame(sections_data)
    section_details_df  = pd.DataFrame(section_details_data)
    hadith_df           = pd.DataFrame(hadith_data)
    
    # Save to CSV        
    csv_path = "output/info/info_sections.csv"
    to_csv(sections_df, csv_path)
    
    # Save to CSV        
    csv_path = "output/info/info_section_details.csv"
    to_csv(section_details_df, csv_path)
    
    # Save to CSV        
    csv_path = "output/info/info_hadith.csv"
    to_csv(hadith_df, csv_path)