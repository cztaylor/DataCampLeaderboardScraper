from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd

driver = webdriver.Chrome('C:\ProgramData\chromedriver')

users = list(pd.read_csv('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCampUsers.csv', header=None)[0])
exercisesAced_list = []
coursesCompleted_dict = {}
tracksCompleted_dict = {}
topicXP_dict = {}


for userName in users:
    url = 'https://www.datacamp.com/profile/' + userName
    
    #import requests
    #r = requests.get(url, allow_redirects=False)
    #html = r.text
    
    driver.get(url)
    htmlSource = driver.page_source
    
    
    soup = BeautifulSoup(htmlSource, "lxml")
    
    stats = soup.find("div", { "class" : "stats" })
    exercisesAced = int(stats.contents[5].b.text)
    exercisesAced_list.append(exercisesAced)
    
    userTopics = soup.find("h4", text = re.compile(r's Topics')).next_sibling.next_sibling.next_sibling.next_sibling
    
    userTopics_Names = []
    userTopics_XP = []
    
    for topic in userTopics:
        if not topic.find("h5") == -1:
            topicName = topic.find("h5").contents[0]
            topicXP = int(re.match(r'[0-9]*', topic.find("p").contents[0]).group())
            userTopics_Names.append(topicName)
            userTopics_XP.append(topicXP)
            
    topicXP_dict[userName] = [userTopics_Names,userTopics_XP]
    
    
    userTracks = [c.contents[0] for c in soup.find_all("h4", {"class" : "track-block__title"})]
    tracksCompleted_dict[userName] = userTracks
    
    userCourses = [c.contents[0] for c in soup.find_all("h4", {"class" : "course-block__title"})]
    coursesCompleted_dict[userName] = userCourses


users_df = pd.DataFrame({'UserName':users,'ExercisesAced':exercisesAced_list})

userCourses_list = []
for k, v in coursesCompleted_dict.items():
    for i in v:
        userCourses_list.append([k,i])
userCourses_df = pd.DataFrame(userCourses_list,columns=['UserName','CourseName'])


userTracks_list = []
for k, v in tracksCompleted_dict.items():
    for i in v:
        userTracks_list.append([k,i])
userTracks_df = pd.DataFrame(userTracks_list,columns=['UserName','TrackName'])



userTopics_list = []
userTopicsNames_list = []
userTopicsXP_list = []
for k, v in topicXP_dict.items():
    for i in v[0]:
        userTopics_list.append(k)
        userTopicsNames_list.append(i)
    for i in v[1]:
        userTopicsXP_list.append(i)
        
topicXP_df = pd.DataFrame(list(zip(userTopics_list,userTopicsNames_list,userTopicsXP_list)),columns=['UserName','TopicName','XP'])


writer = pd.ExcelWriter('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\DataCamp.xlsx')
users_df.to_excel(writer,sheet_name = 'User', index=False)
userCourses_df.to_excel(writer,sheet_name = 'Courses', index=False)
userTracks_df.to_excel(writer,sheet_name = 'Tracks', index=False)
topicXP_df.to_excel(writer,sheet_name = 'Topics', index=False)
writer.save()




