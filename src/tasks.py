# A todo list.

class Task:
  '''A task on the list.'''
  
  # Label is how the task is presented
  Label = ""
  
  # Description is some text about the task
  Description = ""
  
  # Duration is a tuple describing the minimum amount of time you need to 
  # complete a task and the maximum amount of time a task will take.
  Duration = (0,0)
  
  # Deadline is when the task must be done by
  Deadline = 0
  
  # Depend is a list of tasks that must be completed before this one can begin
  Depend = []
  
  # Importance/urgency refer to Covey's four-quadrant table
  Importance = 0
  Urgency = 0
  
  def __init__(self):
    pass
  
class TaskList:
  '''A collection of tasks'''
  
  
