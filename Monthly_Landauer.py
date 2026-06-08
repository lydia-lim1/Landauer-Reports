"""
Script to automate comparing Landauer badge results to their respective
annual investigation levels 
"""

def monthly_landauer_check(
        path_M500070,
        path_M501124,
        path_M500499,
        path_M500488,
        path_M500486,
        path_M500484,
        wearperiod_investigation_levels,
        monthlyreport_location):

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Loading & Pre-prepping data
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Load investigation level excel as a dataframe called 'I'
    I=pd.read_excel(wearperiod_investigation_levels)
    
    
    #Load Landauer dose reports into a single dataframe called 'R'
    M500070 = pd.read_excel(path_M500070)
    M501124 = pd.read_excel(path_M501124)
    M500499= pd.read_excel(path_M500499)
    M500486= pd.read_excel(path_M500486)
    M500484= pd.read_excel(path_M500484)
    M500488=pd.read_excel(path_M500488)
    
    R= pd.concat([M500070, M501124, M500499, M500486, M500484, M500488])
    
    
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
    
    
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Saving investigation levels as variables 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    #Equivalent to filtering an excel sheet according to certain column titles and saving 
    #those filtered excels as separate sheets.
    
    
    def Ivalue_extract(column_title, Code, dose_type, badge_frequency):
        mask=(
            (I[column_title] == Code)
            &(I["Frequency"] == badge_frequency)
            )
        filtered_I= I.loc[mask, dose_type].iloc[0]
        
        return filtered_I
    
    I_XRA_DDE= Ivalue_extract("Subaccount Code", "XRA", "Total DDE", "Monthly")
    I_XRA_LDE= Ivalue_extract("Subaccount Code", "XRA", "Total LDE", "Monthly")
    I_XRA_Extremity= Ivalue_extract("Subaccount Code", "XRA", "Extremity", "Monthly")
    
    I_XRA_DDE_quart= Ivalue_extract("Subaccount Code", "XRA", "Total DDE", "Quarterly")
    
    I_XRD_DDE = Ivalue_extract("Subaccount Code", "XRD", "Total DDE", "Monthly")
    I_XRD_LDE = Ivalue_extract("Subaccount Code", "XRD", "Total LDE", "Monthly")
    I_XRD_Extremity = Ivalue_extract("Subaccount Code", "XRD", "Extremity", "Monthly")
    
    I_XRD_DDE_quart = Ivalue_extract("Subaccount Code", "XRD", "Total DDE", "Quarterly")
    
    I_XPE_DDE = Ivalue_extract("Subaccount Code", "XPE", "Total DDE", "Monthly")
    I_XPE_LDE = Ivalue_extract("Subaccount Code", "XPE", "Total LDE", "Monthly")
    I_XPE_Extremity = Ivalue_extract("Subaccount Code", "XPE", "Extremity", "Monthly")
    
    I_XDE_DDE = Ivalue_extract("Subaccount Code", "XDE", "Total DDE", "Quarterly")
    
    I_XMA_DDE = Ivalue_extract("Subaccount Code", "XMA", "Total DDE", "Quarterly")
    
    I_CAL_DDE = Ivalue_extract("Subaccount Code", "CAL", "Total DDE", "Quarterly")
    
    I_SAL_DDE = Ivalue_extract("Subaccount Code", "SAL", "Total DDE", "Quarterly")
    
    I_SWI_DDE = Ivalue_extract("Subaccount Code", "SWI", "Total DDE", "Quarterly")
    
    
    I_ASU_DDE = Ivalue_extract("Subaccount Code", "ASU", "Total DDE", "Monthly")
    I_ASU_LDE= Ivalue_extract("Subaccount Code", "ASU", "Total LDE", "Monthly")
    I_ASU_Extremity= Ivalue_extract("Subaccount Code", "ASU", "Extremity", "Monthly")
    
    I_NME_DDE = Ivalue_extract("Subaccount Code", "NME", "Total DDE", "Monthly")
    I_NME_Extremity= Ivalue_extract("Subaccount Code", "NME", "Extremity", "Monthly")
    
    I_500486_DDE = Ivalue_extract("Account", 500486, "Total DDE", "Monthly")
    I_500486_LDE= Ivalue_extract("Account", 500486, "Total LDE", "Monthly")
    I_500486_Extremity= Ivalue_extract("Account", 500486, "Extremity", "Monthly")
    
    I_501124_DDE = Ivalue_extract("Account", 501124, "Total DDE", "Monthly")
    I_501124_LDE= Ivalue_extract("Account", 501124, "Total LDE", "Monthly")
    I_501124_Extremity= Ivalue_extract("Account", 501124, "Extremity", "Monthly")
    
    I_RPH_DDE = Ivalue_extract("Subaccount Code", "RPH", "Total DDE", "Quarterly")
    I_RPH_Extremity= Ivalue_extract("Subaccount Code", "RPH", "Extremity", "Quarterly")
    
    
    I_500488_DDE = Ivalue_extract("Account", 500488, "Total DDE", "Quarterly")
    
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Comparing landauer dose report with investigation Levels
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    
    #Equivalent to filtering an excel sheet according to certain column titles and saving 
    #those filtered excels as separate sheets. One of the filters is equivalent to filtering 
    # according to whether the displayed dose is above the investigation level
    
    def function(column_title, code, dosimeter_location, dose_type, IL_value, badge_frequency):
        mask=(
            (R[column_title] == code)
            &(R[dose_type] >= IL_value)
            &(R["Frequency"] == badge_frequency)
            &(R['Dosimeter Location'] == dosimeter_location)
        )
        
        filtered_R=R.loc[mask, :]
        
        return filtered_R
    
    
    
    XRA_Chest=function("Subaccount Code", "XRA", "Chest", "Total DDE",I_XRA_DDE, "Monthly")
    XRA_Lens=function("Subaccount Code","XRA", "Lens of Eye", "Total LDE",I_XRA_LDE, "Monthly")
    XRA_Collar=function("Subaccount Code","XRA", "Collar", "Total LDE",I_XRA_LDE, "Monthly")
    XRA_LFing=function("Subaccount Code","XRA", "Left Finger", "Extremity",I_XRA_Extremity, "Monthly")
    XRA_RFing=function("Subaccount Code","XRA", "Right Finger", "Extremity",I_XRA_Extremity, "Monthly")
    
    XRA_Chest_quart=function("Subaccount Code", "XRA", "Chest", "Total DDE",I_XRA_DDE_quart, "Quarterly")
    
    XRD_Chest=function("Subaccount Code","XRD", "Chest", "Total DDE",I_XRD_DDE, "Monthly")
    XRD_Lens=function("Subaccount Code","XRD", "Lens of Eye", "Total LDE",I_XRD_LDE, "Monthly")
    XRD_Collar=function("Subaccount Code","XRD", "Collar", "Total LDE",I_XRD_LDE, "Monthly")
    XRD_LFing=function("Subaccount Code","XRD", "Left Finger", "Extremity",I_XRD_Extremity, "Monthly")
    XRD_RFing=function("Subaccount Code","XRD", "Right Finger", "Extremity",I_XRD_Extremity, "Monthly")
    
    XRD_Chest_quart=function("Subaccount Code","XRD", "Chest", "Total DDE",I_XRD_DDE_quart, "Monthly")
    
    XDE_Chest=function("Subaccount Code","XDE", "Chest", "Total DDE",I_XDE_DDE, "Quarterly")
    
    XMA_Chest=function("Subaccount Code","XMA", "Chest", "Total DDE",I_XMA_DDE, "Quarterly")
    
    XPE_Chest=function("Subaccount Code","XPE", "Chest", "Total DDE",I_XPE_DDE, "Monthly")
    XPE_Lens=function("Subaccount Code","XPE", "Lens of Eye", "Total LDE",I_XPE_LDE, "Monthly")
    XPE_Collar=function("Subaccount Code","XPE", "Collar", "Total LDE",I_XPE_LDE, "Monthly")
    XPE_LFing=function("Subaccount Code","XPE", "Left Finger", "Extremity",I_XPE_Extremity, "Monthly")
    XPE_RFing=function("Subaccount Code","XPE", "Right Finger", "Extremity",I_XPE_Extremity, "Monthly")
    
    SAL_Chest=function("Subaccount Code","SAL", "Chest", "Total DDE",I_SAL_DDE, "Quarterly")
    
    CAL_Chest=function("Subaccount Code","CAL", "Chest", "Total DDE",I_CAL_DDE, "Quarterly")
    
    SWI_Chest=function("Subaccount Code","SWI", "Chest", "Total DDE",I_SWI_DDE, "Quarterly")
    
    ASU_Chest=function("Subaccount Code","ASU", "Chest", "Total DDE",I_ASU_DDE, "Monthly")
    ASU_Lens=function("Subaccount Code","ASU", "Lens of Eye", "Total LDE",I_ASU_LDE, "Monthly")
    ASU_Collar=function("Subaccount Code","ASU", "Collar", "Total LDE",I_ASU_LDE, "Monthly")
    ASU_LFing=function("Subaccount Code","ASU", "Left Finger", "Extremity",I_ASU_Extremity, "Monthly")
    ASU_RFing=function("Subaccount Code","ASU", "Right Finger", "Extremity",I_ASU_Extremity, "Monthly")
    
    NME_Chest=function("Subaccount Code","NME", "Chest", "Total DDE",I_NME_DDE, "Monthly")
    NME_LFing=function("Subaccount Code","NME", "Left Finger", "Extremity",I_NME_Extremity, "Monthly")
    NME_RFing=function("Subaccount Code","NME", "Right Finger", "Extremity",I_NME_Extremity, "Monthly")
    
    RPH_Chest=function("Subaccount Code","RPH", "Chest", "Total DDE",I_RPH_DDE, "Quarterly")
    RPH_LFing=function("Subaccount Code","RPH", "Left Finger", "Extremity",I_RPH_Extremity, "Quarterly")
    RPH_RFing=function("Subaccount Code","RPH", "Right Finger", "Extremity",I_RPH_Extremity, "Quarterly")
    
    M500486_Chest=function("Account", 500486, "Chest", "Total DDE", I_500486_DDE, "Monthly")
    M500486_Lens=function("Account", 500486, "Lens of Eye", "Total LDE", I_500486_LDE, "Monthly")
    M500486_Collar=function("Account", 500486, "Collar", "Total LDE", I_500486_LDE, "Monthly")
    M500486_LFing=function("Account", 500486, "Left Finger", "Extremity", I_500486_Extremity, "Monthly")
    M500486_RFing=function("Account", 500486, "Right Finger", "Extremity", I_500486_Extremity, "Monthly")
    
    M501124_Chest=function("Account", 501124, "Chest", "Total DDE", I_501124_DDE, "Monthly")
    M501124_LFing=function("Account", 501124, "Chest", "Extremity", I_501124_Extremity, "Monthly")
    M501124_Lens=function("Account", 501124, "Chest", "Total LDE", I_501124_LDE, "Monthly")
    M501124_RFing=function("Account", 501124, "Chest", "Extremity", I_501124_Extremity, "Monthly")
    
    M500488_Chest=function("Account", 500488, "Chest", "Total DDE", I_500488_DDE, "Quarterly")
    
    
    
    #Appending each filtered result to a new dataframe called 'annual_IL'
    wearperiod_IL=pd.concat(
        [XRA_Chest,
         XRA_Lens,
         XRA_Collar,
         XRA_LFing,
         XRA_RFing,
         XRA_Chest_quart,
         XRD_Chest,
         XRD_Lens,
         XRD_Collar,
         XRD_LFing,
         XRD_RFing,
         XRD_Chest_quart,
         XDE_Chest,
         XMA_Chest,
         XPE_Chest,
         XPE_Lens,
         XPE_Collar,
         XPE_LFing,
         XPE_RFing,
         SAL_Chest,
         CAL_Chest,
         SWI_Chest,
         ASU_Chest,
         ASU_Lens,
         ASU_Collar,
         ASU_LFing,
         ASU_RFing,
         NME_Chest,
         NME_LFing,
         NME_RFing,
         RPH_Chest,
         RPH_LFing,
         RPH_RFing,
         M500486_Chest,
         M500486_Lens,
         M500486_Collar,
         M500486_LFing,
         M500486_RFing,
         M501124_Chest,
         M501124_LFing,
         M501124_RFing,
         M501124_Lens,
         M500488_Chest
         ]
        )
    
    
    
    #Converts dataframe to excel and saves it in below filepath with file name given below
    wearperiod_IL.to_csv(monthlyreport_location, encoding='utf-8', index=False)
    
    
    return()


