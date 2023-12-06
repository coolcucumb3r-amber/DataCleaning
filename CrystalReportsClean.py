import pandas 

def clean_data(input_file, output_file):
    # Read data from Crystal Report export (export as a CSV file)
    df = pandas.read_csv(input_file)

    # Filter out records where age is less than 0
    df = df[df['Age'] >= 0]

    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file_path = "path/file.csv"
    output_file_path = "path/cleaned_data.csv"

    clean_data(input_file_path, output_file_path)

    print("Data cleaning completed. Saved to", output_file_path)

