# ValiMail - Email Verification Library

ValiMail is a library designed for advanced and effective verification of email addresses.

## Features

- Verify the format and validity of email addresses.
- Detect if an email address exists in a leaked database.
- Support email domain verification.
- Support email comparison against a blacklist.
- Integration with popular email service providers.

## Installation

You can install the library using the following command:

```python
pip install valimail
```

## How To Use

# Import the library
```python
from valimail import vali_mail, check_domain_name, check_if_known,is_dispose_email
```

# Use library functions to check email addresses

```python
email = "example@email.com"
is_valid = vali_mail(email)
is_in_database = check_if_known(email)
is_valid_domain = check_domain_name(email)
is_dispose = is_dispose_email(email)
```
```python
# Print the results
print(f"Is valid email: {is_valid}")
print(f"Is in database: {is_in_database}")
print(f"Has valid domain: {is_valid_domain}")
print(f"Is blacklisted: {is_dispose}")
```

#Ihad Been Added The RealTime Examples in The File example.py


## Documentation

For detailed documentation and examples, please refer to the [official documentation](#).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
