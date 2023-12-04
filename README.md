# Project: Multiple-Disease-Predictor-ML-Flask-WebApp
### Project Intro/Objective 

It's an end-to-end Machine Learning Project. The purpose of this project is to predict whether a person is suffering from a particular disease or not on the basis of his/her input data. The prediction has been done by using Machine Learning (ML) classification algorithms . Currently, this web app can predict 3 types of diseases (Diabetes, Parkinson's and Heart Disease). 




### Screenshots 

![Screenshot 2023-03-18 at 3 34 48 PM](https://user-images.githubusercontent.com/110475111/226099285-8dc371e0-a9f8-485b-b2ed-c40b8b899b0f.png)

![Screenshot 2023-03-18 at 3 35 01 PM](https://user-images.githubusercontent.com/110475111/226099298-418bf7b0-f102-4d58-a4b9-c29052019582.png)

![Screenshot 2023-03-18 at 3 35 11 PM](https://user-images.githubusercontent.com/110475111/226099303-51995af7-8bd0-4bbb-8776-50551dfb6e55.png)![Screenshot 2023-03-18 at 3 35 19 PM](https://user-images.githubusercontent.com/110475111/226099308-33ad3dbc-90e7-4f8c-812d-b5613b4ad1ea.png)

![Screenshot 2023-03-18 at 3 35 24 PM](https://user-images.githubusercontent.com/110475111/226099309-d0e71a8b-ecb8-4fb7-9e00-b6cc00043169.png)



![Screenshot 2023-03-18 at 3 35 39 PM](https://user-images.githubusercontent.com/110475111/226099321-4e532f92-420c-47ea-b857-50a7809889f6.png)

![Screenshot 2023-03-18 at 3 36 15 PM](https://user-images.githubusercontent.com/110475111/226099326-7808814b-d2af-45a0-97b0-46f2a15df77c.png)!
![Screenshot 2023-03-18 at 3 35 33 PM](https://user-images.githubusercontent.com/110475111/226099417-cd525a82-2625-44f6-835f-d1b0e5c8ff29.png)

![Screenshot 2023-03-18 at 3 36 54 PM](https://user-images.githubusercontent.com/110475111/226099346-cf7356bb-c974-489a-b5a6-34faa863c1a3.png)
![Screenshot 2023-03-18 at 3 37 17 PM](https://user-images.githubusercontent.com/110475111/226099353-1d3daafd-5fda-4661-849c-7e38f9e436fd.png)
![Screenshot 2023-03-18 at 3 37 49 PM](https://user-images.githubusercontent.com/110475111/226099358-553d7afa-58c5-4220-8b82-e1c5e6614bdf.png)![Screenshot 2023-03-18 at 3 39 25 PM](https://user-images.githubusercontent.com/110475111/226099364-75a5baed-c209-4e46-81bd-5a3e69a8df9f.png)

![Screenshot 2023-03-18 at 3 41 02 PM](https://user-images.githubusercontent.com/110475111/226099373-ab9a1210-e156-4cec-a620-c5b1cfd59a9c.png)

The datasets that are used for training the ML models are:

- **The diabetes dataset consists of 768 data points, with each datapoint having 8 features. This dataset is Pima Indians Diabetes Database found on the kaggle.**

**Features**
1. `Pregnancies`: Number of times pregnant
2. `Glucose`: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3. `BloodPressure`: Diastolic blood pressure (mm Hg)
4. `SkinThickness`: Triceps skin fold thickness (mm)
5. `Insulin`: 2-Hour serum insulin (mu U/ml)
6. `BMI`: Body mass index (weight in kg/(height in m)^2)
7. `DiabetesPedigreeFunction`: Diabetes pedigree function
8. `Age`: Age (years)


**Target Variable**
9. `Outcome`: Class variable (0 or 1) 268 of 768 are 1, the others are 0

- **The heart dataset consists of 1025 data points, with each datapoint having 13 features. This dataset is Heart Disease Dataset found on the kaggle.**

**Features**
1. `age`: age in years
2. `sex`: (1 = male; 0 = female)
3. `cp`: chest pain type
4. `trestbps`: resting blood pressure (in mm Hg on admission to the hospital)
5. `chol`: serum cholestoral in mg/dl
6. `fbs`: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
7. `restecg`: resting electrocardiographic results
8. `thalach`: maximum heart rate achieved
9. `exang`: exercise induced angina (1 = yes; 0 = no)
10. `oldpeak`: ST depression induced by exercise relative to rest
11. `slope`: the slope of the peak exercise ST segment
12. `ca`: number of major vessels (0-3) colored by flourosopy 
13. `thal`: 0 = normal; 1 = fixed defect; 2 = reversable defect


**Target Variable**
14. `target`: Class variable (0 or 1) 526 of 1025 are 1, the others are 0. Value 0 = no heart disease and 1 = heart disease

- **The ParkinsonsDisease dataset consists of 195 data points, with each datapoint having 22 features. This dataset is Parkinsons Disease Dataset found on the kaggle.**

**Features**
1. `MDVP:Fo(Hz)`: Average vocal fundamental frequency
2. `MDVP:Fhi(Hz)`: Maximum vocal fundamental frequency
3. `MDVP:Flo(Hz)`: Minimum vocal fundamental frequency
4. `MDVP:Jitter(%)`
5. `MDVP:Jitter(Abs)`
6. `MDVP:RAP`
7. `MDVP:PPQ`
8. `Jitter:DDP`: Several measures of variation in fundamental frequency
9. `MDVP:Shimmer`
10. `MDVP:Shimmer(dB)`
11. `Shimmer:APQ3`
12. `Shimmer:APQ5`
13. `MDVP:APQ`
14. `Shimmer:DDA` :Several measures of variation in amplitude
15. `NHR`
16. `HNR`: Two measures of ratio of noise to tonal components in the voice
17. `RPDE`
18. `DFA`: Signal fractal scaling exponent
19. `spread1`
20. `spread2`
21. `PPE`: Three nonlinear measures of fundamental frequency variation
22. `D2`: Two nonlinear dynamical complexity measures


**Target Variable**
23. `status`: Class variable (0 or 1) 147 of 195 are 1, the others are 0. Value 1 - Parkinson's, 0 - healthy
