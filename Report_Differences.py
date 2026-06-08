import pandas as pd

def compare_reports(previous_month, current_month, comparison_file, wearperiod_investigation_levels):
    
    previous=pd.read_csv(previous_month)
    current=pd.read_csv(current_month)
    current = current.drop_duplicates()
    previous = previous.drop_duplicates()
    
    combined = pd.concat([previous, current])
    combined = combined.reset_index(drop=True)
    combined_gpby = combined.groupby(list(combined.columns))
    idx = [x[0] for x in combined_gpby.groups.values() if len(x) == 1]
    output= combined.reindex(idx)

    
    #Removing unecessary columns to reclutter resultant sheet
    columns_to_drop=[
        "Total Neutron", 
        "Customer Reference", 
        "Dosimeter Type", 
        "Fast Neutron", 
        "Thermal Neutron",
        "Not Accumulated",
        "State",
        "Not In Assigned Dose"]
    
    output = output.drop(columns=columns_to_drop, errors="ignore")
    
    output.insert(12, "Dose Investigation Level (mSv)", "")
    
    
    I=pd.read_excel(wearperiod_investigation_levels)
    
     
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
    
    
    
    def set_il(output, column_title, code, dosimeter, badge_frequency, il_value):
        mask = (
            (output[column_title] == code) &
            (output["Dosimeter Location"] == dosimeter) &
            (output["Frequency"] == badge_frequency)
        )
        if mask.any():
            output.loc[mask, "Dose Investigation Level (mSv)"] = il_value
        return output
    
    output = set_il(output, "Subaccount Code", "XRA", "Chest", "Monthly",    I_XRA_DDE)
    output = set_il(output, "Subaccount Code", "XRA", "Lens of Eye", "Monthly",    I_XRA_LDE)
    output = set_il(output, "Subaccount Code", "XRA", "Left Finger",  "Monthly",    I_XRA_Extremity)
    output = set_il(output, "Subaccount Code", "XRA", "Right Finger",  "Monthly",    I_XRA_Extremity)
    output = set_il(output, "Subaccount Code", "XRA", "Chest", "Quarterly",  I_XRA_DDE_quart)
    
    output = set_il(output, "Subaccount Code", "XRD", "Chest", "Monthly",    I_XRD_DDE)
    output = set_il(output, "Subaccount Code", "XRD", "Lens of Eye", "Monthly",    I_XRD_LDE)         
    output = set_il(output, "Subaccount Code", "XRD", "Left Finger",  "Monthly",    I_XRD_Extremity)
    output = set_il(output, "Subaccount Code", "XRD", "Right Finger",  "Monthly",    I_XRD_Extremity)
    output = set_il(output, "Subaccount Code", "XRD", "Chest", "Quarterly",  I_XRD_DDE_quart)
    
    output = set_il(output, "Subaccount Code", "XPE", "Chest", "Monthly",    I_XPE_DDE)
    output = set_il(output, "Subaccount Code", "XPE", "Lens of Eye", "Monthly",    I_XPE_LDE)        
    output = set_il(output, "Subaccount Code", "XPE", "Right Finger",  "Monthly",    I_XPE_Extremity)
    output = set_il(output, "Subaccount Code", "XPE", "Left Finger",  "Monthly",    I_XPE_Extremity)
    
    output = set_il(output, "Subaccount Code", "XDE", "Chest", "Quarterly",  I_XDE_DDE)
    output = set_il(output, "Subaccount Code", "XMA", "Chest", "Quarterly",  I_XMA_DDE)
    output = set_il(output, "Subaccount Code", "CAL", "Chest", "Quarterly",  I_CAL_DDE)
    output = set_il(output, "Subaccount Code", "SAL", "Chest", "Quarterly",  I_SAL_DDE)
    output = set_il(output, "Subaccount Code", "SWI", "Chest", "Quarterly",  I_SWI_DDE)
    
    output = set_il(output, "Subaccount Code", "ASU", "Chest", "Monthly",    I_ASU_DDE)
    output = set_il(output, "Subaccount Code", "ASU", "Lens of Eye", "Monthly",    I_ASU_LDE)        
    output = set_il(output, "Subaccount Code", "ASU", "Right Finger",  "Monthly",    I_ASU_Extremity)
    output = set_il(output, "Subaccount Code", "ASU", "Left Finger",  "Monthly",    I_ASU_Extremity)
    
    output = set_il(output, "Subaccount Code", "NME", "Chest", "Monthly",    I_NME_DDE)
    output = set_il(output, "Subaccount Code", "NME", "Right Finger",  "Monthly",    I_NME_Extremity)
    output = set_il(output, "Subaccount Code", "NME", "Left Finger",  "Monthly",    I_NME_Extremity)
    
    output = set_il(output, "Account", 500486, "Chest", "Monthly",   I_500486_DDE)
    output = set_il(output, "Account", 500486, "Lens of eye", "Monthly",   I_500486_LDE)      
    output = set_il(output, "Account", 500486, "Right Finger",  "Monthly",   I_500486_Extremity)
    output = set_il(output, "Account", 500486, "Left Finger",  "Monthly",   I_500486_Extremity)
    
    output = set_il(output, "Account", 501124, "Chest", "Monthly",   I_501124_DDE)
    output = set_il(output, "Account", 501124, "Lens of Eye", "Monthly",   I_501124_LDE)       
    output = set_il(output, "Account", 501124, "Right Finger",  "Monthly",   I_501124_Extremity)
    output = set_il(output, "Account", 501124, "Left Finger",  "Monthly",   I_501124_Extremity)
    
    output = set_il(output, "Subaccount Code", "RPH", "Chest", "Quarterly",  I_RPH_DDE)
    output = set_il(output, "Subaccount Code", "RPH", "Right Finger",  "Quarterly",  I_RPH_Extremity)
    output = set_il(output, "Subaccount Code", "RPH", "Left Finger",  "Quarterly",  I_RPH_Extremity)
    
    output = set_il(output, "Account", 500488, "Chest", "Quarterly", I_500488_DDE)

    
        
    output.to_csv(comparison_file, encoding='utf-8', index=False)
        
        
    return()

