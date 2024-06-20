import csv
import random

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


def generate_data(dictionary, age_group):
    data_points = []
    for key, values in dictionary.items():
        for _ in range(values['N']):

            # Create an if statement that checks age-group and as a rresult sets the values for the other test to None, so have all tests present in every dummy data point
            data_point = {
                'Genome': key,
                'Age Group': age_group,
                'Area': 'US' if random.choice([True, False]) else 'EU',
                'Diagnosis Time': 'Prenatal' if random.choice([True, False]) else 'Neonatal',
                'Score': random.normalvariate(values['mean_test1'], values['std_dev_test1'])
            }
            data_points.append(data_point)
    return data_points

if __name__ == "__main__":
    one_to_two_data = generate_data(one_to_two, '1-2')
    two_to_four_data = generate_data(two_to_four, '2-4')

    all_data = one_to_two_data + two_to_four_data

    # Write data to CSV file
    fields = ['Genome', 'Age Group', 'Area', 'Diagnosis Time', 'Score']

    with open('output_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)