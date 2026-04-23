class Course:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.value = None
        
    def assign(self, value):
        self.value = value
    
    def remove_assignment(self):
        self.value = None
        
    def initialize(self, variables, domain):
        self.courses = []
        for variable in variables:
            course = Course(variable, domain.copy())
            self.courses.append(course)
        return self.courses
    def __str__(self):
        return f"{self.name}: {self.value}"


def initialize(variables, domain):
    courses = []
    for variable in variables:
        course = Course(variable, domain.copy())
        courses.append(course)
    return courses


def is_consistent(course, assignedCourses, constraints):
    assignedByName = {c.name: c for c in assignedCourses}
    for constraint in constraints:
        left, right = constraint.split("!=")
        if course.name != left and course.name != right:
            continue
        othername = right if course.name == left else left
        othercourse = assignedByName.get(othername)
        if othercourse is None or othercourse.value is None:
            continue
        if course.value == othercourse.value:
            return False
    return True


def backtracking(course, remainingCourses, assignedCourses, constraints):
    for day in course.domain:
        course.assign(day)
        if not is_consistent(course, assignedCourses, constraints):
            course.remove_assignment()
            continue
        assignedCourses.append(course)
        if not remainingCourses:
            return True
        nextCourse = remainingCourses[0]
        nextRemainingCourses = remainingCourses[1:]
        if backtracking(nextCourse, nextRemainingCourses, assignedCourses, constraints):
            return True
        assignedCourses.pop()
        course.remove_assignment()
    return False
