#!/home/avilash/anaconda3/envs/linevul/bin/python
import fire
import pandas as pd

def main(prediction_filepath, output_location):
    df = pd.read_csv(prediction_filepath)
    print(df.columns)
    df['prediction'] = df['raw_preds']
    for column_name in ('processed_func', 'flaw_line_index', 'flaw_line', 'raw_preds'):
        df = df.drop(column_name, axis=1)
    df.to_csv(output_location, index=False)
    print(df.head(10))

if __name__ == "__main__":
    try:
        fire.Fire(main)
    except fire.core.FireExit:
        print("Common error: not using flags to specify arguments (positional arguments disallowed)")
        print("Common error: not using quotations around input arguments")
        raise
