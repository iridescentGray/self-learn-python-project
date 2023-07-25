from config_loader import config

if __name__ == '__main__':
    print(type(config))
    print(config)
    print(config.get("demo"))
