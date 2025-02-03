import csv


def merge_csv(list_of_input_files: list, output_file: str):
    merged_data = []
    headers = []
    for input_file in list_of_input_files:
        with open(input_file, 'r') as ro_handle:
            csv_reader = csv.DictReader(ro_handle)
            for field_name in csv_reader.fieldnames:
                if field_name not in headers:
                    headers.append(field_name) 
            
            for dict_row in csv_reader:
                merged_data.append(dict_row)

    with open(output_file, 'w') as w_handle:
        csv_writer = csv.DictWriter(w_handle, headers)
        csv_writer.writeheader()
        csv_writer.writerows(merged_data)


# commands used in solution video for reference
if __name__ == '__main__':
    merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
