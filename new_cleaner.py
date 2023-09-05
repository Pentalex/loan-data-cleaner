from utilities import (
    loan_string_to_int, year_string_to_months,
    date_string_to_date, enum_name_by_value, generate_enums
)

(HomeOwnershipEnum, StateEnum,
 VerificationStatusEnum, SubGradeEnum) = generate_enums()

DEFAULT_FICO_LOW = 600
DEFAULT_FICO_HIGH = 750
DEFAULT_EMP_LENGTH = 0
DEFAULT_MORT_ACC = 0
DEFAULT_PUB_REC_BANKRUPTCIES = 0


class NewCleaner():
    @classmethod
    def clean_loan(self, final_loan, new_loan):
        self.assign_regular_fields(final_loan, new_loan)
        self.assign_type_fields(final_loan, new_loan)

        # Fields with nullable fields where default value must be assigned
        self.assign_nullable_fields(final_loan, new_loan)
        #
        self.assign_booleans(final_loan, new_loan)

        return final_loan

    def assign_regular_fields(final_loan, new_loan):
        regular_fields_mapping = {
            'int_rate': 'int_rate',
            'installment': 'installment',
            'sub_grade': 'sub_grade_id',
            'emp_length': 'employment_length',
            'home_ownership': 'home_ownership_id',
            'annual_inc': 'annual_inc',
            'verification_status': 'verification_status_id',
            'purpose': 'purpose_id',
            'addr_state': 'addr_state_id',
            'dti': 'dti',
            'revol_util': 'revol_util',
        }

        # Loop through regular fields mapping and set attributes in final_loan
        for final_field, new_field in regular_fields_mapping.items():
            setattr(final_loan, final_field,
                    getattr(new_loan, new_field, None))

    def assign_type_fields(final_loan, new_loan):
        final_loan.loan_status = bool(new_loan.loan_status)
        final_loan.loan_amnt = loan_string_to_int(new_loan.loan_amnt)
        final_loan.term = year_string_to_months(new_loan.term)
        final_loan.issue_d = date_string_to_date(new_loan.issued)
        final_loan.open_acc = int(new_loan.open_acc)
        final_loan.pub_rec = int(new_loan.pub_rec)
        final_loan.revol_bal = int(new_loan.revol_bal)
        final_loan.age = int(new_loan.age)
        final_loan.pay_status = int(new_loan.payment_status)

    def assign_nullable_fields(final_loan, new_loan):
        # Map attributes to their default values
        attribute_defaults = {
            'fico_range_low': DEFAULT_FICO_LOW,
            'fico_range_high': DEFAULT_FICO_HIGH,
            'mort_acc': DEFAULT_MORT_ACC,
            'emp_length': DEFAULT_EMP_LENGTH,
            'pub_rec_bankruptcies': DEFAULT_PUB_REC_BANKRUPTCIES,
        }

        # Loop through the attributes and set them in final_loan
        for attribute, default_value in attribute_defaults.items():
            attribute_value = getattr(new_loan, attribute, None)
            if attribute_value is not None:
                setattr(final_loan, attribute, int(attribute_value))
            else:
                setattr(final_loan, attribute, default_value)

    @classmethod
    def assign_booleans(self, final_loan, new_loan):
        self.assign_verification_booleans(final_loan, new_loan)
        self.assign_homeownership_booleans(final_loan, new_loan)

    def assign_verification_booleans(final_loan, new_loan):
        status_mapping = {
            "Source Verified": (False, False, True),
            "Not Verified": (False, True, False),
            "Verified": (True, False, False),
        }
        (final_loan.is_verified, final_loan.is_not_verified,
         final_loan.is_source_verified) = status_mapping.get(
             enum_name_by_value(VerificationStatusEnum,
                                new_loan.verification_status_id),
             (False, False, False))

    def assign_homeownership_booleans(final_loan, new_loan):
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
            enum_name_by_value(HomeOwnershipEnum, new_loan.home_ownership_id),
            (False, False, False, False, False)
        )
