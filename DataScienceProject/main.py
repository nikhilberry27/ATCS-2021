#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#read in CSV with survey responses
pd.set_option("display.max_columns", None)
df = pd.read_csv("surveyResponsesFINAL.csv")


#What grade are you in? (histogram)
# df["What grade are you in?"].value_counts().plot(kind='bar', color=("forestgreen"))
# df["What grade are you in?"] = df["What grade are you in?"].apply(str)
# plt.ylabel("Count")
# plt.xlabel("Grade")
#plt.title("What grade are you in?")


#What sport do you play? (histogram)
# sns.histplot(df["What sport do you play?"], color="green")
# plt.tick_params(axis='x', rotation=90)
# plt.title("What sport do you play?")
# plt.gcf().subplots_adjust(bottom=0.4)


#How many AP classes do you take? (histogram)
# df["How many AP classes do you take?"].plot(kind="hist", color=("forestgreen"))
# plt.xticks([0, 1, 2, 3, 4])
# # plt.title("How many AP classes do you take?")
# plt.ylabel("Count")
# plt.xlabel("Number of AP Classes")


#How manny honors classes do you take? (histogram)
# df["How many honors classes do you take?"].plot(kind="hist", rwidth=0.85)
# plt.xticks([0, 1, 2, 3, 4, 5, 6])
# plt.title("How many honors classes do you take?")
# plt.ylabel("Count")
# plt.xlabel("Number of honors Classes")



#average student athlete stress per number of AP classes (line)
# avgStress = df.groupby("How many AP classes do you take?").mean()
# avgStress.plot(y="To what degree would you say being an athlete along with a student fuels your stress levels?", color="forestgreen")
# plt.title("Average Stress due to Being a Student-Athlete per Number of AP Classes")


#average student athlete stress per number of honors classes (line)
# avgStress = df.groupby("How many honors classes do you take?").mean()
# avgStress.plot(y="To what degree would you say being an athlete along with a student fuels your stress levels?")
# plt.title("Average Stress due to Being a Student-Athlete per Number of Honors Classes")


#care for academic performance vs. overall student athlete stress (line)
# academicStress = df.groupby("How much do you care your grades/school performance?").mean()
# academicStress.plot(y="To what degree would you say being an athlete along with a student fuels your stress levels?", color="forestgreen")
# plt.xlabel("How much do you care about your grades/school performance?")
# plt.title("Care for Academic Performance vs. Stress due to Being a Student-Athlete")


#care for academic performance vs. level that being a student athlete is detrimental for mental health (line)
# academicDetrimental = df.groupby("How much do you care your grades/school performance?").mean()
# academicDetrimental.plot(y="How detrimental is being a student athlete to your mental health?", color="forestgreen")
# plt.xlabel("How much do you care about your grades/school performance?")
# plt.title("Care for Academic Performance vs. Amount that Being a Student-Athlete is Detrimental to Mental Health")


#Do you play for a junior varisty or varsity team? (histogram)
# sns.histplot(df["Do you play JV or Varsity? (equivalent if you play outside of school)"], color="green")
# plt.tick_params(axis='x', rotation=90)


#What is the highest athletic level that you have competed in? (histogram)
# df["What is the highest level you compete in your sport?"].value_counts().plot(kind='bar', color="forestgreen")
# plt.title("What is the highest athletic level you compete in?")
# plt.ylabel("Count")
# plt.gcf().subplots_adjust(bottom=0.2)


#What are your athletic plans in college? (histogram)
# sns.histplot(df["Do you plan to continue your sport in college?"], color="green")
# plt.tick_params(axis='x', rotation=90)
# plt.ylabel("Count")
# plt.gcf().subplots_adjust(bottom=0.3)


#care for athletic performance vs. overall student athlete stress (line)
# athleticStress = df.groupby("How much do you care your athletic performance?").mean()
# athleticStress.plot(y="To what degree would you say being an athlete along with a student fuels your stress levels?", color="forestgreen")
# plt.xlabel("How much do you care about your athletic performance?")
# plt.title("Care for Athletic Performance vs. Stress due to Being a Student-Athlete")


#care for athletic performance vs. level that being a student athlete is detrimental for mental health (line)
# athleticDetrimental = df.groupby("How much do you care your athletic performance?").mean()
# athleticDetrimental.plot(y="How detrimental is being a student athlete to your mental health?", color="forestgreen")
# plt.xlabel("How much do you care about your athletic performance?")
# plt.title("Care for Athletic Performance vs. Amount that Being a Student-Athlete is Detrimental to Mental Health")


plt.show()