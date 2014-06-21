#the machine learning stuff here
from models import *
import numpy as np
import numpy.linalg as linalg
from models import *
# **something else needed??**

def updateRecommendations(event_id):
    all_entries = Survey.objects.filter(event_id=event_id)
    resources_used = [entry.resources_used.all() for entry in all_entries]
    ratings = [entry.rating for entry in all_entries]
    all_resources = Event.objects.get(pk=event_id).resources.all()

    #filling up known matrices
    matrix_ratings = np.array(ratings)
    matrix_features = None
    for i in range(len(all_entries)):
        new_row = [1 if resource in resources_used[i] else 0 for resource in all_resources]
        if matrix_features is not None:
            matrix_features = np.vstack((matrix_features, new_row))
        else: 
            matrix_features = new_row

    #computing unknown matrix through linear algebra
    matrix_coefficients = linalg.solve(matrix_features, matrix_ratings)

    # find the best option
    max_rating = max(ratings)
    max_indices = [i for i, j in enumerate(ratings) if j == max_rating]
    scores = []
    for i in max_indices:
        score = 0
        for j in range(len(all_resources)):
            score += matrix_features[i][j] * matrix_coefficients[j]
        scores.append(score)
    scores_indices = [(i, v) for i, v in enumerate(scores)]
    scores_indices = sorted(scores_indices, key=lambda x: (x[1] * (-1)))
    
    if len(scores_indices) > 0:
        index_1 = scores_indices[0][0]
        recommendation_1 = Recommendation(num_volunteers=0)
        recommendation_1.save()
        recommendation_1.resources = resources_used[index_1]
    if len(scores_indices) > 1:
        index_2 = scores_indices[1][0]
        recommendation_2 = Recommendation(num_volunteers=0)
        recommendation_2.save()
        recommendation_2.resources = resources_used[index_2]
    if len(scores_indices) > 2: 
        index_3 = scores_indices[2][0]
        recommendation_3 = Recommendation(num_volunteers=0)
        recommendation_3.save()
        recommendation_3.resources = resources_used[index_3]
