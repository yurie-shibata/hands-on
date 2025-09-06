from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL)

metadata = MetaData()

users_table = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)


def create_tables():
    metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
    print("Database and tables created.")
