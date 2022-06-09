class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


email = input()
while email != "End":
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    parts = email.split('@')
    if len(parts[0]) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    parts_2 = parts[1].split('.')
    domain = f".{parts_2[1]}"
    domains = ['.com', '.bg', '.org', '.net']
    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email = input()
'''
peter@gmail.com
petergmail.com

'''
