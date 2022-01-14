from gfmRecurring.model.Campaign import Campaign
from gfmRecurring.model.Donor import Donor


class ProcessCommands:

    def __init__(self, gfm_dao):
        self.gfm_dao = gfm_dao

    """ 
    This method parses and processes commands based on operation and entity
    operations : Add, Donate
    entities : Donor, Campaign
    It throws an error if operation or entity is not valid
    :param command_list list of all commands submitted
    :return None
    """
    def parse_and_process_commands(self, command_list: list) -> None:
        for i in command_list:
            command = i.strip('\n').split(" ")
            if command[0] == "Add":
                if command[1] == "Donor" and len(command) == 4:
                    self.gfm_dao.add_donor(command[2], command[3])
                elif command[1] == "Campaign" and len(command) == 3:
                    self.gfm_dao.add_campaign(command[2])
                else:
                    raise ValueError("Commands not recognized")
            elif command[0] == "Donate" and len(command) == 4:
                self.process_donation(command[1], command[2], command[3])
            else:
                raise ValueError("Commands not recognized")

    """ 
    This method processes donations
    it throws error if the donor is not already added,
    it skips the donation if the limit is already meet
    :param donor_name name of the donor
    :param campaign_name name of the campaign to which donation is being made
    :param donation amount being donated
    :return None
    """
    def process_donation(self, donor_name, campaign_name, donation) -> None:
        donor, campaign = self.check_return_if_donor_and_campaign_present(donor_name, campaign_name)
        if not donor.donation_limit_meet:
            donor.total_donation = donor.total_donation + int(donation[1:])
            donor.number_of_donations = donor.number_of_donations + 1
            if donor.total_donation == donor.limit_amt:
                donor.donation_limit_meet = True
            campaign.total_donation = campaign.total_donation + int(donation[1:])

    """ 
    Checks if the donor and campaign have been added
    it throws error if the donor is not already added
    :param donor_name name of the donor
    :param campaign_name name of the campaign to which donation is being made
    :return Donor, Campaign
    """
    def check_return_if_donor_and_campaign_present(self, donor_name, campaign_name) -> (Donor, Campaign):
        all_donors = self.gfm_dao.get_all_donors()
        all_campaigns = self.gfm_dao.get_all_campaigns()
        if donor_name not in all_donors:
            raise ValueError("Donor " + donor_name + " was not added. Please add donor before donating.")
        if campaign_name not in all_campaigns:
            raise ValueError("Campaign " + campaign_name + " was not added. Please add campaign before donating.")
        return all_donors.get(donor_name), all_campaigns.get(campaign_name)

    """ 
    This method prints stats
    :return None
    """
    def print_stats(self) -> None:
        all_donors = self.gfm_dao.get_all_donors()
        all_campaigns = self.gfm_dao.get_all_campaigns()
        print("Donors:")
        for key in sorted(all_donors):
            print(key + ": Total:$" + str(all_donors.get(key).total_donation) + " Average:$" +
                  str(all_donors.get(key).total_donation/all_donors.get(key).number_of_donations))
        print("\nCampaigns:")
        for key in sorted(all_campaigns):
            print(key + ": Total:$" + str(all_campaigns.get(key).total_donation))

