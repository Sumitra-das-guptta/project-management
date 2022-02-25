# Project Management
## 5 principles of Project Management
- Initiation
    - project scope
    - higher level porject overview
    - write project charter or Project Initialization Documentation(PID)
    - Select project Leader
    - Budgets

- Planing
    - Key milstones and dates are set
    - Select Methodology
    - Select Team Members
    - Outlining deliverables
    - Estimating resources
    - Determining associated activities
- Execution
    - Managing workflows
    - Recommending changes and corrective actions
- Monitoring/Controlling
    - regular, consistent project check Ins
    - proper project documentation

- Closure
    - project deliverry
    - Conclusion of any formal contracts or agreement
    - A full review or audit of what went well, what didn’t go as planned, and how future teams and projects could learn from this one.

## Gantt Chart
- used for project schedule
- provides clarity on deadlines, milestones, and project progress.
- key components:
    - Date/time duration
    - Tasks/ Items
    - Owner
- why use gantt chart
    - assist the planning and scheduling of projects
    - 

## State Machine Diagram
- Behavior Diagram
- event
- state
- Activity
- Transition
- Fork
## Activity Diagram
- Non programmers use flowchart and programmers use activity diagram to depict workflows.
- Action or activity state
- Control flow
- Decision node or branching
- guards( conditions )
- Fork (concurrent activities)
- join
- merge events : activities not concurrently happened
- swimlanes: not mandatory. Grouping related activity in one column. 
- time event 
- final state

Task Update:

1. Studied about 5 principles of project management.
2. An overview of gantt chart 
3. Studied about Sequence, state machine and activity diagram  and explore tools and extensions in vscode to draw diagrams.

## Project Requirement Analysis
It’s a process of identifying, analyzing, and managing project requirements to determine what the project should accomplish and eliminate any ambiguities or conflicting requirements in your project plan. 
- gather project requirements from sponsors and end users.

3 main stages:
- gather requirements by collecting business documentation and interview with stakeholders
- analyze and validate requirements
- record the requirements and monitor implementation throughout the project

## Requirement Analysis Techniques for business need
- gap analysis
- Business Motivation Model
- Customer Journey Mapping
## Requirement Analysis Techniques for software requirements
- Data Flow Program
- Use cases : define system behavior and communicate from the end users perspective.
- user stories: focus on user's needs.
## Challenges of identifying project requirements
- Stakeholders don't know what they want
- Requirements are often dynamic 
- Poor communication between teams
- The development team is oblivious to the organization's politics
## Requirement Analysis Document
- Purpose
- Audience
- Functional Requirements
- Technical Requirement( how software built, in which language, OS)
## Work Breakdown
It's a way to divide and conquer large projects to get things done faster and more efficiently. 

A deliverable-oriented hierarchical decomposition of the work to be executed by the project team.

Each new level in the hierarchy includes all the work needed to complete its parent task.
## Work breakdown structures
- spreadsheet
- flowchart (mostly used)
- list
- Gantt Chart
## Effort Estimation
- process of forecasting how much effort is required to develop or maintain a software application. 

Rather than using time or cost estimates, they will look at user stories and story points. 
- user story
- story points
## Agile Effort Estimation Techniques
- Planning Poker: team members assign values to story points.
- T-shirt sizes: story points take the form of sizes: extra-small (XS), small (S), medium (M), large (L), and extra-large (XL). 
- Dot voting: 

Relative Sizing:
- T-shirt Sizing
- Finonacci series
- Story points
- Poker Planning
- Agile Estimation
- CoCoMo Model
applied in 3 classes.
1. organic mode: porject_size= 2-50kLOc, small
size, nature of project=experience developers
ex-payroll, inventory
,innovation=little, deadline=not tight
2. Semidetached mode: 50-300kLOC, medium size
ex-db system, not tight deadlines
3. Embedded: over 300kLOC, large project,real time system, 
ex- ATMs, significant, tight deadline
- Basic CoCoMo Model: E = effort applied
D =  development time
people required ,P = E/D
ab,bb,cb,db are coefficients.
have standerd values for this coefficients.
- Intermediate CoCoMo Model:
set of 15 additional predictors(cost drivers)
cost drivers adjust nominal cost of porject to 
actual project environment. 15 cost drivers:
1. product attributes:
    - s/w reliability
    - database size
    - product complexity
2. computer attribute:
    - execution time constants
    - main storasge constraints
    - virtual machine volatility
    - computer turn around time
3. personal attributes:
    - analyst capability
    - app experience
    - programmer capability
    - virtual machine experience
    - programming language experience
4. project attributes
    - modern programming practices
    - use of s/w tools
    - required development schedule

each cost driver is rated for the given project environment
in terms of 
very low, <1
low, <1
normal, 
high, 
very high
,extra high
E = ai(kloc)bi * EAF(effort adjustment factor)
D = C(Ei)di
EAF can be calculated by multiplying all the valuees
that have been obtained after categorizing 
each cost driver.
coefficient values from the defined table.

## task prioritization
Organizing tasks in terms of importance relative to one another.
## Problems:
project scope,
project deliverables/ backlog,







