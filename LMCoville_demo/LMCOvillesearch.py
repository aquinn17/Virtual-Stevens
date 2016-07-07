#LMCOville Basic Flat-file Search

from flask import Flask, render_template
from flask import request

app = Flask(__name__)
app.secret_key = 'charlie'

specialties = {}
employees = {}


theFile = open('LMCOdata.txt', 'r')
for line in theFile:
    employees[line.strip(' ').strip().split(':')[0].lower()] = line.strip().strip(' ').strip().split(':')[1].lower().split(',')
    for i in  line.strip().strip(' ').strip().split(':')[1].lower().split(','):
        if i not in specialties.keys():
            specialties[i] = [] 

for key in employees.keys():
    for j in employees[key]:
        specialties[j].append(key)

def search(inpt):
    search = str(inpt)
    search = search.lower()
    result = False
    end = []
    if search in specialties.keys():
        for i in specialties[search]:
            end.append(i.title())
        return ', '.join(end)
        result = True
    if search in employees.keys():
        for i in employees[search]:
            end.append(i.title())
        return ', '.join(end)
        result = True
    if result == False: return 'none found'

def neat(lst):
    for item in lst:
        return item.title()

file.close(theFile)

@app.route('/')
def my_search():
    return render_template("LMCOville.htm")

@app.route('/', methods=['POST'])
def my_search_link():
    text = request.form['k']
    #processed_text = text.lower()
    #return processed_text
    return search(text)
        
if __name__=='__main__':
    app.run(debug=True)
