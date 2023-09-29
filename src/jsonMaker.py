def jsonMaker(names):
    for name in names:
        f = open(name, 'r', encoding='utf-8')
        f = f.readlines()
        jsonString = '{'
        for line in f:
            jsonString += line.replace('\n','')+','
        jsonString += '}'
        jsonString = jsonString.replace("}',","},")
        f = open('./db/'+name.replace('./rawInfo/','').replace(".txt",".json"),"w",encoding='utf-8')
        f.write(jsonString.replace(',}','}'))
        f.close()