import os
import re
import shutil
import pandas as pd
class Transfer:
    def __init__(self):
        pass

    def get_data(self, folder_name='dataloaders', filename='information.csv'):
        path = os.path.join(folder_name, filename)

        data = pd.read_csv(path, delimiter=',', usecols=['name', 'action', 'coordinates'])
        return data

    def create_directories(self, column_names, folder_name='final_data'):

        for name in column_names:
            name = os.path.join(folder_name, name)
            os.makedirs(name)

    def get_videos(self, df, base_folder, src_folder="final_data"):
        dir_names = os.listdir(base_folder)
        print(dir_names)
        print(len(df))
        file_names = set(list(df.name))
        print(len(file_names))

        count = 0

        for folder in dir_names:
            folder_name = os.path.join(base_folder,folder)
            if folder_name == base_folder+'/'+'.DS_Store':
                continue
            for file_name in os.listdir(folder_name):
                pattern = re.compile(r"^[^.]*")
                file = re.search(pattern, file_name).group(0)
                if file in file_names:
                    count += 1
                    action_name = df[df['name'] == file]["action"].values[0]
                    shutil.copy(folder_name+"/"+file_name, src_folder+"/"+action_name)
        print(count)



if __name__ == '__main__':
    t = Transfer()

    data = t.get_data('dataloaders', 'information.csv')
    column_names = data.action.unique()
    #t.create_directories(column_names, 'final_data')
    #t.get_videos(data, 'data')
    t.create_files()