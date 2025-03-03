from flask_wtf import FlaskForm
import pandas as pd
from wtforms import SelectField,FloatField,IntegerField,SubmitField
from wtforms.validators import DataRequired

train=pd.read_csv("Dataset/train_data.csv")
test=pd.read_csv("Dataset/test_data.csv")
X_data=pd.concat([train,test],axis=0).drop(columns="price")


class InputForm(FlaskForm):
    location=SelectField(
        label="Location",
        choices=X_data.location.unique().tolist(),
        validators=[DataRequired()]
    )
    total_sqft=FloatField(
        label="Total Sqft",
        validators=[DataRequired()]
    )
    bath=IntegerField(
        label="Bath Rooms",
        validators=[DataRequired()]
    )
    balcony=IntegerField(
        label="Balcony",
        validators=[DataRequired()]
    )
    BHK=IntegerField(
        label="BHK",
        validators=[DataRequired()]
    )
    submit=SubmitField("Predict")