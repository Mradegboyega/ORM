from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship
from typing import List

# Create a base class for declarative models
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = "users"
    
    # User ID, primary key
    id = Column(Integer, primary_key=True)
    
    # User's username, cannot be null
    username = Column(String(30), nullable=False)
    
    # User's email
    email = Column(String)
    
    # Relationship with Comment, back_populates connects the User and Comment models
    comments = relationship("Comment", back_populates='user')

    # String representation of the User instance
    def __repr__(self) -> str:
        return f"<User username={self.username}>"

# Define the Comment class
class Comment(Base):
    __tablename__ = "comments"
    
    # Comment ID, primary key
    id = Column(Integer, primary_key=True)
    
    # Foreign key referencing the User ID, cannot be null
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Comment text, cannot be null
    text = Column(Text, nullable=False)
    
    # Relationship with User, back_populates connects the Comment and User models
    user = relationship("User", back_populates='comments')

    # String representation of the Comment instance
    def __repr__(self) -> str:
        return f"<Comment text={self.text} by {self.user.username}>"
