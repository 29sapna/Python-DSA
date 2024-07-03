def decoration(perform):
  print("*************")
  print("****"+perform()+"****")
  print("*************")
@decoration  
def perform():
   return "sapna"