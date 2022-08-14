from global_config.configs import g as global_cfg

def run(event, context):
    print(global_cfg.get_current_dir())