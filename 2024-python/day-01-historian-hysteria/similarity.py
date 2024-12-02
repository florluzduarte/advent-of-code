from distances import get_left_and_right_list

def main():
    left, right = get_left_and_right_list("list_example.txt")
    similarities = get_partial_similarity_score(left, right)
    score = get_similarity_score(similarities)
    print(f"SIMILARITY SCORE: {score}")


def get_partial_similarity_score(left, right):
    index = 0
    pairs_similarity = []
    for item in left:
        appearances = right.count(item)
        pairs_similarity.append(int(item) * appearances)
        index += 1
    return pairs_similarity


def get_similarity_score(partial_similarities):
    score = 0
    index = 0
    for _ in partial_similarities:
        score = score + partial_similarities[index]
        index += 1
    return score


if __name__ == "__main__":
    main()