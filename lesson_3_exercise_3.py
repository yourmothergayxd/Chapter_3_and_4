try:
        user_score = float(input("Enter score: "))
                        
        if user_score > 1.0:
                print("Bad score.")
                                
        elif user_score >= 0.9:
                print ("A")
                                
        elif user_score >= 0.8:
                print ("B")
                                
        elif user_score >= 0.7:
                print ("C")
                                
        elif user_score >= 0.6:
                print ("D")

        elif user_score < 0.6 and user_score >= 0.0:
                print("F")

except ValueError:
        print("Please enter a number.")

                        
                
