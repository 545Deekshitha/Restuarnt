from flask import Flask ,redirect,url_for,request,render_template
app=Flask(__name__)
data={
    'Deekshitha':{'pinno':111}
}
menu1={
    '1':{'name':'pizza','price':100},
    '2':{'name':' Chicken Burger','price':150}
}   
@app.route('/')
def home():
    return render_template('welcome.html')
@app.route('/get_accounts')  
def get_account():
    data_list=[{'account_no':accno,'pinno':details['pinno'] }for accno,details in data.items()]
    data_list1=[{'f'}]
    return data_list  
@app.route('/login',methods=['GET','POST'])       
def login():
    if request.method=='POST':
        accno=request.form['acn'] #surya
        pin=int(request.form['pin'])
        if accno in data:
            if data[accno]['pinno']==pin:#{'pin:pin,'balance':'balance}
                return redirect(url_for('userpanel',account_no=accno,pin_no=pin))
            else:
                return 'pin wrong'
        else:
            return "no account exist"            
    return render_template('login.html')  
@app.route('/userpanel/<account_no>/<pin_no>')
def userpanel(account_no,pin_no):
    return render_template('userpanel.html',account_no=account_no,pin_no=pin_no) 
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        action = request.form.get('action')
    return render_template('menu.html', menu1=menu1)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item_name = request.form['name']
        item_price = request.form['price']
        new_id = str(len(menu1) + 1) 
        menu1[new_id] = {'name': item_name, 'price': int(item_price)} 
        return redirect(url_for('menu'))  
    return render_template('add.html')

@app.route('/update/<item_id>',methods=['GET','POST'])
def update(item_id):
    if request.method == 'POST':
        item_name = request.form['name']
        item_price = request.form['price']
        menu1[item_id] = {'name': item_name, 'price': int(item_price)} 
        return redirect(url_for('menu'))
    item = menu1[item_id]
    return render_template('update.html', item_id=item_id, item=item)
@app.route('/delete/<item_id>') 
def delete(item_id) :
    menu1.pop(item_id)
    return redirect(url_for('menu'))
app.run(debug=True)


