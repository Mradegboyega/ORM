from main import session
from models import User, Comment

# Assuming there is a comment with id=1 in the database
comment = session.query(Comment).filter_by(id=1).first()

if comment:
    session.delete(comment)
    session.commit()
    print("Comment deleted successfully.")
else:
    print("Comment with id=1 not found.")
