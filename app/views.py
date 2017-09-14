# #########
# @Author: Patrick Hastings
# @Title: views
# @Purpose: Serves up different views of the model
# #########


from flask import render_template, url_for, request, redirect, flash
import Accpac_class, threading, Logging_Class, queue
from app import app
from .forms import LoginForm
CompanyName = "Generic"

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
	
        #var = request.form['field1']
	#return var
	try:
	    AP = Accpac_class.Accpac()
	    Results = AP.Summary_Item_Search(item="TEST")
	    #isq = queue.Queue()
	    #threading.Thread(target=AP.Summary_Item_Search, args='TEST')
	    #Results = isq.get()
	    return render_template('item_searching.html', results=Results)
	    #if request.method == 'GET':
	#	SearchField1 = request.form['field1']
	#	SearchField2 = request.form['field2']
	#	SearchField2 = request.form['field3']
	#	SearchField2 = request.form['field4']
	#	if SearchField1 == '':
	#	    return '<a href="/">Nothing searched for, return to home page</a>'
	#	elif SearchField != '':
	#	    if SearchField2 == '':
	#		pass
	#	    else:
	#		# SF1 is full, SF2 is blank, cont with SF1
	#		
	#	else: 
	#	    return "No idea WTF happened"
	 #   else: request.method == 'POST'
	except Exception as ItemSearchingError:
	    print(ItemSearchingError)
	    return 'Bug found: ' + str(ItemSearchingError)


@app.route('/item_searched')
def item_searched():
    '''
    Displays the item results page
    '''
    try:
	AP = Accpac_class.Accpac()
	itemResults = AP.Summary_Item_Search(item="TEST")
	itemCost = AP.Item_Cost_Search(item="TEST")
	itemLoc = AP.Item_Location_Search(item="TEST")
	#OpenPOs = AP.Open_Purchase_Orders_Search(item="TEST")
	#OpenSOs = AP.Open_Sales_Order_Search(item="TEST")
	return render_template('item_searched.html', results=itemResults, itemc=itemCost, itemL = itemLoc)
    except Exception as ErrorItemSearched:
	return ErrorItemSearched

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
	flash('Login requested for OpenID="%s", remember_me=%s' %
	      (form.openid.data, str(form.remember_me.data)))
	return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])