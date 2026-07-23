from utils import generate_password

def main():

    print("=" * 40)
    print("🔑 Password Generator")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 8:
                print("Password should be at least 8 characters.\n")
                continue

            break

        except ValueError:
            print("Please enter a valid number.\n")

    password = generate_password(length)

    print("\nGenerated Password:\n")
    print(password)

if __name__ == "__main__":
    main()
