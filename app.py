from flask import Flask,url_for,render_template
from forms import InputForm
import pandas as pd 
import joblib
app=Flask(__name__, static_folder='static')
app.config['SECRET_KEY']="secret_key"

model=joblib.load("model.joblib")
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home")


@app.route('/predict',methods=['GET','POST'])

def predict():
    form=InputForm()
    if form.validate_on_submit():
        x_new=pd.DataFrame(dict(
            location=[form.location.data],
            total_sqft=[form.total_sqft.data],
            bath=[form.bath.data],
            balcony=[form.balcony.data],
            BHK=[form.BHK.data]
        ))
        prediction=model.predict(x_new)[0]
        message=f"price is {prediction:,.02f} Lakh in INR"
    else:
        message="please provide valid input"
    return render_template("predict.html",title="Predict",form=form,output=message)


if __name__=='__main__':
    app.run(debug=True)