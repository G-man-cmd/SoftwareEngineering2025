import psycopg2
import sys

import time


class Database:

    def __init__(self,dbname='photon'):
        self.dbname = dbname
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database.")



        except Exception as error:
            print(f"Error connecting to PostgreSQL database: {error}")
            print("\n Quitting! \n")
            sys.exit()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            pass
    
            
    def fetch_results(self):
        try:
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error fetching results: {e}")
            return None
