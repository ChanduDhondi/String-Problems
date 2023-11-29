""" Here we are trying to search substring inside the given string"""

class Substring_search:
    
    def logic1(self,strg,sub_str):
        self.result = []
        if sub_str in strg:
            i = strg.find(sub_str)
            while i != -1:
                self.result.append(i)
                i = strg.find(sub_str,i+1)
            return self.result
        else:
            print('Given word in not there in String')
        
    def logic2(self,strg,sub_strg):
        self.result= []
        for i in range(len(strg)):
            if strg.startswith(sub_str,i):
                self.result.append(i)
        return self.result
           
if __name__ == '__main__':
    strg = "I liked the movie, acting in movie was Great!"
    sub_str = "movie"
    a = Substring_search()
    print(a.logic1(strg,sub_str))
    print(a.logic2(strg,sub_str))