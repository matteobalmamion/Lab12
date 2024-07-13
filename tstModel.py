from database.DAO import DAO
from model.retailer import Retailer

DAO=DAO()
'''
countries=[]
years=[]
retailers = DAO.getRetailers()
for retailer in retailers:
    if retailer.Country not in countries:
        countries.append(retailer.Country)
sales = DAO.getAllSales()
for sale in sales:
    if sale.date.year not in years:
        years.append(sale.date.year)
print(len(countries))
print(len(years))'''

