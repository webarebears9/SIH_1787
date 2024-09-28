def levenshtein_distance(s1, s2):
    len1, len2 = len(s1), len(s2)
    
    # Initialize matrix of zeros with (len1+1) x (len2+1)
    dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
    
    # Initialize the first row and column with the index values
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
    
    # Iterate over the matrix and fill in values
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j],  # Deletion
                               dp[i][j - 1],  # Insertion
                               dp[i - 1][j - 1]) + 1  # Substitution
    
    # The final value in the matrix is the Levenshtein distance
    return dp[len1][len2]

def damerau_levenshtein_distance(s1, s2):
    len1, len2 = len(s1), len(s2)
    
    # Initialize matrix of zeros with (len1+1) x (len2+1)
    dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
    
    # Initialize the first row and column with the index values
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
    
    # Iterate over the matrix and fill in values
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                           dp[i][j - 1] + 1,  # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
            
            # Check for transposition
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)  # Transposition

    # The final value in the matrix is the Damerau-Levenshtein distance
    return dp[len1][len2]


# Example usage:
#s1 = "DEVANG"
#s2 = "DEVGAN"
#print(f"Levenshtein Distance between '{s1}' and '{s2}' is:", levenshtein_distance(s1, s2))
#print(f"Damerau-Levenshtein Distance between '{s1}' and '{s2}' is:", damerau_levenshtein_distance(s1, s2))