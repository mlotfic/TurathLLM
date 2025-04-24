import os
import pickle

def save_item_to_list_pkl(xref_id, base_folder = "db", pickle_file = 'xref_ids'):    
    # Generate file path
    file_path = os.path.join("extracted_data", base_folder, f"{pickle_file}.pkl")  # Corrected f-string

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Load data from a pickle file
    try:
        with open(file_path, 'rb') as f:
            xref_ids = pickle.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        xref_ids = []

    # Check if xref_id exists in xref_ids
    if xref_id not in xref_ids:
        # Item not found; append the new item
        xref_ids.append(xref_id)
        # Save data to a pickle file
        with open(file_path, 'wb') as f:
            pickle.dump(xref_ids, f)
        print(f"Added xref_id '{xref_id}' to {file_path}.")
    else:
        print(f"xref_id '{xref_id}' already exists in {file_path}.")

    return xref_ids