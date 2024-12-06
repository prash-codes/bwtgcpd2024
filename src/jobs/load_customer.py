import csv

# Define the schema and generate 10,000 sample records
headers = ["S_ID", "S_FNAME", "S_MNAME", "S_LNAME", "S_EDUCATION", "S_PASSINGYEAR", "S_MOBILENO", "S_EMAILID"]
records = []

# Generate records
for i in range(1, 10001):
    record = [
        1000 + i,  # S_ID
        f"FirstName{i}",  # S_FNAME
        None if i % 5 == 0 else f"MiddleName{i}",  # S_MNAME
        f"LastName{i}",  # S_LNAME
        f"Degree{i % 50}",  # S_EDUCATION
        2000 + (i % 24),  # S_PASSINGYEAR
        f"9{str(i).zfill(9)}",  # S_MOBILENO
        None if i % 7 == 0 else f"user{i}@example.com",  # S_EMAILID
    ]
    records.append(record)

# Save to CSV
output_file_path = '/mnt/data/BW_STUDENTINFO.csv'
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the header
    writer.writerows(records)  # Write all rows

output_file_path
