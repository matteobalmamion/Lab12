from database.DB_connect import DBConnect
from model.connection import Connection
from model.retailer import Retailer
from model.sale import Sale


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getRetailers():
        db = DBConnect.get_connection()
        result=[]
        query="select * from go_retailers"
        cursor=db.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(Retailer(**row))
        return result

    @staticmethod
    def getAllSales():
        db = DBConnect.get_connection()
        result=[]
        query="select * from go_daily_sales"
        cursor=db.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(Sale(**row))
        return result

    @staticmethod
    def getSalesYear(r1,r2,year):
        db = DBConnect.get_connection()
        result=0
        query="select count(distinct(gds1.Product_number)) as weight from go_daily_sales gds1, go_daily_sales gds2 where year(gds1.Date)=year(gds2.Date)  and gds1.Product_number=gds2.Product_number and Year(gds2.Date)=%s and gds1.Retailer_code=%s and gds2.Retailer_code=%s "
        cursor=db.cursor(dictionary=True)
        cursor.execute(query,(year,r1,r2,))
        for row in cursor:
                result=row["weight"]
                print(row)
        cursor.close()
        db.close()
        return result

