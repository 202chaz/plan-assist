import pandas as pd
import numpy as np

def get_plans(file):
  my_file = file
  workbook = pd.ExcelFile(my_file)
  sheets = workbook.sheet_names
  plans_arr = []

  for sheet in sheets:
    # get the cost share sheets
    if 'Cost' in sheet:
      plan_names = pd.read_excel(my_file, sheet_name=sheet, skiprows=[0,1], usecols=["Plan Variant Marketing Name*", "HIOS Plan ID\n(Standard Component + Variant)"])

      for plan in plan_names.values:
        # Only get plans that end in -01
        if plan[0] and '01' in plan[0].split("-")[1]:
          plans_arr.append({'key': plan[0], 'name': plan[1], 'sheet': sheet})

  return plans_arr

def get_plan(content, plan_name, sheet_name):
  arr = []
  df = pd.read_excel(content, sheet_name=sheet_name)
  # Primary Care Visit to Treat an Injury or Illness
  key_start = df.columns.get_loc("Primary Care Visit to Treat an Injury or Illness")
  key_end = df.columns.get_loc("Specialist Visit")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Primary Care Visit to Treat an Injury or Illness', 'data': sub_categories})
  
  # Specialist Visit
  key_start = df.columns.get_loc("Specialist Visit")
  key_end = df.columns.get_loc("Other Practitioner Office Visit (Nurse, Physician Assistant)")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Specialist Visit', 'data': sub_categories})
  
  # Other Practitioner Office Visit (Nurse, Physician Assistant)
  key_start = df.columns.get_loc("Other Practitioner Office Visit (Nurse, Physician Assistant)")
  key_end = df.columns.get_loc("Outpatient Facility Fee (e.g., Ambulatory Surgery Center)")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Other Practitioner Office Visit (Nurse, Physician Assistant)', 'data': sub_categories})
  
  # Outpatient Facility Fee (e.g., Ambulatory Surgery Center)
  key_start = df.columns.get_loc("Outpatient Facility Fee (e.g., Ambulatory Surgery Center)")
  key_end = df.columns.get_loc("Outpatient Surgery Physician/Surgical Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Outpatient Facility Fee (e.g., Ambulatory Surgery Center)', 'data': sub_categories})
  
  # Outpatient Surgery Physician/Surgical Services
  key_start = df.columns.get_loc("Outpatient Surgery Physician/Surgical Services")
  key_end = df.columns.get_loc("Hospice Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Outpatient Surgery Physician/Surgical Services', 'data': sub_categories})
  
  # Hospice Services
  key_start = df.columns.get_loc("Hospice Services")
  key_end = df.columns.get_loc("Urgent Care Centers or Facilities")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Hospice Services', 'data': sub_categories})
  
  # Urgent Care Centers or Facilities
  key_start = df.columns.get_loc("Urgent Care Centers or Facilities")
  key_end = df.columns.get_loc("Home Health Care Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Urgent Care Centers or Facilities', 'data': sub_categories})
  
  # Home Health Care Services
  key_start = df.columns.get_loc("Home Health Care Services")
  key_end = df.columns.get_loc("Emergency Room Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Home Health Care Services', 'data': sub_categories})
  
  # Emergency Room Services
  key_start = df.columns.get_loc("Emergency Room Services")
  key_end = df.columns.get_loc("Emergency Transportation/Ambulance")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Emergency Room Services', 'data': sub_categories})
  
  # Emergency Transportation/Ambulance
  key_start = df.columns.get_loc("Emergency Transportation/Ambulance")
  key_end = df.columns.get_loc("Inpatient Hospital Services (e.g., Hospital Stay)")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Emergency Transportation/Ambulance', 'data': sub_categories})
  
  # Inpatient Hospital Services (e.g., Hospital Stay)
  key_start = df.columns.get_loc("Inpatient Hospital Services (e.g., Hospital Stay)")
  key_end = df.columns.get_loc("Inpatient Physician and Surgical Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Inpatient Hospital Services (e.g., Hospital Stay)', 'data': sub_categories})
  
  # Inpatient Physician and Surgical Services
  key_start = df.columns.get_loc("Inpatient Physician and Surgical Services")
  key_end = df.columns.get_loc("Skilled Nursing Facility")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Inpatient Physician and Surgical Services', 'data': sub_categories})
  
  # Skilled Nursing Facility
  key_start = df.columns.get_loc("Skilled Nursing Facility")
  key_end = df.columns.get_loc("Prenatal and Postnatal Care")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Skilled Nursing Facility', 'data': sub_categories})
  
  # Prenatal and Postnatal Care
  key_start = df.columns.get_loc("Prenatal and Postnatal Care")
  key_end = df.columns.get_loc("Delivery and All Inpatient Services for Maternity Care")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Prenatal and Postnatal Care', 'data': sub_categories})
  
  # Delivery and All Inpatient Services for Maternity Care
  key_start = df.columns.get_loc("Delivery and All Inpatient Services for Maternity Care")
  key_end = df.columns.get_loc("Mental/Behavioral Health Outpatient Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Delivery and All Inpatient Services for Maternity Care', 'data': sub_categories})
  
  # Mental/Behavioral Health Outpatient Services
  key_start = df.columns.get_loc("Mental/Behavioral Health Outpatient Services")
  key_end = df.columns.get_loc("Mental/Behavioral Health Inpatient Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Mental/Behavioral Health Outpatient Services', 'data': sub_categories})
  
  # Mental/Behavioral Health Inpatient Services
  key_start = df.columns.get_loc("Mental/Behavioral Health Inpatient Services")
  key_end = df.columns.get_loc("Substance Abuse Disorder Outpatient Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Mental/Behavioral Health Inpatient Services', 'data': sub_categories})
  
  # Substance Abuse Disorder Outpatient Services
  key_start = df.columns.get_loc("Substance Abuse Disorder Outpatient Services")
  key_end = df.columns.get_loc("Substance Abuse Disorder Inpatient Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Substance Abuse Disorder Outpatient Services', 'data': sub_categories})
  
  # Substance Abuse Disorder Inpatient Services
  key_start = df.columns.get_loc("Substance Abuse Disorder Inpatient Services")
  key_end = df.columns.get_loc("Generic Drugs")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Substance Abuse Disorder Inpatient Services', 'data': sub_categories})
  
  # Generic Drugs
  key_start = df.columns.get_loc("Generic Drugs")
  key_end = df.columns.get_loc("Preferred Brand Drugs")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Generic Drugs', 'data': sub_categories})
  
  # Preferred Brand Drugs
  key_start = df.columns.get_loc("Preferred Brand Drugs")
  key_end = df.columns.get_loc("Non-Preferred Brand Drugs")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Preferred Brand Drugs', 'data': sub_categories})
  
  # Non-Preferred Brand Drugs
  key_start = df.columns.get_loc("Non-Preferred Brand Drugs")
  key_end = df.columns.get_loc("Specialty Drugs")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Non-Preferred Brand Drugs', 'data': sub_categories})
  
  # Specialty Drugs
  key_start = df.columns.get_loc("Specialty Drugs")
  key_end = df.columns.get_loc("Outpatient Rehabilitation Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Specialty Drugs', 'data': sub_categories})
  
  # Outpatient Rehabilitation Services
  key_start = df.columns.get_loc("Outpatient Rehabilitation Services")
  key_end = df.columns.get_loc("Habilitation Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Outpatient Rehabilitation Services', 'data': sub_categories})
  
  # Habilitation Services
  key_start = df.columns.get_loc("Habilitation Services")
  key_end = df.columns.get_loc("Chiropractic Care")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Habilitation Services', 'data': sub_categories})
  
  # Chiropractic Care
  key_start = df.columns.get_loc("Chiropractic Care")
  key_end = df.columns.get_loc("Durable Medical Equipment")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Chiropractic Care', 'data': sub_categories})
  
  # Durable Medical Equipment
  key_start = df.columns.get_loc("Durable Medical Equipment")
  key_end = df.columns.get_loc("Imaging (CT/PET Scans, MRIs)")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Durable Medical Equipment', 'data': sub_categories})
  
  # Imaging (CT/PET Scans, MRIs)
  key_start = df.columns.get_loc("Imaging (CT/PET Scans, MRIs)")
  key_end = df.columns.get_loc("Preventive Care/Screening/Immunization")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Imaging (CT/PET Scans, MRIs)', 'data': sub_categories})
  
  # Preventive Care/Screening/Immunization
  key_start = df.columns.get_loc("Preventive Care/Screening/Immunization")
  key_end = df.columns.get_loc("Acupuncture")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Preventive Care/Screening/Immunization', 'data': sub_categories})
  
  # Acupuncture
  key_start = df.columns.get_loc("Acupuncture")
  key_end = df.columns.get_loc("Routine Eye Exam for Children")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Acupuncture', 'data': sub_categories})
  
  # Routine Eye Exam for Children
  key_start = df.columns.get_loc("Routine Eye Exam for Children")
  key_end = df.columns.get_loc("Eye Glasses for Children")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Routine Eye Exam for Children', 'data': sub_categories})
  
  # Eye Glasses for Children
  key_start = df.columns.get_loc("Eye Glasses for Children")
  key_end = df.columns.get_loc("Dental Check-Up for Children")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Eye Glasses for Children', 'data': sub_categories})
  
  # Dental Check-Up for Children
  key_start = df.columns.get_loc("Dental Check-Up for Children")
  key_end = df.columns.get_loc("Rehabilitative Speech Therapy")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Dental Check-Up for Children', 'data': sub_categories})
  
  # Rehabilitative Speech Therapy
  key_start = df.columns.get_loc("Rehabilitative Speech Therapy")
  key_end = df.columns.get_loc("Rehabilitative Occupational and Rehabilitative Physical Therapy")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Rehabilitative Speech Therapy', 'data': sub_categories})
  
  # Rehabilitative Occupational and Rehabilitative Physical Therapy
  key_start = df.columns.get_loc("Rehabilitative Occupational and Rehabilitative Physical Therapy")
  key_end = df.columns.get_loc("Well Baby Visits and Care")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Rehabilitative Occupational and Rehabilitative Physical Therapy', 'data': sub_categories})
  
  # Well Baby Visits and Care
  key_start = df.columns.get_loc("Well Baby Visits and Care")
  key_end = df.columns.get_loc("Laboratory Outpatient and Professional Services")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Well Baby Visits and Care', 'data': sub_categories})
  
  # Laboratory Outpatient and Professional Services
  key_start = df.columns.get_loc("Laboratory Outpatient and Professional Services")
  key_end = df.columns.get_loc("X-rays and Diagnostic Imaging")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Laboratory Outpatient and Professional Services', 'data': sub_categories})
  
  # X-rays and Diagnostic Imaging
  key_start = df.columns.get_loc("X-rays and Diagnostic Imaging")
  key_end = df.columns.get_loc("Basic Dental Care - Child")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'X-rays and Diagnostic Imaging', 'data': sub_categories})
  
  # Basic Dental Care - Child
  key_start = df.columns.get_loc("Basic Dental Care - Child")
  key_end = df.columns.get_loc("Orthodontia - Child")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Basic Dental Care - Child', 'data': sub_categories})
  
  # Orthodontia - Child
  key_start = df.columns.get_loc("Orthodontia - Child")
  key_end = df.columns.get_loc("Major Dental Care - Child")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Orthodontia - Child', 'data': sub_categories})
  
  # Major Dental Care - Child
  key_start = df.columns.get_loc("Major Dental Care - Child")
  key_end = df.columns.get_loc("Abortion for Which Public Funding is Prohibited")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Major Dental Care - Child', 'data': sub_categories})
  
  # Abortion for Which Public Funding is Prohibited
  key_start = df.columns.get_loc("Abortion for Which Public Funding is Prohibited")
  key_end = df.columns.get_loc("Transplant")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Abortion for Which Public Funding is Prohibited', 'data': sub_categories})
  
  # Transplant
  key_start = df.columns.get_loc("Transplant")
  key_end = df.columns.get_loc("Accidental Dental")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Transplant', 'data': sub_categories})
  
  # Accidental Dental
  key_start = df.columns.get_loc("Accidental Dental")
  key_end = df.columns.get_loc("Dialysis")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Accidental Dental', 'data': sub_categories})
  
  # Dialysis
  key_start = df.columns.get_loc("Dialysis")
  key_end = df.columns.get_loc("Allergy Testing")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Dialysis', 'data': sub_categories})
  
  # Allergy Testing
  key_start = df.columns.get_loc("Allergy Testing")
  key_end = df.columns.get_loc("Chemotherapy")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Allergy Testing', 'data': sub_categories})
  
  # Chemotherapy
  key_start = df.columns.get_loc("Chemotherapy")
  key_end = df.columns.get_loc("Radiation")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Chemotherapy', 'data': sub_categories})
  
  # Radiation
  key_start = df.columns.get_loc("Radiation")
  key_end = df.columns.get_loc("Diabetes Education")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Radiation', 'data': sub_categories})
  
  # Diabetes Education
  key_start = df.columns.get_loc("Diabetes Education")
  key_end = df.columns.get_loc("Prosthetic Devices")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Diabetes Education', 'data': sub_categories})
  
  # Prosthetic Devices
  key_start = df.columns.get_loc("Prosthetic Devices")
  key_end = df.columns.get_loc("Infusion Therapy")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Prosthetic Devices', 'data': sub_categories})
  
  # Infusion Therapy
  key_start = df.columns.get_loc("Infusion Therapy")
  key_end = df.columns.get_loc("Treatment for Temporomandibular Joint Disorders")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Infusion Therapy', 'data': sub_categories})
  
  # Treatment for Temporomandibular Joint Disorders
  key_start = df.columns.get_loc("Treatment for Temporomandibular Joint Disorders")
  key_end = df.columns.get_loc("Nutritional Counseling")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Treatment for Temporomandibular Joint Disorders', 'data': sub_categories})
  
  # Nutritional Counseling
  key_start = df.columns.get_loc("Nutritional Counseling")
  key_end = df.columns.get_loc("Reconstructive Surgery")
  # Get plan row
  selected_plan = df.loc[df['All fields with an asterisk (*) are required'] == plan_name]
  plan_data = selected_plan.iloc[:, key_start:key_end]
  sub_categories = []

  if key_start and key_end:
    column_data = df.iloc[:, key_start:key_end]
    shape = column_data.shape
    num_of_cols = shape[1]
    # Get row names

    for i in range(0, num_of_cols):
      for index, row in column_data.iterrows():
        if index == 0:
          if isinstance(row[i], str):
            sub_categories.append({'key': str(row[i]), 'data': []})
        if index == 1:
          if i <= 2:
            sub_categories[0]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
          if i > 2 and i <= 5:
            sub_categories[1]['data'].append({'key': row[i], 'data': str(plan_data.values[0][i])})
    
    arr.append({'key': 'Nutritional Counseling', 'data': sub_categories})
  
  return {"data": arr}