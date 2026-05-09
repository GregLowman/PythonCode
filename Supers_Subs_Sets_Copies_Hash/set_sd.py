"""Demonstrate symmetric difference: courses offered in the morning or afternoon but not both."""
morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses = set(morning).symmetric_difference(afternoon)

print(possible_courses)
