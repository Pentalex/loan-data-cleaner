#  Name:         Aleksander Arentz
#  Date:         5 September 2023
#  File:         main.py
#  Description:  Looks for a file called "customer_data.sqlite3" in the root
#  directory of the folder and runs the cleaning operations on the tables
#  before combining them into a table called "final_loan" in a new file called
# "clean_customer_data.sqlite3" saved in the root directory.
#
#  Default values for missing data can be customised in the new_cleaner.py and
#  old_cleaner.py files.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.final_loan import FinalLoan
from models.new_loan import NewLoan
from models.old_loan import OldLoan

# Estabilish connection with database
engine = create_engine('sqlite:///customer_data.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

# Query data from new and old customer tables into lists
old_table_data = session.query(OldLoan).all()
new_table_data = session.query(NewLoan).all()


# Iterate over both data lists to create one final list with the cleaned,
# converted final table data.
final_table_data = []

for old_loan in old_table_data:
    final_table_data.append(FinalLoan.from_old_loan(old_loan))

for new_loan in new_table_data:
    final_table_data.append(FinalLoan.from_new_loan(new_loan))


# Create a new DB file called clean_customer_data.sqlite3 and populate the
# final_loan table with all the data generated from the cleaned up loans.
engine = create_engine('sqlite:///clean_customer_data.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

for final_loan in final_table_data:
    session.add(final_loan)

session.commit()
