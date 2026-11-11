# Reddit Typology

## Why
This typology needs to exist because we need a way to categorize 
posts within the McGill and Concordia subreddits. We need to categorize 
them in order to get a better idea of what each subreddit consists of, 
without having to read every single post. This typology allows to get a 
general understanding without having to do so.


## Relations Between Types
There a 7 types in total. Each of them are a possible topic for a 
reddit post to fall under. A lot of random posts end up in Social as 
this type includes random posts that users post for various reason that 
don't fall under the other categories

## Types
### Social

* **Description:** Posts about student community, memes, campus politics, 
events, hobbies, non-academic surveys, students venting, and any random 
post that a student posts that doesn't fit in another category.  
* **Inclusion Criteria & Rationale:**  
  * "Where do yall go on night outs?"- Directly solicits leisure, nightlife, and social activity recommendations within the student community.
  * "VP External elect Justice Bongiovanni disqualified from March SSMU 
    elections" - Relates to student governance, campus politics, and 
    electoral controversies affecting the student body.
* **Exclusion Criteria & Rationale:**
  * "How can I stay motivated to study for courses I’ve lost all 
    passion for?" - While posted to the community for empathy, the core 
    intent is coping with academic burnout and emotional distress; code as `Motivation and Advice`.
  * "Smells like feces on campus…" - Although functioning as a community 
    observation, it reports an environmental hygiene and physical grounds issue; code as `Campus Facilities and Resources`.
* **Edge Cases & Rationale:**
  * "To the guy who checked up on me this morning after my exam" - Code 
    as `Social`**. Although an exam is mentioned contextually, the post functions as an open "missed connection" and an expression of gratitude between peers rather than a discussion of course content (`Course Info and Exams`) or a mental health intervention (`Motivation and Advice`).

### Housing

* **Description:** Posts regarding finding, maintaining, transferring, or leasing student accommodations both off-campus and in student residence buildings.
* **Inclusion Criteria & Rationale:**
  * "Group of 9 looking to take over a plex (or two side-by-side units) for Sept 2027" - An explicit search to take over a multi-unit lease transfer for student living arrangements.
  * "3rd year looking for new housing options sept 2027" - Direct inquiry regarding residential real estate, leases, and apartment hunting.
* **Exclusion Criteria & Rationale:**
  * "Grey Nuns Reading Room ID issue" - Grey Nuns is a residence building, but the reading room functions as a university library and study facility open to students; code as `Campus Facilities and Resources`.
  * "mcgill area water shutoff" - Addresses broad municipal/neighborhood utility infrastructure rather than an individual lease or apartment search; code as `Campus Facilities and Resources`.
* **Edge Cases & Rationale:**
  * "Scared student with no heat" - **Code as `Housing`**. While the title contains emotional distress language ("scared"), the functional problem is residential tenant habitability and landlord obligations regarding winter heating in student lodging, not academic coping (`Motivation and Advice`).

### Course Info and Exams

* **Description:** Posts focused on the operational mechanics, evaluation components, content delivery, grades, and study materials of specific university courses.
* **Inclusion Criteria & Rationale:**
  * "HIST 205 ancient med final"* / *"CLAS210 Test 2" - Direct, specific inquiries about scheduled evaluations and format details in particular registered courses.
  * "Blue link anki deck for ANAT 214" - Involves study resources, flashcards, and prep tools tied to a specific curriculum code.
* **Exclusion Criteria & Rationale:**
  * "Opinion on Data Science (BCompSc) degree" - Evaluates the overarching curriculum and departmental program pathway rather than a single course evaluation; code as `Degree Planning`.
  * "How the future looks after no summer internships" - Pertains to employment prospects and professional recruiting, not course evaluations; code as `Professional Development`.
* **Edge Cases & Rationale:**
  * "MECH 321 missed lab and midterm" - **Code as `Course Info and Exams`**. Missing an assessment induces panic, but the subject matter is an evaluation policy and grade component within a specified course, distinguishing it from general unanchored panic (`Motivation and Advice`).

### Campus Facilities and Resources

* **Description:** Posts related to physical university grounds, study spaces, campus security, hygiene, institutional amenities, student benefits, and campus transit connectivity.
* **Inclusion Criteria & Rationale:**
  * "closing grey nuns is remarkably idiotic - rant" - Focuses on student access to institutional physical study spaces and building closures.
  * "The Person I Asked to Watch Over my Laptop, Stole my Laptop 😭" - 
    Concerns physical security, theft, and lost property on university property.
 * **Exclusion Criteria & Rationale:**
  * "3rd year looking for new housing options sept 2027" - Concerns private off-campus accommodation rather than campus grounds or university-managed amenities; code as `Housing`.
  * "DROP YOUR CLASSES" - Involves academic registration systems and deadlines rather than physical resources; code as `Degree Planning`.
* **Edge Cases & Rationale:**
  * "why is concordia metro blocked at guy entrance??" - **Code as `Campus Facilities and Resources`**. Although the STM metro is municipal, the Guy-Concordia entrance directly connects to campus tunnels and serves as primary student transit infrastructure directly accessing university facilities.

### Motivation and Advice

* **Description:** Posts seeking or sharing emotional encouragement, study motivation, burnout coping mechanisms, general academic crisis navigation, and milestone peer support.
* **Inclusion Criteria & Rationale:**
  * "How do I get out of a negative academic mindset?" - Asks for psychological frameworks and mindset advice to navigate academic pressure.
  * "So burned out what’s happening" - Expresses personal emotional and physical exhaustion caused by prolonged academic stress.
* **Exclusion Criteria & Rationale:**
  * "27 male never held a single job in his life - what should I do?" - Although asking for broad life advice, the focus is career entry and employability; code as `Professional Development`.
  * "Advice for COMM classes" - Asks for strategic curricular choices and program navigation rather than mental wellness or emotional coping; code as `Degree Planning`.
* **Edge Cases & Rationale:**
  * "Missed Multiple Midterms HELP" - **Code as `Motivation and Advice`**. While midterms are mentioned, there are no specific course codes, class syllabi, or instructional queries provided; the post represents a high-distress crisis appeal for how to navigate a personal emergency.

### Degree Planning

* **Description:** Posts concerning long-term curriculum structure, program requirements, scheduling software, course dropping/swapping strategies, and academic standing policies.
* **Inclusion Criteria & Rationale:**
  * "No exam COMP classes for a Comp Minor" - Seeks curricular navigation across an entire academic minor to optimize evaluation formats across a degree path.
  * "Gpa!!!" - Inquires about cumulative academic standing, GPA thresholds, or graduation/probation criteria.
 * **Exclusion Criteria & Rationale:**
  * "Comp 550 next semester" - Targets a single specific course's workload and offering rather than degree-level curriculum mapping; code as `Course Info and Exams`.
  * "Concordia career fair" - Relates to career progression and employer recruitment rather than academic course selection; code as `Professional Development`.
* **Edge Cases & Rationale:**
  * "DROP YOUR CLASSES" - **Code as `Degree Planning`**. Relates to administrative academic registration deadlines (course drop/DNE date), academic record implications, and course-load management.

### Professional Development

* **Description:** Posts regarding career preparation, job hunting, internships, clinical shadowing, networking events, post-grad employment, and career-oriented fellowships.
* **Inclusion Criteria & Rationale:**
  * "Employer canceled Internship" - Discusses an abrupt cancellation of 
    a professional co-op/internship contract.
  * "After 2 months and a half of looking , finally got my first job after graduation in Marketing."- Documents post-graduate employment success and the state of the marketing job market.
* **Exclusion Criteria & Rationale:**
  * "Survey - Engineering students only"- General student-circulated survey data collection rather than professional recruitment or career counseling; code as `Social`.
  * "F students become Concordia employees" - A campus humor/satirical meme post regarding institutional hiring stereotypes rather than job placement or professional training; code as `Social`.
* **Edge Cases & Rationale:**
  * "PSA: Learn French if you're an international student and want to stay in Canada (ex - Quebec)" - **Code as `Professional Development`**. Framed explicitly around post-graduation employability, workforce readiness, and navigating local Quebec labor market realities.


## Comprehensiveness
This typology is comprehensive because every item can easily be 
categorized as one of the seven types. The Social type helps for some 
confusing examples, but most items either fully belong in Social or 
some other more descriptive type.