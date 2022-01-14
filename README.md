This code is built with Python 3.9

Follow below steps in the terminal on macOS

Steps to build the project:
1. Get the project in local system.
2. (Optional) You can install virtual environment and to run this code in virtual env follow instructions here : https://docs.python.org/3/library/venv.html
3. Install pip if not present using this link https://pip.pypa.io/en/stable/installation/
4. Run shell script present in the repo to install pyinstaller and build an executable : sh install.sh

Once these steps are followed you should see a executable in submission folder with name gfm-recurring, if there is any issue with building executable I have added executable in executable_submission folder.

Steps to run the project:
1. Create a input text file with the commands, sample text file is present in the repository
2. Go to submissions folder using this command : cd submission/
3. Once you are inside the submission folder use this command to run the executable : gfm-recurring ../input.txt

To test the project using unit test run this command : 
        python setup.py test
For manual testing following scenarios should be considered:
1. Add a donor
2. Add a campaign
3. Submit a command which is invalid (valid inputs are Add, Donate)
4. Add invalid entity, valid entities are Donor and campaign
5. Submit commands with some data missing
6. Donate command
7. Donate command should skip a command if the limit for the person has reached
8. Submit a donate command without adding a donor

Explanation of the solution:
1. First step is to read the file content using argument parser.
2. Once the content of the file is read we parse and process the command one at a time
   a. For parsing we try to identify if its Add or Donate command
   b. Next step is to check if we are adding a Donor or Campaign
3. Next we add Donor or Campaign to the dictionary with key as donor name or campaign name respectively, this helps to retrive the record in O(n) time complexity
4. Once donor and campaign are added we start processing donations
5. We validate if the donor and campaign is already added if not we throw an error
6. Next we verify if the the donor has already meet his limit for donation, if it has we skip the donation command. We use a flag on the donor to identify this, the reason for using flag is to avoid comaprison of the total amount donated and limit everytime.
7. Donation is added to the campaign total and donated amount total for the donor and the number of donations is also updated
8. Once this is done, we use the donor data and campaign data to print the stats



