#!/usr/bin/env python2.7

env_vars = {
    'AWS_ACCESS_KEY_ID': None,
    'AWS_SECRET_ACCESS_KEY': None
}

def clear_env_vars():
    for var in env_vars.iterkeys():
        # 'None' ensures no error if var doesn't exist. Doing it this way saves
        # a lookup to see if it's in the environment.
        env_vars[var] = os.environ.pop(var, None)

def restore_env_vars():
    for var in env_vars.iterkeys():
        if env_vars[var]:
            os.environ[var] = env_vars[var]

def set_profile(env):
    if env == 'production':
        os.environ['AWS_PROFILE'] = 'vericity-deploy-production'
    else:
        os.environ['AWS_PROFILE'] = 'vericity-deploy-development'
