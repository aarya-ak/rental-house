<h1 align = "center">Rental House Selection System ✨</h1>

> A system which aims to select a rental house based on the priorities of the user.
>
 <br>
<br>
The goal of this project is to create a Decision Companion System that helps users make better decisions by evaluating multiple options against user-defined criteria. The system should accept a list of options and a set of criteria, each with a weight or importance, and then process these inputs to generate a ranked recommendation. It must provide clear explanations for why a particular option was recommended, ensuring the decision logic is transparent and explainable. The system should be flexible, allowing users to change inputs and receive updated outcomes rather than relying on hard-coded comparisons.



## How to Run the Project

Rental House Selection System is a Python-based application. Follow these steps to set it up locally:

### 1. Prerequisites
- **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/rental-house.git
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 7. Run the Application
Start the rental house selection process:
```bash
python3 main.py
```


## System Architecture

The system processes user input through validation, normalization, scoring, and ranking to recommend the best house.

<img width="481" height="612" alt="system_architecture-Page-1 drawio" src="https://github.com/user-attachments/assets/d72e6477-a886-437b-8e44-03f9583a467b" />

## Activity Diagram
the step-by-step process of entering house details and priorities, validating inputs, calculating scores, ranking houses, and displaying the best option.

<img width="653" height="601" alt="activity" src="https://github.com/user-attachments/assets/c8a6150c-3639-4911-9d00-dc3ae6eb6a5b" />


===== RENTAL HOUSE SELECTION SYSTEM =====

Enter number of houses: 2

Enter details for House 1
House name: ABC
Monthly Rent /'missing': 8000
Distance to Workplace (km) / 'missing': 7
Safety Rating 1-10 / 'missing': 6
Facilities Score 1-10 /'missing': 7
Space in sq ft / 'missing': 250

Enter details for House 2
House name: XYZ
Monthly Rent /'missing': 8000
Distance to Workplace (km) / 'missing': 7
Safety Rating 1-10 / 'missing': 8
Facilities Score 1-10 /'missing': 5
Space in sq ft / 'missing': 250

Enter weights (Total must equal 10)
Weight for Rent: 10
Weight for Distance: 10
Weight for Safety: 15
Weight for Facilities: 7
Weight for Space: 8

===== FINAL HOUSE RANKING =====
1. XYZ → Score: 8.6 / 10
2. ABC → Score: 7.0 / 10

Criterion: Rent
  Weight Given: 10.0
  Normalized Score: 1.0
  Contribution to Final Score (out of 10 scale): 2.0

Criterion: Distance
  Weight Given: 10.0
  Normalized Score: 1.0
  Contribution to Final Score (out of 10 scale): 2.0

Criterion: Safety
  Weight Given: 15.0
  Normalized Score: 1.0
  Contribution to Final Score (out of 10 scale): 3.0

Criterion: Facilities
  Weight Given: 7.0
  Normalized Score: 0.0
  Contribution to Final Score (out of 10 scale): 0.0

Criterion: space
  Weight Given: 8.0
  Normalized Score: 1.0
  Contribution to Final Score (out of 10 scale): 1.6

XYZ is the best option because it achieved the highest total weighted score of 8.6 / 10 based on your importance levels.

