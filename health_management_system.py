# health_management_system.py

class HealthManagementSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, name, age, gender, height, weight):
        """Add a new user to the health management system."""
        self.users[name] = {
            'age': age,
            'gender': gender,
            'height': height,
            'weight': weight,
            'activities': []
        }
        print(f"User {name} added successfully.")

    def add_activity(self, name, activity, duration, calories_burned):
        """Add a daily activity for a user."""
        if name in self.users:
            self.users[name]['activities'].append({
                'activity': activity,
                'duration': duration,
                'calories_burned': calories_burned
            })
            print(f"Activity '{activity}' added for {name}.")
        else:
            print(f"User {name} not found.")

    def view_health_report(self, name):
        """View the health report for a user."""
        if name in self.users:
            user = self.users[name]
            print(f"\nHealth Report for {name}:")
            print(f"Age: {user['age']}, Gender: {user['gender']}, Height: {user['height']} cm, Weight: {user['weight']} kg")
            print("\nActivities:")
            total_calories = 0
            for activity in user['activities']:
                print(f"- {activity['activity']} (Duration: {activity['duration']} min, Calories Burned: {activity['calories_burned']} kcal)")
                total_calories += activity['calories_burned']
            print(f"\nTotal Calories Burned: {total_calories} kcal")
        else:
            print(f"User {name} not found.")

    def update_user_info(self, name, height=None, weight=None, age=None):
        """Update user information like height, weight, or age."""
        if name in self.users:
            if height:
                self.users[name]['height'] = height
            if weight:
                self.users[name]['weight'] = weight
            if age:
                self.users[name]['age'] = age
            print(f"User {name}'s information updated.")
        else:
            print(f"User {name} not found.")


def main():
    health_system = HealthManagementSystem()

    while True:
        print("\nHealth Management System")
        print("1. Add User")
        print("2. Add Activity")
        print("3. View Health Report")
        print("4. Update User Info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter user's name: ").strip()
            age = int(input("Enter user's age: ").strip())
            gender = input("Enter user's gender (Male/Female): ").strip()
            height = float(input("Enter user's height (in cm): ").strip())
            weight = float(input("Enter user's weight (in kg): ").strip())
            health_system.add_user(name, age, gender, height, weight)

        elif choice == '2':
            name = input("Enter user's name: ").strip()
            activity = input("Enter activity (e.g., Running, Walking, Yoga): ").strip()
            duration = int(input("Enter duration (in minutes): ").strip())
            calories_burned = float(input("Enter calories burned: ").strip())
            health_system.add_activity(name, activity, duration, calories_burned)

        elif choice == '3':
            name = input("Enter user's name: ").strip()
            health_system.view_health_report(name)

        elif choice == '4':
            name = input("Enter user's name: ").strip()
            print("Update Info: Leave blank to skip updating.")
            height = input("Enter new height (in cm): ").strip()
            weight = input("Enter new weight (in kg): ").strip()
            age = input("Enter new age: ").strip()

            height = float(height) if height else None
            weight = float(weight) if weight else None
            age = int(age) if age else None

            health_system.update_user_info(name, height, weight, age)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
