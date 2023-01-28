#!/usr/bin/env python3

import os

def add(config_dir, target_dir):
    """
    Creates `target_dir/* -> config_dir/*` symlinks, deleting existing targets.
    """
    if not os.path.exists(config_dir):
        raise ValueError(f'Error: config dir {config_dir} does not exist')
    elif not os.path.exists(target_dir):
        raise ValueError(f'Error: target dir {target_dir} does not exist')

    for config in os.listdir(config_dir):
        config_path = f'{config_dir}/{config}'
        target_path = f'{target_dir}/{config}'
        print(f'{target_path} -> {config_path}')
        try:
            os.symlink(config_path, target_path)
        except FileExistsError:
            os.unlink(target_path)
            os.symlink(config_path, target_path)

def remove(config_dir, target_dir):
    """
    Removes the targets for a given config.
    """
    if not os.path.exists(config_dir):
        raise ValueError(f'Error: config dir {config_dir} does not exist')
    elif not os.path.exists(target_dir):
        raise ValueError(f'Error: target dir {target_dir} does not exist')

    for config in os.listdir(config_dir):
        target_path = f'{target_dir}/{config}'
        print(f'Removing {target_path}')
        try:
            os.unlink(target_path)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    home_dir = os.path.expanduser(os.getenv('HOME'))
    
    zsh_config = os.path.join(current_dir, 'zsh')
    zsh_target = home_dir
    add(zsh_config, zsh_target)


