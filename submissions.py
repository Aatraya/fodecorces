import os
class submissions():
  def __init__(self,sid,uid,pid,lang,code,tstamp): #constructor and attributes
    self.submission_id=sid
    self.user_id = uid
    self.problem_id = pid
    self.language = lang
    self.code=code
    self.timestamp = tstamp
  def save_code_file(self, base_dir):
      submission_dir = create_submission_directory(base_dir, self.problem_id, self.submission_id) #method for saving the submitted code into the appropriate file
      if self.language == "python":
        filename = "solution.py"
      elif self.language == "c":
        filename = "solution.c"
      elif self.language == "cpp":
        filename = "solution.cpp"
      elif self.language == "java":
        filename = "Solution.java"
      else:
        raise ValueError("Unsupported language")
      file_path = os.path.join(submission_dir, filename)
      with open(file_path, "w") as f:
        f.write(self.code)
      return file_path
  def save_metadata_txt(self):
    if self.directory_path is None:
      raise ValueError("Directory not created yet. Call save_code_file() first.")
    metadata_file = os.path.join(self.directory_path, "metadata.txt")
    with open(metadata_file, "w") as f:
      f.write(f"submission_id: {self.submission_id}\n")
      f.write(f"user_id: {self.user_id}\n")
      f.write(f"problem_id: {self.problem_id}\n")
      f.write(f"language: {self.language}\n")
      f.write(f"timestamp: {self.timestamp}\n")
      f.write(f"directory_path: {self.directory_path}\n")
    return metadata_file
def create_submission_directory(base_dir, problem_id, submission_id): #method for creating a submission folder
      problem_folder = os.path.join(base_dir, f"problem_{problem_id}")
      submission_folder = os.path.join(problem_folder, f"submission_{submission_id}")
      os.makedirs(submission_folder, exist_ok=True)
      return submission_folder






    


