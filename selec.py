from models import User, Comment
from main import session
from sqlalchemy import select


statement = select(User).where(User.username.in_(["toyinmary", "michelle"]))

# for user in session.scalars(statement):
#     print(user)

result = session.scalars(statement)

for user in result:
    print(user)

# users = session.query(User).all()

# for user in users:
#     print(users)