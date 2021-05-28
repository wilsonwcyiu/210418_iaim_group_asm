#Import svm model
from sklearn import svm


# https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python
if __name__ == '__main__':

    x_input_train_list = [[1], [2], [3], [4], [5], [6], [7], [8]]
    y_output_train_result = [1, 1, 2, 2, 3, 3, 4, 4]


    # https://medium.com/all-things-ai/in-depth-parameter-tuning-for-svc-758215394769
    classifier = svm.SVC(kernel='linear')      # kernal_list: list = ['linear', 'rbf', 'poly']

    #Train the model using the training sets
    classifier.fit(x_input_train_list, y_output_train_result)

    #Predict the response for test dataset
    x_input_test_list = [[1], [1], [6], [6], [8], [8]]
    y_output_test_pred = classifier.predict(x_input_test_list)

    print(y_output_test_pred)