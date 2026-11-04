# Model Card

## Model Details

This project uses a Random Forest Classifier to predict whether an individual's annual income is greater than $50,000 based on demographic and employment-related information. The model uses 100 decision trees and a random state of 42 to ensure reproducibility. The model was developed using Python and scikit-learn.

## Intended Use

The intended purpose of this model is to demonstrate a machine learning classification pipeline using Census data. It predicts whether an individual's income falls into the greater-than-$50,000 or less-than-or-equal-to-$50,000 category. This model is intended for educational and experimental purposes only and should not be used to make decisions about individuals.

## Training Data

The model was trained using the U.S. Census income dataset containing 32,561 records and 15 columns. The dataset includes demographic, educational, and employment-related information. Eight categorical features were processed using OneHotEncoder, and the salary target was converted into binary values using LabelBinarizer. The dataset was divided into 80% training data and 20% testing data using a random state of 42.

## Evaluation Data

The model was evaluated using the 20% held-out testing dataset. This dataset contained approximately 6,513 records. The same encoder and label binarizer fitted on the training data were used to process the testing data.

## Metrics

The model was evaluated using precision, recall, and F1 score.

The overall model performance was:

- Precision: 0.7419
- Recall: 0.6384
- F1 Score: 0.6863

The model also evaluated performance across all unique values of the eight categorical features. These results are saved in slice_output.txt.

## Ethical Considerations

The dataset contains demographic information, including race and sex. These characteristics may introduce bias into the model's predictions. The model's performance also varies across different demographic and socioeconomic groups. These differences should be considered when interpreting results. This model should not be used to make employment, financial, or other consequential decisions about individuals.

## Caveats and Recommendations

The model's performance is not perfect, and it does not correctly identify every individual earning more than $50,000. Some categorical groups contain very few records, which can make their performance metrics less reliable. Additional testing, bias evaluation, and model improvements would be necessary before considering this model for real-world use. The model is intended for educational purposes and should not be used as the sole basis for decisions about individuals.
