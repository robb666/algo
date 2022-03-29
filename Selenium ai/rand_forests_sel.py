import pandas as pd
import numpy as np
from queue import PriorityQueue

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# reading the required files into python using pandas
df = pd.read_csv('file.csv')
test = pd.read_csv('Test.csv')

# Fill the NaN values with 'None'
df = df.fillna('None')

# now since our machine learning model can only understand numeric values
# we'll have to convert the strings to numbers/indicator variables
X_train = pd.get_dummies(df.drop('element', axis=1))
print('X_train')
print(X_train)

# returns all the unique Elements stored in the training data
df['element'].unique()

# creating a dictionary of elements
element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))


# {'_token': 0, 'email': 1, 'password': 2, 'LOGIN': 3, 'on': 4}

# replacing dictionary values into dataframe as we need to convert this into numbers
y_train = df['element'].replace(element_dict)


# Now we need to train our model, we can prefer any model which provides accurate results - Random Forest Model
from sklearn.ensemble import RandomForestClassifier


rf = RandomForestClassifier(n_estimators=50, random_state=0)
rf.fit(X_train, y_train)
print(rf.feature_importances_)


def predict_elements():
    num_of_records = len(test)
    test_ = test.fillna('None')
    concatenated = pd.concat([df, test_], axis=0).drop('element', axis=1)
    print('concatenated')
    print(concatenated)

    score = []
    element_name = None
    if num_of_records == 1:
        processed_test = pd.DataFrame(pd.get_dummies(concatenated).iloc[-num_of_records]).T
        print('processed_test')
        print(processed_test)

        probabilites = list(rf.predict_proba(processed_test)[0])
        # print(probabilites)
        element_name = list(element_dict.keys())[np.argmax(probabilites)]
        element_name = 'Hence, the name of our predicted element is {}'.format(element_name)
        score = list(zip(df['element'].unique(), probabilites))

    elif num_of_records > 1:
        processed_test = pd.get_dummies(concatenated).iloc[-num_of_records:]
        probabilites = list(rf.predict_proba(processed_test))


        for i in range(len(probabilites)):
            score.append(list(zip(df['element'].unique(), list(probabilites[i]))))

        element_index = np.argmax(probabilites, axis=1)
        element_name = []
        for ind_, i in enumerate(element_index):
            element_name.append(
                (ind_, 'Hence, the name of our predicted element is {}'.format(list(element_dict.keys())[i])))

    return score, element_name, test


def get_predicted_element(scores, queue):
    for score in scores:
        queue.put((score[1] * -1, score[0]))
        # dict...element
    return queue.get()


# Calling the predict_elements method to return
scores, element_name, test_df = predict_elements()
# print(scores)
# print(element_name)

# queue = PriorityQueue()
# get_predicted_element(scores, queue)
