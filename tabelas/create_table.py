# read the .csv file and create a markdown table

import pandas as pd
import os


# read the .csv file and create a markdown table considering that the first row is the header
def create_table(file_name):
    df = pd.read_csv(file_name)
    table = df.to_markdown(index=False)
    return table


# write the table to a .md file
def write_table_to_md(table, file_name):
    with open(file_name, "w") as f:
        f.write(table)


write_table_to_md(
    create_table("lista_especies_agricultura_sintropica_caatinga_modificada.csv"),
    "table.md",
)
