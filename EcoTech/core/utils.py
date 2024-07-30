import os

visit_file_path = os.path.join(os.path.dirname(__file__), 'visit_count.txt')

def increment_visits():
    if os.path.exists(visit_file_path):
        with open(visit_file_path, 'r') as file:
            total_visits = int(file.read())
    else:
        total_visits = 0

    total_visits += 1

    with open(visit_file_path, 'w') as file:
        file.write(str(total_visits))

    return total_visits