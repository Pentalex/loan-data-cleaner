from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NewLoan(Base):
    __tablename__ = 'api_newcustomer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    loan_status = Column(Integer)
    loan_amnt = Column(String)
    term = Column(String)
    int_rate = Column(Double)
    installment = Column(Double)
    sub_grade_id = Column(Integer)
    employment_length = Column(Integer)
    home_ownership_id = Column(Integer)
    annual_inc = Column(Integer)
    verification_status_id = Column(Integer)
    issued = Column(String)
    purpose_id = Column(Integer)
    addr_state_id = Column(Integer)
    dti = Column(Double)
    fico_range_low = Column(Double)
    fico_range_high = Column(Double)
    open_acc = Column(Double)
    pub_rec = Column(Double)
    revol_bal = Column(Double)
    revol_util = Column(Double)
    mort_acc = Column(Double)
    pub_rec_bankruptcies = Column(Double)
    age = Column(Double)
    payment_status = Column(Double)

    def __repr__(self):
        return f"<NewLoan(id={self.id})>"
