import pandas as pd

def read_the_file(file_path,selected_sheet):
    sheets_dict = pd.read_excel(file_path, sheet_name=None, engine="odf")
    # print("Available sheets:")
    # for sheet_name in sheets_dict.keys():
    #     print(sheet_name)
    df = sheets_dict[selected_sheet]
    # print(f"Data from '{selected_sheet}':")
    df = df.fillna(0)
    return df
