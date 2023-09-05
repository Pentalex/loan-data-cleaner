import re
from dateutil import parser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.enum_tables import HomeOwnership, State
from models.enum_tables import VerificationStatus, SubGrade
from enums.enum_from_table import EnumFromTable


def generate_enums():
    engine = create_engine('sqlite:///customer_data.sqlite3')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Populate enums for each table
    HomeOwnershipEnum = EnumFromTable.generate(
        HomeOwnership, "HomeOwnershipEnum", session)
    StateEnum = EnumFromTable.generate(State, "StateEnum", session)
    VerificationStatusEnum = EnumFromTable.generate(
        VerificationStatus, "VerificationStatusEnum", session)
    SubGradeEnum = EnumFromTable.generate(SubGrade, "SubGradeEnum", session)

    return (HomeOwnershipEnum, StateEnum, VerificationStatusEnum, SubGradeEnum)


def range_to_int(range_str):
    match = re.match(r'\((\d+\.\d+), (\d+\.\d+)\]', range_str)

    if match:
        lower_bound = float(match.group(1))
        upper_bound = float(match.group(2))
        midpoint = int((lower_bound + upper_bound) / 2)

        return midpoint
    else:
        return None


def loan_string_to_int(loan_amnt):
    # Remove the "k" character and convert to float
    float_value = float(loan_amnt.replace("k", "").strip())

    # Multiply by 1000 to get the integer value
    int_value = int(float_value * 1000)

    return int_value


def year_string_to_months(year_string):
    return int(float(year_string.replace("Y", "").strip())) * 12


def date_string_to_date(date_string):
    if len(date_string.split('-')) == 2:
        date_string += "-01"
    try:
        return parser.parse(date_string).date()
    except ValueError:
        return None  # Parsing failed


def enum_name_by_value(enum, value):
    for entry in enum:
        if entry.value == value:
            return entry.name
    return None
