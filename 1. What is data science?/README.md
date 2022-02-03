# 1. What is data science?

### Data science and data mining

The expression **data scientist** is common nowadays in job descriptions, referred to a mix of data analysis skills and a background of programming languages and data bases. It is a broad job title coming in many forms, with the specific demands depending on the industry, the business and the role. So, certain skillsets suit certain positions better than others. Data scientists do not do anything essentially new. We have long had statisticians, analysts, and programmers. What is new is the way different skills are combined in a single profession.

An ancestor of data science is **data mining**, born in the computer science field. This generic expression applies to a heterogeneous set of methods, used to extract information from large data sets. It is understood as *mining knowledge from data*. The typical applications in management are related to Customer Relationship Management (CRM): market basket analysis, churn modeling, credit scoring, etc. From a technical perspective, the content of a data mining course may do not differ much from that of a data science course.

### Core competencies

At the business place, the data scientist takes care of the **data pipeline**, which is a sequence of data processing elements, in which the output of one element is the input of the next one. These elements involve core competencies such as:

* **Data capture**. This may require managing a data source, using database management skills, and understanding the data domain, to formulate relevant questions. It may also require data-modeling skills in order to understand how the data are connected.

* **Data wrangling** is a generic expression which refers to the operations that are performed on the data until they get ready for the analysis. Regarded as the preliminary steps in a data pipeline, we call this **data preprocessing**. Typical preprocessing steps are: removing duplicates and redundant variables, renaming and/or combining levels of categorical variables, solving the issues associated to missing data, filtering out parts of the data, combining data sets by means of joins and unions, and aggregating the data based on one or more grouping variables. When the data are extracted from a database, some of these operations can be integrated in the data extraction step by means of an appropriate query.

* **Analysis**. The analysis typically starts at an exploratory level, using basic statistical tools, much like those that just about everyone learns in college. In many cases, this is followed by an attack with more advanced machine learning tools.

* **Presentation**. Most people do not understand numbers well. They cannot see the patterns that the data scientist sees. It is important to provide a graphical presentation of these patterns to visualize what the data reveal and how to exploit them. More important, the presentation must tell a specific story so the impact of the data is not lost.

* **Developing data products**, such as a recommendation system, a pricing algorithm or a fraud detection procedure. **Machine learning** techniques are typically used here.

This course is mainly concerned with the first three steps.

### Data science in the computer

Users interact with data science software applications in three possible ways:

* Conventional menus and mouse-clicking, as in Tableau.

* Programming code (Python, R, etc).

* Visual programming, based on flow charts which are a graphical translation of code.

This course is based on code. More specifically, it uses Python, which is, currently, the leading choice of data scientists. About 15 years ago, data mining textbooks were using visual programming and/or menus in their examples, but, nowadays, most data science books are based on Python, and the examples include code.

The majority of the data science tasks are performed on **structured data**, that is, on data sets in tabular form, with rows and columns. The rows correspond to the **samples**, which are typically individuals, companies or transactions, and the columns to **features**. The features are either **numeric** (eg price) or **categorical** (eg gender). Nevertheless, there are also methods for dealing with **string** (text) data and **datetimes**. Categorical features are managed with 1/0 valued **dummies** in many analyses.

In Python, tabular data sets are typically managed as objects called **data frames**. Roughly speaking, a data frame is a collection of data (column) vectors, all of the same length. All the data points in the same column are of the same type, but the data frame can contain columns of different types.
