from cps_backtracking.csp import Course, backtracking, initialize, is_consistent


def test_course_stores_name_domain_and_starts_unassigned():
    course = Course("A", ["Monday", "Tuesday"])

    assert course.name == "A"
    assert course.domain == ["Monday", "Tuesday"]
    assert course.value is None


def test_course_assign_sets_value():
    course = Course("A", ["Monday"])

    course.assign("Monday")

    assert course.value == "Monday"


def test_course_remove_assignment_clears_value():
    course = Course("A", ["Monday"])
    course.assign("Monday")

    course.remove_assignment()

    assert course.value is None


def test_course_str_shows_name_and_value():
    course = Course("A", ["Monday"])
    course.assign("Monday")

    assert str(course) == "A: Monday"


def test_initialize_creates_one_course_per_variable():
    courses = initialize(["A", "B", "C"], ["Monday", "Tuesday"])

    assert [course.name for course in courses] == ["A", "B", "C"]
    assert [course.domain for course in courses] == [
        ["Monday", "Tuesday"],
        ["Monday", "Tuesday"],
        ["Monday", "Tuesday"],
    ]


def test_initialize_copies_domain_per_course():
    courses = initialize(["A", "B"], ["Monday", "Tuesday"])

    courses[0].domain.append("Wednesday")

    assert courses[0].domain == ["Monday", "Tuesday", "Wednesday"]
    assert courses[1].domain == ["Monday", "Tuesday"]


def test_is_consistent_returns_true_when_no_conflict():
    course_a = Course("A", ["Monday", "Tuesday"])
    course_b = Course("B", ["Monday", "Tuesday"])
    course_a.assign("Monday")
    course_b.assign("Tuesday")

    assert is_consistent(course_b, [course_a], ["A!=B"]) is True


def test_is_consistent_returns_false_when_conflict_matches_constraint():
    course_a = Course("A", ["Monday", "Tuesday"])
    course_b = Course("B", ["Monday", "Tuesday"])
    course_a.assign("Monday")
    course_b.assign("Monday")

    assert is_consistent(course_b, [course_a], ["A!=B"]) is False


def test_is_consistent_ignores_unrelated_or_unassigned_courses():
    course_a = Course("A", ["Monday", "Tuesday"])
    course_b = Course("B", ["Monday", "Tuesday"])
    course_c = Course("C", ["Monday", "Tuesday"])
    course_a.assign("Monday")
    course_c.assign("Monday")

    assert is_consistent(course_b, [course_a, course_c], ["A!=C"]) is True


def test_backtracking_returns_true_for_satisfiable_problem():
    courses = initialize(["A", "B", "C"], ["Monday", "Tuesday"])
    first_course = courses[0]
    assigned_courses = []

    solved = backtracking(first_course, courses[1:], assigned_courses, ["A!=B", "B!=C"])

    assert solved is True
    assert len(assigned_courses) == 3
    assert all(course.value is not None for course in courses)
    assert courses[0].value != courses[1].value
    assert courses[1].value != courses[2].value


def test_backtracking_returns_false_for_unsatisfiable_problem():
    courses = initialize(["A", "B"], ["Monday"])
    first_course = courses[0]
    assigned_courses = []

    solved = backtracking(first_course, courses[1:], assigned_courses, ["A!=B"])

    assert solved is False
    assert assigned_courses == []
    assert all(course.value is None for course in courses)


def test_backtracking_finds_valid_solution_for_sample_problem():
    variables = ["A", "B", "C", "D", "E", "F", "G"]
    domain = ["Monday", "Tuesday", "Wednesday"]
    constraints = [
        "A!=B",
        "A!=C",
        "B!=C",
        "B!=D",
        "B!=E",
        "C!=E",
        "C!=F",
        "D!=E",
        "E!=F",
        "E!=G",
        "F!=G",
    ]
    courses = initialize(variables, domain)
    first_course = courses[0]
    assigned_courses = []

    solved = backtracking(first_course, courses[1:], assigned_courses, constraints)
    assignments = {course.name: course.value for course in courses}

    assert solved is True
    assert len(assigned_courses) == len(variables)
    assert sorted(assignments) == sorted(variables)
    assert set(assignments.values()).issubset(set(domain))

    for constraint in constraints:
        left, right = constraint.split("!=")
        assert assignments[left] != assignments[right]
