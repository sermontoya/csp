# class Course
#     function __init__(name, domain)
#         name <- name
#         domain <- domain
#         value <- empty

#     function assign(value)
#         value of the course <- value

#     function remove assignment
#         value of the course <- empty


# function initialize(variables, domain)
#     courses <- empty list

#     for each variable in variables
#         course <- new course with that variable and a copy of the domain
#         add course to courses

#     return courses


# function is consistent(course, assigned courses, constraints)
#     assigned by name <- dictionary of assigned courses using the name as key

#     for each constraint in constraints
#         left, right <- split the constraint by "!="

#         if the course is not left and is not right
#             continue with the next constraint

#         other name <- right if the course is left, otherwise left
#         other course <- assigned course with that name

#         if other course does not exist or has no assigned value
#             continue with the next constraint

#         if the current course value is equal to the other course value
#             return false

#     return true


# function backtracking(course, remaining courses, assigned courses, constraints)
#     for each day in the domain of the course
#         assign that day to the course

#         if the assignment is not consistent
#             remove the assignment from the course
#             continue with the next day

#         add the course to assigned courses

#         if there are no remaining courses
#             return true

#         next course <- first course in remaining courses
#         next remaining courses <- all remaining courses except the first one

#         if backtracking(next course, next remaining courses, assigned courses, constraints)
#             return true

#         remove the last assigned course
#         remove the assignment from the current course

#     return false


# function neighbors(name, constraints)
#     result <- empty list

#     for each constraint in constraints
#         left, right <- split the constraint by "!="

#         if name is equal to left
#             add right to result
#         else if name is equal to right
#             add left to result

#     return result


# function arc satisfied(x val, y val, X, Y, constraints)
#     for each constraint in constraints
#         left, right <- split the constraint by "!="

#         if (X is left and Y is right) or (X is right and Y is left)
#             if x val is equal to y val
#                 return false

#     return true

# function revise(X, Y, constraints)
#     revised <- false

#     for each x in a copy of X domain
#         if no value y in Y domain satisfies arc satisfied(x, y, X, Y, constraints)
#             remove x from X domain
#             revised <- true

#     return revised


# function ac3(courses, constraints)
#     course map <- dictionary of courses using the name as key
#     queue <- empty deque

#     for each constraint in constraints
#         left, right <- split the constraint by "!="

#         add (left, right) to queue
#         add (right, left) to queue

#     while queue is not empty
#         x name, y name <- take the first element from queue
#         X <- course with x name from course map
#         Y <- course with y name from course map

#         if revise(X, Y, constraints)
#             if X domain is empty
#                 return false
#             for each z name in neighbors(x name, constraints)
#                 if z name is not equal to y name
#                     add (z name, x name) to queue

#     return true

# function select mrv(unassigned, constraints)
#     return the course in unassigned with the smallest domain

# function select degree(unassigned, constraints)
#     unassigned names <- set of names of unassigned courses

#     for each course compute degree as the number of constraints
#         involving that course where the other variable is also unassigned

#     return the course with the highest degree

# function select mrv degree(unassigned, constraints)
#     min size <- smallest domain size among unassigned courses
#     candidates <- all unassigned courses whose domain size equals min size

#     if there is only one candidate
#         return that candidate

#     unassigned names <- set of names of unassigned courses

#     for each candidate compute degree as the number of constraints
#         involving that candidate where the other variable is also unassigned

#     return the candidate with the highest degree

# function select first(unassigned, constraints)
#     return the first course in unassigned

# function backtracking with inference(unassigned, assigned, constraints, select var)
#     if unassigned is empty
#         return true

#     course <- select var(unassigned, constraints)
#     remaining <- all courses in unassigned except course

#     for each day in a copy of course domain
#         assign that day to the course

#         if the assignment is not consistent
#             remove the assignment from the course
#             continue with the next day

#         add course to assigned
#         all courses <- assigned combined with remaining
#         saved domains <- save a copy of the domain of every course in all courses
#         set course domain to contain only that day
#         inference ok <- ac3(all courses, constraints)

#         if inference ok
#             if backtracking with inference(remaining, assigned, constraints, select var)
#                 return true

#         restore the domain of every course from saved domains
#         remove course from assigned
#         remove the assignment from the course
#     return false
