Save all of the 4 python files, and open them in your python IDE (e.g. Spyder)
The 'Complete_Check.py' script is the master script, which is the only one you need to interact with and run. The others are helper functions that the Master script pulls from.

In the COmplete_Check script: In order to get an accurate result, you need to edit the filepath to previous month's monthly landauer report (the 'previous_month' variable).
You also need to check that the spreadsheet accessible via the wearperiod_investigation_levels and annual_investigation_levels variable file path is accurate and up-to-date (reflects what is written in local rules)
Unless there has been an update to the local rules in a given area, this spreadsheet should not change. Show the RPA the numbers in these spreadsheets if unsure.

The first time you run this script, you may need to install pandas by typing pip install pandas in the IDE terminal.

Once you have run the script, the results should be saved in the location defined by the output file paths (e.g. the filepaths defined by the variables 
'monthlyreport_location', 'prewarning_report_savelocation', 'annual_report_savelocation', 'previousyear_report_savelocation' and  'comparison_file').


>> If any new landauer accounts or subaccounts get added, this script will need to be updated. Those accounts will need to be checked manually against investigation levels until they are added to the script. 
