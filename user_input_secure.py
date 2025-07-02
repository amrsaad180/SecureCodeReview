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
