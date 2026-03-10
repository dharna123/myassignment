from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL="sqlite:///todos.db"

Base=declarative_base()
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,bind=engine)

class Tasks(Base):
    __tablename__="todo_tasks"

    id=Column(Integer,primary_key=True,index=True)
    content=Column(String(200),nullable=False)
    completed=Column(Boolean,default=False)
    

Base.metadata.create_all(bind=engine)
