# Medical-Insurance-Predictor
Medical Insurance Predictor will help you to estimate the charges by using certain fields like Gender, BMI, etc.


**Project** : **Medical-Insurance-Predictor**

**Work Done** :

      * EDA  ( Handling o outliers)

      * VISUALISATION 

      * MODEL BUILDING 

      * HYPER PARAMETER TUNING OF BEST ACCURACY MODELS


**Choose this project to find out following information**:

      •	To find whether smoking has any effect on medical insuarance charges.
      •	As BMI increases then charges for insurance increases are not.
      •	To find relationship between age and insurance charges .
      •	Find the  chances of winning world cup by host country. 
             
**Conclusion** :

**Visualization** : 

      1. There are total 662 female who buy insuarance out of which 547 are non smokers. 
      2. There are total 676 male who buy insuarance out of which 517 are non smokers. 
      3. So non smokers are purchasing insurance more than smokers.
      2. Chargess doesnot varies much with respect to Gender.
      3. Chargess doesnot varies much with respect to region.
      4. As age increases then charges for insurance also increases.
      5. Higher BMI persons has to pay more than lower ones.
      6. Smokers has to pay  much more than non-smokers.
      7. Smokers with high bmi cost more (almost double the insurance charges).
      8. Having high number of childern means can only spend less expenses on insurance.
              
**Model Building** : 

      1. Before hyperparamter tuning we get following acuuracy 
      2. Linear Regression      : 75%
      3. RandomForest Regressor : 89.77%
      4. XGB Regressor          : 87.46%
      So from above acuuracy analysis we done hyperparamter tuning on RandomForest Regressor and XGB Regressor.

**Result** :

**Visualization** :

      1. If you are a smoker then you has to pay more, depend on your  BMI charges vary and as age increases charges increases.
      2. You need to spend more money on your health insurance, so instead of that be healthy, take your health seriously, quit bad habits like smoking.
      3. Do exercis reduce your BMI and by doing that you can save your money that you are investing on Medical Insurance.
              
**Model Building** : 

      1. After hyperparameter tuning RandomForest Regressor gives best acuuracy (89.77), so we use this model for our predictions.
