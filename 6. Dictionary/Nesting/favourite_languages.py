favourite_languages = {
    'juli' : ['pyton', 'ruby'],
    'sarah' : ['c'],
    'elvish' : ['ruby', 'go'],
    'puttu' : ['pyton' , 'haskell'],
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")