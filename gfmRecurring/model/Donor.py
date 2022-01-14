
class Donor:

    def __init__(self, donor_name: str, limit_amt: int, total_donation: int):
        self.donor_name = donor_name
        self.limit_amt = limit_amt
        self.total_donation = total_donation
        self.number_of_donations = 0
        self.donation_limit_meet = False



