# Question 9: Comments and Indentation
# Program: Simple student score grader

# --- Section 1: Data setup ---
student_name = "Amina Bello"
scores = [78, 92, 65, 49, 85]   # Scores for five subjects

# --- Section 2: Function that converts a score to a grade ---
def get_grade(score):
    # Check the score range and return the matching grade
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

# --- Section 3: Loop through scores and display results ---
print(f"Results for {student_name}")
for score in scores:
    grade = get_grade(score)    # Indented: runs on every loop pass
    print(f"  Score: {score} -> Grade: {grade}")

# --- Section 4: Calculate and show the average ---
average = sum(scores) / len(scores)
print(f"Average score: {average:.1f}")