import pandas as pd
from tabulate import tabulate
from IPython.display import display
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
# Save the file
wb.save("data.xlsx")
df = pd.read_excel('data.xlsx')

dataList =  pd.DataFrame(df) # Convert to data frame to convert to records form
dataList=dataList.to_records()
print(dataList)



dict = {
        'Ticket':0,
        'Company':0,
        'Price':0,
        'Sector':0,
        'Industry':0,
        'PEG' : dataList[1][3],
        'PE' : dataList[0][4],
        'Market Cap': ["AAPL","TSLA"],
        'Free Cash Flow':0,
        'EPS This Y': dataList[2][6] * 100,
        'EPS Grow 1 year':dataList[3][6] * 100,
        'EPS Grow 5 year':dataList[4][6] * 100,
        'ROI': dataList[5][8] * 100,
        'ROE':dataList[4][8]* 100,
        'P/B':dataList[3][4],
        'Dividend Yield':dataList[6][2] * 100,
        'EPS Grow Past 5 Year':dataList[5][6] * 100,
        'Operating Margin':dataList[7][8] * 100,
        'Gross Margin': dataList[6][8] * 100,
        'Profit Margin':dataList[8][8],
        'DCF':0,
        'Rating from me':0,
        'Date Research':0,
        'Cash at beginning':0,
        'Cash at the end':0,
        'Change in Cash':0
}
# display
# df = pd.DataFrame(dict)
#
# # displaying the DataFrame
# display(df)


#ws['M4'] = 42
table = pd.DataFrame(dict)
table.style.set_table_styles([{'selector' : '','props' : [('border','10px solid yellow')]}])

# df = pd.df.to_list(orient="records")