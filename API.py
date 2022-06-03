from flask import Flask,request,jsonify,render_template
# Import the class of the ML model from the python file.
# from PythonCodeMLModel import BreastCancerAnalysis

app=Flask(__name__)
# , static_url_path="/static"
# take object from the class
# MLObject = BreastCancerAnalysis()

@app.route("/")
def home():
    # render_template is used to display a page 
    return render_template('index.html')

@app.route("/symptoms")
def symptoms():
    return render_template('symptoms.html')

@app.route("/test",methods=["GET","POST"])
def test():
    return render_template('test.html')
#----------------------------------{For Example Logistic Regression}-------------------------------------------------------
# this link is for api to can call the fun when the url is called. You can put the fitting and evalution function in the test funtion
# @app.route('/LoModelFitting')
# def ModelFitting1():
#     IM.LoModelFitting()
#     data = {"status_code":200,"message":"Done !"} 
#     when IM.LoModelFitting() is done without errors you will display data['message']
#     return data['message'] 

# @app.route('/LoEvaluate')
# def Evaluate1():
#     IM.LoEvaluate()
#     data = {"status_code":200,"accuracy":IM.LoEvaluate()}
# when IM.LoEvaluate() is done without errors you will display data['accuracy']
#     return str(data['accuracy']) 
    

# @app.route('/Lopredict',methods=["GET","POST"])
# def predict1():
#     if request.method=="GET":
#         return render_template("/Lopredict")
#     else:

#         value1 = request.form['take the name property of of html tag input 1']
#         value2 = request.form['take the name property of of html tag input 1']
#         value3 = request.form['take the name property of of html tag input 1']
#         value4 = request.form['take the name property of of html tag input 1']
#  and so on
#         data = {"status_code":200,'text':text,"prediction":IM.Lopredict(value1,value2,value3,value4)}
#         return jsonify(data)

app.run(debug=True)  # to can run automatic