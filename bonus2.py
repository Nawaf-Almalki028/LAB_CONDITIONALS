Name = input("What is your name: ")
Email = input("What is your mail: ")

x = len(Name)

if x > 2 and Email.endswith("@gmail.com"):
    print(f"welcome {Name}, you registered with the email {Email} !")
else:
    if not Email.endswith("@gmail.com") and x <= 2:

        print("the email is not valid , please provide a valid email .")
        print("the name length must be more than 2 characters, please provide a valid name.")

    elif not Email.endswith("@gmail.com"):
        print("the email is not valid , please provide a valid email .")
    elif x <= 2:
        print("the name length must be more than 2 characters, please provide a valid name.")

