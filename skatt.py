bruttol = input("Mata in bruttolön i kr: ")
arbetsgivaravgift = round(float(bruttol) * 0.3142)
print(f"Arbetsgivaravgift 31,42% - 2023: {arbetsgivaravgift} kr")
print(f"Arbetsgivarens totalakostnad: {arbetsgivaravgift + int(bruttol)} kr") 
