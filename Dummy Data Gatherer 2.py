import pandas as pd
import numpy as np

# Assuming data is available in a DataFrame named 'original_data'
# with columns: 'Genome', 'AgeGroup', 'DiagnosisTime', 'Test1', 'Test2'

# Extract unique `genome types
genome_types = [
    "XX",
    "XY",
    "XXY (Klinefelter Non Mosaic)",
    "XXY/XY (Klinefelter Mosaic)",
    "XXX",
    "XYY",
    "X0 (Turner non mosaic)",
    "X0/XX (Turner mosaic: 50%)",
    "XXXY",
    "XXYY",
    "XXXX",
    ]

one_to_two = {
    "XX": {'mean_test1': 93.32, 'std_dev_test1': 13.71, 'N': 1300},
    "XY": {'mean_test1': 93.32, 'std_dev_test1': 13.71, 'N': 1700},
    "XXY (Klinefelter Non Mosaic)": {'mean_test1': 81.68, 'std_dev_test1': 16.05, 'N': 2000},
    "XXY/XY (Klinefelter Mosaic)": {'mean_test1': 89, 'std_dev_test1': 16.05, 'N': 300},
    "XXX": {'mean_test1': 81.68, 'std_dev_test1': 16.05, 'N': 600},
    "XYY": {'mean_test1': 81.68, 'std_dev_test1': 16.05, 'N': 800},
    "X0 (Turner non mosaic)": {'mean_test1': 71, 'std_dev_test1': 15, 'N': 1500},
    "X0/XX (Turner mosaic: 50%)": {'mean_test1': 75, 'std_dev_test1': 15, 'N': 1500},
    "XXXY": {'mean_test1': 71, 'std_dev_test1': 15, 'N': 500},
    "XXYY": {'mean_test1': 71, 'std_dev_test1': 15, 'N': 400},
    "XXXX": {'mean_test1': 71, 'std_dev_test1': 15, 'N': 400},
}

two_to_four = {
    "XX": {'mean_test1': 1, 'std_dev_test1': 1.44, 'N': 1000},
    "XY": {'mean_test1': 0.5, 'std_dev_test1': 1.44, 'N': 1000},
    "XXY (Klinefelter Non Mosaic)": {'mean_test1': 2.55, 'std_dev_test1': 2.28, 'N': 2000},
    "XXY/XY (Klinefelter Mosaic)": {'mean_test1': 2.1, 'std_dev_test1': 0.5, 'N': 300},
    "XXX": {'mean_test1': 2.5, 'std_dev_test1': 1.73, 'N': 400},
    "XYY": {'mean_test1': 1.25, 'std_dev_test1': 0.5, 'N': 400},
    "X0 (Turner non mosaic)": {'mean_test1': 2.5, 'std_dev_test1': 1.75, 'N': 1500},
    "X0/XX (Turner mosaic: 50%)": {'mean_test1': 2.1, 'std_dev_test1': 1.75, 'N': 1500},
    "XXXY": {'mean_test1': 3, 'std_dev_test1': 1, 'N': 200},
    "XXYY": {'mean_test1': 3.1, 'std_dev_test1': 1, 'N': 200},
    "XXXX": {'mean_test1': 2.9, 'std_dev_test1': 1, 'N': 200},
}

four_to_eight = {
    "XX": {'mean_test1': 1, 'std_dev_test1': 1.44, 'N': 1000},
    "XY": {'mean_test1': 0.5, 'std_dev_test1': 1.44, 'N': 1000},
    "XXY (Klinefelter Non Mosaic)": {'mean_test1': 2.55, 'std_dev_test1': 2.28, 'N': 2000},
    "XXY/XY (Klinefelter Mosaic)": {'mean_test1': 2.1, 'std_dev_test1': 0.5, 'N': 300},
    "XXX": {'mean_test1': 2.5, 'std_dev_test1': 1.73, 'N': 400},
    "XYY": {'mean_test1': 1.25, 'std_dev_test1': 0.5, 'N': 400},
    "X0 (Turner non mosaic)": {'mean_test1': 2.5, 'std_dev_test1': 1.75, 'N': 1500},
    "X0/XX (Turner mosaic: 50%)": {'mean_test1': 2.1, 'std_dev_test1': 1.75, 'N': 1500},
    "XXXY": {'mean_test1': 3, 'std_dev_test1': 1, 'N': 200},
    "XXYY": {'mean_test1': 3.1, 'std_dev_test1': 1, 'N': 200},
    "XXXX": {'mean_test1': 2.9, 'std_dev_test1': 1, 'N': 200},
}

age_groups = [
    "1-2 years",
    "2-4 years",
    "4-8 years",
    ]

time_of_diagnosis = [
    "Prenatal",
    "Neonatal"
    ]

locations = [
    "USA/North America",
    "EU",
]

library_of_ages = [one_to_two, two_to_four]

#Create a way to be able t iterate through the genomes, N*100 times, each time for test score 1 or 2, use the sd and mean to generate a new value
    # You can also set an IF, to check if that grouop should be doing test 1 or 2

# Create an empty DataFrame to store extrapolated data
extrapolated_data = pd.DataFrame(columns=[
                                        'GeneticVariation',
                                        'AgeGroup',
                                        'DiagnosisTime',
                                        'Area',
                                        'Test Score',
                                        ]
                                    )

#Run ther for loop 3 times for each genome type, create three different dictionaries for each age group

# Runnig through number of possible age groups
counter2 = 0
for group in library_of_ages: #The list library_of_ages = [one_to_two, two_to_four]
    #Running through the genomes as keys to their own dictionaries
    counter = 0
    for keyDictionary in group.items(): #Running through the genomes
        genome = genome_types[counter]
        counter += 1
        # Extrapolate N
        for _ in range(int(keyDictionary["N"])):
            # Generate synthetic data
            synthetic_data = {
                'Genome': genome,
                'AgeGroup': age_groups[counter2],
                'DiagnosisTime': np.random.choice(["Prenatal", "Neonatal"], p=[0.5, 0.5]),
                'Area': np.random.choice(["USA/North America", "EU"], p=[0.5, 0.5]),
                'Test Score': np.random.normal(keyDictionary["mean_test1"], keyDictionary["std_dev_test1"])
            }
            # Append to the extrapolated_data DataFrame
            extrapolated_data = extrapolated_data.append(synthetic_data, ignore_index=True)
    counter2 += 1
# Save the extrapolated data to a CSV file
extrapolated_data.to_csv('extrapolated_data.csv', index=False)
