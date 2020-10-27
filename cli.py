import click
import numpy as np
import pandas as pd
from PIL import Image
import time
import os

def score(image1, image2):
    #a simple mean squared err calculations on the images' pixel intensity is used to score similarity
    return np.sum((image1.astype("float") - image2.astype("float")) ** 2) / float(image1.shape[0] * image1.shape[1])

#prompt='CSV path'
@click.command()
@click.option('--file', prompt='Input CSV path',
              help='path to csv file')
@click.option('--output', default=f'{os.getcwd()}/img_compare_{time.strftime("%Y-%m-%d %H-%M-%S")}.csv', help='output csv location')
def main(output, file):
    df = pd.read_csv(file)
    # click.echo(df)
    # rerun
    return_df = pd.DataFrame(columns=['image1', 'image2', 'similar', 'elapsed'])
    for index, row in df.iterrows():
        start_time = time.time()
        similarity = score(np.asarray(Image.open(row['image1']).resize((1280, 720))), np.asarray(Image.open(row['image2']).resize((1280, 720))))
        r = {
            'image1': row['image1'],
            'image2': row['image2'],
            'similar': similarity,
            'elapsed': time.time() - start_time
        }
        return_df = return_df.append(r, ignore_index=True)
    click.echo(return_df)
    return_df.to_csv(output, index=False, header=True)


if __name__ == '__main__':
    main()
