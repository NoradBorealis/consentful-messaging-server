print(tweet.text)

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)


	# so many questions
	statuses = api.user_timeline(screen_name = "im__jane",count=20, tweet_mode="extended")

print(statuses)

# task 1: When Twitter username and a threshold (interger; e.g., 50), return a boolean value of
# whether the number of followers of the Twitter user is higher than the threshold
def compare(username, threshold):
	numfollowers = 100; # find a function (call API to get numfolloers)
	if (numfollowers >= threshold):
		return True
	else:
		return False


		#example code to call functions
		# new test file: test_follower_number("username",threshold);
		#Jupiter notebook, debugger- executes all the code and shows what happens each line- IDE, programming Anaconda, !!!VS code!!! 

#task 2: When given two Twitter usernames (User of our system, Message send), return a boolean value of
# whether User follows Message sender
def check_following(user, messageSender):
	user = userOfSystem;
	messageSender = messageSender;
    print('Getting Follower list of ', messageSender)
    count = input("number of followers");
    followers = []
    followers_screenNames = []
    users = tweepy.Cursor(api.followers, screen_name='@'+screen_name, wait_on_rate_limit=True,count)
    for user in users.items():
        try:
            followers.append(user)
            followers_screenNames.append(user.screen_name)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    
    print('Fetched number of followers for '+screen_name+' : ',len(followers))
    return followers,followers_screenNames

    	if messageSender in followers:
    		return True
    	else:
    		return False

#task 3: When given two Twitter usernames (User of our system, Message sender), return a boolean value
# of whether the sender is followed by at least one account that User follows
def check_following(user, messageSender):
	def check_following(user, messageSender):
	user = userOfSystem;
	messageSender = messageSender;
    print('Getting Follower list of ', messageSender)
    count = input("number of followers");
    followers = []
    followers_screenNames = []
    users = tweepy.Cursor(api.followers, screen_name='@'+screen_name, wait_on_rate_limit=True,count)
    for user in users.items():
        try:
            followers.append(user)
            followers_screenNames.append(user.screen_name)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    
    print('Fetched number of followers for '+screen_name+' : ',len(followers))
    return followers,followers_screenNames

    	if messageSender in >= followers:
    		return True
    	else:
    		return False

#task 4: When given Twitter usernames (User of our system, Message sender), return a boolean value
# of whether User of our system has ever replied back to the Message sender (I'm pretty sure Twitter
# API supports this, but not so sure how (e.g. is there a function that returns a boolean value?). 
# Recommend first googling it up.) 
