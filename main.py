def rank_houses(house_scores):
    return sorted(house_scores, key=lambda x: x["final_score"], reverse=True)

def check_weightage_sum(weighting_criteria):
    total_weight = sum(weighting_criteria.values())
    if total_weight != 50:
        raise ValueError(f"Total weight must be 50. \nCurrent sum = {total_weight}")

def handle_missing_values(house_list, criteria_list):
    for criterion in criteria_list:
        available_values = [
            house[criterion]
            for house in house_list
            if house[criterion] is not None
        ]

        average_value = (
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

        final_score = total_score / 5
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

if __name__ == "__main__":

    criteria_list = ["Rent", "Distance", "Safety", "Facilities", "space"]
    lower_is_better_criteria = ["Rent", "Distance"]
    print("\n===== RENTAL HOUSE SELECTION SYSTEM =====")
    number_of_houses = int(input("\nEnter number of houses: "))
    house_list = []

    for i in range(number_of_houses):
        print(f"\nEnter details for House {i + 1}")
        house_name = input("House name: ")

        def get_value(message):
            value = input(message)
            return None if value.lower() == "missing" else float(value)

        Rent = get_value("Monthly Rent /'missing': ")
        Distance = get_value("Distance to Workplace (km) / 'missing': ")
        Safety = get_value("Safety Rating 1-10 / 'missing': ")
        Facilities = get_value("Facilities Score 1-10 /'missing': ")
        space = get_value("Space in sq ft / 'missing': ")

        house_list.append({
            "house_name": house_name,
            "Rent": Rent,
            "Distance": Distance,
            "Safety": Safety,
            "Facilities": Facilities,
            "space": space
        })

    print("\nEnter weights (Total must equal 10)")

    weighting_criteria = {
        "Rent": float(input("Weight for Rent: ")),
        "Distance": float(input("Weight for Distance: ")),
        "Safety": float(input("Weight for Safety: ")),
        "Facilities": float(input("Weight for Facilities: ")),
        "space": float(input("Weight for Space: "))
    }

    check_weightage_sum(weighting_criteria)
    handle_missing_values(house_list, criteria_list)
    scaled_scores = normalize_values(
        house_list,
        criteria_list,
        lower_is_better_criteria
    )
    house_scores = calculate_final_scores(
        house_list,
        weighting_criteria,
        scaled_scores,
        criteria_list
    )
    ranked_houses = rank_houses(house_scores)

    print("\n===== FINAL HOUSE RANKING =====")
    for rank, house in enumerate(ranked_houses, start=1):
        print(f"{rank}. {house['house_name']} → Score: {house['final_score']} / 10")

    best_house = ranked_houses[0]
    for criterion in criteria_list:
        normalized_value = best_house["normalized_details"][criterion]
        weight = weighting_criteria[criterion]
        contribution = round((normalized_value * weight) / 5, 3)
        print(f"\nCriterion: {criterion}")
        print(f"  Weight Given: {weight}")
        print(f"  Normalized Score: {normalized_value}")
        print(f"  Contribution to Final Score (out of 10 scale): {contribution}")

print(f"\n{best_house['house_name']} is the best option because it achieved the highest total weighted score of "
      f"{best_house['final_score']} / 10 based on your importance levels.")
