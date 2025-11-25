import subprocess
#import psutils
#import times
import os

class Judge:
    def __init__(self, tl=2 ):
        self.time_limit = tl

    def compile_code(self, path, language):
        if language == "python":
            return path
        output_file = path + "_out"
        if language == "c":
            cmd = ["gcc", path, "-o", output_file]
        elif language == "cpp":
            cmd = ["g++", path, "-o", output_file]
        elif language == "java":
            cmd = ["javac", path]
            output_file = path.replace(".java", "")
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

            elif language == "java":
                class_name = os.path.basename(exe_path)
                cmd = ["java", class_name]

            result = subprocess.run(
                cmd,
                input=input_data.encode(),
                capture_output=True,
                timeout=self.time_limit
            )

            return result.stdout.decode().strip(), None

        except subprocess.TimeoutExpired:
            print("TLE bruh be faster")
            return None, "TLE"

        except Exception as err:
            return None, "The error is " +str(err)


    def judge(self, path, language, testcases):#testcases is a list of tuples where first is input string and second is output string
        exe = self.compile_code(path, language)
        if exe is None:
            return {"status": "COMPILE_ERROR"}

        results = []
        all_passed = True

        for inp, exp in testcases:
            out, err = self.run(exe, inp, language)

            if err is not None:
                results.append({"input": inp, "status": err})
                all_passed = False
                continue

            if out == exp.strip():
                results.append({"input": inp, "status": "PASS"})
            else:
                results.append({
                    "input": inp,
                    "status": "FAIL",
                    "got": out,
                    "expected": exp
                })
                all_passed = False

        return {
            "overall": "PASS" if all_passed else "FAIL",
            "details": results
        }