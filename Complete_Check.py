import pandas as pd
from Monthly_Landauer import monthly_landauer_check 
from Annual_Landauer import annual_landauer_check
from Report_Differences  import compare_reports 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEFINE INPUT FILEPATHS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Filepath to previous month's monthy landauer check report generated using this script: CHANGE MONTH FILE POINTING TO
previous_month="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Results staff who exceeded levels/2026/February/monthly_exceeded.csv"


#Save dose history from Jan 2025 to today's date for all accounts and paste filepaths here. Start date must remain Jan 2025 indefinately (unless you update baseline but this process is involved)
path_M500070 ="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/500070.xls"
path_M501124= "H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/501124.xls"
path_M500499="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/500499.xls"
path_M500488="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/500488.xls"
path_M500486="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/500486.xls"
path_M500484= "H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/500484.xls"

#Save History Summary [Current Year] All/YTD data for all accounts and paste filepaths here:
path_YTD500070 ="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500070.xls"
path_YTD501124= "H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD501124.xls"
path_YTD500488="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500488.xls"
path_YTD500486="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500486.xls"
path_YTD500499="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500499.xls"
path_YTD500484= "H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500484.xls"


path_YTD500070_previousyear="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500070py.xls"
path_YTD501124_previousyear="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD501124py.xls"
path_YTD500499_previousyear="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500499py.xls"
path_YTD500488_previousyear="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500488py.xls"
path_YTD500486_previousyear="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500486py.xls"
path_YTD500484_previousyear="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Current Month Reports/YTD500484py.xls"

#Check that the investigation levels in spreadsheet below are up-to-date (see Personal Dosimetry W.I)
wearperiod_investigation_levels="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Investigation Levels Used for Automation/wearperiod_investigation_levels2023.xlsx"

#Check that the investigation levels in spreadsheet below are up-to-date (see Personal Dosimetry W.I)
annual_investigation_levels="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Investigation Levels Used for Automation/annual_investigation_levels2023.xlsx"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEFINE OUTPUT FILEPATHS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Define where you want it saved to and what format/name:
comparison_file="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Results staff who exceeded levels/Latest Results/New_monthly_results.csv"

monthlyreport_location="H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Results staff who exceeded levels/Latest Results/monthly_exceeded.csv"

prewarning_report_savelocation='H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Results staff who exceeded levels/Latest Results/annual_prewarning.csv'

annual_report_savelocation='H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Results staff who exceeded levels/Latest Results/annual_exceeded.csv'

previousyear_report_savelocation='H:/Radiation Protection/Landauer/Landauer reports/Landauer reports for automation/Results staff who exceeded levels/Latest Results/previous_year_annual_exceeded.csv'


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
RUN THE FUNCTIONS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

monthly_landauer_check(
        path_M500070,
        path_M501124,
        path_M500499,
        path_M500488,
        path_M500486,
        path_M500484,
        wearperiod_investigation_levels,
        monthlyreport_location)

annual_landauer_check(
        path_YTD500070,
        path_YTD501124,
        path_YTD500499,
        path_YTD500488,
        path_YTD500486,
        path_YTD500484,
        path_YTD500070_previousyear,
        path_YTD501124_previousyear,
        path_YTD500499_previousyear,
        path_YTD500488_previousyear,
        path_YTD500486_previousyear,
        path_YTD500484_previousyear,
        annual_investigation_levels,
        prewarning_report_savelocation,
        annual_report_savelocation,
        previousyear_report_savelocation)


compare_reports(previous_month, monthlyreport_location, comparison_file, wearperiod_investigation_levels)

