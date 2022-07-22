import database_handler


def input_user():
    print("Welcome To This Buga App! Register by providing the following info")
    name = input("Enter your name: ")
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    profile = []

    user = dict(name=name, user_name=user_name, password=password, profile=profile)
    old_db: list = database_handler.read_data_base()
    old_db.append(user)

    database_handler.write_to_data_base(old_db)


def login():
    print("Kindly enter the following details to login")
    name = input("Enter your name: ")
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    db = database_handler.read_data_base()

    for user in db:
        if user["name"] == name and user["user_name"] == user_name and user["password"] == password:
            print("Logged in")


def update_profile():
    print("To update your profile....")
    user_name = input("Enter your username: ")
    age = int(input("Enter your age in numbers: "))
    gender = input("Enter your gender: ")
    education = input("Enter your highest level of education: ")
    isVerified = input("Are you a verified twitter user? Enter either True/False: ")
    tweets = []
    followers = int(input("Enter your number of followers: "))
    following = int(input("Enter the number of those you're following: "))

    profile_ = dict(age=age, gender=gender, education=education, isVerified=isVerified, tweets=tweets,
                    followers=followers, following=following)
    db = database_handler.profile_update(user_name, profile_)


def tweets():
    print("Tweeetiee time...!")
    user_name = input("Enter your username: ")
    tweet = input("Write the content of your tweet: ")
    likes = int(input("Enter the number of likes for this tweet: "))

    tweet_ = dict(tweet=tweet, likes=likes)
    db_ = database_handler.write_tweet(user_name, tweet_)
