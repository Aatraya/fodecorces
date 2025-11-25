import os
import time
import sys
from problem import Problem
from judge1 import Judge
from submissions import submissions, create_submission_directory



i=0

#making base directory where my submission go into
base_dir = "submission_data"
os.makedirs(base_dir, exist_ok=True) #making sure it exists

# intialising the judging system

judge_sys = Judge()


def load_existing_problem():
    for files in os.listdir():
        if files.endswith("Description"):
            prb_id = files.replace("Description","")
            test_file = prb_id + "Testcases"


            if not os.path.exists(test_file):
                continue

            with open(files,"r") as fp:
                descp = fp.readlines()
                title = descp[0]
                des = descp[1]
                cons = descp[2]

            tests = []
            with open(test_file,"r") as fp:
                for i in fp:
                    tests.append(eval(i.strip()))

            prb = Problem(prb_id , title , des , cons , tests , 1, 64)
            problems[prb_id]=prb

                
def createProblemW():
    # Write problem description and testcases to files
    prb.write_problem()
    prb.write_testcase()
    print(f"Problem {prbid} created.")



def doSubmit():
    subid = i #clarify once
    uid = input("Enter user id: ")
    pid = input("Enter the problem id: ")
    try:
        prb = problems[pid]
    except KeyError:
        print("FodeCorces doesn't host this problem.")
        return
    
    lang = input("Enter language: (python/c/cpp) : ")
    if lang not in ["python","c","cpp"]:
        print("Language is not supported")
        return 

    def get_code_from_terminal():
        print("Paste your code below (press Ctrl+D or Ctrl+Z then Enter to finish):")
        # Reads all lines until EOF (Ctrl+D on Linux/macOS, Ctrl+Z on Windows)
        code_input = sys.stdin.read()
        return code_input

    subcode = get_code_from_terminal()

    if not subcode.strip():
        print("Empty code submitted")
        return 

    if prb is None:
        print("Problem dont exist bruh")
        return


    
    timestamp = time.time()

    sub = submissions(
        subid,
        uid,
        pid,lang,
        subcode,
        timestamp
        )

    code_path = sub.get_code(base_dir)
    sub.metadata()
    print(f"Submission {subid} saved to: {code_path}")
    testcases_judge = prb.judge_test_cases()
    print("\nStarting judge ")
    result = judge_sys.judge(code_path, lang, testcases_judge)

    print("Judge result:")

    if (result.get("status")== "COMPILE_ERROR"):
        print("**Compilation Error** - Code failed to compile")
        return 

    print(f"Overall Status: **{result['overall']}**")


    for detail in result['details']: #displaying the results 
        print(f"Input: '{detail['input']}' | Status: {detail['status']}")
        if detail['status'] == 'FAIL':
            print(f"  Got: {detail['got']} | Expected: {detail['expected']}") # showing comparison of test cases

problems={}
load_existing_problem()
while True:
    print("Menu options:")
    print("1. Create a problem: ")
    print("2. View problem")
    print("3. Submit a problem: ")
    print("4. Exit")

    try:
        choice = int(input("Enter the choice: "))

    except ValueError:
        print("Enter a valid number")
        continue

    if(choice==1):
        prbid = input("Enter problem id: ")

        if not prbid:
            print("Problem id cannot be empty")
            continue

        titl = input("Enter problem title: ")

        if not titl:
            print("Title cannot be empty")
            continue

        des = input("Enter description for problem: ")

        if not des:
            print("Description cannot be empty")
            continue

        cons = input("Enter constraints: ")

        if not cons:
            print("Constraints cannot be empty")
            continue

        tests = eval(input("Enter the test cases as list of tuples where each element is a string: "))

        if not tests:
            print("Testcases need to be given")
            continue

        tl = int(input("Enter time limit (in seconds): "))

        if not tl:
            print("Give a time limit")
            continue

        if tl<0:
            print("Non negative time limits must be given")
            continue

        ml = int(input("Enter Memory limit (in MB): "))

        if not ml:
            print("Give a Memory limit")
            continue

        if ml<0:
            print("Non negative memory limit must be given")

        prb = Problem(
                    prbid, 
                    titl, 
                    des, 
                    cons, 
                    tests, 
                    tl, 
                    ml
                )
        problems[prbid]=prb

        createProblemW()

    elif (choice==2):
        pid = input("Enter problem id")

        if pid not in problems:
            print("No such problem")
            continue

        prb = problems[pid]
        prb.show_problem()
    elif(choice==3):
        doSubmit()
        i+=1

    elif (choice==4):
        print("Thanks for believing in the idea of FodeCorces. We hope you solve again soon.")
        break

    else:print("You did not enter a correct choice, please try again")









    
