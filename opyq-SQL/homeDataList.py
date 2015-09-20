from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class homeDataList(Base):

    __tablename__ = 'homeDataList'
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

new_homeDataList = homeDataList(msgId = '1',userId='1', user='anklee',text='test for mysql',answer='1',time='20150920')

session.add(new_homeDataList)

session.commit()
session.close()
session = DBSession()
homeDataList = session.query(homeDataList).filter(homeDataList.msgId=='1').one()
print('type:', type(homeDataList))
print('homeDataList:', homeDataList.text)

session.close()
