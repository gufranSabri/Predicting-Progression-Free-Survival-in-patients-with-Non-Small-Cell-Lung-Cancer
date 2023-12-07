import zipfile

def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Example usage:
zip_file_path = '/Users/gufran/Desktop/PfsPredictionLungCancer/pathology/tozip.zip'
extract_destination = '/Users/gufran/Desktop/PfsPredictionLungCancer/pathology'

extract_zip(zip_file_path, extract_destination)