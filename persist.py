from models import User, Comment
from main import session

# Create User instances with associated Comment instances
toyinmary = User(
    username='toyinmary',
    email='toyinmary@domain.com',
    comments=[
        Comment(text="Hey love"),
        Comment(text="Come inside")
    ]
)

michelle = User(
    username='michelle',
    email='michelle@domain.com',
    comments=[
        Comment(text="Yo, dad"),
        Comment(text="Follow me")
    ]
)

gboyega = User(
    username='gboyega',
    email='gboyega@domain.com',
    comments=[
        Comment(text="Yo, wifey"),
        Comment(text="Come here")
    ]
)

# Add the User instances (along with associated Comment instances) to the session
session.add_all([toyinmary, michelle, gboyega])

# Commit the changes to persist them in the database
session.commit()
