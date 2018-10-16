"""
This class will generally function to create counts by identified race and/or
ethnicity.  The dataframe sent to this class should already by filtered by TPI
department.  This will work with either service data or entry data.  These data
sources will need to be combined in the case of shelters prior to passing the
data to this class.
"""

import pandas as pd

class raceCountByProvider:
    def __init__(self, dataframe):
        """
        :param dataframe: a pandas dataframe object

        :param department_name: a string
        """
        self.race_dict = {
           "Black or African American (HUD)": "Black or African American",
           "American Indian or Alaska Native (HUD)": "American Indian or Alaska Native",
           "American Indian or Alaska Native (HUD) - DOES NOT MAP": "American Indian or Alaska Native",
           "White (HUD)": "White",
           "Client refused (HUD)": "No Race Information Entered",
           "Native Hawaiian or Other Pacific Islander (HUD)": "Native Hawaiian or Other Pacific Islander",
           "Client doesn't know (HUD)": "No Race Information Entered",
           "Other Multi-Racial": "No Race Information Entered",
           "Asian (HUD)": "Asian",
           "Other (NON-HUD)": "No Race Information Entered",
           "Data not collected (HUD)": "No Race Information Entered"
        }
        self.eth_dict = {
            "Non-Hispanic/Non-Latino (HUD)": "Non-Hispanic/Non-Latino",
            "Client refused (HUD)": "No Ethnicity Information Entered",
            "Client doesn't know (HUD)": "No Ethnicity Information Entered",
            "Hispanic/Latino (HUD)": "Hispanic/Latino",
            "Data not collected (HUD)": "No Ethnicity Information Entered"
        }
        self.data = dataframe.fillna("Data not collected (HUD)")
        self.output_dict = {
            "American Indian or Alaska Native": 0,
            "Asian": 0,
            "Black or African American": 0,
            "Native Hawaiian or Other Pacific Islander": 0,
            "Hispanic/Latino": 0,
            "White": 0
        }


    def process(self):
        """
        First HUD Race and Ethnicity fields will be be simplified, removing
        values that are no longer valid, as well as stripping the (HUD) wording.

        The self.output_dict will then be have values assigned to keys based on
        the values of these simplified fields.
        """
        self.data["Race"] = [self.race_dict[value] for value in self.data["Race(895)"]]
        self.data["Race_Additional"] = [self.race_dict[value] for value in self.data["Race-Additional(1213)"]]
        self.data["Ethnicity"] = [self.eth_dict[value] for value in self.data["Ethnicity (Hispanic/Latino)(896)"]]

        for key in self.output_dict.keys():
            self.output_dict[key] = len(
                self.data[
                    (self.data["Race"] == key) |
                    (self.data["Race_Additional"] == key) |
                    (self.data["Ethnicity"] == key)
                ].drop_duplicates(subset="Client Uid").index
            )
        self.output_dict["All"] = len(self.data.drop_duplicates(subset="Client Uid").index)

        return self.output_dict
