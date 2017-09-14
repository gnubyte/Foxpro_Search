# ####### 
# @Title: Accpac web server
# @Purpose: Replacing garbage infrastructure with a nice clean and simple interface
# @Author: Patrick Hastings
# #####

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Returns the home page of our Accpac web server
    '''
    return render_template("dashlayout.html")


@app.route('/openSalesOrders', methods=['GET'])
def openSalesOrders():
    item = request.form['item']
    Description = request.form['Description']
    ComCode = request.form['ComCode']
    Quantity = request.form['Quantity']
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
