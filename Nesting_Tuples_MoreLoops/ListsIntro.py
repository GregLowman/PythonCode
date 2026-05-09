"""Introduce list creation, indexing, and slice assignment to replace a range of elements."""
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
print(computer_parts)
