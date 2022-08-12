from global_config.configs import g as cfg


def run(event, context):
    print(cfg.get_current_dir())