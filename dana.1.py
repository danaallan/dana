import pandas as pd
import openpyxl
df = pd.read_excel('C:/Users/Admin/Downloads/Employee Sample Data - Copy.xlsx')
df.fillna(200, inplace = True)
df.loc[:4,'EEID'] =['E012030','E12034','E20987','E27640','E03451']
df.loc[:4, 'Full Name'] = ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Brown', 'Daniel Williams']
df.loc[:4, 'Job Title']  = ['HRIS Analyst','Computer Systems Manager','Network Architect','Field Engineer','Manager']
df.loc[:4,'Department'] =['sales','Engineering','Marketing','Human Resources','Accounting']
df.loc[:4,'Business Unit'] =['Manufacturing','Research & Development','Corporate','Speciality Products','Research & Development']
df.loc[:4,'Gender']=['Male','Female','Male','Male','Female']
df.loc[:4,'Ethnicity']=['Asian','Black','Asian','Caucasian','Black']
df.loc[:4,'Age']=['30','40','32','39','44']
df.loc[:4,'Hire Date']=['20/1/2000','1/1/2001','9/8/1990','9/2/1999','17/9/2017']
df.loc[:4,'Annual Salary']=['$119,746','$222,130','$110,230','$420,110','$550,123']
df.loc[:4,'Bonus %']=['1%','2%','5%','3%','10%']
df.loc[:4,'Country']=['China','Jordan','Bali','London','Lebanon']
df.loc[:4,'City']=['Austin','Austin','Austin','Austin','Austin']
df.loc[:4,'Exit Date']=['10/10/2010','20/2/2002','1/3/2003','20/5/2006','3/12/2002']
print(df.to_string())
temp_column = pd.to_numeric(df['Annual Salary'], errors='coerce')
max_salary_index = temp_column.idxmax()
max_salary = temp_column.max()
max_salary_row = df.loc[max_salary_index]
print(f"The largest salary = {max_salary} \n \n")
print(max_salary_row)
df.to_excel('C:/Users/Admin/Downloads/Employee Sample Data - Copy.xlsx')