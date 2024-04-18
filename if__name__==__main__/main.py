# if we don't use if ___name__ == "__main__" , when we import an module it will exceute the code inside it.
import if__name____main__
if__name____main__.main()

# Code outside the main() function (e.g., the if __name__ == "__main__": block) 
# won't execute when you import the script as a module.
# Code inside the main() function will execute when we call it explicitly.