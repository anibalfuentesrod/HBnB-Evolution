import uuid

class User:
    _existing_emails = set()

    def __init__(self, email, password):
        if email in User._existing_emails:
            raise ValueError("Email already exists")
        User._existing_emails.add(email)
        self.email = email
        self.password = password
        self.id = str(uuid.uuid4())

    @classmethod
    def clear_existing_emails(cls):
        cls._existing_emails.clear()
