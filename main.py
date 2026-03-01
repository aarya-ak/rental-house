def rank_houses(scored_houses):
    return sorted(scored_houses, key=lambda x: x["final_score"], reverse=True)
