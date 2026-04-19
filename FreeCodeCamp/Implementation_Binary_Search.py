#code of implementation of binary search lab freecodecamp

def square_root_bisection(num,tolerance=0.01,iteration = 100):
    if num<0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num
    else:
        low = 0
        high = max(1,num)
        cycle = 0
        while (high-low) > tolerance and cycle < iteration:
            mid = (high+low)/2
            sqr = mid**2
            if sqr>num:
                high = mid
            else:
                low = mid
            root = mid
            cycle += 1
            print(mid)
            print(cycle)
        if cycle == iteration and (high-low)>tolerance:
            print(f"Failed to converge within {iteration} iterations")
            return None

        print(f"The square root of {num} is approximately {root}")
        return root


print(square_root_bisection(100, 1e-7, 50))