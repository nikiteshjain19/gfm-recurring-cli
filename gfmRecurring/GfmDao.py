from gfmRecurring.model.Campaign import Campaign
from gfmRecurring.model.Donor import Donor


class GfmDao:

    def __init__(self):
        self.campaign_data = {}
        self.donor_data = {}

    def add_donor(self, donor_name, limit_amt):
        donor = Donor(donor_name, int(limit_amt[1:]), 0)
        self.donor_data[donor_name] = donor

    def add_campaign(self, campaign_name):
        campaign = Campaign(campaign_name, 0)
        self.campaign_data[campaign_name] = campaign

    def get_all_donors(self):
        return self.donor_data

    def get_all_campaigns(self):
        return self.campaign_data

