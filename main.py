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

def normalize_values(house_list, criteria_list, lower_is_better_criteria):
    scaled_scores = {}
    for criterion in criteria_list:
        values = [house[criterion] for house in house_list]
        min_value = min(values)
        max_value = max(values)

        for house in house_list:
            house_name = house["house_name"]
            if house_name not in scaled_scores:
                scaled_scores[house_name] = {}
            if min_value == max_value:
                normalized_value = 1.0
            else:
                if criterion in lower_is_better_criteria:
                    normalized_value = (max_value - house[criterion]) / (max_value - min_value)
                else:
                    normalized_value = (house[criterion] - min_value) / (max_value - min_value)

            scaled_scores[house_name][criterion] = round(normalized_value, 3)
    return scaled_scores
