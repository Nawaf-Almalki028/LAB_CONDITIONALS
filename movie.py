# - Create a variable for the movie (choose any movie you like)
# - Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
# - Create a popularity score of type float , let it be 72.65
# - Using an if statement 
# - - Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
# - - else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
# - - else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
# -  - else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"

movie:str = "Blacklist"
rating:int = 1
popularity:float = 60


#there is empty space between 50 and 60 so thats why I added this comment!

if rating >= 4 and popularity > 80:
    print("Highly Recommended")
    
elif rating >= 3 and popularity > 70:
    print("I recommended it, it is good")

elif rating <= 2 and popularity > 60:
    print("You should check it out!")

else:
    if rating <= 2 and popularity < 50:
        print("Don't watch it. It is a waste of time")
    else:
        print("Wrong Input not possible!")