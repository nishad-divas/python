def calculate_upper_case_alphabate(sample_string):
    upper = 0
    lower = 0

    for ch in sample_string:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print("The total number Upper case alphabate =",upper)
    print("The total number of Lower case alphabate =",lower)
input_string='HeLLo EveryOne My self DIVAS NISHAD from akberpur AMbedkar'
calculate_upper_case_alphabate(input_string)