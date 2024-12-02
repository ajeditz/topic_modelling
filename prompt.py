def prompt(syllabus, pyqs, additional_instructions):
    p=f""" Task Objective:
You are an advanced AI assistant tasked with analyzing a subject's syllabus and previous year question papers to identify the most important topics and questions that are most likely to appear in upcoming exams. You will provide a list of these topics (or questions) ranked by their likelihood of occurrence based on the analysis of the syllabus and past exam patterns.

Input:

Syllabus: The detailed syllabus for the subject, including topics, subtopics, and any additional notes or guidelines.
 {syllabus}
Previous Year Question Papers: A collection of previous year question papers (preferably for the last 3-5 years).
{pyqs}
Instructions:

Understand the Syllabus:

Carefully read through the syllabus and list all the major topics and subtopics mentioned.
Identify key areas that are emphasized, such as topics with more detailed descriptions or specific instructions.
Analyze Previous Year Question Papers:

Look for recurring topics and concepts and questions that appear frequently across multiple years.
Identify the types of questions asked, including theoretical questions, practical problems, case studies, or essays.
Pay attention to any trends in question format, such as specific sections (e.g., long-answer, short-answer, multiple-choice) that are repeatedly targeted.
Cross-Reference Syllabus and Question Papers:

Compare the syllabus with the topics asked in previous exams.
Identify which topics from the syllabus have been most frequently tested.
Note any new emerging patterns or shifts in focus in recent years (e.g., new topics becoming more prominent or older topics being asked less frequently).
Rank the Topics:

Based on frequency, importance, and coverage, rank the topics in order of likelihood of appearing in upcoming exams.
Include brief explanations of why each topic is important, citing its frequency in previous exams and relevance to the syllabus.
Present Your Findings:

Provide a ranked list of the most important topics to study, with a focus on the ones most likely to appear in the upcoming exam.
Include suggestions for additional areas to focus on (if any) based on the trends observed.
Use very simple and concise language (10th grade vocabulary)
Example Prompt Execution:

Syllabus Example: The syllabus for "Data Structures" includes topics like:

Arrays and Strings
Linked Lists
Stacks and Queues
Trees (Binary Trees, AVL Trees)
Graphs
Sorting and Searching Algorithms
Dynamic Programming
Previous Year Question Paper Example: Year 2020: Questions on Linked Lists, Stacks, Sorting Algorithms. Year 2021: Questions on Trees, Dynamic Programming, Graphs. Year 2022: Questions on Linked Lists, Arrays, and Sorting Algorithms.

Output Example:

Linked Lists: Frequently tested in all three years. Appear in theoretical questions and practical problems. A core topic in data structures.
Sorting Algorithms: Appears in 2020 and 2022. Likely to appear in the exam due to its fundamental nature in algorithms.
Trees (Binary Trees): Important from the syllabus and has appeared multiple times. Strong focus on tree traversals and binary search trees.
Dynamic Programming: Appears only once but is a topic gaining importance. Focus on optimization problems.
Graphs: Lesser frequency, but may appear due to their applications in real-world problems.
Stacks and Queues: Appeared in 2020. May be asked in the context of algorithm design or implementation.
Additional Information (Optional):
Weightage: Provide an estimate of the weightage of each topic (e.g., High, Medium, Low) based on its frequency and importance in exams.
Suggestions for Further Study: Based on the analysis, suggest if there are any new topics in the syllabus or any areas that seem to be underrepresented in past exams but are present in the current syllabus.

Additional Instructions by the user: {additional_instructions}
"""
    return p