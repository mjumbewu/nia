#!/usr/bin/python
#
# main.py
# Copyright (C) Mjumbe Wawatu Ukweli 2008 <mjumbewu@gmail.com>
# 
# main.py is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# main.py is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import time

# The following classes are abstract bases for big ideas.

class can_motivate:
  """
  A can_motivate object may be used as a "reason" for some other types of 
  objects.
  """
  
  # __motivated_objects is a dictionary of (type -> set(needs_motivation))
  __motivated_objects = {}
  pass
  
class needs_motivation:
  """
  A needs_motivation object needs some "reason" -- or motivation -- to exist.
  All needs_motivation objects are motivated at least indirectly by some 
  principle.
  """
  
  # motivations - a dict of motivations -- {can_motivate --> note_string}
  __motivations = {}
  
  def __init__(self, motivation = None):
    if motivation is None:
      pass
      
    elif isinstance(motivation, can_motivate):
      self.__motivations[motivation] = ''
      
    elif isinstance(motivation, (set,frozenset,list)):
      for motive in motivation:
        if isinstance(motive, can_motivate):
          self.__motivations[motive] = ''
        else:
          raise ValueError('Motivation must be a can_motivate object or a set of \
            can_motivate objects: ' + str(type(motivation)))
      
    elif isinstance(motivation, dict):
      for (motive,note) in motivation.items():
        if isinstance(motive, can_motivate) and \
           isinstance(note, str):
          self.__motivations[motive] = note
        else:
          raise ValueError('Motivation must be a can_motivate object or a set of \
            can_motivate objects: ' + str(type(motivation)))
      
    else:
      raise ValueError('Motivation must be a can_motivate object or a set of \
        can_motivate objects: ' + str(type(motivation)))
  
  def addMotivation(self, motive, note = ''):
    self.__motivations[motive] = note
  
  def getMotivations(self):
    return self.__motivations.keys()
  
  def removeMotivation(self, motive):
    if motive in self.__motivations:
      del self.__motivations[motive]
    else:
      raise LookupError('Object not in motivations: ' + repr(motive))
  
  def getNote(self, motive):
    if motive in self.__motivations:
      return self.__motivations[motive]
    else:
      raise LookupError('Object not in motivations: ' + repr(motive))
  
  def setNote(self, motive, note):
    if motive in self.__motivations:
      return self.__motivations
    else:
      raise LookupError('Object not in motivations: ' + repr(motive))
  
  def hasMotivation(self, motive):
    return (motive in self.__motivations)
  
class has_a_schedule:
  """
  A has_a_scheduled object needs time points.  It may have one or more.  The
  earliest and latest timepoints denote the beginning and end of the schedule,
  respectively.  A single timepoint, or timepoints in between 
  """
  
  # timepoints is a set of timepoints -- (time,note) tuples.
  timepoints = set()
  
class can_be_achieved:
  """
  A can_be_achieved
  """
  
  is_achieved = False
  due_time = time.time()
  
class completable:
  """
  A completeable is something that your can regard as being in process or as
  being completed.
  """
  _isActive = False
  _isComplete = False
  
  def setActive(self, a):
    self._isActive = a
  
  def setComplete(self, c):
    self._isComplete = c

class contributable:
  """
  A tributable is something that can be contributed to by completables.
  """
  # _contributers
  # Set of completables which contribute to this contributable
  _contributers = {}
  
  def addContributer(self, t):
    self._contributers[t] = None
  
  def hasContributer(self, t):
    return (t in self._contributers)
  
  def removeContributer(self, t):
    if t in self._contributers:
      del self._contributers[t]




# The following classes represent the big ideas in a Nia file.  Some of the
# language is borrowed from the Seven Habbits of Highly Effective People.

class Principle (can_motivate):
  """
  A principle is something that you believe strongly in or a value which is 
  very important to you.  Philosophically speaking, one's purpose should start
  with ones principles.  Taking time to determine what is important is a 
  necessary step in finding a fulfilling path.
  
  Principles never expire.  They may increase or decrease in importance over 
  time relative to your other principles, and those importance levels are good
  to reasses.  I would think the importance of a principle should be roughly
  correlated with the number of tasks that are carried out because of the
  principle (as a direct or indirect reason).
  """
  pass

class Goal (can_motivate,needs_motivation,has_a_schedule):
  """
  A goal is something that you want to achieve.  A goal always has a reason or
  reasons for being wanted (motivation).  A timepoint may be associated with a 
  goal (e.g. a goal of such-and-such by some time).
  """
  # __description
  # The string description of this goal
  __description = ""
  
  __motivated_goals = set()
  __motivated_tasks = set()
  
  def isBeingPursued(self):
    """
    A goal is being pursued if there are tasks motivated by this goal that are
    active, or if there are goals motivated by this goal that are active.
    """
    for goal in self.__motivated_goals:
      if goal.isBeingPursued(): return True
    
    for task in self.__motivated_tasks:
      if task.isActive(): return True
    
    return False
  
  def isAchieved(self):
    return self._isComplete

class Task (needs_motivation,has_a_schedule):
  """
  A task is, simply, something that you do.  Tasks may or may not be performed 
  in service to some goal or principle.
  """
  # _contributes
  # List of tributables to which this task contributes
  _constributes = []
  
  # _[pre/co]reqs
  # List of completables on which this task depends
  _prereqs = []
  _coreqs = []
  
  _deadline = 0
  
  _urgency = 0.0
  _importance = 0.0

class Plan:
  """
  A plan, conceptually, is a way to achieve a goal.
  """
  # _goal
  # The goal or goals to achieve through this plan.  
  _goals = None
  
  # _tasks
  # The list of tasks to be done in order to achieve the goal.
  _tasks = []

class Event (has_a_schedule):
  """
  Event objects exist to interface with calendars.
  """
  _startTime = 0
  _endTime = 0

class Mission:
  pass

class Nia:
  __mission = None
  __principles = []
  __goals = []
  __tasks = []
  __events = []
  
  def addPrinciple(self, p = None):
    if p is None:
      p = Principle()
    
    self.__principles.append(p)
    return p
  
  def getPrinciples(self):
    return self.__principles
  
  def addGoal(self, g = None):
    if g is None:
      g = Goal()
    
    self.__goals.append(g)
    return g
  
  def getGoals(self):
    return self.__goals
  
  def writeToFile(self, filename):
    outfile = open(filename, 'w')
    outfile.write()
    
