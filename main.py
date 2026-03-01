def rank_houses(house_scores):
    return sorted(house_scores, key=lambda x: x["final_score"], reverse=True)

def check_weightage_sum(weighting_criteria):
    total_weight = sum(weighting_criteria.values())
    if total_weight != 10:
        raise ValueError(f"Total weight must be 10. \nCurrent sum = {total_weight}")

def handle_missing_values(house_list, criteria_list):
    for criterion in criteria_list:
        available_values = 
        [
            house[criterion]
            for house in house_list
            if house[criterion] is not None
        ]

        average_value = 
        (
            sum(available_values) / len(available_values)
            if available_values else 0
        )

        for house in house_list:
            if house[criterion] is None:
                house[criterion] = average_value

def calculate_final_scores(house_list, weighting_criteria, scaled_scores, criteria_list):
    house_scores = []
    for house in house_list:
        house_name = house["house_name"]
        total_score = 0
        
        for criterion in criteria_list:
            total_score += scaled_scores[house_name][criterion] * weighting_criteria[criterion]

        final_score = total_score
        house_scores.append({
            "house_name": house_name,
            "final_score": round(final_score, 3),
            "normalized_details": scaled_scores[house_name]
        })
    return house_scores
