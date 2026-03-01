def rank_houses(scored_houses):
    return sorted(scored_houses, key=lambda x: x["final_score"], reverse=True)

def check_weightage_sum(weighting_criteria):
    total_weight = sum(weighting_criteria.values())
    if total_weight != 10:
        raise ValueError(f"Total weight must be 10. \nCurrent sum = {total_weight}")
