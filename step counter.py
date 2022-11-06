def feet_to_steps(num_ft_walked):
    
    steps_walked = int(num_ft_walked / 2.5)
    
    return steps_walked

if __name__ == '__main__':
    
    num_ft_walked = float(input())
    
    print(feet_to_steps(num_ft_walked))
    
    