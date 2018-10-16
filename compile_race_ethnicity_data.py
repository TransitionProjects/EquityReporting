"""

"""

import pandas as pd

from count_by_race import raceCountByProvider
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class CreateCombinedEthnicityData:
    def __init__(self):
        self.entry_data = pd.read_excel(askopenfilename(title="Entry Data"))
        self.providers = {
            "Impact Northwest - SSVF_18-OR-399 – Rapid Re-Housing (VA)(6366)": "Vets",
            "Impact Northwest - SSVF_Renewal 15-ZZ-127 - Homeless Prevention (VA) - SP(4794)": "Vets",
            "Impact Northwest - SSVF_Renewal 15-ZZ-127 - Rapid Re-Housing (VA) - SP(4795)": "Vets",
            "Ticket Home - Served (OR-501)(5431)": "Outreach",
            "Transition Projects (TPI) - ACCESS - CM(5471)": "Housing CM",
            "Transition Projects (TPI) - Agency - SP(19)": "",
            "Transition Projects (TPI) - Clark Center - SP(25)": "Clark Center Shelter",
            "Transition Projects (TPI) - Clark Center Corrections Beds(6035)": "Clark Center Shelter",
            "Transition Projects (TPI) - Clark Guest Beds - SP(3071)": "Clark Center Shelter",
            "Transition Projects (TPI) - Columbia Shelter(6527)": "Columbia Shelter",
            "Transition Projects (TPI) - Coordinated Housing Access Team (CHAT)(5965)": "Outreach",
            "Transition Projects (TPI) - Day Center - SP(26)": "Resource Center",
            "Transition Projects (TPI) - Destination Housing - RRH(6284)": "Placement Provider",
            "Transition Projects (TPI) - Doreen's Place - SP(28)": "Doreen's Place Shelter",
            "Transition Projects (TPI) - Doreen's Place Guest Beds - SP(3072)": "Doreen's Place Shelter",
            "Transition Projects (TPI) - Health Connections - SERVICES ONLY(6481)": "Health and Wellness",
            "Transition Projects (TPI) - Health Navigation(6050)": "Health and Wellness",
            "Transition Projects (TPI) - Holgate Project(6486)": "Placement Provider",
            "Transition Projects (TPI) - Housing Choice Voucher(5961)": "Placement Provider",
            "Transition Projects (TPI) - Housing Services - SP(27)": "Housing CM",
            "Transition Projects (TPI) - Jean’s Place VA Grant Per Diem (GPD) - SP(3362)": "Jean's Place Shelter",
            "Transition Projects (TPI) - Jean's Place L1 - SP(29)": "Jean's Place Shelter",
            "Transition Projects (TPI) - Jean's Place Corrections(6231)": "Jean's Place Shelter",
            "Transition Projects (TPI) - Mental Health Programming - SP(3175)": "Health and Wellness",
            "Transition Projects (TPI) - Oregon Vets (OHA) - PSH(5744)": "Vets",
            "Transition Projects (TPI) - Outreach - SP(3782)": "Outreach",
            "Transition Projects (TPI) - PGE Veteran Families - HP(6484)": "Placement Provider",
            "Transition Projects (TPI) - Residential - CM(5473)": "Housing CM",
            "Transition Projects (TPI) - Retention - CM(5472)": "Retention CM",
            "Transition Projects (TPI) - SOS Shelter(2712)": "SOS Shelter",
            "Transition Projects (TPI) - SSVF_18-OR-399 – Homeless Prevention (VA)(6351)": "Vets",
            "Transition Projects (TPI) - SSVF_18-OR-399 – Rapid Re-Housing (VA)(6350)": "Vets",
            "Transition Projects (TPI) - SSVF_18-OR-399 – SSVF_Screening (VA)(6352)": "Vets",
            "Transition Projects (TPI) - SSVF_C15-OR-501A - Homeless Prevention (VA) - SP(4803)": "Vets",
            "Transition Projects (TPI) - SSVF_C15-OR-501A - Rapid Re-Housing (VA) - SP(4804)": "Vets",
            "Transition Projects (TPI) - SSVF_Renewal 15-ZZ-127 - Homeless Prevention (VA) - SP(4801)": "Vets",
            "Transition Projects (TPI) - SSVF_Renewal 15-ZZ-127 Rapid Re-Housing (VA) - SP(4802)": "Vets",
            "Transition Projects (TPI) - SSVF_Screening C15-OR-501A (VA) - SP(4805)": "Vets",
            "Transition Projects (TPI) - SSVF_Screening_15-ZZ-127 (VA) - SP(4870)": "Vets",
            "Transition Projects (TPI) - Substance Abuse Programming (IAP) - SP(3168)":  "Health and Wellness",
            "Transition Projects (TPI) - Substance Abuse Programming (PIAP) - SP(6074)":  "Health and Wellness",
            "Transition Projects (TPI) - Support Services - Employment(6593)": "Employment",
            "Transition Projects (TPI) - Support Services(4325)": "",
            "Transition Projects (TPI) - Titan Manor - HP(6277)": "Placement Provider",
            "Transition Projects (TPI) - VA Grant Per Diem (inc. Doreen's Place GPD) - SP(3189)": "Doreen's Place Shelter",
            "Transition Projects (TPI) - Wellness Access(6051)": "Health and Wellness",
            "Transition Projects (TPI) - Willamette Center(5764)": "Willamette Shelter",
            "Transition Projects (TPI) - Women's Housing Program - RRH(6153)": "Placement Provider",
            "Transition Projects (TPI) - WyEast Emergency Shelter(6612)": "WyEast Shelter",
            "Transition Projects (TPI) -CCC-PSH-Scattered Site-NonADFC-HOPE-PSH Subsidy-(4999)": "Placement Provider",
            "Transition Projects (TPI) Housing - Barbara Maher Apartments PSH - SP(3018)": "Barbara Maher Shelter",
            "Transition Projects (TPI) Housing - Clark Annex GPD - SP(4259)": "Clark Center Annex Shelter",
            "Transition Projects (TPI) Housing - Clark Annex PSH - SP(2858)": "Clark Center Annex Shelter",
            "Transition Projects (TPI) Rent - Collaboration (HUD) - SP(2563)": "Placement Provider",
            "Transition Projects (TPI) Rent - EHA Vets (STRA) - HP(5794)": "Vets",
            "Transition Projects (TPI) Rent - EHA Vets (STRA) - RRH(4930)": "Vets",
            "Transition Projects (TPI) Rent - EHA (STRA) - HP(6328)": "Placement Provider",
            "Transition Projects (TPI) Rent - EHA (STRA) - RRH(6327)": "Placement Provider",
            "Transition Projects (TPI) Rent - Horizons (HUD) - SP(52)": "Placement Provider",
            "Transition Projects (TPI) Rent - Housing for Veterans (PHB)(5138)": "Vets",
            "Transition Projects (TPI) Rent - Human Solutions Safehome (HUD) - SP(3792)": "Placement Provider",
            "Transition Projects (TPI) Rent - MGF (STRA) - RRH(6711)": "Placement Provider",
            "Transition Projects (TPI) Rent - OTIS (HUD) - SP(56)": "Placement Provider",
            "Transition Projects (TPI) Rent - Portland Housing Bureau (PHB) - SP(3219)": "Placement Provider",
            "Transition Projects (TPI) Rent - START (HUD) - RRH(4431)": "Placement Provider",
            "Transition Projects (TPI) Rent - United Way (STRA) - RRH(4261)": "Placement Provider",
            "Transition Projects (TPI) Rent - Veterans - SP(2715)": "Vets",
            "Transition Projects (TPI) Rent – Vets Section 8 (PHB)(5139)": "Vets",
            "Transition Projects (TPI) Rent - VRLC TH - SP(2428)": "Vets",
            "Transition Projects (TPI) Winter Housing For Women (WH4W) (HUD)(4821)": "Placement Provider",
            "Transition Projects (TPI) Rent - WIHN (Women into Housing Now) - SP(3955)": "Placement Provider",
            "Transition Projects (TPI) x-(END 2018/06) Rent - EHA2 (STRA) - HP(6392)": "Placement Provider",
            "Transition Projects (TPI) x-(END 2018/06) Rent - EHA2 (STRA) - RRH(6393)": "Placement Provider",
            "Transition Projects (TPI) x-(END 2018/06) Rent - PGF (STRA) - RRH(3220)": "Placement Provider",
            "Transition Projects (TPI) x-(END 2018/06) Rent - EHA-OTO (STRA) - RRH(5611)": "Placement Provider",
            "El Programa Hispano Catolico (EPHC) - Coordinated Housing Access Team (CHAT)(6082)": "Outreach",
            "Urban League - Coordinated Housing Access Team (CHAT)(6081)": "Outreach",
            "ZZ - Transition Projects (TPI) - Columbia Shelter (Do not use after 4/25/18)(5857)": "Placement Provider",
            "Transition Projects (TPI) x-(END 2018/06) Rent - ESGP - Rapid Re-Housing - SP(3926)": "Placement Provider",
            "Transition Projects (TPI) - Hansen Emergency Shelter - SP(5588)": "Hansen Shelter"
        }
        self.entry_data["Provider"] = [self.providers[value] for value in self.entry_data["Service Provide Provider"]]
        self.output_data = {}

    def iterate_on_data(self):
        for value in self.entry_data["Provider"].drop_duplicates():
            provider_data = self.entry_data[self.entry_data["Provider"] == value]
            row = raceCountByProvider(provider_data).process()
            self.output_data[value] = row

    def create_df(self):
        output = pd.DataFrame.from_dict(
            self.output_data,
            orient="index"
        )
        return output

    def process(self):
        self.iterate_on_data()
        output = self.create_df()

        writer = pd.ExcelWriter(
            asksaveasfilename(title="Save the Output Data"),
            engine="xlsxwriter"
        )
        output.to_excel(writer, sheet_name="Summary")
        writer.save()

if __name__ == "__main__":
    a = CreateCombinedEthnicityData()
    a.process()
