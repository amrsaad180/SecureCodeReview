# Secure Coding Review Report

**Project:** User Input Storage Script (Python)  
**Reviewer:** Amr Saad  
**Date:** 2025-07-02  

## 1. Introduction  
This report reviews a Python script that stores user input in a text file, focusing on identifying security vulnerabilities and improving the code security.

## 2. Code Description  
The script prompts the user to enter text, then appends this text to a file named `user_data.txt`.

## 3. Discovered Vulnerabilities

| Security Issue               | Description                                      |
|-----------------------------|------------------------------------------------|
| Lack of Input Validation     | The code allows any input without validation, which could cause issues. |
| No Error Handling            | There is no error handling when opening or writing to the file. |
| Unprotected Data Storage     | Data is stored as plain text without encryption. |

## 4. Recommendations and Solutions  

- **Input Validation:**  
  Limit input length and restrict dangerous characters.

- **Exception Handling:**  
  Use try-except blocks to handle file read/write errors.

- **Data Encryption (if needed):**  
  Encrypt sensitive data before storing.

- **Secure Storage:**  
  Use databases with access controls.

- **Logging:**  
  Implement logging to monitor actions and errors.

## 5. Proposed Code Changes

```python
def save_user_input():
    user_input = input("Enter some text (max 100 chars): ")

    if len(user_input) > 100:
        print("Input too long!")
        return

    if any(c in user_input for c in [';', '&', '|', '$']):
        print("Invalid characters in input!")
        return

    try:
        with open("user_data.txt", "a") as f:
            f.write(user_input + "\n")
        print("Data saved!")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    save_user_input()
