import pandas as pd # Import pandas library

# Read parquet file using the read_parquet function and the pyarrow engine
data = pd.read_parquet('filename.parquet', engine='pyarrow')

