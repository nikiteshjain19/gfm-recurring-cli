
class ProcessCommands:

    def __init__(self, gfm_dao):
        self.gfm_dao = gfm_dao

    def parse_and_process_commands(self, command_list: list):
        for i in command_list:
            command = i.strip('\n').split(" ")
            if command[0] == "Add":
                if command[1] == "Donor":
                    self.gfm_dao.add_donor(command[2], command[3])
                elif command[1] == "Campaign":
                    self.gfm_dao.add_campaign(command[2])
            elif command[0] == "Donate":
                self.process_donation(command[1], command[2], command[3])
            else:
                raise ValueError("Commands not recognized")

    def process_donation(self, donor_name, campaign_name, donation):
        donor, campaign = self.check_return_if_donor_and_campaign_present(donor_name, campaign_name)
        if not donor.donation_limit_meet:
            donor.total_donation = donor.total_donation + int(donation[1:])
            donor.number_of_donations = donor.number_of_donations + 1
            if donor.total_donation == donor.limit_amt:
                donor.donation_limit_meet = True
            campaign.total_donation = campaign.total_donation + int(donation[1:])

    def check_return_if_donor_and_campaign_present(self, donor_name, campaign_name):
        all_donors = self.gfm_dao.get_all_donors()
        all_campaigns = self.gfm_dao.get_all_campaigns()
        if donor_name not in all_donors:
            raise ValueError("Donor " + donor_name + " was not added. Please add donor before donating.")
        if campaign_name not in all_campaigns:
            raise ValueError("Campaign " + campaign_name + " was not added. Please add campaign before donating.")
        return all_donors.get(donor_name), all_campaigns.get(campaign_name)

    def print_stats(self):
        all_donors = self.gfm_dao.get_all_donors()
        all_campaigns = self.gfm_dao.get_all_campaigns()
        print("Donors:")
        for key, val in all_donors.items():
            print(key + ": Total:$" + str(val.total_donation) + " Average:$" + str(val.total_donation/val.number_of_donations))
        print("\nCampaigns:")
        for key, val in all_campaigns.items():
            print(key + ": Total:$" + str(val.total_donation))

