class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        username = email.split('@')[0]
        mail, domain = email.split('@')[1].split('.')
        if self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False


