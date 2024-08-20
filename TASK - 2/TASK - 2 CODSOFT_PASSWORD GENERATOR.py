import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)
    for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    password = password_generator(length)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main() 
