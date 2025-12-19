14. Let's assume that you are collecting training data from multiple persons for scientific purposes. The goal is to have
a SQL database and related visualisations that contain the following:
- Long-term general statistics that aggregate all the users
- Long-term statistics for individual users 
- Exercise-specific statistics for individual users
Assume that the raw data format is the JSON data in exercise 10.
Create the plans for:
a) Conceptual, logical and physical data model.
b) Related DAG workflow. 
c) Related data quality measures.
Note that you don't need to include all the observations and parameters. The aim of this exercise is to see the "big picture" 
and understand how data processing takes place.

## a) Conceptual, Logical, and Physical Data Model

### **Conceptual Data Model**  
<u>High-level view of the system</u>

The main entities in the system are:

- **User** – a person performing training activities  
- **Exercise** – type of activity (e.g. running, cycling)  
- **Training Session** – a single workout session  
- **Measurement** – recorded values during a session (heart rate, speed, calories)

**Relationships:**
- One **User** can have many **Training Sessions**
- One **Training Session** belongs to one **Exercise**
- One **Training Session** contains many **Measurements**

This model allows analysis at:
- Global level (all users)
- Individual user level
- Individual exercise level

---

### **Logical Data Model**  
<u>Relational database structure</u>

The conceptual model is translated into relational tables:

**Users**
- `user_id` (Primary Key)
- age
- gender
- height
- weight

**Exercises**
- `exercise_id` (Primary Key)
- exercise_name

**Training_Sessions**
- `session_id` (Primary Key)
- `user_id` (Foreign Key)
- `exercise_id` (Foreign Key)
- start_time
- duration

**Measurements**
- `measurement_id` (Primary Key)
- `session_id` (Foreign Key)
- timestamp
- heart_rate
- speed
- calories

This structure supports efficient joins and flexible queries.

---

### **Physical Data Model**  
<u>Implementation details</u>

- **Database:** PostgreSQL  
- **Indexes:**  
  - `user_id`, `session_id`, `timestamp`
- **Partitioning:**  
  - Measurements table partitioned by time
- **Storage strategy:**  
  - Raw JSON stored in a staging area or data lake  
  - Cleaned and validated data stored in normalized SQL tables

---

## b) DAG Workflow (Data Pipeline)

<u>End-to-end data processing flow</u>

A typical DAG (e.g. implemented with Airflow) consists of the following steps:

1. **Ingest raw JSON data**  
   - Data arrives from devices or APIs
2. **Schema validation**  
   - Check required fields and data types
3. **Data cleaning**  
   - Remove duplicates  
   - Handle missing or invalid values
4. **Data transformation**  
   - Flatten JSON  
   - Convert units if needed
5. **Load into SQL database**
6. **Aggregation**
   - Daily, weekly, and monthly statistics
7. **Visualization**
   - Dashboards for users and global insights

The DAG can run **daily or hourly**, depending on data volume.

---

## c) Data Quality Measures

<u>Ensuring reliable and trustworthy data</u>

Key data quality checks include:

- **Completeness**  
  - No missing `user_id`, `timestamp`, or `exercise_id`
- **Validity**  
  - Heart rate within realistic range (e.g. 40–220 bpm)
- **Consistency**  
  - Units and formats consistent across users
- **Uniqueness**  
  - No duplicate `session_id` or measurements
- **Timeliness**  
  - Data arrives within expected time window

**Tools and techniques:**
- SQL constraints
- Pandas validation
- Great Expectations

## Final Remarks

This architecture:
- Scales to many users
- Separates raw and processed data
- Supports both analytics and visualization
- Provides a strong foundation for future machine learning use cases
