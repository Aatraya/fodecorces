import os
class submissions:
  def __init__(self,sid,uid,pid,lang,code,tstamp): #constructor and attributes
    self.submission_id=sid
    self.user_id = uid
    self.problem_id = pid
    self.language = lang
    self.code=code
    self.timestamp = tstamp
    self.directory_path = None
  def get_code(self, base_dir):
    submission_dir = create_submission_directory(base_dir, self.problem_id, self.submission_id) #method for saving the submitted code into the appropriate file
    self.directory_path = submission_dir
    if self.language.lower() == "python":filename = "solution.py"
    elif self.language.lower() == "c":filename = "solution.c"
    elif self.language.lower() == "cpp":filename = "solution.cpp"
    elif self.language.lower() == "java":filename = "Solution.java"
    else:raise ValueError("The language is not supported, please try again with a valid option.")
    file_path = os.path.join(submission_dir, filename)
    with open(file_path, "w") as f:
      f.write(self.code)
    return file_path
  def metadata(self):
    if self.directory_path is None:
      raise ValueError("The required problem's directory is not created yet. Please do so.")
    metadata = os.path.join(self.directory_path, "metadata.txt")
    with open(metadata, "w") as f:
      f.write(f"submission_id: {self.submission_id}\nuser_id: {self.user_id}\nproblem_id: {self.problem_id}\nlanguage: {self.language}\ntimestamp: {self.timestamp}\ndirectory_path: {self.directory_path}\n")
    return metadata
def create_submission_directory(base_dir, problem_id, submission_id): #method for creating a submission folder
  problem_folder = os.path.join(base_dir, f"problem_{problem_id}")
  submission_folder = os.path.join(problem_folder, f"submission_{submission_id}")
  os.makedirs(submission_folder, exist_ok=True)
  return submission_folder
