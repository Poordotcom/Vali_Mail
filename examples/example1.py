from MailModule import *

########################################################################################
# Email Exprestion Validation =======>>>  vali_mail(email)
########################################################################################

####### Example 1 ###### 
email_to_check = "user@example.com"

validation_result = vali_mail(email_to_check)

print(f"The email format is: {validation_result}") # Valid

####### Example 2 ###### 

email1 = "user@example.com"
email2 = "invalid_email"
email3 = "user@example.com"
email4 = "user@example.co.uk"

print(vali_mail(email1))  # Valid
print(vali_mail(email2))  # NotValid
print(vali_mail(email3))  # Valid
print(vali_mail(email4))  # Valid

########################################################################################
# Chech Domain Name is Availble or Not =======>>>  check_domain_name(domain)
########################################################################################

domain1 = "example.com"
domain2 = "google.com"
domain3 = "invalid123456.com"

print(check_domain_name(domain1))  # Not Available
print(check_domain_name(domain2))  # Not Available
print(check_domain_name(domain3))  # Invalid Domain

########################################################################################
# Cheking IF The Email Domain Name  Is Known =======>>>  check_if_known(email)
########################################################################################

email_to_check = "ahmad4tiktok@hi2.in"

result = check_if_known(email_to_check)

print(result) #Invalid Email or Not in Known Service


########################################################################################
# Check if Email is Fake =======>>>  is_dispose_email(email)
########################################################################################

email1 = "user@example.com"
email2 = "user@mailinator.com"
email3 = "user@temp-mail.org"

print(is_dispose_email(email1))  # False
print(is_dispose_email(email2))  # True
print(is_dispose_email(email3))  # True