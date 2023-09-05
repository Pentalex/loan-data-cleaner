from enum import Enum


# Manually implemented to match the uses in old customer table.
class PurposeEnum(Enum):
    debt_consolidation = 1
    credit_card = 2
    other = 3
    house = 4
    vacation = 5
    home_improvement = 6
    moving = 7
    medical = 8
    car = 9
    small_business = 10
    major_purchase = 11
    renewable_energy = 12
    wedding = 13
    educational = 14
