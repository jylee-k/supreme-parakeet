import os
import requests
from tqdm import tqdm
import pandas as pd


# Global variables
asr_endpoint = 'http://localhost:8001/asr'
data_dir = '/Users/jylee/Downloads/common_voice/cv-valid-dev/cv-valid-dev' # Path to cv-valid-dev directory
csv_path = '/Users/jylee/Downloads/common_voice/cv-valid-dev.csv' # Path to original cv-valid-dev.csv

# Get the sorted list of files
filenames = os.listdir(data_dir)
filenames.sort()
assert len(filenames) == 4076, 'Number of files in cv-valid-dev =/= 4076. Please check your data_dir' # Number of files in cv-valid-dev

def get_transcription(filepath):
    """
    Retrieves the transcription of the audio file located at the given filepath.

    Args:
        filepath (str): The path to the audio file.

    Returns:
        str: The transcription of the audio file.
    """
    response = requests.post(
        url = asr_endpoint,
        files={'file': open(filepath, 'rb')}
    )
    return response.json()['transcription']


# Loop through each file and get the transcription
transcription_list = []
for filename in tqdm(filenames):
    filepath = os.path.join(data_dir, filename)
    transcription = get_transcription(filepath)
    transcription_list.append(transcription)

# Read csv file into pandas dataframe
df = pd.read_csv(csv_path) # Path to original cv-valid-dev.csv

# Add the transcription to the dataframe
df['generated_text'] = transcription_list

# Save the dataframe to a new csv file
df.to_csv('asr/cv-valid-dev.csv', index=False)