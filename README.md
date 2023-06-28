# Pipa5
Programming in python assignment 5
## Background
Diabetes type 1 is an autoimmune disease where beta cells of the pancreas are attacked and destroyed. Because of this, patients produce little to no insulin. Insulin is a hormone that signals tisues to store glucose. A lack of insulin will cause glucose concentrations in the blood to be too high; hyperglycemia. Before the use of medical insulin, this condition would often be deadly. However, if the use of insulin is not controlled well, the patient may experience hypoglycemia, too little glucose in the blood, which can also lead to illness. This makes modeling extremly important for treating diabetes.

* What is pk and pd modeling
* How is modeling used in the pharmaceutical industry
   
## The problem
I will simulate the glucose levels of a diabetes type 1 patient, in the following four steps;

1.	A pharmacokinetic model, which models the concentration of insulin in blood against time. 
2.	A pharmacodynamic model, which models the drug effect, in this case blood glucose level.
3.	A model of glucose level rises with meals.
4.	A control program that adds insulin, so the blood glucose level returns to normal.

The parameters of the pharmacokinetic and pharmacodynamic models were calculated with data from an article in the journal _Diabetes, obesity and metabolism_ (https://doi.org/10.1111/j.1463-1326.2012.01580.x).  The other parameters were estimated.

## Assumptions
To simplify the model and fit within the scope of the project, the following assumptions were made:
* Other factors effecting glucose concentrations, e.g. metabolism, were ignored.
* The rate of glucose uptake was simplified to a linear formula
