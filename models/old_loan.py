from sqlalchemy import Column, Integer, Double, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OldLoan(Base):
    __tablename__ = 'api_oldcustomer'

    id = Column(Integer, primary_key=True)
    loan_status_2 = Column(String)
    loan_status = Column(Integer)
    loan_amnt = Column(Double)
    term = Column(Integer)
    int_rate = Column(Double)
    installment = Column(Double)
    sub_grade = Column(String)
    emp_length = Column(Integer)
    home_ownership = Column(String)
    annual_inc = Column(String)
    verification_status = Column(String)
    issue_d = Column(String)
    purpose = Column(String)
    addr_state = Column(String)
    dti = Column(Double)
    fico_range_low = Column(Integer)
    fico_range_high = Column(Integer)
    open_acc = Column(Integer)
    pub_rec = Column(Integer)
    revol_bal = Column(Integer)
    revol_util = Column(Double)
    mort_acc = Column(Integer)
    pub_rec_bankruptcies = Column(Integer)
    age = Column(Integer)
    pay_status = Column(Integer)

    def __repr__(self):
        return f"<OldLoan(id={self.id})>"
