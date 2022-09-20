from app import app

@app.route('/')
def home():
    return "<h1>Home</h1>"



@app.route('/contact page')
def contact_page():
    return '''
    <h1> contact page </h1>
    
    '''

@app.route('/blog')
def blog():
    return '''
    <h1> Blog </h1>
    
    '''

@app.route('/shopping')
def shopping():
    return '''
    <h1> Shopping </h1>
    
    '''