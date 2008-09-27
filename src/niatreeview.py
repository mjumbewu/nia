import gtk;

from gtk import TreeView;
from gtk import TreeStore;

class NiaTreeModel (TreeStore):
  
  def __init__(self, m):
    TreeStore.__init__(str,str)
    self.set_mission(m)
  
  def add_goal(goal, toiter):
    goal_iter = self.append(toiter)
    
    for contributer in m.getContributers():
      add_contributer(contributer, goal_iter)
    
    return goal_iter
    
  def add_contributer(contributer, toiter):
    contributer_iter = None
    
    if isinstance(contributer,Goal):
      contributer_iter = add_goal(contributer, toiter)
    
    return contributer_iter
    
  def set_mission(self, m):
    self._mission = m
    
    for principle in m.getPrinciples():
      principle_iter = self.append()
      
      for contributer in principle.getContributers():
        add_contributer(contributer, principle_iter)
          
  
class NiaTreeView (TreeView):
  pass
