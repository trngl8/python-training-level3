dict={
    'ID':[1,2,3],
    'TITLE':['learn python hard way','clean code','clean architecture '],
    'AUTHOR':['zed shaw','robert martin','robert martin'],
    'YEAR':['2021','2018','2020']
}
print("Id\t TITLE \t \t AUTHOR \t YEAR",)
for i in range(3):
    print(dict['ID'][i],'\t',dict['TITLE'][i],'\t',dict['AUTHOR'][i],'\t',dict['YEAR'][i],'\t')