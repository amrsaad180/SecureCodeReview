# Secure Coding Review Report

**Project:** User Input Storage Script (Python)  
**Reviewer:** Amr Saad  
**Date:** 2025-07-02  

## 1. Introduction  
This report reviews a Python script that stores user input in a text file, focusing on security improvements.

## 2. Code Description  
The script prompts the user to enter text, validates the input, and appends it to a file named `user_data.txt`.

## 3. Discovered Vulnerabilities

| Security Issue               | Description                                   |
|-----------------------------|-----------------------------------------------|
| Lack of Input Validation     | The code previously allowed any input without validation, which may lead to injection attacks. |
| No Error Handling            | There was no error handling during file operations, risking data loss or crashes. |
| Unprotected Data Storage     | Data was stored in plain text without encryption. |

## 4. Improvements Made

- Added input length validation (max 100 characters).  
- Blocked dangerous characters like `;`, `&`, `|`, and `$`.  
- Implemented try-except for file writing errors.  

## 5. Recommendations

- Encrypt sensitive data before storage.  
- Use secure storage mechanisms in production environments.

## 6. Conclusion

The code was reviewed and improved by adding input validation and error handling. Further recommendations were provided to secure the data as needed.

# Task 3 - Secure Coding Review

This repository contains the solution for Task 3 in the CodeAlpha Cybersecurity internship.

The task involves reviewing a Python script for security issues, improving it with input validation and error handling, and documenting the findings.
