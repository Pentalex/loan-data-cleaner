from datetime import datetime
from enums.purpose_enum import PurposeEnum
from utilities import range_to_int, generate_enums

DEFAULT_FICO_LOW = 600
DEFAULT_FICO_HIGH = 750
DEFAULT_EMP_LENGTH = 0
DEFAULT_MORT_ACC = 0

(HomeOwnershipEnum, StateEnum,
 VerificationStatusEnum, SubGradeEnum) = generate_enums()


class OldCleaner():
    @classmethod
    def clean_loan(self, final_loan, old_loan):
        # Fields with no special treatment
        self.assign_regular_fields(final_loan, old_loan)
        # Fields with enum conversion
        self.assign_enum_fields(final_loan, old_loan)
        # Fields with type conversion
        self.assign_type_fields(final_loan, old_loan)
        # Fields with nullable fields where default value must be assigned
        self.assign_default_nullable_fields(final_loan, old_loan)
        # Fields with booleans set based on other fields
        self.assign_booleans(final_loan, old_loan)

        return final_loan

    def assign_regular_fields(final_loan, old_loan):
        # List of attributes to copy from old_loan to final_loan
        attributes_to_copy = [
            'term', 'int_rate', 'installment', 'open_acc', 'pub_rec',
            'revol_bal', 'revol_util', 'dti', 'pub_rec_bankruptcies', 'age',
            'pay_status'
        ]

        # Loop through the attributes and copy them from old_loan to final_loan
        for attribute in attributes_to_copy:
            setattr(final_loan, attribute, getattr(old_loan, attribute))

    def assign_enum_fields(final_loan, old_loan):
        final_loan.purpose = PurposeEnum[old_loan.purpose].value
        final_loan.addr_state = StateEnum["USA_" + old_loan.addr_state].value
        final_loan.sub_grade = SubGradeEnum[old_loan.sub_grade].value
        final_loan.home_ownership = \
            HomeOwnershipEnum[old_loan.home_ownership].value
        final_loan.verification_status = \
            VerificationStatusEnum[old_loan.verification_status].value

    def assign_type_fields(final_loan, old_loan):
        final_loan.loan_status = bool(old_loan.loan_status)
        final_loan.loan_amnt = int(old_loan.loan_amnt)
        final_loan.annual_inc = range_to_int(old_loan.annual_inc)
        final_loan.issue_d = \
            datetime.strptime(old_loan.issue_d, "%Y-%m-%d %H:%M:%S").date()

    def assign_default_nullable_fields(final_loan, old_loan):
        attribute_defaults = {
            'fico_range_low': DEFAULT_FICO_LOW,
            'fico_range_high': DEFAULT_FICO_HIGH,
            'mort_acc': DEFAULT_MORT_ACC,
            'emp_length': DEFAULT_EMP_LENGTH,
        }

        # Loop through the attributes and set them in final_loan
        for attribute, default_value in attribute_defaults.items():
            attribute_value = getattr(old_loan, attribute, None)
            if attribute_value is not None:
                setattr(final_loan, attribute, int(attribute_value))
            else:
                setattr(final_loan, attribute, default_value)

    @classmethod
    def assign_booleans(self, final_loan, old_loan):
        self.assign_verification_booleans(final_loan, old_loan)
        self.assign_homeownership_booleans(final_loan, old_loan)

    def assign_verification_booleans(final_loan, old_loan):
        status_mapping = {
            "Source Verified": (False, False, True),
            "Not Verified": (False, True, False),
            "Verified": (True, False, False),
        }
        (final_loan.is_verified, final_loan.is_not_verified,
         final_loan.is_source_verified) = status_mapping.get(
             old_loan.verification_status, (False, False, False))

    def assign_homeownership_booleans(final_loan, old_loan):
        status_mapping = {
            "MORTGAGE": (True, False, False, False, False),
            "RENT": (False, True, False, False, False),
            "OWN": (False, False, True, False, False),
            "ANY": (False, False, False, True, False),
            "OTHER": (False, False, False, False, True),
            "NONE": (False, False, False, False, False)
        }
        (final_loan.is_mortgage, final_loan.is_rent, final_loan.is_own,
         final_loan.is_any, final_loan.is_other) = status_mapping.get(
            old_loan.home_ownership, (False, False, False, False, False)
        )
