# ---------------------Program Starts----------------------

print("Enter Ratings Between 1 to 10\n10 Is Best and 1 Is Worst")

# Taking Input from the user

rate = int(input("Enter your Ratings : "))

# Defining the ratings

bestRatings = 9 , 10
goodRatings = 7 , 8
okRatings = 5 , 6
worstRatings = 1 , 2 , 3 , 4

# Checking the input and Printing the result

if rate in bestRatings:
    print("Thanks For Your Valuable Ratings")
    print("....We are Glad That You Liked It....")

elif rate in goodRatings:
    print("Thanks For Your Valuable Ratings")
    print("....We Have To Make It A Little Better....")

elif rate in okRatings:
    print("Thanks For Your Valuable Ratings")
    print("....We Will Improve It....")

elif rate in worstRatings:
    print("Thanks For Your Valuable Ratings")
    print("....We Are Extremely Sorry That You Didn\'t Get What You Want....")
    feedBack = str(input("What Do You Wanted And You Didn\'t Get ? : "))
    print(f"OK ! We Will {feedBack}")
else:
    print("Invalid Ratings !!!")
