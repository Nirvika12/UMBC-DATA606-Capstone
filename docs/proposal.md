# UMBC DATA606 Capstone -  Predicting Student Startup Success Proposal

**Project Title:**  Predicting Student Startup Success Using Team, Innovation, and Support Factors

**Prepared for:** Dr. Chaojie (Jay) Wang  

**Author:** Nirvika Rajendra

**GitHub Repository:** https://github.com/Nirvika12/UMBC-DATA606-Capstone

**LinkedIn Profile:** https://www.linkedin.com/in/nirvika-rajendra-70555b2b2/

---

## Background

This project aims to predict the success of student-led startup projects by leveraging a dataset containing key structural, strategic, and support-related factors. The dataset includes 2,100 student startup initiatives from 40 academic institutions spanning 2019–2023. By understanding which internal factors such as team experience, innovation level, funding, mentorship, and incubation drive startup success, the study seeks to develop predictive models that can guide educational institutions and incubators in nurturing effective entrepreneurial ventures.

### Why it Matters?

Student entrepreneurship is an important engine for innovation and economic growth. Successful startup projects lead to job creation, new products and services, and can significantly impact regional economies. This study can help:

1. Identify critical factors contributing to student startup success.

2. Inform institutional policies on mentorship, funding, and incubation programs.

3. Provide actionable insights for educators and startup incubators.

4. Enhance resource allocation to maximize the success rates of student ventures.

### Research Questions:

1. Which project-related factors best predict the success of student-led startups?

2. How do team characteristics (size, experience) influence project outcomes?

3. What role do innovation and technology maturity play in predicting success?

4. How impactful are institutional supports like mentorship and incubation on startup outcomes?

5. Can predictive models built on these factors reliably classify successful vs unsuccessful projects


---

## Data

### Data Source

Kaggle dataset: [Student Startup Success Dataset](https://www.kaggle.com/datasets/ziya07/student-startup-success-dataset/data)

### Data Size and Shape

* ~2,100 records, 16 columns.

* File size: ~176 KB (CSV).

### Time Period

* Dataset sourced from 40 academic institution's startup initiatives, 2019–2023.

### Unit of Observation
* Each row in this dataset represents one startup project

| Column                   | Type        | Description                                       | Possible Values / Range                          |
| ------------------------ | ----------- | ------------------------------------------------- | ------------------------------------------------ |
| `project_id`             | String      | Unique project identifier                         | Alphanumeric (e.g., P0001, P0002, etc.)          |
| `institution_name`       | Categorical | Name of the institution                           | Multiple university/college names                |
| `institution_type`       | Categorical | Type of institution                               | Public, Private, Technical, Non-tech             |
| `project_domain`         | Categorical | Startup domain (sector/industry)                  | AgriTech, FinTech, GreenTech, HealthTech, EdTech |
| `team_size`              | Integer     | Number of students in the startup team            | 1–10+                                            |
| `avg_team_experience`    | Float       | Average years of prior entrepreneurial experience | 0–10                                             |
| `innovation_score`       | Float       | Novelty/originality score normalized (0–1)        | 0–1                                              |
| `funding_amount_usd`     | Float       | Initial funding received in USD                   | 0 – Millions                                     |
| `mentorship_support`     | Binary      | Mentorship received                               | 0 or 1 (1 = Yes, 0 = No)                         |
| `incubation_support`     | Binary      | Whether incubated                                 | 0 or 1 (1 = Yes, 0 = No)                         |
| `market_readiness_level` | Integer     | Stage of product readiness                        | 1–5 (1 = idea, 5 = market-ready)                 |
| `competition_awards`     | Integer     | Number of awards won                              | 0+                                               |
| `business_model_score`   | Float       | Clarity and scalability of business model (0–1)   | 0–1                                              |
| `technology_maturity`    | Integer     | Maturity level of technology                      | 1–5 (1 = prototype, 5 = production)              |
| `year`                   | Integer     | Year project was submitted                        | 2019–2023                                        |
| `success_label`          | Binary      | Target variable: success or failure               | 0 or 1 (1 = Success, 0 = Failure)                |

### Project Scope and Methodology

Target Variable: success_label (binary: 1 = Successful, 0 = Unsuccessful).

Features: All other columns (e.g., funding_amount_usd, innovation_score, team_size, etc.).

## Steps:
1. Exploratory Data Analysis (EDA):

* Analyze feature distributions, missing values, and correlations with success.
* Visualize patterns and trends.

2. Feature Engineering:

* Create new features (e.g., team dynamics, support systems, innovation metrics).
* Normalize/scale continuous features.

3. Model Selection & Training:

* Models: Random Forest, XGBoost, Logistic Regression.
* Tune models with cross-validation.

4. Model Evaluation:

* Evaluate using accuracy, precision, recall, F1-score.
* Compare performance of models.

5. Feature Importance Analysis:

* Identify most influential features (e.g., funding, mentorship support).

6. Practical Implications:

* Insights for universities, incubators to enhance startup support systems.

7. Frontend Application:

* Deploy the model via Streamlit for real-time success predictions and insights.
