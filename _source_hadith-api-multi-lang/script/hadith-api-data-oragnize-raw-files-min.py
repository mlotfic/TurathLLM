# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:52:23 2025

@author: m
"""

import os
import shutil

def move_min_json_files(source_dir, destination_base):
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        # Filter files ending with .min.json
        min_json_files = [f for f in files if f.endswith('.min.json')]
        
        for file in min_json_files:
            # Get the relative path from source directory
            relative_path = os.path.relpath(root, source_dir)
            
            # Create the new destination path
            new_dir = os.path.join(destination_base, relative_path)
            
            # Create destination directory if it doesn't exist
            os.makedirs(new_dir, exist_ok=True)
            
            # Source and destination file paths
            source_file = os.path.join(root, file)
            dest_file = os.path.join(new_dir, file)
            
            # Move the file
            shutil.move(source_file, dest_file)
            print(f"Moved: {source_file} -> {dest_file}")

def remove_empty_folders(directory):
    # Walk bottom-up through the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                # Check if directory is empty
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Removed empty folder: {dir_path}")
            except OSError as e:
                print(f"Error removing directory {dir_path}: {e}")
                
# Example usage
source_directory = "data"
destination_directory = "data_new"

move_min_json_files(source_directory, destination_directory)

# Remove empty folders from both source and destination
print("\nRemoving empty folders from source directory...")
remove_empty_folders(source_directory)

print("\nRemoving empty folders from destination directory...")
remove_empty_folders(destination_directory)


print("\nRemoving empty folders from destination directory...")
remove_empty_folders("hadith-api-data")


