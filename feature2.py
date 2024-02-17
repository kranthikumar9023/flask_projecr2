from flask import Flask,render_template


FAI=Flask(__name__)
@FAI.route('/return_static')
def return_static():
    return render_template('return_static.html')

if __name__=='__main__':
    FAI.run(debug=True)