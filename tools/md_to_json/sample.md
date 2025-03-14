# Introduction to DBMS

## Data Vs Information

**Data** are a collection of raw facts, measurements or statitistics, often used as a foundation for reasoning, discussion or calculation to produce information.

**Information** is data that has been processed and changed into a meaningful and useful form for interpretation.
i.e: Information is data that has been contextualized via processess such as aggregation, manipulation and organization.


Information is affect by:

- Time (Timeliness, Currency, Frequency)
- Content (Accuracy, Relevance, Completeness)
- Form (Clarity, Detail, Order, Presentation)

## From Traditional Files to Databases

**Manual File Systems** are generally made up of file folders, each labelled and kept in physical storage.

**Computerized File Systems** were introduced to better handle the increased volume of data and files.

### Problems with Traditional File Systems

A file consists of **records**. Each **entity** about which data is stored has one record.
Each record of a file has the same **fields**.
A field (attribute) describe the record.


The issue with traditional files, is that data redundancy was more common. So if a change needed to be made for one record, a search would have to be conducted to reflect the change across all records. I.E, there was no centralized system or source of truth.

The basic problems are as follows:

- *Structural Dependence*
- *Data Dependence*
- *Data Redundancy*
- *Limited Data Sharing & Inadequate Security*
- *Not suitable for Ad Hoc Queries*
- *Excessive Program Maintenance*
- *Complex System administration*

## Databases

*Database* may have the following meanings:

1. A database is an organized collection of stored data.
2. A database is a shared collection of logically related data, designed to meet the information needs of multiple users in an organization.
3. A database is a shared, integrated computer structure that houses a collection of raw facts and metadata.
4. A database is a repository for stored data. It is *integrated* and *shared*.

The main definition we want to use is: A **database** is an organized and structured collection of data, composed of **fields**, **records** and **files**.

## Why databases?

With databases, the files are designed to meet the needs of the enterprise and all application programs.

### Advantages:

- Reduced Structural Dependence
- Reduced Data dependence
- Minimal Data Redundancy
- Consolidated Update Procedures
- Improved Data sharing and access.
- Reduced Program Maintenance
- Improved Productivity of Application Development
- Reduced Data Retrieval Times

## Database Architectures & Major Types of Databases.

There are 2 generic database architectures: **centralized** and **distributed**

### Centralized

This architecture encourages all data to be located at a single site. Centralized Databases provide greater control over accessing and updating data than distributed databases.
However, this makes them more vulnerable, since they depend on resources at a central site.

### Distributed

Here, the DBMS (Database Management System) supports a database distributed across several different sites. 
Databases are replicated to various sites and inter-connected via a network.

This improves database perofrmance and security.

### Transactional vs Decision Support Systems.

Database Management Systems, are sometimes classified according to the expected **type** and exxtent of use. IN this case, a distrinction is made between **transactional databases** and **decision support systems**.

A transactional database information is time-critical, such as inventory systems. Whereas, in the **DSS**, the data isn't as time-critical, but is instead used to make tactical / strategic decisions.

## Types of Databases

We will examine the following types of databases:

- Operational Databases
- Data Warehouses
- External Databases

### Operational Databases

These are used to hold data generated by a business' operations, such as inventory or product data. They provide a centralized area of storage which is important for information sharing.

Operational Databases have the ability to handle simultaneous read / write requests via pre-defined reports & queries. 

### Data Warehouses

Data warehouses mainly hold the organization's archival & historical data. This data is collected from databases across an organization.

This is the centeral source of data that has been cleaned, trnasformed and catalogued for business analysis.

### External databases

External Databases exxist outside of the organization and are used to hold a wide range of data that can include web databases.

## Database Management Systems

A ***database management system*** (DBMS) is software designed to aid increating, maintaining and utilizing large collections of data. It serves as a software interface between users and databases and therefore, amnages the structure of and controls access to the data.

### Components of a DBMS

**Storage Manager**: DBMS goes far beyond the file system in providing flexibility, such as data structures that support efficient access to very large amounts of data.

**Query Manager**: DBMS allows the user or application program to access and modify data through a pwoerful query language.

**Transaction manager**: Supports concurrent access to data, in three (3) different methods. These being: *isolation*, *atomicity* and *durability*

### Components of DBMS Environment

There are five main components which make up the DBMS **environment**.

- Users
- Software
- Hardware
- Data
- Procedures

## Major Functions of DBMS

The major functions of a database management system are expressed as:

- Database Development
- Database Interrogation
- Database Maintenance
- Multi-User Access Control
- Application Development

### Database Development

Developers can create databases using a **Data Definition Language** (DDL) in DBMS to specify the **entities**, **relationships** and **structure** of each databases.
These specifications are then stored in a **data dictionary**, which is a computer-based catalogue / directory containing the **metadata**

### Database Interrogation

A **query language** (Data Manipulation language) or **report generator** is used to ask the database for information. A query language allows ad hoc requests by keying in a query. A report generator however, allows users to specify a report format for presentation.

### Database Maintenance

The DBMS is used to effect database updates to reflect new transactions and other events, to ensure accuracy of data.

### Multi-user Access Control

To maintain data integrity and consistency, concurrent user transactions must be properly managed. The DBMS achieves this by ensuring that structures are in place to control simultaneous access by multiple users.

### Application Development

The DBMS may be used to create custom application programs, such as data entry screens, forms, reports and web pages.

## Levels of Data Representation.

There are 3 main levels of abstractions to consider when specifying a database structure:

1. External Level (View Level)
2. Conceptual Level (Logical Level)
3. Internal Level (Physical Level)

### External Level

This defines the user's interaction with the database and the different ways in which users can see or view their data based on their requirements.


### Conceptual Level

This describes the basic data elements of the real world (persons, things, etc) referred to as **entities**, data elements that describe the entities known as **attributes** and associations between the data elements called **relationships**.

### Internal Level

This level describes how data is actually stored and consists of the raw data existing on a physical device.

## Data Independence
maan
This is fundamental to database theory. It gives the Database Admin (DBA) the freedom of changing both the physical and logical aspects of the database system without disturbing the applications built on the External Level.
# Database Design

- Basic Components of Data Models
- Business Rules
- Historical database Models
- Hierarchiacal Model
- Network or CADASYL model
- Relational Model
- Object Oriented - Database
- Hybrid Relational / Object Oriented
- File Systems versus Databases


## Data Models

- Collection of concepts for describing the structure of data.
- Representation of data and its interrelationships which describe ideas about the real world.

- Help to reduce complexity and aid understandinig between desingers, developers and end users.
- Allows data to be given structure and manipulated


### Components

- **Entities** (Concept to be modeled)	
- **Attributes** (traits that define the entity)
- **Relationships** (Used to describe interactions or associations between entities)
- **Constraints** (Restrictions placed on that data. EX: age > 0)

## Business Rules

- A business rule is a statement which allows you to determine the entities, attributes, relationships and constraints on the model you are using.

- This is a statmeent which defines some constraint on a particular aspect of a database.

- Includes descriptions of:
	- Policies, procedures or processes within the organization which governs how it operates;
	- Operations and transactions
	- The characteristics of data.

Many sources of business rules, and these include but are not limited to:

- Company managers and end-users
- Policy makers
- Written documents
- Interviews with end users

During the database design process, guided by business rules:

- **Nouns** become **entities**
- **Verbs** become entity **relationships**

Relationships are bi-directional and may be identified by asking:

- How many instances of A are related to one instance of B?
- How many instances of B are related to one instance of A?

## Historical Database Models.

Types of models:

- Hierarrchical Model
- Network Model
- Relational Model
- Object-oriented Model

Note: This course will focus on the Relational Model

### Hierarchical Model

- Used in early mainframe DBMS packages
- Has a tree-like structure
- All records are dependent and arranged in a multilevel structure
- Problem arises when you need to represent Many-To-Many relationships

### Network Model

- More flexible than hierarchical
- Can be used to represent more complex logical relationshops
- Allows many to many relationships
- Cannot easily handle ad hoc queries


### Relational Model

- Consists of "flat file" tables, called **relations**
- Relations are made up of **tuples** (records) and **attributes** (fields or item types). **Relationships** between relations are implicit in the overlapping attributes used to define them.
- Major advantage, has a strong mathematical foundation, and properties useful for defining Data Manipulation Languages.
- SQL (Structured Query Language) is simple enough to learn that users can ask ad hoc queries to answer questions that had never been anticipitated at length

#### Issues

- cannot process large amounts of business transactions as quickly and efficiently as hierarchical and network models.
- Cannot process complex, high-volume data.

### Object-Oriented Model

- Other databases view entities in the world as having attributes.
- Each object has attributes as well as behaviours.
- Generally recommended when there is a business need for high performance;

### Hybird Relational / Object Oriented

Most vendors of relational databases allow the users to define their own data types. 
This allows users to continue to use SQL, in a database that may contain pictures, sound clips, and other multimedia objects.
# DB Design Intro & Conceptual Modelling

## Database Design

**Database Design** is the process of developing a database structure from user requirements.

The process beings with **analysis** of those requirements and goes thrrough a series of refinements to produce the desired database.

## Database System Life Cycle

- Analysis
- Conceptual Model (Construction of the **Entity-Relationship Diagrams** ERD's based on analysis)
- Logical Model (Conversion of conceptual model to a logical schema)
- Physical Model (Implementation of database based on the logical schema)
- Testing
- Maintenance

## Design and Development Process.

The **Conceptual Data Model** is used to define **WHAT** things of the 'real world' are to be modeled. It involves the analysis of data requirements to determine what data is important and should be maintained.

Defines: Entities, Attributes and Relationships.

The **Logical Data Model** is used to define **HOW** to best represent the characterisitics of these things we are interested in and the associations between them.

This is influenced by the chosen database theoretical framework (RDMS, OBject Oriented, Etc), and built using a **Database Schema**

This process involves converting the conceptual model to a logical schema using the sleelcted logical data model (e.g. relational), construct the data dictionary and normalize the attributes.

The **Physical Data Model** implements or entities, attributes and relations by mapping the logical model onto a physical system.

## The Conceptual Data Model

This is the design of the entire information content of the database, and is the consolidation of all user requirements in a DBMS-independent information structure or schema.

### The Entity-Relationship (E-R) Model

The E-R model is an important model of real-wrold situations,a nd is used to construct a conceptual data model.

ERD contains 3 main elements:

**Entities**
: The things you are collecting information about, represented by *rectangeles*

**Attributes**
: The characteristics of these things, represented by *ovals*.

**Relationships**
: The associations between these entities, represented by *diamonds*.

#### Entities

These can be thought of as *nouns*. Some examples of entities are Customer, Product, Order, Supplier.

Any entities included in the ERD must play a necessary role in the system. 
These entities must have a name that is a singular, concise and meaningful noun, and must be described by one or more attributes.

**Strong Entities**: These have primary keys, and their existence is not dependent on other entities.

**Weak Entities**: These depend on other entities for their existence, and cannot be uniquely identified using only their attributes. Their identifying primary key, is made up of their attributes, along with a foreign key from their parent entity. These are identified by a double bordered rectangle.

#### Attributes

These are used to describe the properties or *characteristics* of an entity, and can be thought of as adjectives, and are represented using an oval.

##### Types of Attributes

1. Simple Attribute: These are atomic values which cannot be broken down further.
2. Composite Attribute: These can be divided into smaller parts. For example, Name could be composed of FirstName and lastName.
3. Derived Attribute: These values can be derived from other values stored in the database and are therefore not stored in the physical database. Example, Age derived from Birthdate. These are represented using an oval with a dashed border.
4. Single-Valued Attribute: This is similar to a simple attribute and contains only one value.
5. Multi-Valued Attribute: These attributes can contain more than one value at any time. These are represented using an oval with a double border.

**Key Attributes**

Each entity requires a **key attribute** which can be used to uniquely identify each instance / record from another.

This is the minimum number of attributes that, when given value(s), uniquely identify one entity occurrence from another.

Key attributes are often called **primary keys** and they **must** contain values. 

A **foreign key** is a primary key which acts as an attribute for another entity.

Note:

- Key attributes **must** contain values.
- Primary keys are underlined with a Solid Line.
- Foreign keys are underlined with a dashed line.

#### Relationships

These define the associations between entities and can be thought of as verbs. These relationships are represented using a diamond.

Both the **type** and the **degree** (1:1, 1:M, M:M) must be specified.

The **type** must be a succint & meaningful verb, as well as bi-directional.

***Decomposing***

When given a Many to Many relationship, you must decompose it by creating a new entity. This will create two (2) 1:M relationships. This new *entity* will have a composite key of the primary keys of the entities connecting to it. For example:

Customer <--> Purchase <--> Product.

This is a many to many relationship, where multiple customers can purchase multiple products, and multiple prroducts can be purchased by multiple customers.

To resolve this, we turn the **type** (purchases) into a new entity called Purchase, who's attributes are the CustNo (the Customer entity's primary key) and ProdId (the Product entity's primary key).

This now creates a 1 to many relationship, where 1 customer can have many purchases.
And another where, 1 product can be part of many purchases.

## Dependencies in ERDs (Weak Entities)

A **data dependency** or **constraint** is a rule or condition that the data instances must obey.

1) **Existence Dependency** can occur between 2 entities. If X and Y are entities and each instance of Y must have a corresponding instance of X, then Y is **existence dependent** on X. As such, a Y entity cannot exist without some X entity. 

2) **Identitfier Dependency** is a special type of dependency that occurs when the weak entitiy set does not have a candidate key, and its instances are indistinguishable without a relationship with another entity.
# The Conceptual process

Three primary questions:

- What are the entities for which I am collecting information?
    - They must play a necessary role in the system.
    - Each entity with become a **table** in the (relational) logical design.

- What are the attrirbutes of these entities?
    - Select primary key attributes.
    - Each attribute will become a **column** in the (relational) logical design. 

- What are the **relationships** between these entities?
    - Determine the degree and type (1:1, !:M, M:M)
    - Attempt to decompose any M:M relationships identified.
    - Each relationship will become either a **column** or a **new table** in the logical design.
    - We don't get to choose. It depends on the nature of the relationships

## Entities - The things of interest

What things am I collecting information about?

- Student
- Course
- Lecturer
- Department
- Faculty

These will be the initial set of entitites - we may find more as we work.

## Attributes - Their Characterisitics

What pieces of information do i want to store for each entity?

- Student: StudentID, Name, Age, Gender, Phone, Address, Email

- Course: CourseID, Name, Lecturuer, Schedule, Meeting location, Pre-requisite

- Lecturer: LectureID, Name, Age, Gender, Phone, Address, Email

- Department: DeptID, Name, Dept_Head, Courses, Staff Members
- Faculty: FacultyID, Name, Fac_Head, Departments

## Relationships - Their Associations.

How are the entities related?

- A student takes one or more courses.
- A lecturer teaches one or more ecourses.
- A department offers one or more courses.
- A lecturer works in one department.
- A department employes one or more lecturers.
- A faculty has one or more departments.

Should be described:
- Qualitatively
- Quantitatively.

ERD (Entity Relationship Diagrams) can be used to help visualize

- Attributes are bubbles
- Entities are rectangles
- Include relationships


Given a 1:M (1 to many) relationship, we need to **add a foreign key column** to the table on the "many" side of the relationship.

# Decomposing Our ERD

Given a Many to Many relationship, we need to decompose (add a 'bridge' table).

This refers to adding a table between the 2, creating 2 1:M relationships.

Example:

Course (M) => Student (M)

Will be broken down into:

Course (1) => Registration (Many) <= Student (1) />

# Weak Entities

This is one who's existence is dependent on the existence of another entity.

Can only be identified uniquely by considering the primary key of another entity.

Example:

Employee (1) => Dependent(M)

Dependent can only be uniquely identified through the existence of the Employee entry.

# Design and Development Process

## Conceptual Design

- Analysis of business requirements.
- Construction of ERD's based on analysis

## Logical Design

- Conversion of ERD to Logical Model
- Functional Dependencies
- Normalization

Defines the database structures:

- The tables
- The fields in each tables
- The relationships between these tables and fields.

Influenced by a chosen database theoretical framework.

This involves:

- Converting the conceptual model to logical schemea using the selected logical data model.
- Construct the data dictionary
- Normalize the attributes

## Physical Design

- Implementation based on the logical model
- Testing to ensure it meets requirements

# Relational Databases.

A **relation** on sets D1, D2, ..., Dn is a subset of the Cartesian product D1 x D2 x .... x Dn.

# Relations

By convention, a relation is written using the format:

REL_NAME (attrib-1, attrib-2, ..., attrib-n)

Example:

TEACHER (Name, FacNum, Rank,...)

- TEACHER is called a **schema** or **intension**

- A table with actual values is called an **instance table**, **instance**, or **extension**

**intension** -> meaning


## Properties of Relations

- Entries in columns are atomic (No repeating groups)
- Entries in columns are from the same domain.
- Each row is unique
- Order of columns is insignificant


## Relational DML's 

- Relational Data Manipulation Languages

DML is used to query the relationships in a database. There are 2 main kinds

    - Relational Algebra
    - Relational Calculus

- The typical Relational Database commands are:
    - Projection (on columns / fields)
    - Selection (on rows / records)
    - Join (On tables / relations)

# Conceptual Model To Relational Schema

## The process

ERD -> Appropriate relational structure.
The structure is then fine-tuned to ensure efficiency during the implementation (and operation) phase.


Represent Entities -> Represent Relationships -> Normalize Relations (Refinement)

### Representing Entities

Each **entity** in the ERD is a relation (table) in the relational database.

Entity sets represented by **rectangles** become **relations**.

The relation name is the same as the entity name.

For strong entity sets, attributes become attributes (fields) of the relation.

Weak entity sets may require additional attributes (fields): an entity that is identifier dependent on another entiity has no key of its own, so the primary key of the corresponding strong entity is added to the list of attributes of the weak entity.

### Representing Relationships

Each **relationship** is defined using **key attributes**.

Generally, the relation representing the relationship has at least 2 attributes:

- Primary keys of the associated entities.
- Its own descriptive attributes if any.
/
1:1 relationships: Put the key of either relation in the other to show the connection.

1:M relationships: Place the key of A (the "one" side) in the relation for B(the "many" side), where it becomes a foreign key.

M:M relationships: a relation must be explicitly represented.


### Normalize The Relations

A series of stages called **normal forms** to remove specific types of dependencies and to ensure that databases are normalized correctly.

Refines each relation to avoid unnecessary redundancy and possible update anomalies.

Note:

Foreign keys are dashed underlines.
Primary keys are solid underlines.

## The Data Dictionary

This provides details of all tables in the user / designer-created database.

Contains (at least) all the attribute names and characterisitcs for each of the tables. It contains metadata as well.

Helps a database user in:

- Communicating with other users.
- Controlling data elementins in a simple way
- Reducing data redundancy and inconsistency.
- Determining the impact of changes to data elements on the whole database.
- Centralizing the control of data elements as an aid in database design.

# Relational Integrity Constraints

**Constraints**: These are conditions which must be followed.

Every relation (table) has somee condition which must hold true to be a valid value.

Types:

- Entity Constraints
- Domain Constraints
- Referential Integrity Constraints

## Entity (Key) Constraints

A key attribute in a relation must uniquely identify distinct tuples (records).

i.e, each record MUST contain a **PRIMARY KEY**

Note: Key attributes are unique identifiers which cannot contain null values.

Note: If there are more than one fields that can be the primary key, these are referred to as **candidate keys**.

## Domain Constraints

<b style='color:red'> **Each attribute will have a specific range of values** </b>

## Referential Integrity Constraints

**A record cannot be removed from the parent table if there are records in the child table referring to it**

**A record cannot be added to a child table if there is no existing parent record for the child record to refer to**

Note: Used to prevent the presence of **orpahn records** in tables.

# Key Attributes

We need keys to uniquely identify each record in your table.
Without them, duplicate or incorrect records may be returned.

| Key | Can Have redundancies |
| --- | --------------------- |
| Sk  |             Y         | 
| CK  |             x         |
| PK  |             x         |

## Super Key

A super key is a set of attributes used to uniquely identity each record in a table.

It specifies that no two records can have the same value for a super key value. The key value will not be repeated.

May contain redundant attributes.

## Candidate Key

These are a subset of your super key. THis is a super key **without** redundant attributes. 

Candidate keys are a minimal set of attributes used for the unique identification of records.

## Primary Key

A primary key is a candidate key which has been selected as being most appropriate to be the main key for a table.

Primary Keys:

- Contain unique Values
- Must never be null
- Uniquely identify records in a table
- Are mandatory for every table

## Secondary / Alternate Key

A table may have multiple candidate keys.

Once one of the candidates has beenn selected as the primary key, all remaining candidadate keys are deemed as being **secondary** or **alternate keys**.

Candidate keys not selected as the primary key are secondary / alternate keys

## Composite Key

A key made up of multiple attributes.

May also be called a **compound** or **concactenated key**


## Foreign Key

A key which identifies or defines a relationship between two tables.

Resides in one table, and is used to refer to the primary key in the other tbale.

1:M relationship:

Foreign Key's also used to ensure referential integrity constraints and prevent orphan records


# Determining Functional Dependencies

A functional dependency is a relationship that exists when one attribute uniequely determines another attribute.

If an attribute A uniquely determines an attribute B, we say A determines B (denotated as A -> B) where A is the 'determinant'

## Inference Rules For Functional Dependencies.

### Reflexivity

If X is a subset of Y, then Y -> X, ie, Y determines X.

Example: Given the set R (A, B, C)

- ABC -> ABC
- ABC -> AB
- ABC -> BC
- ABC -> AC

### Augmentation

If X -> Y then XZ -> YZ

### Transitivity

If X -> Y and Y -> Z then X -> Z

### Additive / Union Rule

If X -> Y and X -> Z then X -> YZ


### Pseudotransitive Rule

If X -> Y and YZ -> W then XZ -> W


### Productive Rule 

If X -> YZ then X -> Y and X -> Z

## Fully Functional Dependencies

Rule: If X -> Y then Y is fully functional dependent on X if it cannot be determined by any of the subsets of X

## Closure of an Attribute

The closure of an attribute is the set of attributes which can be determined by that attributes.

The closure of attribute A is denoted as *A+*

Assume R(A, B, C, D) with functional dependencies: A -> B, B -> D and C -> B

The closure of A:

A -> A by Reflexivity

A -> A, B since A -> B

A -> A, B, D since B -> D (transivity)

Therefore the closure of A is A+:{A, B, D}

To be a valid candidate, the attribute must be able to determine every other attribute

## Finding Candidate Keys

Assume relation R(A, B, C, D, E, F) and functional dependecnies: A -> C , C -> D, D -> B, E -> F. Find a possible candidate key.

Attributes C, D, B and F can be determined.

This is because each of these appear on the right hand side of a functional dependency.

If it cannot be determined then it will be part of the determinemant. Therefore, AE is a candidate.

Determining the closure of AE:

AE -> A, E                  Through Reflexivity

AE -> A, E, C               since A -> C

AE -> A, E, C, D            since C -> D

AE -> A, E, C, D, B         since D -> B

AE -> A, E, C, D, B, F      since E -> F

Therefore (AE) is minimal, and AE is a candidate key.

AE is minimal, as you cannot separate them and it still function as a key.


## Normalization

Process of obtaining "stable" groupings of attributes into relations bby decomposing a table into smaller, simpler tables.

Breaks up table into more than one table topo reduce redundancy and make it more efficient.

Aims:

- Minimize data anomalies and the presence of null values in relational tables.
- To minimize the number of relational tables that are created.

### Motivation

To reduce redundancy of data, that is, the same data is being stored repeatedly.
The redundancy needs to be removed as redundancies can lead to data anomalies, which are undesirable.

### Types of Data Anomalies

- Insertion
- Update
- Deletion

## Insertion Anomalies.

- Data redundancy increases the possibility of data entry errors and inconsistencies between new and existing data.


Example: 
- Insert a new record for student S2 to take CS420 database Sys.

## Update Anomalies

## Deletion Anomalies

## Normalization Process

- Used to remove unwanted redundancies and both partial and transitive dependencies from database design.

This has a series of *normal forms* to remove specific types of dependencies to ensure that databases are normalized correctly.

- 1NF
- 2NF
- 3NF
- BCNF (Boyce-Codd Normal Form)
- 4NF
- 5NF

 Generally, you will commonly see First Normal Form to Third Normal Form being used.

 4NF and FnF rarely seen as they can make a database too *granular* and cause problems when attempting to retrieve data.

 Granularity results in complex query commands being written to join many tables in the data retrieval process


## Normal Forms

1NF - Remove Repeating Groups
2NF - Remove partial Dependencies
3NF - Remove Transitive Dependencies


### First Normal Forms.

Ensure all columns (fields) are atomic. i.e, data in columns are single valued

Create separate tables for each group of related data and identify each row with a unique column or set of columns.

Ensure each column has a unique meaningful name

Ensure that a primary key is present.

#### Steps:

Step 1
: Eliminate the repeating groups
Step 2
: Identify the primary key
Step 3
: Identify all Dependencies 

*Notes*
Partial Dependency is when an attribute that is a part of a composite key, determines another field.
Transitive Dependency is when an attribute that is NOT a part of a composite key, determines annother field.

### Second normal forms

Rule: A relation is in Second Normal Form (2NF) if:

- It is in 1NF, and
- All non-prime attributes are fully dependent on the entire primary key

Process:

If an attribute(s) is partially dependent on the primary key. Move the partial dependecny out to new table.
Make the primary key from the original table, the primary key for new table.
Place all items that appear in the repeating groups in the new table.

### Third Normal Form

Rule: A relation is in 3NF if:

- It is in 2NF
- It has no transitive Dependencies.

Process:

Assume R(A, B, C) with primary key A and transitive dependency B -> C

Replace R with two tables:

R1(B, C) with primary key B
R2(A, B) with primary key A

Therefore, attribute B in R2 is a foreign key
