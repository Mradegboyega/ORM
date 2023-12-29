import pprint
from main import session
from models import User

gboyega = session.query(User).filter_by(username="gboyega").first()

# print(gboyega)

if gboyega:
    print(f"User found: {gboyega.username}, Email: {gboyega.email}")
else:
    print("User not found.")


