# Housing Price Project

## Overview
This project predicts housing prices using machine learning models and statistical analysis.

## Features
- Data preprocessing and exploration
- Feature engineering
- Model training and evaluation
- Price prediction capabilities

## Installation
```bash
git clone https://github.com/Kman0908/housing-price
cd housing-price
pip install -r requirements-app.txt
```

## Usage
https://housing-price-8r8f.onrender.com/

## Project Structure
```
housing-price/
├── data/
├── notebooks/
├── src/
├── README.md
└── requirements-app.txt
```

## Requirements
- Python 3.8+
- pandas
- scikit-learn
- numpy

## Results
Model:  LinearRegression
Training result: 
Mean absloute error:  19893.241946582333
Mean squared error:  1041148273.2290652
r^2 score:  0.8642628429213994
********************
Model:  Ridge
Training result: 
Mean absloute error:  19547.592144432685
Mean squared error:  1024343442.49672
r^2 score:  0.8664537315848567
********************
Model:  Lasso
Training result: 
Mean absloute error:  19868.90868890737
Mean squared error:  1038262459.3294791
r^2 score:  0.8646390738432189
********************
Model:  RandomForestRegressor
Training result: 
Mean absloute error:  16775.371061643837
Mean squared error:  823996053.2620695
r^2 score:  0.8925735319457493
********************
Model:  AdaBoostRegressor
Training result: 
Mean absloute error:  23790.1797258256
Mean squared error:  1057382560.2053304
r^2 score:  0.8621463375032787
********************
Model:  DecisionTreeRegressor
Training result: 
Mean absloute error:  26686.29109589041
Mean squared error:  1852720344.1061645
r^2 score:  0.7584561211529494
********************
Model:  XGBRegressor
Training result: 
Mean absloute error:  16574.318359375
Mean squared error:  681996864.0
r^2 score:  0.9110863208770752
********************
Model:  CatBoostRegressor
Training result: 
Mean absloute error:  15082.687986526134
Mean squared error:  645876898.8356583
r^2 score:  0.915795380614912
********************

## Contributing
Pull requests are welcome.
