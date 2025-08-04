def better_than_average(class_points, your_points):
    average_score = sum(class_points + [your_points]) / len(class_points + [your_points])
    if average_score < your_points:
        return True
    else:
        return False
