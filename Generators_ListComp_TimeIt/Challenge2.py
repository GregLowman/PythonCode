"""Converts inch measurements to centimetres using a list comprehension inside tuple()."""
inch_measurement = (3, 8, 20)

cm_measurement = tuple([number * 2.54 for number in inch_measurement])
print(cm_measurement)
print(type(cm_measurement))