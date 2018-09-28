# coding=UTF-8


class Outputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    
    def output_result(self):
        fout = open('result.txt','w',encoding='utf-8')
        flag = 0
        for data in self.datas:
            if flag == 1:
                fout.write("""\n\n\n""");
            fout.write(str(data['id']) + '\n')
            fout.write("Title: %s"%data['title'] + '\n')
            fout.write("Absreact: %s"%data['abstract'])
            flag = 1
        print("Success!")
    
    
    



