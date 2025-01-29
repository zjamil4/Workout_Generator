# workout_generator.py

def get_user_input():
    while True:
        gender = input("What is your gender? (Male, Female, Other): ").lower()
        if gender in ("male", "female", "other"):
            break
        else:
            print("Invalid input! Please enter one of the provided options (Male, Female, Other).")

    while True:
        equipment = input("What equipment do you have available? (weights, machines, or none): ").lower()
        if equipment in ("weights", "machines", "none"):
            break
        else:
            print("Invalid input! Please enter one of the provided options (weights, machines, or none).")

    while True:
        strength_level = input(
            "What is the strength level you would like to workout at? (beginner, intermediate, advanced): ").lower()
        if strength_level in ("beginner", "intermediate", "advanced"):
            break
        else:
            print("Invalid input! Please enter one of the provided options (beginner, intermediate, advanced).")

    return gender, equipment, strength_level

def determine_reps (strength_level):
    if strength_level == "beginner":
        return 6
    elif strength_level == "intermediate":
        return 10
    elif strength_level == "advanced":
        return 15
    else:
        return 6

def create_workout(equipment, strength_level):
    workouts = {
        "none": {
            "beginner" : ["Squats", "Wall Push-ups", "Lunges"],
            "intermediate": ["Mountain Climbers", "Burpees", "Planks"],
            "advanced": ["Reverse Crunches", "Single-Leg Squat", "Jump Squat"]
        },

        "weights" : {
            "beginner" : ["Goblet Squats", "Dumbbell Shoulder Press", "Dumbbell Romanian Deadlifts"],
            "intermediate" : ["Dumbbell Bulgarian Split Squats", "Dumbbell Bent-Over Rows", "Dumbbell Thrusters"],
            "advanced" : ["Dumbbell Snatch", "Dumbbell Man Makers", "Dumbbell Bulgarian Deadlifts"],
        },

        "machines": {
            "beginner" : ["Leg Press Machine", "Seated Chest Press Machine", "Lat Pulldown Machine"],
            "intermediate" : ["Hack Squat Machine", "Cable Row Machine", "Shoulder Press Machine"],
            "advanced" : ["Smith Machine Squats", "Cable Woodchoppers", "Leg Curl Machine"],
        }

    }

    chosen_exercises = workouts.get(equipment, {}).get(strength_level, [])

    if not chosen_exercises:
        return None

    reps = determine_reps(strength_level)

    workout_plan = "\n".join([
        f"Equipment: {equipment}",
        f"Strength Level: {strength_level}",
        "Workout Plan:\n"
    ])

    workout_plan += "\n".join([f"- {workouts}: {reps} reps" for workouts in chosen_exercises]) + "\n"
    return workout_plan


def main():
    print("Welcome to the Workout Planner!")

    while True:
        gender, equipment, strength_level = get_user_input()
        workout = create_workout(equipment, strength_level)

        if workout:
            print(workout)
            break
        else:
            print("Sorry! No suitable workout found. Please try again with different options.\n")

if __name__ == "__main__":
    main()