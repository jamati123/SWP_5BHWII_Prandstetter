import Pker



if __name__ == "__main__":
    for _ in range(how_many):
        deck = set_deck()
        hand = draw_hand(deck)
        combination = determine_combination(hand)
        combinations[combination] += 1

    for combination, amount in combinations.items():
        
        df = pd.DataFrame([[combinations]], columns=["Combination"]) 
        with pd.ExcelWriter("/home/florian/Documents/GithubRepos/SWP/SWP_5BHWII_Prandstetter/SWP_RubnerSabo/poker.xlsx") as writer:
            df.to_excel(writer)
        print(f"{combination}: {amount} ({amount/how_many*100:.9f}%)")
    
    
   
    print("Ziehungen: ", how_many)