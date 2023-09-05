from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HomeOwnership(Base):
    __tablename__ = 'api_homeownership'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Purpose(Base):
    __tablename__ = 'api_purpose'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class State(Base):
    __tablename__ = 'api_state'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class SubGrade(Base):
    __tablename__ = 'api_subgrade'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class VerificationStatus(Base):
    __tablename__ = 'api_verificationstatus'

    id = Column(Integer, primary_key=True)
    name = Column(String)
