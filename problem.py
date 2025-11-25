import ast 
class Problem:
    def __init__(self,prb_id,tit,des,cons,testcase,time_l,mem_l):
        #constructor

        if not prb_id or not isinstance(prb_id,str):
             raise ValueError("Problem ID must be a non-empty string")

        if not tit or not isinstance(tit,str):
            raise ValueError("Problem Title needs to ba a non empty string")

        if not des or not isinstance(des,str):
            raise ValueError("Description has to be a non empty string")

        if not cons or not isinstance(cons,str):
            raise ValueError("Constraints need to be given in right form")

        if not isinstance(testcase,list) or  len(testcase)==0:
            raise ValueError("Testcases have to list of tuples ")

        if not time_l or not isinstance(time_l,int):
            raise ValueError("Time limit needs to be an integer")

        if not mem_l or not isinstance(mem_l,int):
            raise ValueError("Memory limit needs to be an integer")



        self.problem_id=prb_id #problem id
        self.title=tit #title 
        self.description=des #description
        self.constraint=cons
        self.testcase=testcase #testcases list of tuples
        self.time_limit=time_l #time limit
        self.memory_limit=mem_l #memory limit

    
    def duplicate_entries(self,s,data):

        t="Description" if(s==0) else "Testcases"
        file_name = self.problem_id + t

        try:
            with open(file_name,"r") as fp:
                l=fp.readlines()

                for i in l:
                    if i.strip()==str(data):
                        return 1

                return 0

        except FileNotFoundError:
            print("File not found so no duplicate exists")
            return 0

        except Exception as e:
            print("Unknown Error has occured")
            return -1


                
    def write_problem(self):

        file_name = self.problem_id + "Description" #file name
        try:
            with open(file_name,"w") as fp:
                s = self.title + "\n" + self.description + '\n' + self.constraint #writning the problem statemt in a file
                fp.write(s)

        except Exception as e:
            print(f"Error occured {e}")
            return -1

    
        
    def write_testcase(self):
        l = self.testcase
        file_name = self.problem_id + "Testcases" #self constructing  the file name

        try:
            with open(file_name,"w") as fp: #better coz automatically closes the files
                for i in l:
                    s = str(i) + "\n"
                    fp.write(s)

        except Exception as e:
            print(f"Unkowon Error {e}")
            return -1

      
                
            
    def show_problem(self):
        # show the entire problem cf style
        file_name = self.problem_id + "Description"

        try:
            with open(file_name,"r") as fp: # for descripttion
                s=fp.read()
                print(s)
            
        except FileNotFoundError:
            print("No such problem exists") #except block

        
        file_name1 = self.problem_id + "Testcases" #format the file name
         

        try:
            with open(file_name1,"r") as fp1: # using with
                while(True):
                    s=fp1.readline()
                    if(s!=""):
                        print(s,end="")

                    else:
                        break

        except FileNotFoundError: # using except 
            print("No such problem")


    def get_all_testcases(self):
        file_name = self.problem_id + "Testcases"

        try:
            with open(file_name,"r") as fp:

                l=[]

                while(True):
                    s=fp.readline()
                    if(s!=""): # i am returning [[(1,2,3),(2,3,4)]] vvimp for each line
                        l.append(ast.literal_eval(s.strip()))

                    else:
                        break
                return l

        except FileNotFoundError:
            print("Could not open the file")
            return []

    
    def judge_test_cases(self):
        testjudge = []

        for i in self.testcase:
            output = i[-1] # last element is output of problem
            input_j = i[:len(i)-1] # extracting inputs
            input_jstr = " ".join(map(str,input_j)) # conversion
            outputstr = str(output) # string conversion

            testjudge.append((input_jstr,outputstr))

        return testjudge







        
        

       


       


        











    


           
        


    



        


        










    



    