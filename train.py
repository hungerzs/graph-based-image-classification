from __future__ import print_function

import argparse
import sys
import os
import json

import tensorflow as tf

# Possible arguments (look up each help parameter for additional information)
DATA = './data'
NETWORK_PARAMS = './network_params.json'
LEARNING_RATE = 1e-3
EPOCHS = int(1e5)  # 50.000
CHECKPOINT_EVERY = 50


# Parses the given arguments and overrides their corresponding default values.
# Returns all arguments as a dictionary.
def get_arguments():
    parser = argparse.ArgumentParser(description='Training script for the '
                                     'Graph-based Image Classification')

    parser.add_argument('--data', type=str, default=DATA,
                        help='The directory containing the training samples')
    parser.add_argument('--network_params', type=str, default=NETWORK_PARAMS,
                        help='JSON file with the network parameters')
    parser.add_argument('--learning_rate', type=float, default=LEARNING_RATE,
                        help='Learning rate for training')
    parser.add_argument('--epochs', type=int, default=EPOCHS,
                        help='Number of training steps')
    parser.add_argument('--checkpoint_every', type=int,
                        default=CHECKPOINT_EVERY,
                        help='How many steps to save each checkpoint after')

    return parser.parse_args()


def save(saver, sess, checkpoint_dir, step):
    print('Storing checkpoint to %s...' % (checkpoint_dir), end=' ')
    sys.stdout.flush()  # don't wait for buffer before writing to the terminal

    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)

    model_name = 'model.ckpt'
    checkpoint_path = os.path.join(checkpoint_dir, model_name)

    # save checkpoint with version suffix
    saver.save(sess, checkpoint_path, global_step=step)

    print('Done.')


def main():
    args = get_arguments()

    # load the json network parameter from disk
    with open(args.network_params, 'r') as f:
        network_params = json.load(f)


# only run if the script is executed directly
if __name__ == '__main__':
    main()
