from gfmRecurring.model.Campaign import Campaign
from gfmRecurring.model.Donor import Donor


class GfmDao:

    def __init__(self):
        self.campaign_data = {}
        self.donor_data = {}

    """ 
    This method adds donor
    :param donor_name name of the donor to be added
    :param limit_amt limit amount donor would be paying
    :return None
    """
    def add_donor(self, donor_name, limit_amt):
        donor = Donor(donor_name, int(limit_amt[1:]), 0)
        self.donor_data[donor_name] = donor

    """ 
    This method adds campaign
    :param campaign_name name of the campaign to be added
    :return None
    """
    def add_campaign(self, campaign_name):
        campaign = Campaign(campaign_name, 0)
        self.campaign_data[campaign_name] = campaign

    """ 
    This method returns all the donors
    :return dictionary of donors
    """
    def get_all_donors(self):
        return self.donor_data

    """ 
    This method returns all the campaigns
    :return dictionary of campaigns
    """
    def get_all_campaigns(self):
        return self.campaign_data

