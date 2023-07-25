fast,slow=head,head    #two pointers use karisu 
while first and first.next:    #a check karse ke first and en pachino node che e empty nathi 
   slow=slow.next #ahiya slow will move 1 step
   fast=fast.next.next   # 2var next means ke two steps lese.
       if fast==slow: #ahiya check karisu ke apde last node par pochiya che ke nai
          return(fast)  
  return(False)
