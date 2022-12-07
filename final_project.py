# IMPORT LIBRARIES
from pycaret.classification import *
import xgboost
import pandas as pd
import shap

# INITIALIZE DATAFRAMES
df_train = pd.read_csv("/home/ubuntu/environment/data/train.csv")
df_test = pd.read_csv("/home/ubuntu/environment/data/test.csv")

# INITIALIZE PYCARET
clf1 = setup(data=df_train, target="Survived",
            ignore_features=["Name", "Ticket", "Cabin", "Embarked"],
            categorical_features=["Sex"],
            numeric_features=["PassengerId", "Pclass", "Age", "SibSp", "Parch", "Fare"])
# best = clf1.compare_models()
# tuned = tune_model(best)

# INITIALIZE XGBOOST AND TUNE MODEL
xgboost = create_model("xgboost")
tuned = tune_model(xgboost)

# FEATURE IMPORTANCE ANALYSIS
plot_model(tuned, plot="feature", save=True)

# SHAPLEY ADDITIVE EXPLANATIONS
interpret_model(tuned, plot="reason", save=True)

# MAKE PREDICTIONS
predictions = predict_model(tuned, data=df_test, raw_score=True)

# CLEAN THE DATA FOR SUBMISSION
cleaned = predictions[["PassengerId","prediction_label"]]
cleaned = cleaned.astype(int)
cleaned.rename(columns={"prediction_label": "Survived"}, inplace=True)

# EXPORT TO CSV
cleaned.to_csv("/home/ubuntu/environment/results.csv", index=False)

