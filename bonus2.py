Name = input("What is your name: ")
Email = input("What is your mail: ")

x = len(Name)

if x > 2 and Email.endswith("@gmail.com"):
    print(f"welcome {Name}, you registered with the email {Email} !")
else:
    print("the email is not valid , please provide a valid email .")
