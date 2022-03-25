class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


emails = []

line = input()
while line != 'Stop':
    elements = line.split(" ")
    sender = elements[0]
    receiver = elements[1]
    content = elements[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

send_emails = [int(x) for x in input().split(', ')]
for x in send_emails:
    emails[x].send()
for email in emails:
    email.get_info()

