from models.Engine import Engine

datas = ["toto", "tata", "tutu", "été", "2023-06-30"]

# exemple d'utilisation
# print(Engine(datas).passwords)
# print(len(Engine(datas).passwords))
# print(Engine(datas, ["upper", "lower", "capitalize"]).passwords)
print(Engine(datas, ["upper", "lower", "capitalize", "accent", "leet", "char"]).passwords)
# print(len(Engine(datas, ["upper", "lower", "capitalize", "accent", "leet", "char"]).passwords))