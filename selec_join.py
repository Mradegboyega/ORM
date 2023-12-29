from main import session
from models import User, Comment
from sqlalchemy import select

stmt = select(Comment).join(Comment.user).where(
    User.username == 'toyinmary'
).where(
    Comment.text == 'Hey love'
)

result = session.execute(stmt).scalars().first()

print(result)

# results = session.execute(stmt).scalars()
# for result in results:
#     print(result)

