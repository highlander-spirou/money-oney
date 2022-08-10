from global_config.configs import g as global_cfg

def test_global_variable():
    print(global_cfg.get_current_dir())


test_global_variable()