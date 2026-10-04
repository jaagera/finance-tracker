languages = ["Python", "JavaScript", "Java", "C++", "Go"]
print("Python" in languages)    #True
print("Ruby" in languages)      #False
print("Ruby" not in languages)  #True

if "Python" in languages:
    print("Python exists in the list")
else:
    print("Python is not in the list")