import mysql.connector
from flask import Flask, render_template, request

from main import scrape_products
app = Flask(__name__)



@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
  article_name = request.form['keyword']
  print(article_name)
  user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
  url = "https://www.amazon.com"
  product_name, p
  roduct_price, product_link, product_image = scrape_products(url, user_agent, article_name)
  # Connect to the RDS instance
  cnx = mysql.connector.connect(
    host="test.c9sygdvwszim.us-east-1.rds.amazonaws.com",
    port=3306,
    database="tutorial",
    user="shlomi",
    password="Shimi431$$"
  )

  # Create a cursor
  cursor = cnx.cursor()

  # Execute the CREATE TABLE statement
  cursor.execute("CREATE TABLE table1  (Name VARCHAR(255), Price INT, Link VARCHAR(255), Image VARCHAR(255))")

  # Iterate through the lists and execute an INSERT statement for each element
  for i in range(len(product_name)):
    cursor.execute("INSERT INTO table1 (Name, Price, Link, Image) VALUES (%s, %s, %s, %s)",
                   (product_name[i], product_price[i], product_link[i], product_image[i]))


  # Execute a SELECT statement to retrieve the data
  cursor.execute("SELECT * FROM table1")

  # Fetch the rows
  rows = cursor.fetchall()

  # Close the cursor and connection
  cursor.close()
  cnx.close()

  # Render the HTML templates and pass the rows to the templates
  return render_template("display.html", rows=rows)




if __name__ == '__main__':
  app.run(host='0.0.0.0')