
import unittest
from unittest.mock import Mock, MagicMock
from gfmRecurring.GfmDao import GfmDao
from gfmRecurring.ProcessCommands import ProcessCommands
from gfmRecurring.model.Campaign import Campaign
from gfmRecurring.model.Donor import Donor


class ProcessCommandsTest(unittest.TestCase):

    def test_parse_add_donor(self):
        command_list = ["Add Donor Greg $1000"]
        mock_gfm_dao = Mock()
        process_commands = ProcessCommands(mock_gfm_dao)
        process_commands.parse_and_process_commands(command_list)
        mock_gfm_dao.add_donor.assert_called()
        mock_gfm_dao.add_campaign.assert_not_called()

    def test_parse_add_campaign(self):
        command_list = ["Add Campaign SaveTheDogs"]
        mock_gfm_dao = Mock()
        process_commands = ProcessCommands(mock_gfm_dao)
        process_commands.parse_and_process_commands(command_list)
        mock_gfm_dao.add_campaign.assert_called()
        mock_gfm_dao.add_donor.assert_not_called()

    def test_throws_value_error_for_wrong_operation(self):
        command_list = ["Delete Campaign SaveTheDogs"]
        mock_gfm_dao = Mock()
        process_commands = ProcessCommands(mock_gfm_dao)
        with self.assertRaises(ValueError):
            process_commands.parse_and_process_commands(command_list)

    def test_throws_value_error_for_wrong_entity(self):
        command_list = ["Add Hero SaveTheDogs"]
        mock_gfm_dao = Mock()
        process_commands = ProcessCommands(mock_gfm_dao)
        with self.assertRaises(ValueError):
            process_commands.parse_and_process_commands(command_list)

    def test_process_donation(self):
        mock_gfm_dao = GfmDao()
        all_donor = {"Greg": Donor("Greg", 100, 0)}
        all_campaign = {"SaveAnimals": Campaign("SaveAnimals", 0)}
        process_commands = ProcessCommands(mock_gfm_dao)
        mock_gfm_dao.get_all_donors = MagicMock(return_value=all_donor)
        mock_gfm_dao.get_all_campaigns = MagicMock(return_value=all_campaign)
        process_commands.process_donation("Greg", "SaveAnimals", "$100")
        self.assertEqual(all_donor.get("Greg").total_donation, 100)
        self.assertEqual(all_campaign.get("SaveAnimals").total_donation, 100)
        self.assertEqual(all_donor.get("Greg").donation_limit_meet, True)

    def test_skips_donation_after_limit_meet(self):
        mock_gfm_dao = GfmDao()
        all_donor = {"Greg": Donor("Greg", 100, 0)}
        all_campaign = {"SaveAnimals": Campaign("SaveAnimals", 0)}
        process_commands = ProcessCommands(mock_gfm_dao)
        mock_gfm_dao.get_all_donors = MagicMock(return_value=all_donor)
        mock_gfm_dao.get_all_campaigns = MagicMock(return_value=all_campaign)
        process_commands.process_donation("Greg", "SaveAnimals", "$100")
        process_commands.process_donation("Greg", "SaveAnimals", "$100")
        self.assertEqual(all_donor.get("Greg").total_donation, 100)
        self.assertEqual(all_campaign.get("SaveAnimals").total_donation, 100)
        self.assertEqual(all_donor.get("Greg").donation_limit_meet, True)

    def test_throws_error_if_donor_not_present(self):
        mock_gfm_dao = GfmDao()
        all_donor = {"Greg": Donor("Greg", 100, 0)}
        all_campaign = {"SaveAnimals": Campaign("SaveAnimals", 0)}
        process_commands = ProcessCommands(mock_gfm_dao)
        mock_gfm_dao.get_all_donors = MagicMock(return_value=all_donor)
        mock_gfm_dao.get_all_campaigns = MagicMock(return_value=all_campaign)
        with self.assertRaises(ValueError):
            process_commands.process_donation("Sam", "SaveAnimals", "$100")