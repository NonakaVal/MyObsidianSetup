---
created: "[[2025-05-02]]"
tags:
  - snippet
HUB:
  - "[[hub-python]]"
  - "[[hub-jupyterNotebook]]"
connections:
  - "[[index-pandas-methods|index-pandas-methods]]"
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}
listar todos os arquivos em um diretório

# {código}

```python
import os

def list_files(directory_path):
    """
    List all files in the specified directory.
    
    Args:
        directory_path (str): Path of the directory to scan
        
    Returns:
        list: List of file names in the directory
    """
    try:
        # Get all entries in the directory
        entries = os.listdir(directory_path)
        
        # Filter out directories, keep only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
        
        return files
    except FileNotFoundError:
        print(f"Error: Directory not found - {directory_path}")
        return []
    except PermissionError:
        print(f"Error: Permission denied for directory - {directory_path}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    path = input("Enter directory path: ")
    files = list_files(path)
    
    if files:
        print("\nFiles in directory:")
        for file in files:
            print(file)
    else:
        print("No files found or directory is empty.")
##v
```