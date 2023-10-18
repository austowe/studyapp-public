from bs4 import BeautifulSoup
import os
import json
import pages

page = pages.page


soup = BeautifulSoup(page, 'html.parser')

questions = {'questions':[]}
values = ''
referencesSoup = soup.find_all('div', {"class": ["pl-12", "-ml-8", "-mr-4", "pr-4", "w-full"]})

letters = ["A. ","B. ","C. ","D. ","E. ","F. ","G. "]

cwd = os.getcwd()
f = open(os.path.join(cwd, "questions.json"))
questionsLoad = json.load(f)

for i in referencesSoup:
    subsoup = i.find_all('div', {"class": ["mb-2", "default-list", "default-table", "instructorText", "font-nunito", "break-words"]})
    count = 0
    for j in subsoup:
        print(j.text)
        if count == 0:
            values = j.text
        else:
            values += '\n' + letters[count - 1] + j.text
        count += 1
    if values != '':
        #Answers need to be manually added for now, future versions to include answer autofil.
        questionsLoad['questions'].append({'text':values.replace('\u00a0',''),'answer':'X'})
    values = ''



json_object = json.dumps(questionsLoad, indent=4)
with open("questions.json", "w") as outfile:
    outfile.write(json_object)