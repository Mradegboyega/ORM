from main import session
from models import Comment

# Assuming there is a comment with id=1 in the database
comment = session.query(Comment).filter_by(id=1).first()

if comment:
    comment.text = "I don change ooo"
    session.commit()
    print("Comment updated successfully.")
else:
    print("Comment with id=1 not found.")
