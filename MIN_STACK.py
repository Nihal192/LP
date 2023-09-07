class min stack(self):
  self.stack=[]
  self.minstack=[]
  def push(slef,val):
    self.stack.append(val)
    val=min(val,self.minstack[-1]) if self.minstack else val
    self.minstack.append(val)
  def pop(self):
    self.stack.pop()
    self.minstack.pop()
  def top(self):
    return self.stack[-1]
  def min(self):
    return self.minstack[-1]
    
