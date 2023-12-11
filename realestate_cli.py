import argparse
import sqlite3

def search_vacant_houses(location, bedrooms, price_range):

    conn = sqlite3.connect("realestate.db")
    cursor = conn.cursor()

#     # Build the SQL query based on the provided criteria
#     query = "SELECT * FROM houses WHERE location = ?"
#     parameters = [location]

#     if bedrooms is not None:
#         query += " AND bedrooms = ?"
#         parameters.append(bedrooms)

#     if price_range is not None:
#         query += " AND price >= ? AND price <= ?"
#         min_price, max_price = map(float, price_range.split('-'))
#         parameters.extend([min_price, max_price])

#     # Execute the query
#     cursor.execute(query, parameters)

#     # Fetch and print the results
#     results = cursor.fetchall()
#     for row in results:
#         print(f"House ID: {row[0]}, Location: {row[1]}, Bedrooms: {row[2]}, Price: {row[3]}")

#     # Close the connection
#     conn.close()
