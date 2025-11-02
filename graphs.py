import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# output_dir = "resault"
output_dir = "results"
import os

df = pd.read_csv('students.csv')

def Head():
    return print(df.head(10))

def Columns():
    return print(f"ustunlar nomlari:->\n{df.columns}")

def Shape():
    return df.shape   
def Pie():
    gender_counts = df['gender'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(x=gender_counts,colors=sns.color_palette('bright'), labels=gender_counts.index,  autopct="%1.2f%%",startangle=140)
    plt.title("Gender diversification", fontsize=16)
    plt.axis("equal")
    plt.savefig(os.path.join(output_dir, "gender_pie.png"), dpi=300, bbox_inches='tight')
    plt.close()





def Age():
    age = df["age"]
    plt.figure(figsize=(5,5))
    plt.hist(x=age,bins=40,color='red',edgecolor='black')
    plt.title("Age distribution")
    plt.ylabel("Number of students")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "age_hist.png"), dpi=300, bbox_inches='tight')
    plt.show()



def Age_pie():
    age=df["age"].value_counts()
    plt.figure(figsize=(7,7))
    plt.pie(x=age,colors=sns.color_palette('bright'),labels=age.index,autopct="%1.2f%%",startangle=140)
    plt.title("Age distribution")
    plt.xlabel("NUmbe of students")
    plt.axis('equal')
    plt.savefig(os.path.join(output_dir, "age_pie.png"), dpi=300, bbox_inches='tight')
    plt.show()
def Parental_edication():
    parental_edication=df['parental_education_level'].value_counts()
    plt.figure(figsize=(7,7))
    plt.pie(x=parental_edication ,colors=sns.color_palette('bright6'),labels=parental_edication.index,autopct="%1.2f%%", explode=[0.2,0.2,0.2] )
    plt.title("Parental edication level")
    plt.xlabel("Level")
    plt.axis('equal')
    plt.savefig(os.path.join(output_dir, "parental_education.png"), dpi=300, bbox_inches='tight')   
    plt.show()

def Extracurricular_participation():
    extracurricular_participation=df['extracurricular_participation'].value_counts()
    plt.figure(figsize=(7,7))
    plt.pie(x=extracurricular_participation ,colors=sns.color_palette('bright6'),labels=extracurricular_participation.index,autopct="%1.2f%%", explode=[.1,0]  )
    plt.title("extracurricular participation")
    plt.xlabel("YES & NO")
    plt.axis('equal')
    plt.savefig(os.path.join(output_dir, "extracurricular_participation.png"), dpi=300, bbox_inches='tight')
    plt.show()


# Exam score ga qaysi omillar ta'sir qilayotgani

def  Impact_of_attendance():
    plt.figure(figsize=(7,7))
    sns.scatterplot(data = df, x='study_hours_per_day', y='exam_score', hue='gender', palette='viridis',
                alpha=0.7 )
    plt.title("Attendance Percentage & Exam Score", fontsize=14)
    plt.xlabel('Study hours per day', fontsize=12)
    plt.ylabel('Exam Score', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "study_hours_vs_exam_score.png"), dpi=300, bbox_inches='tight')
    plt.show()

def  Part_time_job_exam_score():
    plt.figure(figsize=(7,7))
    sns.scatterplot(data = df, x='part_time_job', y='exam_score', hue='gender', palette='viridis',
                alpha=0.7 )
    plt.title("Attendance Percentage & Exam Score", fontsize=14)
    plt.xlabel('Study hours per day', fontsize=12)
    plt.ylabel('Exam Score', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "part_time_job_exam_score.png"), dpi=300, bbox_inches='tight')
    plt.show()


def Diet_quality_exam_score():
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='exam_score', hue='diet_quality', kde=True, multiple='stack', palette='Set2')
    plt.title("Exam Score Distribution by Diet Quality")
    plt.xlabel("Exam Score")
    plt.ylabel("Count")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "diet_quality_exam_score.png"), dpi=300, bbox_inches='tight')
    plt.show()

def Internet_quality():
    plt.figure(figsize=(7,8))
    sns.histplot(data=df,x='exam_score',hue='internet_quality',kde=True,bins=50,multiple='stack',palette='Set2')
    plt.title("Internet quality &Exam score")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students") 
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "internet_quality_exam_score.png"), dpi=300, bbox_inches='tight')
    plt.show()
