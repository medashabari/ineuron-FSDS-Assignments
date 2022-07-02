import logging as log

try:
    log.basicConfig(filename="tasks.log", level=log.INFO, format='%(name)s %(levelname)s %(asctime)s %(message)s')
except Exception as e:
    print("Cannot create log file")


class String_qtns:

    # Try to extract data from index one to index 300 with a jump of 3

    def qtn1(self):
        data = """Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and 
        systems to extract knowledge and insights from noisy, structured and unstructured data,[1][2] and apply 
        knowledge and actionable insights from data across a broad range of application domains. Data science is related 
        to data mining, machine learning and big data.Data science is a "concept to unify statistics, data analysis,
        informatics, and their related methods"""
        return data[1:300:3]

    # Try to reverse a string without using reverse function

    def qtn2(self):
        s = "DaTa ScienCe"
        return s[::-1]

    # Try to split a string after conversion of entire string in uppercase

    def qtn3(self):
        s = "DaTa ScienCe"
        try:
            s = s.upper()
            return s, s.split()
        except Exception as e:
            return e

    # try to convert the whole string into lower case and Try to capitalize the whole string

    def qtn4_5(self):
        s = "daTa ScienCe"
        return s.lower(), s.capitalize()

    # Try to give an example of expand tab
    def qtn6(self):
        try:
            st = "DataScience\tDataAnalysis\tMachineLearning\tDeepLearning\tRL"
            st = st.expandtabs()
            return st
        except Exception as e:
            return e

    #  Give an example of strip , lstrip and rstrip

    def qtn7(self):
        s = "   Data Science  "
        return [s.strip(), s.lstrip(), s.rstrip()]

    #  Replace a string charecter by another charector by taking your own example and Try to give a defination of string
    #  center function with and exmple
    def qtn8(self):
        s = "DaTa ScienCe"
        return s.replace("a", "A", 2), s.center(30, "$")

try:
    str_qtns = String_qtns()
    log.info(str_qtns.qtn1())
    log.info(str_qtns.qtn2())
    log.info(str_qtns.qtn3())
    log.info(str_qtns.qtn4_5())
    log.info(str_qtns.qtn6())
    log.info(str_qtns.qtn7())
    log.info(str_qtns.qtn8())
except Exception as e:
    log.info(e)


class List_qtns:
    def __init__(self,l):
        self.l = l
    # Try to extract all the list entity

    def qtn1(self):
        for i in self.l:
            if type(i) == list:
                yield i

    # Try to extract all the dict enteties

    def qtn2(self):
        for i in self.l:
            if type(i) == dict:
                yield i

    #  Try to extract all the tuples entities

    def qtn3(self):
        for i in self.l:
            if type(i) == tuple:
                yield i

    #  Try to extract all the numerical data it may b a part of dict key and values

    def qtn4(self):
        for i in self.l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for ele in i:
                    if type(ele) == int:
                        yield ele
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int:
                        yield k
                    if type(v) == int:
                        yield v

    #  Try to give summation of all the numeric data
    def qtn5(self):
        sum = 0
        for i in self.l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for ele in i:
                    if type(ele) == int:
                        sum += ele
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int:
                        sum += k
                    if type(v) == int:
                        sum += v
        return sum

    #  Try to filter out all the odd values out all numeric data which is a part of a list

    def qtn6(self):
        for i in self.l:
            if type(i) == list:
                for ele in i:
                    if type(ele) == int:
                        if ele % 2 != 0:
                            yield ele

    # Try to extract "ineruon" out of this data

    def qtn7(self):
        return self.l[4]['k2'], self.l[5][0]

    # Try to find out a number of occurances of all the data

    def qtn8(self):
        d = {}
        for i in self.l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for ele in i:
                    if ele in d:
                        d[ele] += 1
                    else:
                        d[ele] = 1
            if type(i) == dict:
                for k, v in i.items():
                    if k in d:
                        d[k] += 1
                    else:
                        d[k] = 1
                    if v in d:
                        d[v] += 1
                    else:
                        d[v] = 1
        return d

    # Try to find out number of keys in dict element

    def qtn9(self):
        try:
            keys = self.l[4].keys()
            return len(keys)
        except Exception as e:
            return e

    # Try to filter out all the string data

    def qtn10(self):
        for i in self.l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for ele in i:
                    if type(ele) == str:
                        yield ele
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == str:
                       yield ele
                    if type(v) == str:
                        yield ele

    # Try to Find out alphanum in data

    def qtn11(self):
        for i in self.l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for ele in i:
                    if type(ele) == str:
                        if ele.isalnum():
                            yield ele
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == str:
                        if k.isalnum():
                            yield k
                    if type(v) == str:
                        if v.isalnum():
                            yield v

    # Try to find out multiplication of all numeric value in the individual collection inside dataset

    def qtn12(self):
        res = []
        for i in self.l:
            mul = 1
            if type(i) == list or type(i) == tuple or type(i) == set:
                for ele in i:
                    if type(ele) == int:
                        mul *= ele
                res.append(mul)
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int:
                        mul *= k
                    if type(v) == int:
                        mul *= v
                res.append(mul)

        return res

    # Try to unwrape all the collection inside collection and create a flat list

    def qtn13(self):
        flat_list = []
        for i in self.l:
            if type(i) == list or type(i) == tuple or type(i) == set:
                flat_list.extend(i)
            if type(i) == dict:
                for k, v in i.items():
                    flat_list.extend([k, v])
        return flat_list








l = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh", "k2" : "ineuron", "k3":
            "kumar", 3: 6, 7:8} , ["ineuron", "data science "]]
try:
    list_qtns = List_qtns(l)
    log.info(list(list_qtns.qtn1()))
    log.info(list(list_qtns.qtn2()))
    log.info(list(list_qtns.qtn3()))
    log.info(list(list_qtns.qtn4()))
    log.info(list_qtns.qtn5())
    log.info(list(list_qtns.qtn6()))
    log.info(list_qtns.qtn7())
    log.info(list_qtns.qtn8())
    log.info(list_qtns.qtn9())
    log.info(list(list_qtns.qtn10()))
    log.info(list(list_qtns.qtn11()))
    log.info([list_qtns.qtn12()])
    log.info([list_qtns.qtn13()])
except Exception as e:
    log.info(e)