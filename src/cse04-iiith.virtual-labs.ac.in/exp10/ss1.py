import os.path
f=open("template1.html",'r')
template=f.read()
s=""
with open('index.php?section=Introduction', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
   
    
f=open('introduction.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Theory', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('theory.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Objective', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('objective.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Experiment', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('experiment.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
if os.path.isfile('index.php?section=Manual'):
    f=open('index.php?section=Manual', 'r') 
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
elif os.path.isfile('index.php?section=Procedure'):
    f=open('index.php?section=Procedure', 'r') 
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
f=open('manual.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Quizzes', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('quizzes.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Further%20Readings', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('further_readings.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)
