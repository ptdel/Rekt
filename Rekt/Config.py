import toml


class Config:
    """
    Fancy config class with sections as nested attributes.
    """

    def __init__(self, config):
        for k, v in config.items():
            if isinstance(v, dict):
                setattr(self, k, Config(v))
            else:
                setattr(self, k, v)


with open("config.toml", "r") as fp:
    config_file = toml.load(fp)

#: what should be imported by other classes.
configuration = Config(config_file)
