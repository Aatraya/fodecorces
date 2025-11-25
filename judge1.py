import subprocess
#import psutils
#import times
import os

class Judge:
    def __init__(self, tl=3):
        self.time_limit = tl

    def compile_code(self, path, language):#returns a list of commands to execute in cmd
        if language == "python":
            return path
        output_file = path + "_out"
        if language == "c":
            cmd = ["gcc", path, "-o", output_file]
        elif language == "cpp":
            cmd = ["g++", path, "-o", output_file]

        try:
            subprocess.run(cmd, capture_output=True, timeout=self.time_limit)
            return output_file
        except:
            print("Compilation error")
            return None

    def run(self, exe_path, input_data, language):
        try:
            if language == "python":
                cmd = ["python3", exe_path]
            elif language in ("c", "cpp"):
                cmd = [exe_path]
            result = subprocess.run(cmd,input=input_data.encode("utf-8"),capture_output=True,timeout=self.time_limit)
            return result.stdout.decode("utf-8").strip(), None
        except subprocess.TimeoutExpired:
            print("Time Limit Exceeded")
            return None, "TLE"
        except Exception as error:
            return None, "The error is " +str(error)

    def judge(self, path, language, testcases):#testcases is a list of tuples where first is input string and second is output string
        exe = self.compile_code(path, language)
        if exe is None:
            return {"status": "COMPILE_ERROR"}
        results = []
        all_have_passed = True
        for input, expected in testcases:
            output, error = self.run(exe, input, language)
            if error is not None:
                results.append({"input": input, "status": error})
                all_have_passed = False
                continue
            if output == expected.strip():
                results.append({"input": input, "status": "PASS"})
            else:
                results.append({"input": input,"status": "FAIL","got": output,"expected": expected})
                all_have_passed = False
        return {"overall": "PASS" if all_have_passed else "FAIL","details": results}