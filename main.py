from models.Engine import Engine

datas = ["manger", "boire", "toto", "tata", "tutu", "été"]

# exemple d'utilisation
# print(Engine(datas).passwords)
# print(len(Engine(datas).passwords))
# print(Engine(datas, ["upper", "lower", "capitalize"]).passwords)
print(len(Engine(datas, ["upper", "lower", "capitalize", "accent", "leet", "char"]).passwords))