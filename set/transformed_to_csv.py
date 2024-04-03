#!/home/avilash/anaconda3/envs/linevul/bin/python
import fire
import os
import pandas as pd

from pathlib import Path

def main(predictions_location, input_dir, output_location):
    df = pd.read_csv(predictions_location)
    df = df[df['target'] == 1]
    df = df[df['raw_preds'] == True]
    true_positives = df['index'].tolist()
    result = []
    index = 0
    for true_positive in true_positives:
        input_folder = os.path.join(input_dir, f"{true_positive}")
        if not Path.exists(Path(input_folder)):
            print(f"Skipped failed or non-localized parse {true_positive}")
            continue
        for file in os.listdir(input_folder):
            output = {}
            input_filepath = os.path.join(input_folder, file)
            if not Path.exists(Path(input_filepath)):
                raise AssertionError(f"Improperly joined file {file} to folder {input_folder}")
            with open(input_filepath) as input_file:
                output['initial_index'] = true_positive
                output['filename'] = file
                output['target'] = 1
                output['processed_func'] = input_file.read()
                output['index'] = index
                output['flaw_line_index'] = None
                output['flaw_line'] = None
                index += 1
            result.append(output)
        print(input_folder)
    df = pd.DataFrame(result)
    df.to_csv(output_location, index=False)
    print(df.columns)

if __name__ == '__main__':
    try:
        fire.Fire(main)
    except fire.core.FireExit:
        print("Common error: not using flags to specify arguments (positional arguments disallowed)")
        print("Common error: not using quotations around input arguments")
        raise
