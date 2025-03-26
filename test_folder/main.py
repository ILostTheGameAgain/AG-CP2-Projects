import pandas as pd

df= pd.read_csv('test_folder/file.csv')

print(df)
dictionary_data = df.to_dict()
#print(dictionary_data)
dictionary_data = pd.DataFrame(dictionary_data)
#print(dictionary_data.describe())
print(dictionary_data)
dictionary_data.to_csv('test_folder/file2.csv', index=False)

import pandas as pd  
  
