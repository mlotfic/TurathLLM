import json
from datetime import datetime, date
from decimal import Decimal
import numpy as np
from bson import ObjectId
from pathlib import Path
import uuid

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON Encoder that handles additional Python data types."""
    def default(self, obj):
        # Handle datetime objects
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        
        # Handle Decimal
        if isinstance(obj, Decimal):
            return str(obj)
            
        # Handle NumPy arrays and data types
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        
        # Handle MongoDB ObjectId
        if isinstance(obj, ObjectId):
            return str(obj)
            
        # Handle UUID
        if isinstance(obj, uuid.UUID):
            return str(obj)
            
        # Handle sets
        if isinstance(obj, set):
            return list(obj)
            
        # Handle Paths
        if isinstance(obj, Path):
            return str(obj)
            
        # Handle bytes
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
            
        # Let the base class default method handle other types
        return super().default(obj)

def json_to_dict(json_data, encoding='utf-8'):
    """
    Convert JSON to dictionary with support for various data types and encodings.
    
    Args:
        json_data: Can be a JSON string, bytes, or file path
        encoding (str): Character encoding to use (default: 'utf-8')
    
    Returns:
        dict: Python dictionary containing the parsed data
    """
    try:
        # If json_data is a file path
        if isinstance(json_data, (str, Path)) and Path(json_data).is_file():
            with open(json_data, 'r', encoding=encoding) as f:
                return json.load(f)
        
        # If json_data is bytes
        if isinstance(json_data, bytes):
            return json.loads(json_data.decode(encoding))
        
        # If json_data is a string
        if isinstance(json_data, str):
            return json.loads(json_data)
        
        # If json_data is already a dict
        if isinstance(json_data, dict):
            return json_data
            
        raise ValueError("Unsupported JSON data type")
        
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None
    except Exception as e:
        print(f"Error converting JSON to dict: {e}")
        return None

def dict_to_json(data, output_file=None, encoding='utf-8', **kwargs):
    """
    Convert dictionary to JSON with support for various data types and encodings.
    
    Args:
        data (dict): Python dictionary to convert
        output_file (str, optional): Path to save JSON file
        encoding (str): Character encoding to use (default: 'utf-8')
        **kwargs: Additional arguments for json.dumps()
    
    Returns:
        str: JSON string if output_file is None
        bool: True if successfully written to file, False otherwise
    """
    try:
        # Default JSON configuration
        json_config = {
            'ensure_ascii': False,  # Properly handle non-ASCII characters
            'indent': 4,           # Pretty printing
            'cls': CustomJSONEncoder,  # Use custom encoder
            'sort_keys': False     # Preserve dictionary order
        }
        
        # Update with any user-provided configurations
        json_config.update(kwargs)
        
        # Convert to JSON string
        json_str = json.dumps(data, **json_config)
        
        # If output_file is specified, write to file
        if output_file:
            try:
                # Create directory if it doesn't exist
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Write JSON to file
                with open(output_file, 'w', encoding=encoding) as f:
                    f.write(json_str)
                return True
            except Exception as e:
                print(f"Error writing to file: {e}")
                return False
        
        # Return JSON string if no output file specified
        return json_str
        
    except Exception as e:
        print(f"Error converting dict to JSON: {e}")
        return None

# Example usage and testing function
def test_json_conversion():
    """Test the JSON conversion functions with various data types and languages."""
    
    # Test data with various types and languages
    test_data = {
        'string': 'Hello, World!',
        'arabic': 'مرحبا بالعالم',
        'chinese': '你好，世界',
        'number': 42,
        'float': 3.14159,
        'boolean': True,
        'null': None,
        'datetime': datetime.now(),
        'date': date.today(),
        'decimal': Decimal('3.14159'),
        'array': [1, 2, 3],
        'nested': {
            'a': 1,
            'b': 2
        },
        'set': {1, 2, 3},
        'numpy_array': np.array([1, 2, 3]),
        'object_id': ObjectId(),
        'uuid': uuid.uuid4(),
        'path': Path('/path/to/file'),
        'bytes': b'Hello, World!'
    }
    
    # Test dict to JSON conversion
    print("\nTesting dict to JSON conversion...")
    json_str = dict_to_json(test_data)
    print(f"JSON string created successfully: {bool(json_str)}")
    
    # Test JSON to dict conversion
    print("\nTesting JSON to dict conversion...")
    converted_dict = json_to_dict(json_str)
    print(f"Dictionary created successfully: {bool(converted_dict)}")
    
    # Test file operations
    print("\nTesting file operations...")
    
    # Save to file
    success = dict_to_json(test_data, 'test_output.json')
    print(f"File written successfully: {success}")
    
    # Read from file
    loaded_dict = json_to_dict('test_output.json')
    print(f"File read successfully: {bool(loaded_dict)}")
    
    return json_str, converted_dict, loaded_dict

if __name__ == "__main__":
    # Run the test
    json_str, converted_dict, loaded_dict = test_json_conversion()