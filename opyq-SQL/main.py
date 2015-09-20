from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask
from flask import request


Base = declarative_base()
class User(Base):
    __tablename__ = 'userList'
    userId = Column(String(45), primary_key=True)
    user = Column(String(45))
    userGroup = Column(String(45))
    userPWD = Column(String(45))
    time = Column(String(45))




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    engine = create_engine('mysql+mysqlconnector://anklee:870216qq@localhost/akappios02')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    new_user = User(userId='9', user='root',userGroup='root',userPWD='1234',time='20150920')
    session.add(new_user)
    session.commit()
    session.close()
    session = DBSession()
    user = session.query(User).filter(User.userId=='1').one()
    print('type:', type(user))
    print('user:', user.user)
    session.close()
    return '<h1>OK</h1>'
    

if __name__ == '__main__':
    app.run()
