# UMBC DATA606 Capstone –  Predicting Student Startup Success Proposal

**Project Title:** Predicting Startup Success from Academic and Entrepreneurial Development Factors

**Prepared for:** Dr. Chaojie (Jay) Wang  

**Author:** Nirvika Rajendra

**GitHub Repository:** https://github.com/Nirvika12/UMBC-DATA606-Capstone

**LinkedIn Profile:** https://www.linkedin.com/in/nirvika-rajendra-70555b2b2/

---

## Background

Many student startups struggle to sustain themselves because we lack clear ways to identify success factors early on. This project is necessary to bridge that gap and guide future entrepreneurial support.

This dataset contains student-level information used to predict startup success. It includes demographic, academic, extracurricular, and personal development attributes. The goal is to identify which factors contribute to a student successfully launching a startup.

The primary objective of this study is to predict student startup success using academic performance, behavioral traits, and entrepreneurial development factors. By analyzing this dataset, the project aims to identify which academic indicators, extracurricular activities, and entrepreneurial traits contribute most significantly to the likelihood of students successfully founding and sustaining startups.

### Why it Matters?
Entrepreneurship plays a vital role in economic growth, innovation, and job creation. Understanding the factors that drive student entrepreneurial success can help universities, policymakers, and incubators design better support systems and training programs. This research not only aids in identifying potential entrepreneurs early but also enables institutions to nurture critical skills, provide targeted mentorship, and allocate resources more effectively. Predictive insights can lead to stronger educational outcomes and higher startup success rates.

Key Benefits

1. Early identification of potential entrepreneurs – Recognize students with high entrepreneurial potential.

2. Improved training and mentorship programs – Tailor programs to address gaps in skills or knowledge.

3. Better resource allocation – Ensure institutional support is directed effectively.

4. Economic impact – Contribute to innovation, job creation, and sustainable economic growth.


### Research Questions:

1. Will a student’s startup succeed or not, based on academic and entrepreneurial factors?

2. Which features (academic, extracurricular, institutional, personal) contribute most to predicting startup success?

3. How do demographic and socioeconomic backgrounds influence startup outcomes?

4. What role do psychological traits (e.g., motivation, resilience) play in entrepreneurial success?

---

## Data

### Data Source

Kaggle dataset: [Real-Time Dataset on Academic and Entrepreneurial Development](https://www.kaggle.com/datasets/datasetengineer/academic-and-entrepreneurial-development-dataset/data)

### Data Size and Shape

* ~214,354 records, 49 columns.

* File size: ~56 MB (CSV).

### Time Period

* Cross-sectional (no explicit time period given, real-time institutional data).

### Unit of Observation

* Each row represents a student record, including academic, extracurricular, personal, and entrepreneurial attributes.


## Data Dictionary

| Column                                        | Type        | Definition                             | Possible Values                                |
| --------------------------------------------- | ----------- | -------------------------------------- | ---------------------------------------------- |
| `Student_ID`                                  | String      | Unique identifier for each student     | S000001, S000002
| `Age`                                         | Int         | Age of student                         | 18–22                                          |
| `Gender`                                      | Categorical | Gender of student                      | Male, Female, Other                            |
| `Major`                                       | Categorical | Academic major                         | Business, Engineering, Arts, Sciences          |
| `Year_of_Study`                               | Int         | Year in degree program                 | 1, 2, 3, 4                                     |
| `Educational_Background`                      | Categorical | Type of prior education                | Low, Medium, High                              |
| `Socioeconomic_Status`                        | Categorical | Financial/social background            | Low, Middle, High                              |
| `Location`                                    | Categorical | Student’s living environment           | Urban, Rural                                   |
| `High_School_Type`                            | Categorical | Type of high school                    | Public, Private                                |
| `Cumulative_GPA`                              | Float       | Overall GPA (0–4 scale)                | 0.0–4.0                                        |
| `Course_Grades`                               | Float       | Average grades across courses (%)      | 50–100                                         |
| `Attendance`                                  | Float       | Attendance percentage                  | 60–100                                         |
| `Project_Scores`                              | Float       | Project evaluation score               | 50–100                                         |
| `Internship_Experience`                       | Binary      | Internship completion                  | Yes / No                                       |
| `Applied_Courses_Count`                       | Int         | Number of courses enrolled in          | 0-10+                                          |
| `Club_Membership`                             | Binary      | Participation in student clubs         | Yes / No                                       |
| `Workshops_Attended`                          | Int         | Workshops attended                     | 0–10+                                          |
| `Competitions_Participated`                   | Int         | Competitions joined                    | 0–10+                                          |
| `Leadership_Roles`                            | Binary      | Leadership positions held              | Yes / No                                       |
| `Volunteering_Activities`                     | Int         | Volunteering participation count       | 0–10+                                          |
| `Leadership_Skills_Score`                     | Float       | Assessed leadership ability            | 0–100                                          |
| `Communication_Skills_Score`                  | Float       | Communication ability                  | 0–100                                          |
| `Creativity_Score`                            | Float       | Creative thinking skills               | 0–100                                          |
| `Problem_Solving_Skills`                      | Float       | Problem-solving score                  | 0–100                                          |
| `Risk_Taking_Tendency`                        | Float       | Willingness to take risks              | 0–100                                          |
| `Networking_Skills`                           | Float       | Ability to build professional networks | 0–100                                          |
| `Entrepreneurial_Mindset`                     | Float       | Entrepreneurial orientation            | 0–100                                          |
| `Business_Acumen`                             | Float       | Business knowledge & awareness         | 0–100                                          |
| `Learning_Style`                              | Categorical | Learning preference                    | Visual, Auditory, Kinesthetic                  |
| `Motivation_Level`                            | Float       | Intrinsic motivation score             | 0–100                                          |
| `Resilience_Score`                            | Float       | Ability to recover from setbacks       | 0–100                                          |
| `Adaptability`                                | Float       | Ability to adjust to change            | 0–100                                          |
| `Self_Efficacy_Score`                         | Float       | Confidence in abilities                | 0–100                                          |
| `Mentorship_Hours`                            | Float       | Hours spent with mentors               | 0–100+                                         |
| `Institutional_Resources_Used`                | Float       | Institutional resources accessed       | 0–100                                          |
| `Faculty_Feedback_Score`                      | Float       | Faculty assessment score               | 0–100                                          |
| `Exposure_to_Entrepreneurial_Curriculum`      | Categorical | Level of exposure                      | Low, Medium, High                              |
| `Institutional_Support_Score`                 | Float       | Support from institution               | 0–100                                          |
| `Startup_Success`                             | Binary      | Outcome of startup                     | Success / Failure                              |

---

### Target Variable Selection
There are three potential target variables in this dataset:

`Startup_Success` (Success/Failure)

`Entrepreneurial_Talent_Level` 

`Innovative_Skill_Score` 

Reason for choosing Startup_Success as the target:

- In the real world, the ultimate question institutions and investors care about is whether a student’s entrepreneurial efforts succeed or not? 

### Columns Dropped
The following columns are removed from the dataset:

`Funding_Secured`, `Startup_Founded`, `Prototypes_Developed`, `Prototype_Completion`, `Competitions_Won`, `Research_Publications`, `Employment_in_Entrepreneurial_Roles`, `Business_Plan_Quality_Score` , `Entrepreneurial_Talent_Level`, `Innovative_Skill_Score` 

Reason for dropping these columns:

- These are post-success outcomes, so including them would artificially inflate model performance because the model would be learning from information that is not available before the outcome occurs.

### Features Used
All other remaining columns are considered as predictive features.

