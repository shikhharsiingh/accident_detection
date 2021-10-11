import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def labels_to_csv(path):
    files = []
    for x_file in glob.glob(path + "/*.xml"):
        tree = ET.parse(x_file)
        root = tree.getroot()
        for elem in root.findall('object'):
            datapoint = (root.find('filename').text,
            elem[0].text,
            int(elem[4][0].text),
            int(elem[4][1].text),
            int(elem[4][2].text),
            int(elem[4][3].text),
            )
        files.append(datapoint)
    col_name = ['filename', 'class', 'xmin', 'xmax', 'ymin', 'ymax']
    df = pd.DataFrame(files, columns = col_name)
    return df

# For the function, you need images/train and images/test directories with respective images and label xml files inside your root directory
if __name__ == "__main__":
    for directory in ['train', 'test']:
        img_pth = os.path.join(os.getcwd(), 'images/{}'.format(directory))
        df = labels_to_csv(img_pth)
        df.to_csv('dat/{}_labels.csv'.format(directory), index = None)
        print("Succesfully converted xml to csv")