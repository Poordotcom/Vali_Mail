import re
import requests
import whois
import socket
from disposable_email_domains import blocklist
# from publicsuffix2 import fetch
from bs4 import BeautifulSoup


########################################################################################
# Email Exprestion Validation
########################################################################################

def vali_mail(email):
    # تعبير مناسب للتحقق من تنسيق البريد الإلكتروني
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return "Valid"
    else:
        return "NotValid"


########################################################################################
# Chech Domain Name is Availble or Not
########################################################################################

def check_domain_name(domain):
    try:
        domain_info = whois.whois(domain)
        if domain_info.status == None:
            return "Available"
        else:
            return "Not Available"
    except whois.parser.PywhoisError:
        return "Invalid Domain"
    

########################################################################################
# Cheking IF The Email Domain Name  Is Known
########################################################################################

def read_domains_from_file(file_path):
    domains = []
    with open(file_path, 'r') as file:
        for line in file:
            domain = line.strip()  # يزيل الأمور الزائدة مثل الفواصل والمسافات الزائدة
            if domain:
                domains.append(domain)
    return domains

KNOWN_SERVICES = read_domains_from_file('src/data/file.txt')

def check_if_known(email):
    domain = email.split('@')[1]
    if domain in KNOWN_SERVICES:
        return "Valid Email in Known Service"
    else: 
        return "Invalid Email or Not in Known Service"


########################################################################################
# Check if Email is Fake
########################################################################################

def is_dispose_email(email):
    domain = email.split('@')[-1]
    return domain in blocklist
