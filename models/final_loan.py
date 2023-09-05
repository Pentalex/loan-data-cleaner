from sqlalchemy import Column, Integer, Date, Boolean, Double, create_engine
from sqlalchemy.ext.declarative import declarative_base
from new_cleaner import NewCleaner
from old_cleaner import OldCleaner
Base = declarative_base()


class FinalLoan(Base):
    __tablename__ = 'final_loan'

    id = Column(Integer, primary_key=True)
    loan_status = Column(Boolean)
    loan_amnt = Column(Integer)
    term = Column(Integer)
    int_rate = Column(Double)
    installment = Column(Double)
    sub_grade = Column(Integer)
    emp_length = Column(Integer)
    home_ownership = Column(Integer)
    is_mortgage = Column(Boolean)
    is_rent = Column(Boolean)
    is_own = Column(Boolean)
    is_any = Column(Boolean)
    is_other = Column(Boolean)
    annual_inc = Column(Integer)
    verification_status = Column(Integer)
    is_verified = Column(Boolean)
    is_not_verified = Column(Boolean)
    is_source_verified = Column(Boolean)
    issue_d = Column(Date)
    purpose = Column(Integer)
    addr_state = Column(Integer)
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
        return f"<FinalLoan(id={self.id})>"

    @classmethod
    def from_old_loan(cls, old_loan):
        final_loan = cls()
        final_loan = OldCleaner.clean_loan(final_loan, old_loan)
        return final_loan

    @classmethod
    def from_new_loan(cls, new_loan):
        final_loan = cls()
        final_loan = NewCleaner.clean_loan(final_loan, new_loan)
        return final_loan


engine = create_engine('sqlite:///clean_customer_data.sqlite3')
Base.metadata.create_all(bind=engine)
