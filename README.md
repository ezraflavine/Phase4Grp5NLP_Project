## HATE SPEECH IDENTIFICATION

![image3.png](https://github.com/ezraflavine/Phase3_project/blob/main/image3.png)




# Hate Speech Identification Dataset

# About the Data
This dataset utilizes Twitter data and was created for research purposes in hate-speech identification. The text is classified into three categories: hate-speech, offensive language, and neither. It is crucial to note that the dataset contains text that may be considered racist, sexist, homophobic, or generally offensive.

Dataset Link: Hate Speech Identification Dataset

Definitions of Terms

CF: CrowdFlower
Tweet: Text tweet
Offensive Language Identifier
The data are stored as a CSV with each data file containing 5 columns:

count: Number of CrowdFlower users who voted for each tweet.

hate_speech: Number of CF users who judged the tweet to be hate speech.

offensive_language: Number of CF users who judged the tweet to be offensive.

neither: Number of CF users who judged the tweet to be neither offensive nor non-offensive.

class: Class label for majority of CF users in three categories:

a) 0 - hate speech
b) 1 - offensive language
c) 2 - neither

# Problem Statement
Identifying and detecting hate speech represents a pressing challenge in the realm of natural language processing (NLP) systems. Hate speech includes offensive language, discriminatory comments, and expressions of prejudice directed at individuals or groups based on attributes such as race, religion, ethnicity, gender, or other protected characteristics. Effective mechanisms for hate speech detection are crucial for maintaining the security of online spaces and fostering an environment that promotes peace and inclusivity.

Stakeholders
The ability to identify and detect hate speech in online communication platforms is crucial for various stakeholders who play distinct roles in the digital landscape.

Online Platforms:

Social Media Companies
Content Hosting Websites
Discussion Forums and Communities
These platforms are responsible for ensuring a safe and inclusive environment for their users. Detecting hate speech helps uphold community guidelines and maintain a positive user experience.

Users and General Public:

Individuals Engaging in Online Communication
Users benefit from platforms that actively identify and curb hate speech. It contributes to their safety, reduces the risk of online harassment, and fosters a more respectful online community.

Governments and Regulatory Bodies:

Government Agencies
Regulatory Authorities
Governments and regulatory bodies are concerned with safeguarding citizens and maintaining societal harmony. Policies and regulations related to hate speech detection can combat online hate crimes and protect vulnerable groups.

Non-Governmental Organizations (NGOs):

Civil Rights Organizations
Anti-Hate Groups
NGOs focused on civil rights and combating hate speech can leverage this capability to monitor and address instances of online hate, contributing to their advocacy efforts and promoting a more inclusive digital space.

Law Enforcement Agencies:

Police Departments
Cybercrime Units
Law enforcement may utilize hate speech detection to investigate and address cases where online communication escalates into criminal activity, ensuring legal consequences for those engaging in hate crimes.

Educational Institutions:

Schools and Universities
Educational institutions can benefit from hate speech detection to maintain a respectful online learning environment, prevent bullying, and educate students on digital citizenship.

Technology Companies and Developers:

NLP Algorithm Developers
AI and Machine Learning Experts
Those involved in developing NLP algorithms play a pivotal role. Improving hate speech detection algorithms contributes to the responsible development of AI technologies and aligns with ethical considerations.

# EDA Analysis

![image1.png](https://github.com/ezraflavine/Phase4Grp5NLP_Project/blob/main/image1.png)


![image2.png](https://github.com/ezraflavine/Phase4Grp5NLP_Project/blob/main/image2.png)

# Modelling
The best performing model is the Tuned Gradient Boosting Machine, that has shown good results in terms of accurately predicting words into hate speech and non hate speech category

![image4.png](https://github.com/ezraflavine/Phase4Grp5NLP_Project/blob/main/image4.png)

![image5.png](https://github.com/ezraflavine/Phase4Grp5NLP_Project/blob/main/image5.png)

# Recommendation

1. Tuned Gradient Boosting Machine (Tuned_GBM) appears to be the most balanced model with improved performance on both training and testing sets compared to the untuned GBM.

2. Logistic Regression (LR) remains a good option, especially if interpretability is important.

3. Decision Tree (DT) seems to overfit and may not generalize well to new data.

Tuned_GBM will accurately result to desirable predictions when used to sort out hate speech and non hate speech words from tweets.

# Conclusion

Therefore, the recommended model for adoption is Tuned Gradient Boosting Machine (Tuned_GBM).




