# Pipa5
Programming in python assignment 5
## Background
Diabetes type 1 is an autoimmune disease where beta cells of the pancreas are attacked and destroyed. Because of this, patients produce little to no insulin. Insulin is a hormone that signals tissues to store glucose. A lack of insulin will cause glucose concentrations in the blood to be too high: hyperglycaemia. Before the use of medical insulin, this condition would often be deadly. However, if the use of insulin is not controlled well, the patient may experience hypoglycaemia, too little glucose in the blood, which can also lead to illness. This makes modelling extremely important for treating diabetes.

In pharmaceutics, there are two main types of models. Pharmacokinetic models are used to predict the concentration of the drug over time. Pharmacodynamic models are used to predict the effect caused by the drug, in this case, the effect measured is glucose concentrations in the blood. By using models, scientists can better predict at which doses the drug is effective or toxic, thus saving money and unnecessary animal or clinical trials.

## The problem
The problem I want to solve is how much insulin a diabetes type 1 patient should take after a meal. I will do this in four steps:
1.	A model of glucose level rises with meals.
2.	A pharmacokinetic model, which models the concentration of insulin in blood against time. 
3.	A pharmacodynamic model, which models the drug effect, in this case blood glucose level.
4.	A program that calculates how much insulin to add, so the blood glucose level returns to base level.

At the end, you can input how much sugar is in your meal and the program will return a recommended dose and a graph of glucose and insulin concentrations.

## Data and assumptions
The parameters of the pharmacokinetic and pharmacodynamic models were calculated with data from an article in the journal _Diabetes, obesity and metabolism_ (https://doi.org/10.1111/j.1463-1326.2012.01580.x).  The other parameters were estimated.

To simplify the model and fit within the scope of the project, the following assumptions were made:
* Other factors effecting glucose concentrations, e.g. metabolism, were ignored.
* The rate of glucose uptake was simplified to a linear formula
