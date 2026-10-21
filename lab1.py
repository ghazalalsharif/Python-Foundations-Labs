"""Worked examples for the original introductory lists and strings worksheet."""

def list_exercises():
    predictions = ["Cat", "Dog", "Cat", "Bird", "Dog"]
    confidence_scores = [0.95, 0.88, 0.91, 0.76, 0.84]
    print("First prediction:", predictions[0])
    print("Last confidence:", confidence_scores[-1])
    print("First three:", predictions[:3])
    predictions[3] = "Fish"
    predictions.append("Horse")
    print("Updated predictions:", predictions)
    print("Count:", len(predictions))
    print("Minimum confidence:", min(confidence_scores))
    print("Maximum confidence:", max(confidence_scores))
    print("Contains Cat:", "Cat" in predictions)
    return predictions, confidence_scores


def string_exercises():
    user_text = "   Artificial Intelligence is Powerful   "
    print("Original length:", len(user_text))
    cleaned = user_text.strip()
    print("Trimmed:", cleaned)
    lowered = cleaned.lower()
    print("Lowercase:", lowered)
    replaced = lowered.replace("powerful", "useful")
    print("Replaced:", replaced)
    words = replaced.split()
    print("Words:", words)
    return words


if __name__ == "__main__":
    list_exercises()
    string_exercises()
