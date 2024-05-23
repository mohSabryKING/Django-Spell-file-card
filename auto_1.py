import os as Run


read_file=open("n.txt",'r')
act_call=[]
act_len=0
print("->"*10+"\n")
act_call=read_file.readlines()[0:]

print("the list model\n"+str(act_call))


read_file.close()
print("->"*10+"\n")








print("->"*5+"\n")
act1=Run.system("dir")
print("->"*5+"\n")
act1=Run.chdir("../..")
"place your virtual env her"
act2=Run.chdir(act_call[2])
act3=Run.system("dir")
print("->"*5)
print("->"*5+"\n")
act4=Run.system("activate")
print("->"*5)
print("->"*5+"\n")
print("->"*5)
print("->"*5+"\n")


print("")



req_list_1=["html","static","media"]
req_list_2=["css","img","js"]

req_list_3=["admin","dpt_1","dpt_2","dpt_3","dpt_4"]

act6=Run.system("django-admin startproject "+act_call[0].replace('\n',''))

act6=Run.system("py manage.py runserver 3000")
act6=Run.chdir(str(act_call[0].replace('\n','')))
#act6=Run.system("django-admin startapp core20")
act6=Run.system("py manage.py startapp "+act_call[1].replace('\n',''))
#act6=Run.system("cd core_1")
#act6=Run.chdir("core_1")
act6=Run.system("nul>"+act_call[1].replace('\n','')+"/l.py")
act6=Run.system("nul>"+act_call[1].replace('\n','')+"/Forms.py")
act6=Run.system("nul>"+act_call[1].replace('\n','')+"/Act_1.py")
act6=Run.system("nul>"+act_call[1].replace('\n','')+"/Act_2.py")
for i in range(len(req_list_1)):
  print("creating "+req_list_1[i]+" folder\n")
  act6=Run.mkdir(req_list_1[i])

act6=Run.chdir("html")
act6=Run.system("nul>html/home.html")
for i in range(len(req_list_3)):
  print("creating "+req_list_3[i]+" folder at html folder\n")
  act6=Run.mkdir(req_list_3[i])
  for f in range(1,5):
    act6=Run.system("nul>"+req_list_3[i]+"/view"+str(f)+".html")
#point of foucs
act6=Run.chdir("..")
#point of foucs

act6=Run.chdir("static")

for i in range(len(req_list_2)):
  print("creating "+req_list_2[i]+" folder\n")
  act6=Run.mkdir(req_list_2[i])
  for x in range(3):
    act6=Run.system("nul>"+req_list_2[i]+"/model"+str(x)+".css")


#act6=Run.system("cd Monja")

#act6=Run.chdir("core")


print("->"*5)
print("->"*5+"\n")
ac7=Run.system("dir")
print("->"*5)
print("->"*5+"\n")

print("\nINFO:go to your Virtual env through...\' your_venv/Scripts\' to get your created django project\n")

