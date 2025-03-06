Ice Cream Sales Prediction

This repository contains a small machine learning project that uses linear regression to predict temperature based on ice cream sales.

📌 Description

The project utilizes the scikit-learn library to train a linear regression model with a dataset (IceCreams.csv). The analyzed relationship is between temperature and ice cream sales.

📁 Project Structure

IceCreams.csv - CSV file containing training data.

script.py - Python script that trains the model and makes predictions.

📦 Dependencies

Make sure you have the following libraries installed:

pip install pandas scikit-learn

🚀 How to Run

Ensure the IceCreams.csv file is in the same directory as the script.

Run the Python script:

python script.py

🛠 Functionality

The code performs the following steps:

Reads the data from the CSV file using pandas.

Defines x (ice cream sales) as the independent variable and y (temperature) as the dependent variable.

![image](https://github.com/user-attachments/assets/710fe927-3b1c-47b6-ba74-209380d16689)


Trains a linear regression model using scikit-learn.

Makes temperature predictions based on new ice cream sales inputs.

📊 Example Usage

If ice cream sales are 4 units, the predicted temperature will be displayed in the terminal with the following command:

print(model.predict([[4]])[0][0]), change the number to your preference

📜 License

This project is open-source and can be used freely.
