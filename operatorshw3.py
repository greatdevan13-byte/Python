is_loggedin=True
is_subscribed=False
user_credits = 100
max_credits = 200
min_credits = 50
credits_valid=(user_credits>=min_credits) and (user_credits<=max_credits)

bonus_credits=is_subscribed or user_credits>min_credits

user_credits+=50
user_credits-=20
user_credits*=2
user_credits%=150

power_results=user_credits*user_credits

full_access=is_loggedin and is_subscribed

is_true_login = is_loggedin is True

access_result=is_loggedin or is_subscribed and False

print("Log in ststus :",is_loggedin)
print("Subscription :",is_subscribed)
print("Credits validiy :",credits_valid)
print("Bonus eligibility :",bonus_credits)
print("Credit score of user :",user_credits)
print("Power of user credits :",power_results)
print("Complete accessibility ? :", full_access)
print("Is it true login :",is_true_login)
print("Acess result :",access_result)



