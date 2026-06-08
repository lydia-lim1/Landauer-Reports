
"""
Script to automate comparing Landauer badge results to their respective
annual investigation levels 
"""



def annual_landauer_check(
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
        previousyear_report_savelocation):
    
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Loading & Pre-prepping data
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Load investigation level excel as a dataframe called 'I'
    I=pd.read_excel(annual_investigation_levels)
    
    
    #Load Landauer dose reports into a single dataframe called 'R'
    YTD500070 = pd.read_excel(path_YTD500070)
    YTD501124 = pd.read_excel(path_YTD501124)
    YTD500499= pd.read_excel(path_YTD500499)
    YTD500488= pd.read_excel(path_YTD500488)
    YTD500486= pd.read_excel(path_YTD500486)
    YTD500484= pd.read_excel(path_YTD500484)
    YTD500070_py = pd.read_excel(path_YTD500070_previousyear)
    YTD501124_py = pd.read_excel(path_YTD501124_previousyear)
    YTD500499_py= pd.read_excel(path_YTD500499_previousyear)
    YTD500488_py= pd.read_excel(path_YTD500488_previousyear)
    YTD500486_py= pd.read_excel(path_YTD500486_previousyear)
    YTD500484_py= pd.read_excel(path_YTD500484_previousyear)
    
    R= pd.concat([YTD500070, YTD501124, YTD500499, YTD500486, YTD500484, YTD500488])
    
    PY=pd.concat([YTD500070_py, YTD501124_py, YTD500499_py, YTD500486_py, YTD500484_py, YTD500488_py])
    
    #Convert 'M' (landauer's way of saying no dose) to the numerical value 0
    R['Total DDE'] = R['Total DDE'].replace('M',0).apply(pd.to_numeric)
    R['Total LDE'] = R['Total LDE'].replace('M',0).apply(pd.to_numeric)
    R['Total SDE'] = R['Total SDE'].replace('M',0).apply(pd.to_numeric)
    R['Extremity'] = R['Extremity'].replace('M',0).apply(pd.to_numeric)
    
    
    #Ensure the DDE,LDE,SDE and Extremity values are treated as numerical data type
    R['Total DDE'] = pd.to_numeric(R['Total DDE'], errors='coerce')
    R['Total LDE'] = pd.to_numeric(R['Total LDE'], errors='coerce')
    R['Total SDE'] = pd.to_numeric(R['Total SDE'], errors='coerce')
    R['Extremity'] = pd.to_numeric(R['Extremity'], errors='coerce')
    
    #Convert 'M' (landauer's way of saying no dose) to the numerical value 0
    PY['Total DDE'] = PY['Total DDE'].replace('M',0).apply(pd.to_numeric)
    PY['Total LDE'] = PY['Total LDE'].replace('M',0).apply(pd.to_numeric)
    PY['Total SDE'] = PY['Total SDE'].replace('M',0).apply(pd.to_numeric)
    PY['Extremity'] = PY['Extremity'].replace('M',0).apply(pd.to_numeric)
    
    
    #Ensure the DDE,LDE,SDE and Extremity values are treated as numerical data type
    PY['Total DDE'] = pd.to_numeric(PY['Total DDE'], errors='coerce')
    PY['Total LDE'] = pd.to_numeric(PY['Total LDE'], errors='coerce')
    PY['Total SDE'] = pd.to_numeric(PY['Total SDE'], errors='coerce')
    PY['Extremity'] = pd.to_numeric(PY['Extremity'], errors='coerce')
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Saving investigation levels as variables 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    #Equivalent to filtering an excel sheet according to certain column titles and saving 
    #those filtered excels as separate sheets.
    
    def Ivalue_extract(column_title, Code, dose_type):
        mask=(
            (I[column_title] == Code)
            )
        filtered_I= I.loc[mask, dose_type].iloc[0]
        return filtered_I
    
    I_XRA_DDE= Ivalue_extract("Subaccount Code", "XRA", "Total DDE")
    I_XRA_LDE= Ivalue_extract("Subaccount Code", "XRA", "Total LDE")
    I_XRA_Extremity= Ivalue_extract("Subaccount Code", "XRA", "Extremity")
    
    I_XRD_DDE = Ivalue_extract("Subaccount Code", "XRD", "Total DDE")
    I_XRD_LDE = Ivalue_extract("Subaccount Code", "XRD", "Total LDE")
    I_XRD_Extremity = Ivalue_extract("Subaccount Code", "XRD", "Extremity")
    
    I_XPE_DDE = Ivalue_extract("Subaccount Code", "XPE", "Total DDE")
    I_XPE_LDE = Ivalue_extract("Subaccount Code", "XPE", "Total LDE")
    I_XPE_Extremity = Ivalue_extract("Subaccount Code", "XPE", "Extremity")
    
    I_XDE_DDE = Ivalue_extract("Subaccount Code", "XDE", "Total DDE")
    
    I_XMA_DDE = Ivalue_extract("Subaccount Code", "XMA", "Total DDE")
    
    I_CAL_DDE = Ivalue_extract("Subaccount Code", "CAL", "Total DDE")
    
    I_SAL_DDE = Ivalue_extract("Subaccount Code", "SAL", "Total DDE")
    
    I_SWI_DDE = Ivalue_extract("Subaccount Code", "SWI", "Total DDE")
    
    I_RUH_DDE = Ivalue_extract("Subaccount Code", "RUH", "Total DDE")
    
    I_ASU_DDE = Ivalue_extract("Subaccount Code", "ASU", "Total DDE")
    I_ASU_LDE= Ivalue_extract("Subaccount Code", "ASU", "Total LDE")
    I_ASU_Extremity= Ivalue_extract("Subaccount Code", "ASU", "Extremity")
    
    I_NME_DDE = Ivalue_extract("Subaccount Code", "NME", "Total DDE")
    I_NME_Extremity= Ivalue_extract("Subaccount Code", "NME", "Extremity")
    
    I_500486_DDE = Ivalue_extract("Account", 500486, "Total DDE")
    I_500486_LDE= Ivalue_extract("Account", 500486, "Total LDE")
    I_500486_Extremity= Ivalue_extract("Account", 500486, "Extremity")
    
    I_501124_DDE = Ivalue_extract("Account", 501124, "Total DDE")
    I_501124_Extremity= Ivalue_extract("Account", 501124, "Extremity")
    
    I_RPH_DDE = Ivalue_extract("Subaccount Code", "RPH", "Total DDE")
    I_RPH_Extremity= Ivalue_extract("Subaccount Code", "RPH", "Extremity")
    
    I_500488_DDE =Ivalue_extract("Account", 500488, "Total DDE")
    
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Comparing landauer dose report with investigation Levels
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    
    #Equivalent to filtering an excel sheet according to certain column titles and saving 
    #those filtered excels as separate sheets. One of the filters is equivalent to filtering 
    # according to whether the displayed dose is above the investigation level
    
    def function(column_title, code, dosimeter_location, dose_type, IL_value):
        mask=(
            (R[column_title] == code)
            & (R['Monitoring Period'] != 'Lifetime')
            &(R[dose_type] >= IL_value)
            &(R['Dosimeter Location'] == dosimeter_location)
        )
        
        filtered_R=R.loc[mask, :]
        
        return filtered_R
    
    
    
    annual_XRA_Chest=function("Subaccount Code", "XRA", "Chest", "Total DDE",I_XRA_DDE)
    annual_XRA_Lens=function("Subaccount Code","XRA", "Lens of Eye", "Total LDE",I_XRA_LDE)
    annual_XRA_Collar=function("Subaccount Code","XRA", "Collar", "Total LDE",I_XRA_LDE)
    annual_XRA_LFing=function("Subaccount Code","XRA", "Left Finger", "Extremity",I_XRA_Extremity)
    annual_XRA_RFing=function("Subaccount Code","XRA", "Right Finger", "Extremity",I_XRA_Extremity)
    
    annual_XRD_Chest=function("Subaccount Code","XRD", "Chest", "Total DDE",I_XRD_DDE)
    annual_XRD_Lens=function("Subaccount Code","XRD", "Lens of Eye", "Total LDE",I_XRD_LDE)
    annual_XRD_Collar=function("Subaccount Code","XRD", "Collar", "Total LDE",I_XRD_LDE)
    annual_XRD_LFing=function("Subaccount Code","XRD", "Left Finger", "Extremity",I_XRD_Extremity)
    annual_XRD_RFing=function("Subaccount Code","XRD", "Right Finger", "Extremity",I_XRD_Extremity)
    
    annual_XDE_Chest=function("Subaccount Code","XDE", "Chest", "Total DDE",I_XDE_DDE)
    
    annual_XMA_Chest=function("Subaccount Code","XMA", "Chest", "Total DDE",I_XMA_DDE)
    
    annual_XPE_Chest=function("Subaccount Code","XPE", "Chest", "Total DDE",I_XPE_DDE)
    annual_XPE_Lens=function("Subaccount Code","XPE", "Lens of Eye", "Total LDE",I_XPE_LDE)
    annual_XPE_Collar=function("Subaccount Code","XPE", "Collar", "Total LDE",I_XPE_LDE)
    annual_XPE_LFing=function("Subaccount Code","XPE", "Left Finger", "Extremity",I_XPE_Extremity)
    annual_XPE_RFing=function("Subaccount Code","XPE", "Right Finger", "Extremity",I_XPE_Extremity)
    
    annual_SAL_Chest=function("Subaccount Code","SAL", "Chest", "Total DDE",I_SAL_DDE)
    
    annual_CAL_Chest=function("Subaccount Code","CAL", "Chest", "Total DDE",I_CAL_DDE)
    
    annual_SWI_Chest=function("Subaccount Code","SWI", "Chest", "Total DDE",I_SWI_DDE)
    
    annual_RUH_Chest=function("Subaccount Code","RUH", "Chest", "Total DDE",I_RUH_DDE)
    
    annual_ASU_Chest=function("Subaccount Code","ASU", "Chest", "Total DDE",I_ASU_DDE)
    annual_ASU_Lens=function("Subaccount Code","ASU", "Lens of Eye", "Total LDE",I_ASU_LDE)
    annual_ASU_Collar=function("Subaccount Code","ASU", "Collar", "Total LDE",I_ASU_LDE)
    annual_ASU_LFing=function("Subaccount Code","ASU", "Left Finger", "Extremity",I_ASU_Extremity)
    annual_ASU_RFing=function("Subaccount Code","ASU", "Right Finger", "Extremity",I_ASU_Extremity)
    
    annual_NME_Chest=function("Subaccount Code","NME", "Chest", "Total DDE",I_NME_DDE)
    annual_NME_LFing=function("Subaccount Code","NME", "Left Finger", "Extremity",I_NME_Extremity)
    annual_NME_RFing=function("Subaccount Code","NME", "Right Finger", "Extremity",I_NME_Extremity)
    
    annual_RPH_Chest=function("Subaccount Code","RPH", "Chest", "Total DDE",I_RPH_DDE)
    annual_RPH_LFing=function("Subaccount Code","RPH", "Left Finger", "Extremity",I_RPH_Extremity)
    annual_RPH_RFing=function("Subaccount Code","RPH", "Right Finger", "Extremity",I_RPH_Extremity)
    
    annual_500486_Chest=function("Account", 500486, "Chest", "Total DDE", I_500486_DDE)
    annual_500486_Lens=function("Account", 500486, "Lens of Eye", "Total LDE", I_500486_LDE)
    annual_500486_Collar=function("Account", 500486, "Collar", "Total LDE", I_500486_LDE)
    annual_500486_LFing=function("Account", 500486, "Left Finger", "Extremity", I_500486_Extremity)
    annual_500486_RFing=function("Account", 500486, "Right Finger", "Extremity", I_500486_Extremity)
    
    annual_501124_Chest=function("Account", 501124, "Chest", "Total DDE", I_501124_DDE)
    annual_501124_LFing=function("Account", 501124, "Chest", "Extremity", I_501124_Extremity)
    annual_501124_RFing=function("Account", 501124, "Chest", "Extremity", I_501124_Extremity)
    
    annual_500488_Chest=function("Account", 500488, "Chest", "Total DDE", I_500488_DDE)
    
    #Appending each filtered result to a new dataframe called 'annual_IL'
    annual_IL=pd.concat(
        [annual_XRA_Chest,
         annual_XRA_Lens,
         annual_XRA_Collar,
         annual_XRA_LFing,
         annual_XRA_RFing,
         annual_XRD_Chest,
         annual_XRD_Lens,
         annual_XRD_Collar,
         annual_XRD_LFing,
         annual_XRD_RFing,
         annual_XDE_Chest,
         annual_XMA_Chest,
         annual_XPE_Chest,
         annual_XPE_Lens,
         annual_XPE_Collar,
         annual_XPE_LFing,
         annual_XPE_RFing,
         annual_SAL_Chest,
         annual_CAL_Chest,
         annual_SWI_Chest,
         annual_RUH_Chest,
         annual_ASU_Chest,
         annual_ASU_Lens,
         annual_ASU_Collar,
         annual_ASU_LFing,
         annual_ASU_RFing,
         annual_NME_Chest,
         annual_NME_LFing,
         annual_NME_RFing,
         annual_RPH_Chest,
         annual_RPH_LFing,
         annual_RPH_RFing,
         annual_500486_Chest,
         annual_500486_LFing,
         annual_500486_RFing,
         annual_500486_Lens,
         annual_500486_Collar,
         annual_501124_Chest,
         annual_501124_LFing,
         annual_501124_RFing,
         annual_500488_Chest
         ]
        )
    
    #Converts dataframe to excel and saves it in below filepath with file name given below
    annual_IL.to_csv(annual_report_savelocation, encoding='utf-8', index=False)
    
    
    
    def function2(column_title, code, dosimeter_location, dose_type, IL_value):
        mask=(
            (R[column_title] == code)
            & (R['Monitoring Period'] != 'Lifetime')
            &(R[dose_type] >= IL_value/2)
            &(R['Dosimeter Location'] == dosimeter_location)
        )
        
        filtered_R=R.loc[mask, :]
        
        return filtered_R
    
    
    
    annual_XRA_Chest=function2("Subaccount Code", "XRA", "Chest", "Total DDE",I_XRA_DDE)
    annual_XRA_Lens=function2("Subaccount Code","XRA", "Lens of Eye", "Total LDE",I_XRA_LDE)
    annual_XRA_Collar=function2("Subaccount Code","XRA", "Collar", "Total LDE",I_XRA_LDE)
    annual_XRA_LFing=function2("Subaccount Code","XRA", "Left Finger", "Extremity",I_XRA_Extremity)
    annual_XRA_RFing=function2("Subaccount Code","XRA", "Right Finger", "Extremity",I_XRA_Extremity)
    
    annual_XRD_Chest=function2("Subaccount Code","XRD", "Chest", "Total DDE",I_XRD_DDE)
    annual_XRD_Lens=function2("Subaccount Code","XRD", "Lens of Eye", "Total LDE",I_XRD_LDE)
    annual_XRD_Collar=function2("Subaccount Code","XRD", "Collar", "Total LDE",I_XRD_LDE)
    annual_XRD_LFing=function2("Subaccount Code","XRD", "Left Finger", "Extremity",I_XRD_Extremity)
    annual_XRD_RFing=function2("Subaccount Code","XRD", "Right Finger", "Extremity",I_XRD_Extremity)
    
    annual_XDE_Chest=function2("Subaccount Code","XDE", "Chest", "Total DDE",I_XDE_DDE)
    
    annual_XMA_Chest=function2("Subaccount Code","XMA", "Chest", "Total DDE",I_XMA_DDE)
    
    annual_XPE_Chest=function2("Subaccount Code","XPE", "Chest", "Total DDE",I_XPE_DDE)
    annual_XPE_Lens=function2("Subaccount Code","XPE", "Lens of Eye", "Total LDE",I_XPE_LDE)
    annual_XPE_Collar=function2("Subaccount Code","XPE", "Collar", "Total LDE",I_XPE_LDE)
    annual_XPE_LFing=function2("Subaccount Code","XPE", "Left Finger", "Extremity",I_XPE_Extremity)
    annual_XPE_RFing=function2("Subaccount Code","XPE", "Right Finger", "Extremity",I_XPE_Extremity)
    
    annual_SAL_Chest=function2("Subaccount Code","SAL", "Chest", "Total DDE",I_SAL_DDE)
    
    annual_CAL_Chest=function2("Subaccount Code","CAL", "Chest", "Total DDE",I_CAL_DDE)
    
    annual_SWI_Chest=function2("Subaccount Code","SWI", "Chest", "Total DDE",I_SWI_DDE)
    
    annual_RUH_Chest=function2("Subaccount Code","RUH", "Chest", "Total DDE",I_RUH_DDE)
    
    annual_ASU_Chest=function2("Subaccount Code","ASU", "Chest", "Total DDE",I_ASU_DDE)
    annual_ASU_Lens=function2("Subaccount Code","ASU", "Lens of Eye", "Total LDE",I_ASU_LDE)
    annual_ASU_Collar=function2("Subaccount Code","ASU", "Collar", "Total LDE",I_ASU_LDE)
    annual_ASU_LFing=function2("Subaccount Code","ASU", "Left Finger", "Extremity",I_ASU_Extremity)
    annual_ASU_RFing=function2("Subaccount Code","ASU", "Right Finger", "Extremity",I_ASU_Extremity)
    
    annual_NME_Chest=function2("Subaccount Code","NME", "Chest", "Total DDE",I_NME_DDE)
    annual_NME_LFing=function2("Subaccount Code","NME", "Left Finger", "Extremity",I_NME_Extremity)
    annual_NME_RFing=function2("Subaccount Code","NME", "Right Finger", "Extremity",I_NME_Extremity)
    
    annual_RPH_Chest=function2("Subaccount Code","RPH", "Chest", "Total DDE",I_RPH_DDE)
    annual_RPH_LFing=function2("Subaccount Code","RPH", "Left Finger", "Extremity",I_RPH_Extremity)
    annual_RPH_RFing=function2("Subaccount Code","RPH", "Right Finger", "Extremity",I_RPH_Extremity)
    
    annual_500486_Chest=function2("Account", 500486, "Chest", "Total DDE", I_500486_DDE)
    annual_500486_Lens=function2("Account", 500486, "Lens of Eye", "Total LDE", I_500486_LDE)
    annual_500486_Collar=function2("Account", 500486, "Collar", "Total LDE", I_500486_LDE)
    annual_500486_LFing=function2("Account", 500486, "Left Finger", "Extremity", I_500486_Extremity)
    annual_500486_RFing=function2("Account", 500486, "Right Finger", "Extremity", I_500486_Extremity)
    
    annual_501124_Chest=function2("Account", 501124, "Chest", "Total DDE", I_501124_DDE)
    annual_501124_LFing=function2("Account", 501124, "Chest", "Extremity", I_501124_Extremity)
    annual_501124_RFing=function2("Account", 501124, "Chest", "Extremity", I_501124_Extremity)
    
    annual_500488_Chest=function2("Account", 500488, "Chest", "Total DDE", I_500488_DDE)
    
    #Appending each filtered result to a new dataframe 
    prewarning_IL=pd.concat(
        [annual_XRA_Chest,
         annual_XRA_Lens,
         annual_XRA_Collar,
         annual_XRA_LFing,
         annual_XRA_RFing,
         annual_XRD_Chest,
         annual_XRD_Lens,
         annual_XRD_Collar,
         annual_XRD_LFing,
         annual_XRD_RFing,
         annual_XDE_Chest,
         annual_XMA_Chest,
         annual_XPE_Chest,
         annual_XPE_Lens,
         annual_XPE_Collar,
         annual_XPE_LFing,
         annual_XPE_RFing,
         annual_SAL_Chest,
         annual_CAL_Chest,
         annual_SWI_Chest,
         annual_RUH_Chest,
         annual_ASU_Chest,
         annual_ASU_Lens,
         annual_ASU_Collar,
         annual_ASU_LFing,
         annual_ASU_RFing,
         annual_NME_Chest,
         annual_NME_LFing,
         annual_NME_RFing,
         annual_RPH_Chest,
         annual_RPH_LFing,
         annual_RPH_RFing,
         annual_500486_Chest,
         annual_500486_LFing,
         annual_500486_RFing,
         annual_500486_Lens,
         annual_500486_Collar,
         annual_501124_Chest,
         annual_501124_LFing,
         annual_501124_RFing,
         annual_500488_Chest
         ]
        )
    
    #Converts dataframe to excel and saves it in below filepath with file name given below
    prewarning_IL.to_csv(prewarning_report_savelocation, encoding='utf-8', index=False)
    
    
    def function3(column_title, code, dosimeter_location, dose_type, IL_value):
        mask=(
            (PY[column_title] == code)
            & (PY['Monitoring Period'] != 'Lifetime')
            &(PY[dose_type] >= IL_value)
            &(PY['Dosimeter Location'] == dosimeter_location)
        )
        
        filtered_PY=PY.loc[mask, :]
        
        return filtered_PY
    
    
    
    annual_XRA_Chest=function3("Subaccount Code", "XRA", "Chest", "Total DDE",I_XRA_DDE)
    annual_XRA_Lens=function3("Subaccount Code","XRA", "Lens of Eye", "Total LDE",I_XRA_LDE)
    annual_XRA_Collar=function3("Subaccount Code","XRA", "Collar", "Total LDE",I_XRA_LDE)
    annual_XRA_LFing=function3("Subaccount Code","XRA", "Left Finger", "Extremity",I_XRA_Extremity)
    annual_XRA_RFing=function3("Subaccount Code","XRA", "Right Finger", "Extremity",I_XRA_Extremity)
    
    annual_XRD_Chest=function3("Subaccount Code","XRD", "Chest", "Total DDE",I_XRD_DDE)
    annual_XRD_Lens=function3("Subaccount Code","XRD", "Lens of Eye", "Total LDE",I_XRD_LDE)
    annual_XRD_Collar=function3("Subaccount Code","XRD", "Collar", "Total LDE",I_XRD_LDE)
    annual_XRD_LFing=function3("Subaccount Code","XRD", "Left Finger", "Extremity",I_XRD_Extremity)
    annual_XRD_RFing=function3("Subaccount Code","XRD", "Right Finger", "Extremity",I_XRD_Extremity)
    
    annual_XDE_Chest=function3("Subaccount Code","XDE", "Chest", "Total DDE",I_XDE_DDE)
    
    annual_XMA_Chest=function3("Subaccount Code","XMA", "Chest", "Total DDE",I_XMA_DDE)
    
    annual_XPE_Chest=function3("Subaccount Code","XPE", "Chest", "Total DDE",I_XPE_DDE)
    annual_XPE_Lens=function3("Subaccount Code","XPE", "Lens of Eye", "Total LDE",I_XPE_LDE)
    annual_XPE_Collar=function3("Subaccount Code","XPE", "Collar", "Total LDE",I_XPE_LDE)
    annual_XPE_LFing=function3("Subaccount Code","XPE", "Left Finger", "Extremity",I_XPE_Extremity)
    annual_XPE_RFing=function3("Subaccount Code","XPE", "Right Finger", "Extremity",I_XPE_Extremity)
    
    annual_SAL_Chest=function3("Subaccount Code","SAL", "Chest", "Total DDE",I_SAL_DDE)
    
    annual_CAL_Chest=function3("Subaccount Code","CAL", "Chest", "Total DDE",I_CAL_DDE)
    
    annual_SWI_Chest=function3("Subaccount Code","SWI", "Chest", "Total DDE",I_SWI_DDE)
    
    annual_RUH_Chest=function3("Subaccount Code","RUH", "Chest", "Total DDE",I_RUH_DDE)
    
    annual_ASU_Chest=function3("Subaccount Code","ASU", "Chest", "Total DDE",I_ASU_DDE)
    annual_ASU_Lens=function3("Subaccount Code","ASU", "Lens of Eye", "Total LDE",I_ASU_LDE)
    annual_ASU_Collar=function3("Subaccount Code","ASU", "Collar", "Total LDE",I_ASU_LDE)
    annual_ASU_LFing=function3("Subaccount Code","ASU", "Left Finger", "Extremity",I_ASU_Extremity)
    annual_ASU_RFing=function3("Subaccount Code","ASU", "Right Finger", "Extremity",I_ASU_Extremity)
    
    annual_NME_Chest=function3("Subaccount Code","NME", "Chest", "Total DDE",I_NME_DDE)
    annual_NME_LFing=function3("Subaccount Code","NME", "Left Finger", "Extremity",I_NME_Extremity)
    annual_NME_RFing=function3("Subaccount Code","NME", "Right Finger", "Extremity",I_NME_Extremity)
    
    annual_RPH_Chest=function3("Subaccount Code","RPH", "Chest", "Total DDE",I_RPH_DDE)
    annual_RPH_LFing=function3("Subaccount Code","RPH", "Left Finger", "Extremity",I_RPH_Extremity)
    annual_RPH_RFing=function3("Subaccount Code","RPH", "Right Finger", "Extremity",I_RPH_Extremity)
    
    annual_500486_Chest=function3("Account", 500486, "Chest", "Total DDE", I_500486_DDE)
    annual_500486_Lens=function3("Account", 500486, "Lens of Eye", "Total LDE", I_500486_LDE)
    annual_500486_Collar=function3("Account", 500486, "Collar", "Total LDE", I_500486_LDE)
    annual_500486_LFing=function3("Account", 500486, "Left Finger", "Extremity", I_500486_Extremity)
    annual_500486_RFing=function3("Account", 500486, "Right Finger", "Extremity", I_500486_Extremity)
    
    annual_501124_Chest=function3("Account", 501124, "Chest", "Total DDE", I_501124_DDE)
    annual_501124_LFing=function3("Account", 501124, "Chest", "Extremity", I_501124_Extremity)
    annual_501124_RFing=function3("Account", 501124, "Chest", "Extremity", I_501124_Extremity)
    
    annual_500488_Chest=function3("Account", 500488, "Chest", "Total DDE", I_500488_DDE)
    
    previousyear_IL=pd.concat(
        [annual_XRA_Chest,
         annual_XRA_Lens,
         annual_XRA_Collar,
         annual_XRA_LFing,
         annual_XRA_RFing,
         annual_XRD_Chest,
         annual_XRD_Lens,
         annual_XRD_Collar,
         annual_XRD_LFing,
         annual_XRD_RFing,
         annual_XDE_Chest,
         annual_XMA_Chest,
         annual_XPE_Chest,
         annual_XPE_Lens,
         annual_XPE_Collar,
         annual_XPE_LFing,
         annual_XPE_RFing,
         annual_SAL_Chest,
         annual_CAL_Chest,
         annual_SWI_Chest,
         annual_RUH_Chest,
         annual_ASU_Chest,
         annual_ASU_Lens,
         annual_ASU_Collar,
         annual_ASU_LFing,
         annual_ASU_RFing,
         annual_NME_Chest,
         annual_NME_LFing,
         annual_NME_RFing,
         annual_RPH_Chest,
         annual_RPH_LFing,
         annual_RPH_RFing,
         annual_500486_Chest,
         annual_500486_LFing,
         annual_500486_RFing,
         annual_500486_Lens,
         annual_500486_Collar,
         annual_501124_Chest,
         annual_501124_LFing,
         annual_501124_RFing,
         annual_500488_Chest
         ]
        )
    previousyear_IL.to_csv(previousyear_report_savelocation, encoding='utf-8', index=False)
    
    return()
    

    
