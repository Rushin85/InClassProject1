def main():
    print("This program generates computer usernames.\n")

    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    username = first[0] + last[:7]

    # output the username
    print("Your username is:", username)

main()