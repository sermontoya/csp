from csp import backtracking, initialize

variables = ["A", "B", "C", "D"]  
domain = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
constraints = ["A!=B", "A!=C", "B!=D", "C!=D"]


def main():
    courses = initialize(variables, domain)
    first_course = courses[0]
    remaining_courses = courses[1:]
    assigned_courses = []
    if backtracking(first_course, remaining_courses, assigned_courses, constraints):
        for course in courses:
            print(f"{course.name}: {course.value}")
    else:
        print("No solution found")
main()
