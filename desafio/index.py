from flask import Flask, request, render_template
import sqlite3
from models import Merchant, Purchase

app = Flask('desafio')

index_puchaser_name = 0
index_item_description = 1
index_item_price = 2
index_purchase_count = 3
index_merchant_adress = 4
index_merchant_name = 5


def create_merchant():
	con = sqlite3.connect('desafio.db')
	c = con.cursor()

	create_merchant = """ CREATE TABLE IF NOT EXISTS merchants (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name VARCHAR(100),
					adress VARCHAR(200));
					"""

	c.execute(create_merchant)
	con.close()

def create_purchase():
	con = sqlite3.connect('desafio.db')
	c = con.cursor()

	create_purchase = """ CREATE TABLE IF NOT EXISTS purchases (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					purchaser_name VARCHAR(50),
					item_description VARCHAR(100),
					item_price DECIMAL(5,2),
					purchase_count INTEGER,
					merchant_name VARCHAR(100));
					"""

	c.execute(create_purchase)
	con.close()

def insere_merchant(item):
	con = sqlite3.connect('desafio.db')
	c = con.cursor()

	insere_merchant = """INSERT INTO merchants (name, adress) 
					VALUES ("%s", "%s");
					""" % (item.name, item.adress)

	c.execute(insere_merchant)
	c.close()


def insere_purchase(item):
	con = sqlite3.connect('desafio.db')
	c = con.cursor()

	insere_purchase = """INSERT INTO purchases (purchaser_name, item_description, item_price, purchase_count, merchant_name) 
					VALUES ("%s", "%s", %d, %d, "%s");
					""" % (item.purchaser_name, item.item_description, item.item_price, item.purchase_count, item.merchant_name)

	c.execute(insere_purchase)
	c.close()

@app.route("/")
def index():
	create_merchant()
	create_purchase()

	return app.send_static_file('index.html')

@app.route("/save", methods=['POST'])
def save():
	# import ipdb; ipdb.set_trace()
	create_merchant()
	create_purchase()

	lines = []
	i = 0
	receita_total = 0

	file_upload = request.files.get('file')
	content = file_upload.read()
	lines = content.split('\n')
	for line in lines:
		#pula o cabecalho
		if i == 0:
			i = i + 1
			continue

		if line == '':
			continue

		line = line.split('\t')
		merchant = Merchant(line[index_merchant_name], line[index_merchant_adress])
		purchase = Purchase(line[index_puchaser_name], line[index_item_description], float(line[index_item_price]), int(line[index_purchase_count]), line[index_merchant_name])
		receita_total = float(line[index_item_price]) * int(line[index_purchase_count]) + receita_total

		insere_merchant(merchant)
		insere_purchase(purchase)

	return render_template('save.html', receita=receita_total)



app.run()