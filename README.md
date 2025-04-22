# FILE-INTEGRITY-CHECKER
*COMPANY*: CODTECH IT SOLUTIONS 

*NAME*: N KEERTHI VASAN

*INTERN ID*: CT6MTLUD

*DOMAIN*: FRONT END DEVELOPMENT

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH


---

###  **File Integrity Checker Tool – Description**

The **File Integrity Checker Tool** is a Python-based application designed to monitor and verify the integrity of files within a given directory using cryptographic hashing techniques. This tool is especially useful in environments where maintaining the authenticity and reliability of files is critical—such as in cybersecurity, digital forensics, system administration, and software deployment pipelines.

At its core, the File Integrity Checker employs the `hashlib` library, a standard Python module used to compute secure hash functions such as SHA-256. Hash functions are cryptographic algorithms that transform input data into fixed-length hash values. Any modification—even a single character—in the original file changes its hash, making hashing an ideal method for detecting unauthorized or unintended changes.

---

###  **How It Works**

When the tool is run for the first time, it scans all files recursively in the specified directory and calculates their SHA-256 hash values. These values are then stored in a local JSON file (`file_hashes.json`). This JSON file acts as a reference snapshot of the file states at that moment.

Upon subsequent executions, the tool again scans the files in the same directory and recalculates their current hash values. It then compares these against the previously stored values to determine three key statuses:

1. **Modified Files** – Files that exist in both the current and stored snapshot but have different hash values, indicating they have been altered.
2. **New Files** – Files that are found in the current directory but do not exist in the stored snapshot, indicating they were added after the initial scan.
3. **Missing Files** – Files that were in the original snapshot but are no longer found, indicating they have been deleted or moved.

These results are then displayed clearly in the terminal, allowing users to take necessary actions depending on the findings. For example, a system administrator may investigate modified files for signs of tampering, or a developer may double-check newly added files in a software deployment process.

---

###  **Why This Tool Matters**

In today’s digital landscape, data integrity is more important than ever. Files can be modified, deleted, or corrupted due to malicious activities (e.g., malware, unauthorized access), system errors, or even human mistakes. This tool helps mitigate those risks by providing a lightweight, fast, and effective method to monitor and validate file changes.

Unlike complex enterprise-level tools that may require extensive configurations and resources, this Python script offers a simple command-line interface, easy deployment, and a portable design that works across operating systems. It's ideal for internships, small businesses, personal projects, and educational purposes.

---

###  **Key Features**

- **Cryptographic Hashing**: Uses SHA-256 by default for robust integrity checking.
- **Recursive Directory Scan**: Automatically includes files from all subdirectories.
- **JSON-based Storage**: Stores hash records in a readable and easy-to-update format.
- **CLI Options**: Supports arguments like `--dir` for selecting directories and `--update` to refresh stored hashes.
- **Platform Independent**: Works on Windows, Linux, and macOS systems.
- **Modular and Extensible**: Easy to add support for other hash algorithms or file types.

---

###  **Use Cases**

- **Security Audits**: Detects unauthorized file changes in sensitive directories.
- **Software Development**: Ensures build artifacts or deployment files haven't been tampered with.
- **Backup Validation**: Verifies that backup files remain unchanged over time.
- **Compliance Monitoring**: Assists in adhering to regulations requiring data integrity verification.

---

In conclusion, the File Integrity Checker Tool is a powerful, beginner-friendly, and efficient solution for maintaining the trustworthiness of your file systems. Built entirely in Python and utilizing standard libraries, it serves as both a practical utility and an excellent learning project for those interested in cybersecurity, automation, or system scripting.

Let me know if you want a PDF version or want this included in a formatted `README.md` file!
