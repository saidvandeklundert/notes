import configparser

cfg = configparser.ConfigParser()
cfg.read("example.ini")
print(cfg.sections())
print(cfg.get("section-x", "name"))
