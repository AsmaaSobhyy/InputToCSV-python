import csv

name=''
email=''
mobile=''
uni=''
major=''

with open('info.csv','w',newline='' ) as f:
    fieldnames=['Name','Email','Mobile','university','major']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    
    while name!='stop':
        
        name= input('Name: ' )
        if name == 'stop':
            break
        email= input('Email: ' )
        if email == 'stop':
            break
        mobile= input('Mobile: ' )
        if mobile == 'stop':
            break
        uni= input('university: ' )
        if uni == 'stop':
            break
        major= input('Major: ' )
        if major == 'stop':
            break
        writer.writerow({'Name': name,'Email':email,'Mobile':mobile,'university':uni,'major':major})
        
  