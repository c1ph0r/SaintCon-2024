def check_password(input_password):
    encoded_password = [67, 84, 70, 49, 50, 51]
    actual_password = ''.join([chr(c) for c in encoded_password])
    
    return input_password == actual_password

def print_flag():
    encoded_flag = [83, 65, 73, 78, 84, 45, 67, 79, 78, 45, 56, 48, 48, 56]
    flag = ''.join([chr(c) for c in encoded_flag])
    print(f"Correct! Here's your flag: {flag}")

def main():
    password = input("Enter the password: ")

    if check_password(password):
        print_flag()
    else:
        print("Incorrect password!")

if __name__ == "__main__":
    main()