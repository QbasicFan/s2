# s2
Simple template 2
Template starter

3 Sections 

editable Model


Section1s

Section2s




![alt text](https://github.com/QbasicFan/s2/blob/master/ss2.png)



*****************
Install
*****************

1)

git clone https://github.com/QbasicFan/s2 

2) settings.py

INSTALLED_APPS = (
    "s2",
    
    ...
3) settings.py

 os.path.join(PROJECT_ROOT, "[full path to ]/s2/templates"),

4) urls.py

  url("^$", include("s2.urls")),
  
5)
python manage.py makemigrations s2
python manage.py migrate s2

6) re-runserver

*****************
If you like this starter theme, want help with your django projects or want more advanced django templates visit my website. Www.afrodoo.co
