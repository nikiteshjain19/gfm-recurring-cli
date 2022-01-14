import unittest

from gfmRecurring.GfmDao import GfmDao


class GfmDaoTest(unittest.TestCase):

    def test_add_donor(self):
        gfm_dao = GfmDao()
        gfm_dao.add_donor("Greg", "$1000")
        self.assertEqual(gfm_dao.get_all_donors().get("Greg").donor_name, "Greg")
        self.assertEqual(gfm_dao.get_all_donors().get("Greg").limit_amt, 1000)
        self.assertEqual(gfm_dao.get_all_donors().get("Greg").total_donation, 0)
        self.assertEqual(gfm_dao.get_all_donors().get("Greg").number_of_donations, 0)
        self.assertEqual(gfm_dao.get_all_donors().get("Greg").donation_limit_meet, False)

    def test_add_campaign(self):
        gfm_dao = GfmDao()
        gfm_dao.add_campaign("SaveClimate")
        self.assertEqual(gfm_dao.get_all_campaigns().get("SaveClimate").campaign_name, "SaveClimate")
        self.assertEqual(gfm_dao.get_all_campaigns().get("SaveClimate").total_donation, 0)

