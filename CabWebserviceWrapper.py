import requests
import json
import pandas as pd

class CabWrapper:
    def __init__(self,
    analyzer='default',
    format='json',
    clean='1',
    pretty='1',
    raw='1',
    exlex='0',
    output='raw'):
        self.analyzers = ['caberr','caberr1','default','default1','default1.1600-1700','default1.1700-1800','default1.1800-1900','expand','expand.1600-1700','expand.1700-1800','expand.1800-1900','expand.all','expand.eqlemma','expand.eqpho','expand.eqrw','expand.ext','expand.gn','expand.gn-asi','expand.gn-isa','expand.gn-syn','expand.ot','expand.ot-asi','expand.ot-isa','expand.ot-syn','lemma','lemma.1600-1700','lemma.1700-1800','lemma.1800-1900','lemma1','lemma1.1600-1700','lemma1.1700-1800','lemma1.1800-1900','norm','norm.1600-1700','norm.1700-1800','norm.1800-1900','norm.hlgl','norm1','norm1.1600-1700','norm1.1700-1800','norm1.1800-1900','norm1.hlgl']
        self.analyzer = analyzer
        self.format = format
        self.clean = clean
        self.pretty = pretty
        self.raw = raw
        self.exlex = '0'
        self.output = output
        self.exampleText = 'Ick bin een groszer Aff. Unnt du biszt ein kleines Katz.\nIck bin een kleins Hundt. Unnt du biszt ein groszes Elevandt.'
        self.baseurl =  f'https://kaskade.dwds.de/demo/cab/query?'

    def __repr__(self):
        return f'CAB-Wrapper: Analyzer: {self.analyzer}, Format: {self.format}'

    def __str__(self):
        return f'CAB-Wrapper: Analyzer: {self.analyzer}, Format: {self.format}, Output: {self.output}'

    @property
    def analyzer(self):
        # Weitere Logik
        return self.__analyzer

    @analyzer.setter
    def analyzer(self, analyzer):
        if(analyzer in self.analyzers):
            self.__analyzer = analyzer
        else:
            print('Analyzer not found. Analyzer set to "default".')
            self.__analyzer = 'default'


    @property
    def format(self):
        # Weitere Logik
        return self.__format

    # Setter
    @format.setter
    def format(self, format):
        if(format in ['json','text','csv', 'raw','ltwxml', 'dataframe', 'list']):
            self.__format = format
        else:
            print('Format not found. Format set to "json".')
            self.__format = 'json'

    @property
    def output(self):
        # Weitere Logik
        return self.__output

    # Setter
    @output.setter
    def output(self, output):
        self.__output = output

    ####
    def getText(self, text=''):
        if(text == ''):
            text = self.exampleText

        print('Text:', text.split('\n'))
        output = []
        output_text = ''

        for i in text.split('\n'):
            query_parameters = {
                'a': self.analyzer,
                'fmt': self.format,
                'clean': self.clean,
                'pretty': self.pretty,
                'raw': self.raw,
                'q': i
            }

            if(self.format in ['dataframe', 'list']):
                query_parameters['fmt'] = 'json'

            r = requests.get(self.baseurl, params=query_parameters)

            if(r.status_code != 200):
                print(f'Error Code: {r.status_code}\nError Text: {r.text}')

            if(self.format in ['text','csv','raw']):
                output_text = output_text + r.text
            elif(self.format in ['ltwxml']):
                output_text = output_text + "\n".join(r.text.split('\n')[2:-2])
            elif(self.format in ['json', 'dataframe', 'list']):
                json = r.json()
                for sentence in json['body']:
                    sent = []
                    for token in sentence['tokens']:
                        if(self.format != 'list'):
                            word = {}
                            if('word' in self.output):
                                word['word'] = token['moot']['word']
                            if('lemma' in self.output):
                                word['lemma'] = token['moot']['lemma']
                            if('pos' in self.output):
                                word['pos'] = token['moot']['tag']
                            if(len(word.keys()) == 0):
                                word['word'] = token['moot']['word']
                        else:
                            word = token['moot']['word']
                        sent.append(word)
                    output.append(sent)

        if(self.format in ['text','csv','raw']):
            print(output_text)
            return output_text
        elif(self.format in ['ltwxml']):
            output_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<text>\n' + output_text + '\n</text>'
            print(output_xml)
            return output_xml
        elif(self.format in ['dataframe']):
            columns = []
            if('word' in self.output):
                columns.append('word')
            if('lemma' in self.output):
                columns.append('lemma')
            if('pos' in self.output):
                columns.append('pos')
            df = pd.DataFrame(columns=columns)
            for sent in output:
                ap = pd.DataFrame.from_dict(sent)
                df = df.append(ap, sort=False)
            print(df)
            return df
        else:
            if(len(output) == 1):
                output = output[0]
            print(output)
            return output

if __name__ == "__main__":
    import getopt
    import sys

    try:
        opts, args = getopt.getopt(sys.argv[1:],"ha:f:o:t:",["help","analyzer=","format=","output=", "text="])
    except getopt.GetoptError:
        print('Help: cab-webservice-wrapper.py -a <analyzer> -f <format> -o <output> -t <text>')
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('Help: cab-webservice-wrapper.py -a <analyzer> -f <format> -o <output> -t <text>')
            sys.exit()
        elif opt in ("-a", "--analyzer"):
            analyzer = arg
        elif opt in ("-f", "--format"):
            formating = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-t", "--text"):
            text = arg


    CAB = CabWrapper()

    try:
        CAB.analyzer = analyzer
    except:
        CAB.analyzer = 'default'
    try:
        CAB.format = formating
    except:
        CAB.format = 'json'
    try:
        CAB.output = output
    except:
        CAB.output = 'raw'
    try:
        text = text
    except:
        text = ''

    print(CAB)
    CAB.getText(text)
