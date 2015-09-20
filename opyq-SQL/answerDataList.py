from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class answerDataList(Base):

    __tablename__ = 'answerDataList'
    msgId = Column(String(45), primary_key=True)
    userId = Column(String(45))
    user = Column(String(45))
    text = Column(String(45))
    answer = Column(String(45))
    likes = Column(String(45))
    time = Column(String(45))

engine = create_engine('mysql+mysqlconnector://anklee:870216qq@localhost/akappios02')

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_answerDataList = answerDataList(msgId = '1',userId='1', user='anklee',text='root:test for mysql,answer.',answer='1',time='20150920')

session.add(new_answerDataList)

session.commit()
session.close()
session = DBSession()
answerDataList = session.query(answerDataList).filter(answerDataList.msgId=='1').one()
print('type:', type(answerDataList))
print('answerDataList:', answerDataList.text)

session.close()
