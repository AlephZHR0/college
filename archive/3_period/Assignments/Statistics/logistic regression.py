# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Reading the dataset
df = pd.read_csv('./credit_data.csv')

# Removing rows with missing values
df = df.dropna()

# Converting the 'Status' column to binary
df['Status'] = df['Status'].apply(lambda x: 1 if x == 'good' else 0)

# Defining the numeric columns and categorical columns
numeric_columns = ['Seniority', 'Time', 'Age', 'Expenses', 'Income', 'Assets', 'Debt', 'Amount', 'Price']
categorical_columns = ['Home', 'Marital', 'Records', 'Job']

# Function to create dummy variables for categorical columns
def dummyfy(column_name):
    global df, numeric_columns
    new_columns = df[column_name].unique()
    for column in new_columns:
        numeric_columns.append(f'{column_name}_{column}')
    dummies = pd.get_dummies(df[column_name], prefix = column_name)
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column_name, axis=1)

# Creating dummy variables for all categorical columns
for column_name in categorical_columns:
    dummyfy(column_name)

# Defining the X and Y variables
X = df[numeric_columns]
Y = df['Status']

# Defining a function to perform logistic regression and return accuracy
def logistic_regression(test_size = 0.2, seed = 1):
    # Defining the training and testing variables
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = test_size, random_state = seed)
    
    # Defining the logistic regression model and fitting it to the training data
    logistic_regression = LogisticRegression(max_iter = 10000)
    logistic_regression.fit(X_train, y_train)
    
    # Predicting the target variable for the test data
    y_predicted = logistic_regression.predict(X_test)
    
    # Creating a confusion matrix and displaying it as a heatmap
    confusion_matrix = pd.crosstab(y_test, y_predicted, rownames=['Real'], colnames=['Predicted'])
    sn.heatmap(confusion_matrix, annot=True, cmap='coolwarm')
    plt.show()
    
    # Calculating the accuracy score and printing it along with the test size and seed values
    accuracy = metrics.accuracy_score(y_test, y_predicted)
    print(f'Test size: {test_size} | Seed: {seed} | Accuracy: {accuracy}')    

    # Calculating the ROC curve and the area under the curve (AUC)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_predicted)
    # fpr = false positive rate
    # tpr = true positive rate

    auc = metrics.roc_auc_score(y_test, y_predicted)
    plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line (random classifier)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve (Receiver Operating Characteristic)')
    plt.legend(loc='lower right')
    plt.show()
    # Returning the test size, seed, and accuracy score
    return test_size, seed, accuracy


# Calling the logistic regression function
logistic_regression()
