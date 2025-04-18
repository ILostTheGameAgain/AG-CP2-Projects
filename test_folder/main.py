import pandas as pd

items = {
    "name": ["1", "2", "3"],
    "playlists": [['1','2','3'],['1','2','3'],['1','2','3']]
}

pd.DataFrame(items).to_csv("test_folder/file.csv")

playlists = {

}


for ind, val in enumerate(items['playlists']):
    for x in val:
        if x not in playlists.keys():
            playlists[x] = []
        playlists[x].append(items["name"][ind])

print(playlists)