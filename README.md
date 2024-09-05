# HeartDiseaseNN
I programmed a **multilayer neural network** from scratch using **PyTorch** to classify heart disease's and wrote a function to tune it's hyperparameters.

### Guide to Understanding this Project
If you want a detailed read I sugest reading my [Final Project Report](./Saeed_Final_Project_Report.pdf).
You can also visit the **Jupyter notebooks** and follow them along with my report. here is an explination of each one:
1. [184A_final](./184A_final.ipynb)
    - Took a look at the results based off of just using 1 of the 4 datasets (Cleveland Dataset)
2. [184A_final_Understanding_Data](./184A_final_Understanding_Data.ipynb)
    - Load and clean all 4 datasets. 
    - Visualized the data and focused on finding the most significant
    - Rescaled and over/undersampled datasets
    - Found top features using univariate selection and feature importance
    - Combined all 4 datasets and created 3 datasets that vary based on the feature to use to train the models
3. [184A_final_V2](./184A_final_V2.ipynb)
    - Rescale the datasets, and over/undersample to balance them
4. [184A_final_V3](./184A_final_V3.ipynb)
    - Finetune hyperparameters. Varying between:
        - 1, 2, 3 hidden layers
        - Hidden units
        - Epochs

## Results:
- Fine-tuning hyperparameters boosted accuracy from 35% baseline to 66%.
- Tested SMOTE and 7 other undersampling techniques to address class imbalance in data, bringing the difference between the highest and lowest class from 10:1 to approximately 1:1.
- Developed a data preprocessing pipeline, eliminating 39% of data due to invalid values, reducing the number of features 7x using univariate selection and feature importance, and scaling using Min-Max normalization. 

## Methods Utilized:
- Rescaling
    - MinMaxScale
- Undersampler
    - NeighbourhoodCleaningRule
    - TomekLinks
    - ClusterCentroids
    - NearMiss
    - EditedNearestNeighbours
    - CondensedNearestNeighbour
    - OneSidedSelection
    - RandomUnderSampler
- Oversampler
    -  Synthetic Minority Oversampling Technique (SMOTE)
- Feature Selection
    - Univariate selection
    - Feature importence