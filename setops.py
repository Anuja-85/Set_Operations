def set_operations():
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Powerset")
    print("5. Cartesian Product")
    opt = int(input("Enter your choice "))
    if opt == 1:
        s1 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        s2 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        
        result = list(set(s1 + s2))
        
        print(f"Union of s1 and s2 is = {result}")
        
    if opt == 2:
        s1 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        s2 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        result = []
        for i in s2:
            if i in s1:
                result.append(i)
        
        print(f"Intersection of s1 and s2 is = {result}")
        
    if opt == 3:
        s1 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        s2 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        result = []
        for i in s2:
            if i not in s1:
                result.append(i)
        
        print(f"Difference of s1 and s2 is = {result}")
        
    if opt == 4:
        s1 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        #s2 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        
        result = [[]]

        for  i in s1:
            n = len(result)

            for j in range(n):
                r = result[j] + [i]
                result.append(r)
    
        for element in result:
            print(f"Powerset of s1 is = {element}")
    
    if opt == 5:
        s1 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        s2 =  list(map(int,input("Enter the numbers (separated by spaces): ").split()))
        result = [(a, b) for a in s2 for b in s1]
        
        print(f"Cartesian Product of s1 and s2 is = {result}")
        