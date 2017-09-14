# #########
# @Author: Patrick Hastings
# @Title: views
# @Purpose: Serves up different views of the model
# #########


from flask import Flask, render_template, url_for, request, redirect, flash
import Accpac_class, threading, Logging_Class, queue
CompanyName = "Certified Retail Solutions"

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    try:
	with open('app/locations.txt', 'r') as f:
	    results = f.readlines()    
	    comcodes = results
	    print (comcodes)
	return render_template('index.html',title=CompanyName, comcodes=comcodes)
    except Exception as indexError:
	print(indexError)

@app.route('/item_searching', methods=['GET','POST'])
def item_searching():
	'''
	CRS Metasearch Item search
	'''
	try:
	    if request.method == 'GET':
		SearchField1 = request.form.get['field1']
		SearchField2 = request.form.get['field2']
		SearchField2 = request.form.get['field3']
		SearchField2 = request.form.get['field4']
		if SearchField1 == '':
		    return '<a href="/">Nothing searched for, return to home page</a>'
		elif SearchField != '':
		    if SearchField2 == '':
			pass
		    else:
			# SF1 is full, SF2 is blank, cont with SF1
			AP = Accpac_class.Accpac()
			isq = queue.Queue()
			threading.Thread(target=AP.Summary_Item_Search, args=SearchField1)
			Results = isq.get()
			return Results
		else: 
		    return "No idea WTF happened"
	    else: request.method == 'POST'
	except Exception as ItemSearchingError:
	    print(ItemSearchingError)
	    return 'Bug found: ' + str(ItemSearchingError)


if __name__ == "__main__":
    app.run(debug=True)