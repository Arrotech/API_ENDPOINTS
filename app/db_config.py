import psycopg2
import os


url = "dbname='postgres' host='localhost' user='Arrotech' password='root' port='5432'"

#Returns the connection
def connection(url):
	con = psycopg2.connect(url)
	return con

#Doesnt require the url
def init_db():
	con = connection(url)
	return con

def create_tables():
	conn = connection(url)
	curr = conn.cursor()
	queries = tables()
	for query in queries:
		curr.execute(query)
	conn.commit()

def destroy_table():
	table = tables()
	conn = connection
	curr = conn.cursor()
	orders = "DROP TABLE IF EXISTS orders CASCADE"
	users = "DROP TABLE IF EXISTS users CASCADE"
	queries = [orders,users]
	for query in queries:
		curr.execute(query)
	conn.commit()

def tables():
	tb1 = """CREATE TABLE IF NOT EXISTS order(
		parcel_id serial PRIMARY KEY NOT NULL,
		sender_name varying(30 NOT NULL,)
		recipient varying(30) NOT NULL,
		destination varying(30) NOT NULL,
		pickup varying(30) NOT NULL,
		weight numeric NOT NULL,
		date_created timestamp with time zone DEFAULT('now'::text)::datetime
		)"""
	
	query = [tb1]