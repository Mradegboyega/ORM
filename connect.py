from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///database.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result.all())