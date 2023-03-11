def solution(my_string):
    my_string = my_string.replace("- ", "-")
    my_string = my_string.replace("+ ", "")
    return sum(map(int, my_string.split()))