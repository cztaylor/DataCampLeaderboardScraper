from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
<<<<<<< HEAD
import datetime
from openpyxl import load_workbook

# webdriver is needed in order to run javascript on webpage
driver = webdriver.Chrome('C:\ProgramData\chromedriver')


# Create DataFrames for data previously pulled
existingExercises = pd.read_excel('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCamp.xlsx', sheetname = 'Exercises')
existingCourses = pd.read_excel('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCamp.xlsx', sheetname = 'Courses')
existingTracks = pd.read_excel('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCamp.xlsx', sheetname = 'Tracks')
existingXP = pd.read_excel('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCamp.xlsx', sheetname = 'Topics')


# Create a list of user names
users = list(pd.read_csv('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCampUsers.csv', header=None)[0])


# initialize lists & dictionaries
=======

driver = webdriver.Chrome('C:\ProgramData\chromedriver')

users = list(pd.read_csv('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\\DataCampUsers.csv', header=None)[0])
>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
exercisesAced_list = []
coursesCompleted_dict = {}
tracksCompleted_dict = {}
topicXP_dict = {}

<<<<<<< HEAD
# loop through each user, visiting their Data Camp public profile and scraping the data
for userName in users:
    url = 'https://www.datacamp.com/profile/' + userName
    
    # We can't run these commented requests lines because we need to run the javascript on the page
=======

for userName in users:
    url = 'https://www.datacamp.com/profile/' + userName
    
>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
    #import requests
    #r = requests.get(url, allow_redirects=False)
    #html = r.text
    
<<<<<<< HEAD
    # Get the HTML and store it as a BeautifulSoup object
    driver.get(url)
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, "lxml")
    
    
    # find the number of exercises aced and append to list
=======
    driver.get(url)
    htmlSource = driver.page_source
    
    
    soup = BeautifulSoup(htmlSource, "lxml")
    
>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
    stats = soup.find("div", { "class" : "stats" })
    exercisesAced = int(stats.contents[5].b.text)
    exercisesAced_list.append(exercisesAced)
    
<<<<<<< HEAD
    # find each users XP for each topic and add the topicXP_dict
    userTopics = soup.find("h4", text = re.compile(r's Topics')).next_sibling.next_sibling.next_sibling.next_sibling
=======
    userTopics = soup.find("h4", text = re.compile(r's Topics')).next_sibling.next_sibling.next_sibling.next_sibling
    
>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
    userTopics_Names = []
    userTopics_XP = []
    
    for topic in userTopics:
        if not topic.find("h5") == -1:
            topicName = topic.find("h5").contents[0]
            topicXP = int(re.match(r'[0-9]*', topic.find("p").contents[0]).group())
            userTopics_Names.append(topicName)
            userTopics_XP.append(topicXP)
            
    topicXP_dict[userName] = [userTopics_Names,userTopics_XP]
    
    
<<<<<<< HEAD
    # find all tracks the user has completed and add them the the tracks dictionary
    userTracks = [c.contents[0] for c in soup.find_all("h4", {"class" : "track-block__title"})]
    tracksCompleted_dict[userName] = userTracks
    
    # find all courses the user has completed and add them the the courses dictionary
    userCourses = [c.contents[0] for c in soup.find_all("h4", {"class" : "course-block__title"})]
    coursesCompleted_dict[userName] = userCourses

#End of for loop


# Create DataFrame for Exercises Aced data
exercises_df = pd.DataFrame({'UserName':users,'ExercisesAced':exercisesAced_list})

# Use existingExercises and exercises_df to find the new Exercises Aced
exerciseSum = existingExercises.groupby(['UserName'], as_index=False)[['ExercisesAced']].sum()
exerciseJoin = pd.merge(exercises_df,exerciseSum,'left',on='UserName')
exerciseJoin['ExercisesAced'] = exerciseJoin['ExercisesAced_x'] - exerciseJoin['ExercisesAced_y']
exerciseNew = exerciseJoin[exerciseJoin['ExercisesAced'] != 0]
exerciseNew = exerciseNew[['ExercisesAced', 'UserName']]
exerciseNew['Date'] = datetime.datetime.now().date()


# Create DataFrame for Courses Completed data
=======
    userTracks = [c.contents[0] for c in soup.find_all("h4", {"class" : "track-block__title"})]
    tracksCompleted_dict[userName] = userTracks
    
    userCourses = [c.contents[0] for c in soup.find_all("h4", {"class" : "course-block__title"})]
    coursesCompleted_dict[userName] = userCourses


users_df = pd.DataFrame({'UserName':users,'ExercisesAced':exercisesAced_list})

>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
userCourses_list = []
for k, v in coursesCompleted_dict.items():
    for i in v:
        userCourses_list.append([k,i])
userCourses_df = pd.DataFrame(userCourses_list,columns=['UserName','CourseName'])

<<<<<<< HEAD
# Use existingCourses and userCourses_df to find the new Courses Completed
coursesJoin = pd.merge(userCourses_df,existingCourses,'outer',on=['UserName','CourseName'])
coursesNew = coursesJoin[coursesJoin['DateCompleted'].isnull()]
coursesNew = coursesNew[['UserName','CourseName']]
coursesNew['DateCompleted'] = datetime.datetime.now().date()


# Create DataFrame for Tracks Completed data
=======

>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
userTracks_list = []
for k, v in tracksCompleted_dict.items():
    for i in v:
        userTracks_list.append([k,i])
userTracks_df = pd.DataFrame(userTracks_list,columns=['UserName','TrackName'])

<<<<<<< HEAD
# Use existingTracks and userTracks_df to find the new Courses Completed
tracksJoin = pd.merge(userTracks_df,existingTracks,'outer',on=['UserName','TrackName'])
tracksNew = tracksJoin[tracksJoin['DateCompleted'].isnull()]
tracksNew = tracksNew[['UserName','TrackName']]
tracksNew['DateCompleted'] = datetime.datetime.now().date()


# Create DataFrame for Topic XP data
=======


>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
userTopics_list = []
userTopicsNames_list = []
userTopicsXP_list = []
for k, v in topicXP_dict.items():
    for i in v[0]:
        userTopics_list.append(k)
        userTopicsNames_list.append(i)
    for i in v[1]:
        userTopicsXP_list.append(i)
<<<<<<< HEAD
topicXP_df = pd.DataFrame(list(zip(userTopics_list,userTopicsNames_list,userTopicsXP_list)),columns=['UserName','TopicName','XP'])

# Use existingXP and topicXP_df to find the new XP per Topic
topicXPSum = existingXP.groupby(['UserName', 'TopicName'], as_index=False)[['XP']].sum()
topicXPJoin = pd.merge(topicXP_df,topicXPSum,'left',on=['UserName','TopicName'])
topicXPJoin['XP'] = topicXPJoin['XP_x'] - topicXPJoin['XP_y']
topicXPNew = topicXPJoin[topicXPJoin['XP'] != 0]
topicXPNew = topicXPNew[['UserName','TopicName','XP']]
topicXPNew['Date'] = datetime.datetime.now().date()




# load excel workbook
book = load_workbook('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\DataCamp.xlsx')
writer = pd.ExcelWriter('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\DataCamp.xlsx', engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)


# append new exercises, courses, tracks, and XP to existing sheets
exerciseNew.to_excel(writer, "Exercises", index=False, header = False, startrow = writer.sheets['Exercises'].max_row)
coursesNew.to_excel(writer, "Courses", index=False, header = False, startrow = writer.sheets['Courses'].max_row)
tracksNew.to_excel(writer, "Tracks", index=False, header = False, startrow = writer.sheets['Tracks'].max_row)
topicXPNew.to_excel(writer, "Topics", index=False, header = False, startrow = writer.sheets['Topics'].max_row)


# save file
=======
        
topicXP_df = pd.DataFrame(list(zip(userTopics_list,userTopicsNames_list,userTopicsXP_list)),columns=['UserName','TopicName','XP'])


writer = pd.ExcelWriter('C:\\Users\\christian.taylor\\OneDrive - Decisive Data\\DataCampLeaderboard\DataCamp.xlsx')
users_df.to_excel(writer,sheet_name = 'User', index=False)
userCourses_df.to_excel(writer,sheet_name = 'Courses', index=False)
userTracks_df.to_excel(writer,sheet_name = 'Tracks', index=False)
topicXP_df.to_excel(writer,sheet_name = 'Topics', index=False)
>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
writer.save()




<<<<<<< HEAD


=======
>>>>>>> 01d479d9a8ca10697b2e6a997008db1ed37f7361
