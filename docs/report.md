# UMBC DATA606 Capstone – Predicting Student Startup Success

**Project Title:** Predicting Student Startup Success Using Team, Innovation, and Support Factors  
**Prepared for:** Dr. Chaojie (Jay) Wang  
**Author:** Nirvika Rajendra  
**GitHub Repository:** [https://github.com/Nirvika12/UMBC-DATA606-Capstone](https://github.com/Nirvika12/UMBC-DATA606-Capstone)  
**LinkedIn Profile:** [https://www.linkedin.com/in/nirvika-rajendra-70555b2b2/](https://www.linkedin.com/in/nirvika-rajendra-70555b2b2/)  

---

## 2. Background

Student entrepreneurship is a growing field of innovation and economic development. Across universities worldwide, student-led startups have become a critical mechanism for transforming academic ideas into viable business ventures. However, while many student startups emerge every year, only a small percentage achieve sustainable success.  

This project aims to **predict the success of student-led startup projects** using data-driven methods. The dataset captures key dimensions of team composition, innovation, institutional support, and market readiness across 40 academic institutions between **2019 and 2023**.  

By identifying which factors — such as **team experience**, **innovation level**, **funding**, **mentorship**, and **incubation** — most influence startup success, this project contributes to understanding how universities can enhance their entrepreneurial ecosystems.

### Why It Matters

Student entrepreneurship contributes to:
1. **Innovation:** Encouraging creative problem-solving and applied research.  
2. **Economic growth:** Successful startups create employment and regional development.  
3. **Policy design:** Universities can tailor incubation, mentorship, and funding programs for higher success rates.  
4. **Sustainability:** Data-driven decision-making helps optimize limited institutional resources.  

This research helps institutions identify **what factors truly matter** — guiding better support for early-stage founders.

### Research Questions

1. Which project-related factors best predict the success of student-led startups?  
2. How do team characteristics (size, experience) influence outcomes?  
3. What role do innovation and technology maturity play in success prediction?  
4. How impactful are institutional supports like mentorship and incubation?  
5. Can machine learning models effectively classify startups as successful or unsuccessful?

---

## 3. Data

### Data Source

Dataset from Kaggle: [Student Startup Success Dataset](https://www.kaggle.com/datasets/ziya07/student-startup-success-dataset/data)  

The dataset consolidates information from **40 academic institutions** and includes **2,100 startup projects** from **2019–2023**.

### Data Size and Structure
- **Records:** ~2,100  
- **Columns:** 16  
- **File Size:** ~175kb (CSV format)  
- **Time Period:** 2019–2023  
- **Observation Unit:** Each record represents one **student startup project**.

### Data Dictionary

| Column                   | Type        | Description                                       | Possible Values / Range                          |
| ------------------------ | ----------- | ------------------------------------------------- | ------------------------------------------------ |
| `project_id`             | String      | Unique project identifier                         | Alphanumeric (e.g., P0001, P0002, etc.)          |
| `institution_name`       | Categorical | Name of the institution                           | University/college names e.g. (Institution_39)                |
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


### Target and Predictors

- **Target Variable:** `success_label` (binary classification)  
- **Predictors:** All other columns, including `innovation_score`, `funding_amount_usd`, `mentorship_support`, and `market_readiness_level` etc.

---

## Methodology

The project follows a structured analytical pipeline:

1. **Data Quality and Preprocessing**
    Initial inspection revealed:
    - No missing data.  
    - No duplicate records.  
    - No extreme values detected.  
    - Text-based categorical variables were standardized (lowercase, underscore format).  
These steps ensured a **tidy and consistent dataset** for EDA and model preparation.

2. **Exploratory Data Analysis (EDA):**
   - Examine distributions and correlations among key features.
   - Identify variables most associated with startup success.

3. **Feature Engineering:**
   - Create new derived metrics:
     - `funding_per_member = funding_amount_usd / team_size`
     - `innovation_per_member = innovation_score / team_size`
     - `innovation_support_index = innovation_score * (mentorship_support + incubation_support + 1)`

   - Normalize/scale continuous variables as needed.

4. **Model Development (next phase):**
   - Train models such as **Random Forest**, **XGBoost**, and **Logistic Regression**.
   - Evaluate using **accuracy**, **precision**, **recall**, and **F1-score**.
   - Identify **feature importance** to interpret key success drivers.

5. **Application Development:**
   - Build a **Streamlit web app** for interactive success prediction.

---

## 4. Exploratory Data Analysis (EDA)

### 4.1 Overview

The EDA focused on understanding the distribution of variables, identifying patterns that differentiate successful startups from unsuccessful ones, and assessing the influence of institutional support and innovation.

The following key analyses were conducted:
- Missing value inspection and data cleaning.  
- Distribution analysis of numeric and categorical variables.  
- Correlation analysis to identify strong predictors of success.  
- Visualization of relationships between features and outcomes.

---

### 4.2 Data Cleaning and Preparation

The dataset was found to be clean, consistent, and well-structured, requiring minimal preprocessing.  
Key validation checks confirmed the following:

- **Missing Values:** No missing data were found across any columns, ensuring complete information for all startup records.  
- **Duplicates:** No duplicate rows were detected.  
- **Categorical Standardization:** Text-based categorical variables (`institution_type`, `institution_name`, and `project_domain`) were standardized to lowercase and underscore-separated to maintain uniform formatting and ensure compatibility during machine learning encoding.  
- **Domain Normalization:** The `project_domain` variable was mapped to standardized labels for analytical clarity, resulting in the following categories:  
  - `agricultural_technology`  
  - `financial_technology`  
  - `green_environmental_technology`  
  - `healthcare_technology`  
  - `educational_technology`  
- **Outlier Detection:** Statistical inspection confirmed that all numerical features (e.g., `funding_amount_usd`, `team_size`, `innovation_score`) were within reasonable and expected ranges, with no extreme values requiring adjustment.

Overall, the dataset was **complete, consistent, and analysis-ready**, making it ideal for exploratory data analysis (EDA) and subsequent model development.

---

### 4.3 Summary Statistics

The dataset includes 2,100 startup projects. Team sizes range from 2 to 7 members (mean ≈ 4.5).
Average team experience is 2.3 years, while the mean innovation score is 0.65 on a 0–1 scale.
Funding values range from approximately `$1,000 to $50,000`, with an average of $25,372, indicating moderate funding variability.
Around half of the projects received mentorship and incubation support.
The success rate is 41.9%, suggesting a balanced target distribution suitable for classification modeling.

---

### 4.4 Visual Insights

#### (a) Success Distribution

![Success Distribution](/docs/eda-plots/Distribution-of-Startup-Success.png)

> The dataset shows a relatively balanced distribution of startup outcomes. Approximately **41.95%** of student-led startups were successful, while **58.05%** were unsuccessful.  
> Although slightly skewed toward failure, the distribution indicates that the dataset maintains a good balance for binary classification modeling - neither class is overwhelmingly dominant.  

> This suggests that predictive models trained on this data are unlikely to suffer from severe class imbalance issues, allowing for reliable performance evaluation across both successful and unsuccessful startups.

#### (b) Distribution of Institution Type by Startup Success

![Institution Type](/docs/eda-plots/Institution-type.png)

> All institution types contributed both successful and unsuccessful startups.  
> Among the 2,100 total projects, **non-technical (549)** and **public (546)** institutions had the highest participation, followed closely by **technical (508)** and **private (497)** institutions.  

> Across all categories, the proportion of **failed startups** is slightly higher than successful ones - for instance, non-technical institutions recorded **300 failed** versus **249 successful** projects,  
and technical institutions had **296 failed** versus **212 successful**.  

> This pattern suggests that startup outcomes are relatively consistent across institution types,  
with no single category demonstrating a markedly higher success rate.  
>Institutional environment may influence participation volume more than success likelihood.


#### (c) Success/Failure Distribution by Project Domain

![Project Domain](/docs/eda-plots/Project-Domain.png)

> Across all five domains, both successful and unsuccessful startups are represented.  
> The largest participation is seen in **Agricultural Technology (439 projects)**, followed by **Financial (425)** and **Green Technology (422)**.  
> While the number of failed startups slightly exceeds successful ones in every category, the **success proportions are relatively consistent** — roughly 40–45% of projects succeed regardless of domain.  
> This suggests that innovation sector alone may not be a strong predictor of startup success in the dataset.


#### (d) Density Plots of Numerical Variables

![Density Plots](/docs/eda-plots/density-numerical.png)

>The density plots indicate that most numerical features follow roughly normal or slightly right-skewed distributions.  
`funding_amount_usd` display higher variance, suggesting diverse funding across startups.  
>In contrast, `innovation_score` and `business_model_score` are more concentrated, indicating consistent scoring patterns among student startups.  
Overall, the numerical features show well-distributed data without extreme skewness or irregularities, making them suitable for predictive modeling.

#### (e) Funding and Innovation vs Startup Success

![Funding and Innovation](/docs/eda-plots/Funding-Amount.png)
![Funding and Innovation](/docs/eda-plots/Innovation-Score.png)


>Successful startups exhibit **higher median funding levels** and **greater innovation scores** compared to unsuccessful ones.  
>The funding box plot shows a clear upward shift for successful projects, suggesting that access to financial resources may enhance the likelihood of success.  
>Similarly, successful ventures have higher innovation scores, indicating that creativity and technological novelty contribute to positive outcomes.  
>Together, these findings emphasize the importance of both **innovation** and **financial support** in predicting startup success.


#### (f) Average Team Experience by Startup Success

![Average Team Experience](/docs/eda-plots/Team-Experience.png)

>The box plot compares the average team experience between successful and failed startups.
>Successful startups (green) have a slightly higher mean team experience of 2.31 years, compared to 2.24 years for failed startups (red).
>The median experience for successful startups is 2.34 years, while for failed ones it is 2.25 years.
>Both groups show similar variability (standard deviation ≈ 1.0), indicating that experience levels vary widely across teams regardless of outcome.
>While the difference is modest, the trend suggests that teams with slightly higher average experience tend to achieve better startup outcomes. Experienced teams may be more adept at strategic decision-making and handling startup challenges effectively.

#### (g) Business Model Score by Startup Success

![Business Model Score](/docs/eda-plots/Business-Model.png)

> The `business_model_score` represents a numerical rating (0–1) that measures how well-defined, feasible, and scalable each startup’s business model is.
> It captures how clearly the startup explains:
> 1. What problem it solves
> 2. Who the target customers are
> 3. How it generates revenue, and
> 4. How scalable or sustainable the model is.

**Summary:**  
>- The box plot compares business model scores between successful and failed startups.
>- Successful startups (green) have a higher mean business model score of 0.66, compared to 0.55 for failed startups (red).
>- The median score for successful startups is 0.70, while for failed startups it is 0.52, indicating a clear upward shift in performance.

> Both groups have similar variability (standard deviation ≈ 0.23), but the overall distribution shows that successful startups consistently achieve stronger business model evaluations.

> This suggests that startups with well-structured and viable business models are significantly more likely to succeed. A higher business model score reflects better planning, clearer value propositions, and sustainable revenue approaches — all of which contribute to greater success potential.


### (h) Trends of Numeric Features Over Time by Startup Success

![Numeric Features](/docs/eda-plots/Numeric-Features.png)

> 1. The multi-feature line plots illustrate the yearly progression (2019–2023) of key quantitative factors for both successful and failed startups.
> 2. Overall, successful startups demonstrate higher average values across critical attributes such as innovation score, business model score, and technology maturity, indicating stronger operational maturity and planning.
> 3. Funding levels and team experience show modest growth over time, reflecting a general improvement in project quality among student-led ventures.
> 4. In contrast, failed startups maintain lower average scores across most dimensions, suggesting that a combination of innovation, technological readiness, and structured business models contributes substantially to startup success.


#### (i) Correlation Heatmap

![Correlation Heatmap](/docs/eda-plots/CorrelationHeatmap.png)

 > 1. Funding Amount (r = 0.39) shows the strongest positive correlation with startup success, highlighting the critical role of financial support in achieving favorable outcomes.
>  2. Mentorship Support (r = 0.37) and Incubation Support (r = 0.37) both have strong positive relationships with success, confirming that institutional and expert guidance significantly enhance startup performance.
>  3. Innovation Score (r = 0.34) also correlates positively, suggesting that originality and creativity are essential contributors to successful student ventures.
>  4. Business Model Score (r = 0.24) and Technology Maturity (r = 0.19) demonstrate moderate associations, emphasizing that structured business planning and technically mature products improve the chances of success.
>  5. Market Readiness Level (r = 0.16) shows a mild correlation, indicating that projects closer to commercialization tend to perform slightly better.
>  6. Team Size (-0.06) and Average Team Experience (0.03) exhibit weak correlations, implying that team structure and experience alone do not significantly influence outcomes without adequate innovation and support mechanisms.
>  7. Competition Awards (-0.01) and Year (0.01) have minimal correlation, suggesting these factors are not directly tied to startup success in this dataset.

---

### 4.5 Key Insights

#### Descriptive Statistics of Successful Startups by Domain

To identify patterns among successful student startups, key statistics (median team size, mean innovation score, average funding, and average team experience) were computed for each project domain.

| Project Domain                  | Team Size | Innovation Score | Funding (USD) | Avg. Team Experience (Years) |
|----------------------------------|-----------:|-----------------:|---------------:|-----------------------------:|
| Agricultural Technology          | 4.0        | 0.73             | 33,175.26      | 2.35                        |
| Educational Technology           | 4.0        | 0.75             | 31,801.39      | 2.30                        |
| Financial Technology             | 4.0        | 0.72             | 31,668.31      | 2.27                        |
| Green Environmental Technology   | 4.0        | 0.74             | 31,234.39      | 2.25                        |
| Healthcare Technology            | 4.0        | 0.71             | 31,883.56      | 2.39                        |

**Observations:**
- All domains show a **median team size of four**, indicating that small to medium teams are the most common configuration among successful ventures.  
- **Educational Technology (0.75)** and **Green Environmental Technology (0.74)** demonstrate the **highest innovation scores**, suggesting these sectors encourage creative and forward-thinking solutions.  
- **Agricultural Technology** projects receive the **highest average funding (~$33,175)**, potentially reflecting increased investment in sustainability and agri-tech solutions.  
- **Healthcare Technology** teams show slightly higher **average experience (2.39 years)**, implying that domain knowledge and prior exposure may be particularly valuable in this sector.  
- Overall, successful startups maintain **balanced innovation, moderate experience, and comparable funding** across all domains, with small variations indicating domain-specific strengths rather than structural differences.


#### Descriptive Statistics of Successful Startups by Institution Type

To assess the influence of institutional environments on startup outcomes, descriptive statistics were calculated for successful student startups across different institution types.

| Institution Type | Team Size | Innovation Score | Funding (USD) | Avg. Team Experience (Years) |
|------------------|-----------:|-----------------:|---------------:|-----------------------------:|
| Non-Technical    | 4.0        | 0.739            | 32,511.49      | 2.25                        |
| Private          | 4.0        | 0.723            | 32,582.30      | 2.34                        |
| Public           | 4.0        | 0.741            | 31,362.54      | 2.40                        |
| Technical        | 4.0        | 0.718            | 31,327.08      | 2.27                        |

**Observations:**
- All institution types show a **consistent median team size of four**, confirming a stable collaborative structure among successful ventures.  
- **Public (0.74)** and **Non-Technical (0.74)** institutions record the **highest innovation scores**, reflecting stronger creativity and ideation culture in these settings.  
- **Private institutions** show slightly higher **average funding (~$32,582)**, suggesting more access to private or corporate investment channels.  
- **Public institutions** exhibit the **highest average experience (2.40 years)**, possibly due to exposure to structured entrepreneurship programs and mentorship networks.  
- Overall, differences among institution types are minor, implying that **institutional support mechanisms** play a more crucial role than structural or categorical differences.


#### Startup Success Distribution by Institution Type

The relationship between institution type and startup success was analyzed by grouping projects according to success outcomes.

- **Non-technical institutions** demonstrate the **highest success rate (~45%)**, suggesting that diverse or interdisciplinary project environments may foster stronger entrepreneurial outcomes.  
- **Public** and **Technical institutions** show comparable success rates (~42%), indicating stable performance likely supported by structured programs and technical expertise.  
- **Private institutions**, while contributing a large volume of projects, exhibit a slightly lower success rate (~39%), hinting at potential gaps in mentorship or funding access.  

Overall, the findings suggest that while institutional type has only a **moderate impact** on success, **non-technical institutions** may offer more flexible, cross-domain innovation spaces that support stronger startup outcomes.

1. **Innovation and Funding** are the most powerful predictors of startup success.  
2. **Institutional Support** (mentorship and incubation) correlates strongly with better outcomes.  
3. **Team Experience** plays a supporting role but is less critical than innovation intensity.  
4. **Business Model Clarity** and **Technology Maturity** also contribute meaningfully to overall success.  
5. The dataset is **clean, balanced, and ready** for predictive model training.

---
### 4.6 Feature Engineering

After completing exploratory analysis, several new features were engineered to enhance the dataset’s predictive power and capture key relationships between innovation, funding, and institutional support.

#### Engineered Features

| Feature Name | Description | Formula / Logic | Expected Insight |
|---------------|-------------|-----------------|------------------|
| **innovation_per_member** | Measures innovation efficiency per team member | `innovation_score / team_size` | Higher per-capita innovation may lead to success |
| **funding_per_member** | Funding efficiency per member | `funding_amount_usd / team_size` | Reflects resource utilization efficiency |
| **innovation_support_index** | Combines innovation with institutional backing | `innovation_score * (mentorship_support + incubation_support + 1)` | Captures synergy between creativity and support |
| **innovation_funding_interaction** | Joint influence of innovation and funding | `innovation_score * funding_amount_usd` | Measures how funding amplifies innovation |
| **total_support** | Total mentorship and incubation support | `mentorship_support + incubation_support` | Indicates institutional involvement |

#### Correlation Results

![Correlation Engineered Features ](/docs/eda-plots/correlation-featured.png)

| Feature | Correlation with Success |
|----------|--------------------------:|
| Innovation Support Index | 0.61 |
| Total Support | 0.52 |
| Innovation–Funding Interaction | 0.51 |
| Funding per Member | 0.29 |
| Innovation per Member | 0.23 |

#### Interpretation

- **Innovation Support Index (0.61)** shows the strongest relationship with success, confirming that innovation combined with institutional mentorship and incubation significantly drives outcomes.  
- **Total Support (0.52)** and **Innovation–Funding Interaction (0.51)** indicate that institutional and financial backing amplify startup potential when aligned with innovative ideas.  
- **Efficiency metrics** (*funding per member* and *innovation per member*) have moderate correlations, suggesting resource utilization contributes but is less critical than combined support.  
- These engineered variables outperform original features in correlation strength, validating their inclusion for model training.


## 5. Model Training

This section documents the exact modeling approach, evaluation metrics, and results obtained from the Jupyter Notebook used in this project. All values reported below are derived directly from the implemented experiments.

---

### 5.1 Predictive Models Implemented

Given the binary classification problem (startup success vs. failure), multiple supervised learning models were trained and evaluated to compare performance and interpretability.

#### Logistic Regression
- Used as a strong and interpretable baseline model  
- Helps understand feature importance and directionality  

#### Random Forest Classifier (with HyperTuning)
- Captures non-linear relationships and feature interactions  
- Robust to noise and multicollinearity  

Each model was trained using:
- **Original feature set**
- **Engineered feature set** (after encoding and transformations)

---

### 5.2 Training Strategy

#### Train–Test Split
The dataset was divided using an **80/20 train–test split**:
- **80%** of the data used for training  
- **20%** held out for final evaluation  

This ensures that all reported results reflect performance on unseen data.

#### Preprocessing Steps
- Categorical variables encoded using **one-hot encoding**
- Numerical features scaled where required
- Target variable (`success`) encoded as binary  
  - `0` = Unsuccessful startup  
  - `1` = Successful startup  

---

### 5.3 Python Libraries and Tools

The following Python libraries were used in model development and evaluation:

- **pandas** – Data cleaning and manipulation  
- **numpy** – Numerical computations  
- **scikit-learn** – Model training, preprocessing, and evaluation  
- **plotly.express** – Interactive EDA and performance visualizations  
- **matplotlib** – Supplementary plots  

---

### 5.4 Development Environment

- Local machine (laptop)
- **Jupyter Notebook** for experimentation and documentation
- **GitHub** for version control and reproducibility

---

### 5.5 Model Evaluation Metrics

Model performance was evaluated using multiple classification metrics:

- **Accuracy** – Overall correctness of predictions  
- **Precision** – Proportion of correctly predicted successful startups  
- **Recall** – Ability to identify truly successful startups  
- **F1-Score** – Harmonic mean of precision and recall  
- **ROC-AUC** – Ability of the model to distinguish between classes  

Additionally, **confusion matrices** and **ROC curves** were analyzed to better understand classification behavior.

---

### 5.6 Model Performance Comparison

Model performance was evaluated across two feature sets:
- **Set 1:** Original features
- **Set 2:** Original + engineered features

For the Random Forest model, an additional tuned version was evaluated using hyperparameter optimization.

The table below summarizes the evaluation metrics obtained on the test dataset.

![Model Comparision](/docs/model-plots/ComparisionTable.png)

---

### 5.7 Model Selection and Analysis

Among all evaluated models and feature sets, **Logistic Regression trained on the original feature set (Set 1)** achieved the best overall performance.

Key observations include:

- Logistic Regression outperformed Random Forest across all evaluation metrics
- The **original feature set** consistently produced better results than the engineered feature set
- Hyperparameter tuning for Random Forest resulted in marginal ROC-AUC improvement but did not improve accuracy or F1-score
- The Logistic Regression model demonstrated near-perfect class separation with a ROC-AUC of **0.9992**

Based on these results, **Logistic Regression (Set 1)** was selected as the final model due to:

- Highest accuracy and F1-score
- Exceptional ROC-AUC performance
- Model simplicity and interpretability
- Lower risk of overfitting on a relatively small dataset

This balance of performance and interpretability makes Logistic Regression well-suited for deployment in decision-support applications.

### 5.8 Feature Importance Analysis

To improve interpretability and understand the drivers of startup success, feature importance was analyzed using the coefficients from the final Logistic Regression model.

Figure below shows the **top 10 predictors of student startup success**, ranked by the magnitude of their logistic regression coefficients. Positive coefficients indicate a higher likelihood of startup success, while negative coefficients indicate a lower likelihood.

![Model Comparision](/docs/model-plots/TopPredictors.png)

**Key observations:**

- **Funding amount (USD)** emerged as the strongest predictor of startup success, highlighting the importance of financial backing.
- **Incubation support** and **mentorship support** showed strong positive influence, reinforcing the value of structured guidance and institutional resources.
- **Innovation score** and **business model score** also played a significant role, suggesting that idea quality and strategic planning are critical success factors.
- Features related to **technology maturity** and **market readiness** contributed positively but with relatively lower impact.
- Institution-specific features showed minimal or negative influence, indicating that startup success is more dependent on venture-level characteristics than institutional affiliation.

These results align with real-world expectations and provide actionable insights for university entrepreneurship programs and student founders.

### 5.9 ROC Curve Analysis

The Receiver Operating Characteristic (ROC) curve was used to evaluate the classification performance of the trained models across different decision thresholds.

Figure below presents the ROC curve for the final Logistic Regression model. The model achieved a **ROC-AUC score of 0.9992**, indicating near-perfect discrimination between successful and unsuccessful student startups.

This strong performance demonstrates that the model effectively separates the two classes and confirms its suitability for deployment in a decision-support application.

![Model Comparision](/docs/model-plots/ROC-Curve.png)

### 5.10 Confusion Matrix Analysis

To further evaluate classification performance, a confusion matrix was analyzed for the final Logistic Regression model.

The confusion matrix results are as follows:

- **True Negatives (TN): 242**  
- **False Positives (FP): 2**  
- **False Negatives (FN): 10**  
- **True Positives (TP): 166**

These results indicate that the model performs exceptionally well in distinguishing between successful and unsuccessful student startups.

**Interpretation:**

- The high number of **true negatives (242)** shows that the model accurately identifies unsuccessful startups.
- The very low number of **false positives (2)** indicates a minimal risk of incorrectly predicting success for unsuccessful startups.
- The model correctly identified **166 successful startups**, demonstrating strong predictive capability.
- A small number of **false negatives (10)** suggests that some successful startups were misclassified as unsuccessful, which may be addressed in future work through additional features or threshold tuning.

Overall, the confusion matrix confirms the robustness and reliability of the Logistic Regression model for this classification task.

![Model Comparision](/docs/model-plots/ConfusionMatrix.png)


