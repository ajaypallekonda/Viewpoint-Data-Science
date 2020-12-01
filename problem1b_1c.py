import pandas as pd

d = {'StudentID': ['V001', 'V002', 'V003', 'V004'], 'Name': ['Abe','Abhay', 'Acelin', 'Adelphos']}
name_table = pd.DataFrame(data=d)

d2 = {'StudentID': ['V001', 'V002', 'V003', 'V004'], 'Total_marks': [95,80,74,81]}
mark_table = pd.DataFrame(data=d2)

# Problem 1b:
def change_df(df):
    for i in range(df.shape[0]):
        if ('e' in df['Name'][i] or 'E'in df['Name'][i]):
            df['Name'][i] = df['Name'][i].upper()
        else:
            df['Name'][i] = df['Name'][i].lower()

    return df

name_table = change_df(name_table)
print("Problem 1b:\n", name_table)

# Problem 1c:
def comapare_df(df1, df2):
    upper_total = 0
    upper_count = 0
    lower_total = 0
    lower_count = 0
    for i in range(df1.shape[0]):
        if (df1['Name'][i].islower()):
            for j in range(df2.shape[0]):
                if (df2['StudentID'][j] == df1['StudentID'][i]):
                    lower_total += df2['Total_marks'][j]
                    lower_count += 1
        else:
            for j in range(df2.shape[0]):
                if (df2['StudentID'][j] == df1['StudentID'][i]):
                    upper_total += df2['Total_marks'][j]
                    upper_count += 1

    upper_avg = upper_total/upper_count
    lower_avg = lower_total/lower_count

    d = {'UpperAverage': [upper_avg], 'LowerAverage': [lower_avg]}
    return pd.DataFrame(data=d)

averages = comapare_df(name_table, mark_table)
print("Problem 1c:\n", averages)
        
