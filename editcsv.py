import pandas as pd

#Load the CSV file
df = pd.read_csv('synonyms.csv')

# Keep only the first synonym and antonym for each word
df['Words'] = df['Words'].apply(lambda x: ' '.join(x.split()[1:]) if pd.notnull(x) else x)
df.to_csv('edited_file.csv', index=False)

with open('edited_file.csv', 'r') as infile:
    with open('edited_synonyms.csv', 'w') as outfile:
        for line in infile:
            # Replace space between words and synonyms with an empty string
            updated_line = line.replace(', ', ',')
            outfile.write(updated_line)


with open('antonyms.csv', 'r') as infile:
    with open('edited_antonyms.csv', 'w') as outfile:
        for line in infile:
            # Split the space-delimited values and join them with commas
            comma_delimited_line = ','.join(line.strip().split())
            outfile.write(comma_delimited_line + '\n')
