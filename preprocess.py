import pandas as pd
import json
#pip install pandas openpyxl


# Load the necessary libraries
# (Note: In Python, you need to install these libraries using 'pip install pandas openpyxl')

# Importing the CSV file (Main audit log)
main_audit_log = pd.read_csv("AduitLogs.csv")

# Define a function to spread JSON data
def spread_json_data(json_str):
    json_data = json.loads(json_str)
    return json_data

# Apply the function to each row of the AuditData column
main_audit_log['AuditData'] = main_audit_log['AuditData'].astype(str)
main_audit_log['json_data'] = main_audit_log['AuditData'].apply(spread_json_data)
main_audit_log = main_audit_log.drop('AuditData', axis=1)

# Function to extract unique keys from a list of JSON data
def extract_unique_keys(json_data_list):
    keys = set()
    for item in json_data_list:
        keys.update(item.keys())
    return list(keys)

# Extract unique keys from the json_data column
unique_keys = extract_unique_keys(main_audit_log['json_data'])

# Create separate columns for each unique key
for key in unique_keys:
    main_audit_log[key] = main_audit_log['json_data'].apply(lambda x: x.get(key, None))

# Remove the original json_data column
main_audit_log = main_audit_log.drop('json_data', axis=1)

# Getting unique list of operation names
operation_names = main_audit_log['Operation'].unique()

# Making Excel workbook with different sheets as operations
with pd.ExcelWriter("BrettAuditLog_Preprocessed.xlsx", engine='openpyxl', mode='w') as writer:
    for operation_name in operation_names:
        operation_df = main_audit_log[main_audit_log['Operation'] == operation_name]
        operation_df = operation_df.dropna(axis=1, how='any')
        operation_df.to_excel(writer, sheet_name=operation_name, index=False)
