# Audit-PreProcess
This script is designed to preprocess Microsoft 365 audit logs in CSV format. It extracts information from the "AuditData" column, spreads JSON data, creates separate columns for each unique key, and generates an Excel workbook with different sheets for each operation.

## Prerequisites

- Python 3.x
- Required Python packages: `pandas`, `json`, `openpyxl`

## Usage

1. Clone the repository or download the script.
2. Install the required packages using `pip install pandas json openpyxl`.
3. Run the script by executing `python your_script.py` in the terminal.
4. The preprocessed data will be saved in an Excel workbook named "BrettAuditLog_Preprocessed.xlsx."

## Additional Information

- The script assumes the input data is in the format of the provided CSV file.
- Make sure to customize the script according to your specific requirements.

