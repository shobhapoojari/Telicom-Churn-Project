#Telecom Churn Project
Customer churn is a big problem for telecommunications companies. Indeed , their annual churn rates are usually higher than 10%. For that reason, they develop strategies to keep as many clients as possible. This is a classification project since the variable to be predicted is binary(churn or loyal customer). The goal here to model churn probability, conditioned on the customer features.


Requirements
python
pandas
sklearn
numpy
pickle(save model)

# Model Building

1.Model1 - LogisticRegression - 0.7670175438596492 2.Model2 - KNN - 0.8975438596491228 3.Model3 - Random Forest - 0.9978947368421053 4.Model4 - SVM - 0.8968421052631579 5.Model5 - NB - 0.8091228070175439 6.Model6 - XG boost - 0.9950877192982456

We have used six diffrent algorithm and we got diffrent accuracy. I have used Logistic Regression, k-nearest neighbors, Support Vector Machine, Random Forest, Naive Bayes, XGBoost. In this i can see that Random forest and XGBoost is having good accuracy. Random Forest = 0.9978947368421053 and XG boost = 0.9950877192982456. Hence my final algorithm is Random Forest.

#HOW TO REDUCE CUSTOMER CHURN

    Lean into your best customers.
    Be proactive with communication.
    Define a roadmap for your new customers.
    Offer incentives.
    Ask for feedback often.
    Analyze churn when it happens.
    Stay competitive

#CONCLUSION

    The importance of this type of research in the telecom market is to help companies make more profit. It has become known that predicting churn is one of the most important sources of income to Telecom companies.
    Hence, this research aimed to build a system that predicts the churn of customers i telecom company.

