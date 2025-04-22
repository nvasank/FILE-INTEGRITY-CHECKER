import hashlib
import os
import json
import argparse
from datetime import datetime
import sys # Import sys to exit if directory not found

HASH_FILE = "file_hashes.json"

def calculate_file_hash(file_path, algo='sha256'):
    """Calculate hash of a file using specified algorithm."""
    h = hashlib.new(algo)
    try:
        with open(file_path, 'rb') as f:
            # Use a buffer for large files
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        # This case is less likely to be hit if scan_directory is used correctly,
        # but good to keep for robustness.
        print(f"[!] File not found during hashing: {file_path}")
        return None
    except IOError as e:
        print(f"[!] Error reading file {file_path}: {e}")
        return None


def load_hashes():
    """Load stored hashes from JSON file."""
    if os.path.exists(HASH_FILE):
        try:
            with open(HASH_FILE, 'r') as f:
                # Handle empty file or invalid JSON
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print(f"[!] Warning: Could not decode JSON from {HASH_FILE}. Starting with empty hashes.")
                    return {}
        except IOError as e:
            print(f"[!] Error reading hash file {HASH_FILE}: {e}. Starting with empty hashes.")
            return {}
    return {} # Return empty dict if file doesn't exist


def save_hashes(hashes):
    """Save hash values to a JSON file."""
    try:
        with open(HASH_FILE, 'w') as f:
            json.dump(hashes, f, indent=4)
    except IOError as e:
        print(f"[!] Error writing hash file {HASH_FILE}: {e}")


def scan_directory(directory):
    """Scan directory and return hash dictionary."""
    file_hashes = {}
    # os.walk handles non-existent directories gracefully by yielding nothing,
    # but we added a check in main for a clearer error message.
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Ensure we have a valid file path before trying to hash
            if os.path.isfile(filepath):
                file_hash = calculate_file_hash(filepath)
                if file_hash: # Only add if hashing was successful
                    file_hashes[filepath] = file_hash
    return file_hashes


def compare_hashes(current, stored):
    """Compare current and stored hash values."""
    modified, new, missing = [], [], []

    # Check for modified and new files in the current scan
    for filepath, current_hash in current.items():
        if filepath not in stored:
            new.append(filepath)
        elif stored[filepath] != current_hash:
            modified.append(filepath)

    # Check for missing files from the stored hashes
    for filepath in stored:
        if filepath not in current:
            missing.append(filepath)

    return modified, new, missing


def display_results(modified, new, missing):
    """Print integrity check results."""
    if modified:
        print("Modified files:") # Fixed newline
        for f in modified:
            print(f" - {f}")

    if new:
        print("New files detected:") # Fixed newline
        for f in new:
            print(f" - {f}")

    if missing:
        print("Missing files:") # Fixed newline
        for f in missing:
            print(f" - {f}")

    if not modified and not new and not missing:
        print(" All files are intact.") # Fixed newline


def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker using hashlib.")
    parser.add_argument("-d", "--dir", required=True, help="Directory to scan")
    parser.add_argument("--update", action="store_true", help="Update stored hashes after scan")

    args = parser.parse_args()
    directory = args.dir

    # Check if the provided directory exists
    if not os.path.isdir(directory):
        print(f"[!] Error: Directory not found or is not a directory: {directory}")
        sys.exit(1) # Exit the script

    print(f"Scanning directory: {directory} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") # Fixed newline
    
    stored_hashes = load_hashes()
    current_hashes = scan_directory(directory)
    
    modified, new, missing = compare_hashes(current_hashes, stored_hashes)
    display_results(modified, new, missing)

    if args.update:
        save_hashes(current_hashes)
        print("Hashes updated in file_hashes.json") # Fixed newline

if __name__ == "__main__":
    main()

#codebyvasan