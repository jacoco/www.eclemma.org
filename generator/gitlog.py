"""API to read git log information
"""

import subprocess
import os, os.path

_PROPERTIES = (('commithash', '%H'),
               ('commitdate', '%ci'),
               ('committername', '%cn'),
               ('committeremail', '%ce'),
               ('subject', '%s'))
               
def get_log_info(file):
    file = os.path.abspath(file)
    repo_dir = _get_repo_dir(file)
    fmt = '%n'.join(map(lambda p : '='.join(p), _PROPERTIES))
    output = _execute(repo_dir, 'git', 'log', '-1', '--pretty=%s' % fmt, '--name-only', '--', file)
    lines = output.split('\n')
    info = {}
    for l in lines:
        if not l:
            # Empty line terminates the properties:
            break
        (key, value) = l.split('=')
        info[key] = value
    info['path'] = lines[-2]
    info['repo'] = os.path.basename(repo_dir)
    return info

def _get_repo_dir(file):
    dir = os.path.dirname(file)
    if os.path.isdir(os.path.join(dir, '.git')):
        return dir
    else:
        return _get_repo_dir(dir)

def _execute(cwd, *args):
    popen = subprocess.Popen(args, stdout=subprocess.PIPE, cwd=cwd)
    popen.wait()
    return popen.stdout.read()
