def make_move(opponent_score, my_score):
    difference = abs(opponent_score - my_score)
    threshold = 21 + (difference / 8)

    if my_score >= 71 or opponent_score >= 71:
        return 'roll'  # If either player has a score of 71 or higher, roll to win.
    elif my_score >= threshold:
        return 'hold'  # If my score is significantly higher than the threshold, hold to minimize risk.
    elif my_score <= threshold:
        return 'roll'  # If my score is significantly lower than the threshold, roll to catch up.
    else:
        return 'roll'  # Default action (for example, if my_score is exactly equal to threshold).

# Example usage:
opponent_score = 76
my_score = 31
print(make_move(opponent_score, my_score))

