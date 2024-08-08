# Crime Interval Prediction and Classification using Logistic Regression, Random Forest & C5 Algorithm

## Authors
- Laveena D’Costa (MCA, St Aloysius Institute of Management and Information Technology, India)
- Ashoka Wilson D’Souza (Senior Business Intelligence Analyst, Atlantic Data Bureau Service, Mangalore, India)
- Prajwal K Augustine (MSc, St Aloysius Institute of Management and Information Technology, India)
- Dillon Arwin Ashwal (MSc, St Aloysius Institute of Management and Information Technology, India)

## Contact Information
- Laveena D’Costa: laveenacrasta@staloysius.ac.in
- Ashoka Wilson D’Souza: ashokdesouza@gmail.com
- Prajwal K Augustine: prajwalaugustine97@gmail.com
- Dillon Arwin Ashwal: dillonarwinashwal@gmail.com

## Abstract
This project focuses on predicting the crime time interval for the occurrence of different types of crimes using various classification models. The models used are Logistic Regression, Random Forest, and C5.0 classification models. The prediction utilizes features such as crime type, crime category, district ID, and others to determine the crime time intervals.

## Keywords
- Logistic Regression
- Crime Interval
- Random Forest
- C5.0 Classification

## Table of Contents
- [Introduction](#introduction)
- [Literature Review](#literature-review)
- [Data and Empirical Analysis](#data-and-empirical-analysis)
  - [Denver Crimes Dataset](#denver-crimes-dataset)
  - [Procedure and Data Analysis](#procedure-and-data-analysis)
- [Models Used](#models-used)
  - [Logistic Regression](#logistic-regression)
  - [Random Forest Classifier](#random-forest-classifier)
  - [C5.0 Classification Model](#c50-classification-model)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction
The crime rate has significantly increased over the past few years, making it challenging for law enforcement agencies to keep track of them. However, advancements in statistics and technology now enable us to analyze crime patterns to preemptively address potential incidents. This project explores the correlation between crime type and the time of occurrence to predict future crimes.

## Literature Review
Several studies have applied various algorithms to predict crime patterns. Notably:
- Almanie et al. analyzed crime patterns in Denver and Los Angeles using the Apriori algorithm and other classifiers, achieving an accuracy of up to 54%.
- Gök and Sait compared Naïve Bayes and Decision Tree classifiers for predicting criminal incidents, with Naïve Bayes achieving 78.05% accuracy.
- Monish et al. achieved 97.59% accuracy using the J48 Decision Tree classifier.
- Agarwal et al. used the Apriori algorithm to predict the likelihood of offenders repeating certain crimes.

## Data and Empirical Analysis

### Denver Crimes Dataset
This dataset includes real-world crime data from Denver, Colorado, covering the years 2014 to 2019. It contains various attributes such as crime type, category, district ID, etc.

### Procedure and Data Analysis
The dataset required preprocessing to standardize the date and time formats to a 24-hour format. The primary features used for modeling are listed in Table T1. The SMOTE method was employed to balance the classes.

## Models Used

### Logistic Regression
Logistic Regression is used for binary classification problems. It employs the sigmoid function to model the probability of a binary outcome.

### Random Forest Classifier
Random Forest creates a collection of decision trees from randomly selected subsets of the training data and aggregates their votes to determine the final class.

### C5.0 Classification Model
The C5.0 algorithm constructs a decision tree or rule set by repeatedly splitting the sample based on the field that offers the maximum information gain.

## Results
The models were evaluated before and after addressing class imbalance. The results are summarized in tables T2 to T7. The C5.0 classification model demonstrated superior performance with an accuracy of 65%, outperforming Logistic Regression and Random Forest.

## Conclusion
Based on the accuracy measures, the C5.0 classification model is identified as the most effective for predicting crime time intervals. It maintains a robust accuracy of 65% even after balancing the class variable.

## References
1. Gök, M., & Sait, M. (2016). Criminal prediction using Naive Bayes theory. Springer, 28(9), 2581-2592.
2. Agarwal, A., Chougule, D., & Chimote, D. (2016). Application for analysis and prediction of crime data using data mining. International Journal of Advanced Computational Engineering and Networking.
3. Monish, P., Ranjith, K. R., Varun, G., & Sridhar, S. (Year). CRIME ANALYSIS: PROBABILISTIC PREDICTION.
4. Almanie, T., Mirza, R., & Lor, E. (Year). Crime prediction based on crime type and using

## Installation and Usage
1. Clone the repository:
   ```
   git clone https://github.com/username/repository.git
   ```
2. Navigate to the project directory:
   ```
   cd repository
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the analysis:
   ```
   python main.py
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out to any of the authors for more information or if you have any questions. Thank you for your interest in our work!



check https://github.com/Au9u5tu-s/Flaskcrime/blob/master/Crime%20Interval%20Prediction%20and%20Classification.pdf for the research study
