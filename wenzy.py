def odd_or_even(n):
    return ["even", "odd"][n % 2]

def vowel_or_consonant(c):
    return "vowel" if c.lower() in "aeiou" else "consonant"

def is_special_character(c):
    return "a special character" if not c.isalnum() else "not a special character"

def analyze_string(text):
    for ch in text:
        if ch.isdigit():
            print(f"{ch} is an {odd_or_even(int(ch))} number.")
        elif ch.isalpha():
            print(f"{ch} is a {vowel_or_consonant(ch)} letter.")
        else:
            print(f"{ch} is {is_special_character(ch)}.")

def main():
    while True:
        print("\nOptions:\n1. Odd or Even\n2. Vowel or Consonant\n3. Special Character\n4. Full String Analysis\n(Type 'STOP' to exit)")
        
        selection = input("Choose an option: ").strip().lower()

        if selection == "stop":
            print("Goodbye!")
            break
        
        if selection == "1":
            num = input("Enter a number: ").strip()
            print(f"{num} is an {odd_or_even(int(num))} number.") if num.isdigit() else print("Invalid input.")

        elif selection == "2":
            char = input("Enter a letter: ").strip()
            print(f"{char} is a {vowel_or_consonant(char)} letter.") if char.isalpha() and len(char) == 1 else print("Invalid input.")

        elif selection == "3":
            char = input("Enter a character: ").strip()
            print(f"{char} is {is_special_character(char)}.") if len(char) == 1 else print("Invalid input.")

        elif selection == "4":
            analyze_string(input("Enter a string: ").strip())

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
