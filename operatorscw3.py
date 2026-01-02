has_account=True
email_verified=False
can_login=(has_account and email_verified)
email="sas@gmail.com"
is_email_valid="@" in email
user_age=17
age_valid=(user_age>=18)
can_login_final=(has_account and email_verified and is_email_valid and age_valid)

print("Can login ?:",can_login)
print("Email validity :",is_email_valid)
print("Age validity :",age_valid)
print("Complete login status :",can_login_final)
print("The account is true :",has_account is True)