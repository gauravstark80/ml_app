from flask import Flask,render_template, request, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    #return 'Hi'
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age=request.form.get('age') #variable type here is str
    salary=request.form.get('salary')
    '''
    if int(age)>20:
        return 'Will Purchase'
    if int(age)<=20:
        return 'Will Not Purchase' '''
    '''
    if int(age)>20:
        return render_template('index.html',label='Will Purchase')
    if int(age)<=20:
        return render_template('index.html',label='Will not Purchase') '''
    
    return jsonify({'label': 'will not purchase'}) 
    #return 'Hi, my age is {} and my salary is {}'.format(age,salary)
    
if __name__=='__main__':
    app.run(debug=True)