# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:21:16 2025

@author: m
"""

import os
import shutil

def move_section_contents_to_parent(base_directory):
    # Walk through the directory tree
    for root, dirs, files in os.walk(base_directory, topdown=False):
        # Check if current directory name is "sections"
        if os.path.basename(root).lower() == "sections":
            parent_dir = os.path.dirname(root)
            print(f"\nProcessing section folder: {root}")
            
            # Move all files to parent directory
            for file in files:
                source_path = os.path.join(root, file)
                dest_path = os.path.join(parent_dir, file)
                
                # Handle file name conflicts
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_name = f"{base}_{counter}{ext}"
                        dest_path = os.path.join(parent_dir, new_name)
                        counter += 1
                
                shutil.move(source_path, dest_path)
                print(f"Moved file: {source_path} -> {dest_path}")
            
            # Move all subdirectories to parent directory
            for dir_name in dirs:
                source_path = os.path.join(root, dir_name)
                dest_path = os.path.join(parent_dir, dir_name)
                
                # Handle directory name conflicts
                if os.path.exists(dest_path):
                    counter = 1
                    while os.path.exists(dest_path):
                        new_name = f"{dir_name}_{counter}"
                        dest_path = os.path.join(parent_dir, new_name)
                        counter += 1
                
                shutil.move(source_path, dest_path)
                print(f"Moved directory: {source_path} -> {dest_path}")
            
            # Remove the empty section folder
            try:
                os.rmdir(root)
                print(f"Removed empty section folder: {root}")
            except OSError as e:
                print(f"Error removing directory {root}: {e}")

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
base_directory = "hadith-api-data\json"

# Move contents of section folders to their parents
print("Moving contents of section folders to parent directories...")
move_section_contents_to_parent(base_directory)

# Clean up any remaining empty folders
print("\nRemoving any remaining empty folders...")
remove_empty_folders(base_directory)