if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
    scores_list = list(arr)  
    sorted_scores = sorted(scores_list, reverse=True)

    runner_up_score = None
    for score in sorted_scores:
        if score < max(sorted_scores):
            runner_up_score = score
            break

    if runner_up_score is not None:
        print(runner_up_score)
    else:
        print("There is no runner-up score.")
