import os
import numpy as np
import pandas as pd
import argparse

def parse_args_():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_folder', type=str, required=True, help='Path to the data folder')
    parser.add_argument('--dataset', type=str, required=True, help='Name of the dataset')
    return parser.parse_args()

def preprocess_data(data_path, dataset_name):
    if dataset_name == 'elect':
        data_frame = pd.read_csv(data_path, sep=";", header=0, index_col=0, parse_dates=True, decimal=',')
        data_frame.to_csv(data_path.replace('.txt', '.csv'), sep=',', decimal='.')
        
        data_frame = pd.read_csv(data_path.replace('.txt', '.csv'), sep=',', header=0, index_col=0, parse_dates=True)
        data_frame = data_frame.fillna(0)
        
        data_array = np.array(data_frame)
        
        np.save(os.path.join(os.path.dirname(data_path), 'data_elect.npy'), data_array)
        
        split_idx = int(0.7 * len(data_array))
        train_data = data_array[:split_idx]
        valid_test_data = data_array[split_idx:]
        
        valid_idx = int(0.5 * len(valid_test_data))
        valid_data = valid_test_data[:valid_idx]
        test_data = valid_test_data[valid_idx:]
        
        np.save(os.path.join(os.path.dirname(data_path), 'train_data_elect.npy'), train_data)
        np.save(os.path.join(os.path.dirname(data_path), 'valid_data_elect.npy'), valid_data)
        np.save(os.path.join(os.path.dirname(data_path), 'test_data_elect.npy'), test_data)

    elif dataset_name == 'exchange':
        # Read the exchange rate data without headers
        data_frame = pd.read_csv(data_path, header=None)
        data_frame = data_frame.fillna(0)  # Fill missing values if necessary
        
        data_array = np.array(data_frame)
        
        np.save(os.path.join(os.path.dirname(data_path), 'data_exchange.npy'), data_array)
        
        split_idx = int(0.7 * len(data_array))
        train_data = data_array[:split_idx]
        valid_test_data = data_array[split_idx:]
        
        valid_idx = int(0.5 * len(valid_test_data))
        valid_data = valid_test_data[:valid_idx]
        test_data = valid_test_data[valid_idx:]
        
        np.save(os.path.join(os.path.dirname(data_path), 'train_data_exchange.npy'), train_data)
        np.save(os.path.join(os.path.dirname(data_path), 'valid_data_exchange.npy'), valid_data)
        np.save(os.path.join(os.path.dirname(data_path), 'test_data_exchange.npy'), test_data)

        # If labels are separate, ensure they are saved as well
        # Assuming the last column is the label
        train_labels = train_data[:, -1]
        valid_labels = valid_data[:, -1]
        test_labels = test_data[:, -1]

        train_data = train_data[:, :-1]
        valid_data = valid_data[:, :-1]
        test_data = test_data[:, :-1]

        np.save(os.path.join(os.path.dirname(data_path), 'train_label_exchange.npy'), train_labels)
        np.save(os.path.join(os.path.dirname(data_path), 'valid_label_exchange.npy'), valid_labels)
        np.save(os.path.join(os.path.dirname(data_path), 'test_label_exchange.npy'), test_labels)

if __name__ == '__main__':
    args = parse_args_()
    data_path = os.path.join(args.data_folder, 'LD2011_2014.txt' if args.dataset == 'elect' else 'exchange_rate.txt')
    preprocess_data(data_path, args.dataset)