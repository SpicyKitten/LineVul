#!/home/avilash/anaconda3/envs/linevul/bin/python
import fire
import os
import pandas as pd


def main(predictions_file, output_file):
    df = pd.read_csv(predictions_file)
    print(df.columns)
    df = df[['index', 'target', 'file_name', 'processed_func', 'raw_preds']]
    df = df[df['target'] == 1]
    df = df[df['raw_preds'] == True]
    df = df[['index', 'processed_func']]
    prefix = output_file
    def write(row):
        index, func = row
        output_filepath = os.path.join(prefix, f"{index}.c")
        with open(output_filepath, 'w') as output_file:
            output_file.write(str(func))
            print(output_filepath)
    df.apply(write, axis=1)


if __name__ == '__main__':
    try:
        fire.Fire(main)
    except fire.core.FireExit:
        print("Common error: not using flags to specify arguments (positional arguments disallowed)")
        print("Common error: not using quotations around input arguments")
        raise
