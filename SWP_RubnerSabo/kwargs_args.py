def beispiel_funktion(*args, **kwargs):
    print("\nArgs:")
    for arg in args:
        print(f"- {arg}")   
    
    print("\nKwargs:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")
 

def outer(var):
    def inner(andere_var):
        return var * andere_var
    return inner









def main():
    beispiel_funktion(1, 2, 3, name="Alice", alter=25, stadt="Berlin")
    beispiel_funktion(1, 3, name="Alice", alter=25)

# 1,2,3 in args als tupel
# kwargs -> dictonary
    multiply_five = outer(5)

    print(multiply_five(5))
    print(multiply_five(10))


#   multiply_five = outer(var)
#                      |
#                      -> outer(var)
#                           |                     Da muss es hin
#                           -> inner(ander_var) <-------------
#                                   return var + andere_var  |
#                                       ^                    |
#                                       |                    |
#                                      Dort abbruch also ____|                      
#


#     print(multiply_five(5))
#                      |                    Da muss es hin
#                      -> outer(var)  <-----------------------
#                           |                                |
#                           -> inner(ander_var)              |
#                                   return var + andere_var  |
#                                                   ^        |
#                                                   |        |
#                                      Dort scho voll also __|                      
#


if __name__ == "__main__":
    main()
