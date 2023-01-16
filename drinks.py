### DRINK MANAGER BY Tadeo98

def main(): #runs as first function from which other functions are triggered
    width = 120  # should be divisible by the number of methods
    methods = ['Search drink','Search ingredient','Edit drink list','Edit list of ingredients']
    print('\n\n\n{0}\n'.format((width-1)*'*'),end='')
    print('{0:^{1}}\n'.format('WELCOME TO DRINK MANAGER!', width))
    remain = 'y'
    while remain == 'y':
        print('{0:^{1}}\n'.format('Choose method (or type \'help\' for further actions).', width-1))
        print_titles(width, methods, '|')
        print_titles(width, range(1,len(methods)+1), '|')

        method = in_method_control(list(range(1,len(methods)+1)),'\nEnter app number\n',width)

        if method == 1:
            search_drink(width)
        elif method == 2:
            search_ingredient(width)
        elif method == 3:
            edit_drink_list(width)
        elif method == 4:
            edit_ingredients(width)
        else:
            continue

        remain = input('\n{0:^{1}}\n'.format('To remain in the program, enter [Y].', width)).lower()

def search_drink(width):    #function for searching drinks
    methods = ['Search by name','Search by ingredients(s)','Search by available ing.','Find source']
    remain = 'y'
    while remain == 'y':
        print('\n\n{0}\n'.format((width-1) * '-'), end='')
        print('{0:^{1}}\n'.format('SEARCH DRINK APPLICATION', width-1))
        print_titles(width, methods, '|')
        print_titles(width, range(1,len(methods)+1), '|')
        print('\n',end='')
        method = in_method_control(list(range(1,len(methods)+1)),'\nEnter app number\n',width)
        if method == 1:
            search_drink_by_name(width)
        elif method == 2:
            search_drink_by_ing(width)
        elif method == 3:
            search_drink_by_av_ing(width)
        elif method == 4:
            find_source(width)
        else:
            continue

        remain = input('\n{0:^{1}}\n'.format('To remain in the application, enter [Y].', width)).lower()

def search_ingredient(width):   #function for searching ingredients
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('SEARCH INGREDIENT APPLICATION', width - 1))
    while True:
        print('Enter ingredient to search or type \'help\' for further actions:\n')
        search = in_method_control('noint','Enter ingredient name (lowercase, capitals, doesn\'t matter)\n. Don\'t use '
                            'symbols \';\' or \',\'.\nEnter any character to quit this application\n',width)
        if search == None:
            continue

        if len(search) < 2:
            break

        forb = ';,'
        if len(set(search) & set(forb)) > 0:
            print('\nForbidden symbols were used.\n\n', end='')
            continue

        search = search.lower()
        ingredients = read_ingredient_file()
        met_ings = {}
        for name in ingredients.keys():
            if search in name.lower():
                met_ings.update({name: ingredients.get(name)})
        if met_ings == {}:
            print('No results.\n')
            continue
        ingredient_table(width,met_ings)

def edit_drink_list(width): #function for editing the text file containing list of drinks
    methods = ['Add drink','Edit drink','Delete drink']
    remain = 'y'
    while remain == 'y':
        print('\n\n{0}\n'.format((width-1) * '-'), end='')
        print('{0:^{1}}\n'.format('EDIT DRINK LIST APPLICATION', width-1))
        print_titles(width, methods, '|')
        print_titles(width, range(1,len(methods)+1), '|')
        print('\n',end='')
        method = in_method_control(list(range(1,len(methods)+1)),'\nEnter app number\n',width)
        if method == 1:
            add_drink(width)
        elif method == 2:
            edit_drink(width)
        elif method == 3:
            delete_drink(width)
        else:
            continue

        remain = input('\n{0:^{1}}\n'.format('To remain in the application, enter [Y].', width)).lower()

def edit_ingredients(width):    #function for editing the text file containing list of ingredients
    methods = ['Add ingredient','Edit ingredient','Delete ingredient']
    remain = 'y'
    while remain == 'y':
        print('\n\n{0}\n'.format((width-1) * '-'), end='')
        print('{0:^{1}}\n'.format('EDIT INGREDIENT LIST APPLICATION', width-1))
        print_titles(width, methods, '|')
        print_titles(width, range(1,len(methods)+1), '|')
        print('\n',end='')
        method = in_method_control(list(range(1,len(methods)+1)),'\nEnter app number\n',width)
        if method == 1:
            add_ingredient(width)
        elif method == 2:
            edit_ingredient(width)
        elif method == 3:
            delete_ingredient(width)
        else:
            continue

        remain = input('\n{0:^{1}}\n'.format('To remain in the application, enter [Y].', width)).lower()

def search_drink_by_name(width):    #searches drinks by name
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('SEARCH DRINK BY NAME APPLICATION', width - 1))
    while True:
        print('Enter drink to search or type \'help\' for further actions:\n')
        search = in_method_control('noint','Enter drink name (lowercase, capitals, doesn\'t matter)\n. Don\'t use '
                            'symbols \';\' or \',\'.\nEnter any character to quit this application\n',width)
        if search == None:
            continue

        if len(search) < 2:
            break

        forb = ';,'
        if len(set(search) & set(forb)) > 0:
            print('\nForbidden symbols were used.\n\n', end='')
            continue

        search = search.lower()
        drinks = read_drink_file()
        met_drinks = {}
        for name in drinks.keys():
            if search in name.lower():
                met_drinks.update({name: drinks.get(name)})
        if met_drinks == {}:
            print('\nNo results.\n')
            continue
        drink_table(width,met_drinks)

def search_drink_by_ing(width):  #searches all drinks containing at least entered ingredient(s)
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('SEARCH DRINKS CONTAINING ENTERED INGREDIENTS APPLICATION', width - 1))
    while True:
        print('Enter ingredients or type \'help\' for further actions:\n')
        search = in_method_control('noint','Format of entries:\ningredient 1,...,ingredient n\n'
                            'Don\'t use symbol \';\'.\nEnter any character to quit this application\n',width)
        if search == None:
            continue

        if len(search) < 2:
            break

        forb = ';'
        if len(set(search) & set(forb)) > 0:
            print('\nForbidden symbols were used.\n\n', end='')
            continue

        search = set(ing.lower() for ing in search.split(','))
        met_drinks = met_drinks_by_ings(search, 0, 0)
        if met_drinks == {}:
            print('\nNo results.\n')
            continue
        drink_table(width,met_drinks)

def search_drink_by_av_ing(width):  #searches all possible drinks by available ingredients
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('SEARCH DRINK BY AVAILABLE INGREDIENTS APPLICATION', width - 1))
    while True:
        print('Enter available ingredients or type \'help\' for further actions:\n')
        search = in_method_control('noint','Format of entries:\ningredient 1,...,ingredient n\nFormat for entries'
                            ' with number of allowed missing ingredients:\ningredient 1,...,ingredient n[space]number\n'
                            'Don\'t use symbol \';\'.\nEnter any character to quit this application\n',width)
        if search == None:
            continue

        if len(search) < 2:
            break

        forb = ';'
        if len(set(search) & set(forb)) > 0:
            print('\nForbidden symbols were used.\n\n', end='')
            continue

        if ' ' in search:
            [search, missing] = search.split(' ')
        else:
            missing = '0'
        missing = int(missing)
        search = set(ing.lower() for ing in search.split(','))
        met_drinks = met_drinks_by_ings(search, 1, missing)
        if met_drinks == {}:
            print('\nNo results.\n')
            continue
        drink_table(width,met_drinks)

def find_source(width): #prints sources for each variation of entered drink
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('FIND SOURCE FOR DRINK RECIPE APPLICATION', width - 1))
    while True:
        print('Enter drink name or type \'help\' for further actions:\n')
        search = in_method_control('noint','Don\'t use symbol \';\' or \',\'.\n'
                    'Enter any character to quit this application\n',width)
        if search == None:
            continue

        if len(search) < 2:
            break

        forb = ',;'
        if len(set(search) & set(forb)) > 0:
            print('\nForbidden symbols were used.\n\n', end='')
            continue

        search = search.title()
        drinks = read_drink_file()
        try:
            print('\nSources for {0} variations:\n'.format(search), end='')
            for var in drinks[search]:
                print('\n{0}\n{1}\n'.format(var[0],var[2]),end='')
        except KeyError:
            print('\nNo such drink in drink list. Use search app to find out precise name of drink.\n\n',end='')
            continue
        print('\n', end='')

def add_drink(width):   #subfunction for adding new drinks
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('ADD DRINK TO LIST APPLICATION', width - 1))
    while True:
        print('Add new drink or type \'help\' for further actions:\n')
        new_drink = in_method_control('noint','Format for new drink (one variation) input:\nDrink,'
                    'Variation,ingredient 1,...,ingredient n,'
                  'source\nFormat for new drink (more variations) input:\nDrink,Variation 1,ingredient 1,...,'
                  'ingredient n,source;...;Variation n,ingredient 1,...,ingredient n,source\n'
                                              'Enter any character to quit this application\n',width)
        if new_drink == None:
            continue

        if len(new_drink) < 2:
            break

        if new_drink.count(',') < 3 or len(new_drink) < 7:
            print('\nIncorrect format.\n\n',end='')
            continue

        new_drink = read_drink_row(new_drink)
        drinks = read_drink_file()

        if new_drink[0] in drinks.keys():
            var_entered = set([var[0].lower() for var in new_drink[1:]])
            var_list = set([var[0].lower() for var in drinks.get(new_drink[0])])
            if len(var_entered & var_list) > 0:
                print('\nVariation(s): {0} for {1} already exist(s). No change.\n\n'.format(', '.join
                        (var_entered & var_list),new_drink[0]), end='')
                continue
            else:
                file_lines = read_file_lines('drink_list.txt')
                i = 0
                for line in file_lines:
                    line = line.strip('\n')
                    if new_drink[0] == line.split(',',1)[0]:
                        break
                    i += 1
                new_line = create_drink_line(file_lines[i],new_drink)
                if new_line == None:
                    continue
                if file_lines[i] != file_lines[-1]:
                    file_lines[i] = new_line + '\n'
                else:
                    file_lines[i] = new_line
                edit_file_line(new_drink[0],file_lines,'drink_list.txt','edited')
                continue
        new_line = create_drink_line('',new_drink)
        if new_line == None:
            continue
        add_line_to_file(new_line,'drink_list.txt','drinks')

def edit_drink(width):  #subfunction for editing drinks
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('EDIT DRINK APPLICATION', width - 1))
    while True:
        print('Enter edited drink or type \'help\' for further actions:\n')
        edit_drink = in_method_control('noint','Enter drink name to search and show its line or enter whole drink '
                'line.\nFormat for drink (one variation) input:\nDrink,Variation,ingredient 1,...,ingredient n,'
                'source\nFormat for drink (more variations) input:\nDrink,Variation 1,ingredient 1,...,'
                'ingredient n,source;...;Variation n,ingredient 1,...,ingredient n,source\n'
                'Enter any character to quit this application\n',width)
        if edit_drink == None:
            continue

        if len(edit_drink) < 2:
            break

        if edit_drink.count(',') == 0:
            edit_drink = edit_drink.title()
            print('\nLine for {0}:\n'.format(edit_drink),end='')
            file_lines = read_file_lines('drink_list.txt')
            for line in file_lines:
                if edit_drink == line[:line.index(',')]:
                    drinks = read_drink_file()
                    line_print = '{0},'.format(edit_drink)
                    for var in drinks[edit_drink]:
                        line_print += '{0},{1},{2};'.format(var[0],','.join(var[1]),var[2])
                    print('{0}\n\n'.format(line_print[:-1]),end='')
                    break
                if line == file_lines[-1]:
                    print('No such drink in drink list. Use search app to find out precise name of drink.\n')
            continue

        if edit_drink.count(',') < 3 or len(edit_drink) < 7:
            print('\nIncorrect format.\n\n',end='')
            continue

        edit_drink = read_drink_row(edit_drink)
        file_lines = read_file_lines('drink_list.txt')
        i = 0
        for line in file_lines:
            if edit_drink[0] == line[:line.index(',')]:
                break
            i += 1
        if file_lines[i] != file_lines[-1]:
            file_lines[i] = create_drink_line('', edit_drink) + '\n'
        else:
            file_lines[i] = create_drink_line('', edit_drink)
        edit_file_line(edit_drink[0],file_lines,'drink_list.txt','edited')

def delete_drink(width):    #subfunction for removing drinks
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('DELETE DRINK APPLICATION', width - 1))
    while True:
        print('Enter drink to delete or type \'help\' for further actions:\n')
        delete_drink = in_method_control('noint','Enter drink name to delete\n'
                'Enter any character to quit this application\n',width)
        if delete_drink == None:
            continue

        if len(delete_drink) < 2:
            break

        file_lines = read_file_lines('drink_list.txt')
        delete_drink = delete_drink.title()
        i = 0
        for line in file_lines:
            if delete_drink == line[:line.index(',')]:
                break
            i += 1
        if i == len(file_lines):
            print('\nNo such drink in drink list. Use search app to find out precise name of drink.\n\n',end='')
            continue
        if file_lines[i] == file_lines[-1]:
            file_lines[i-1] = file_lines[i-1].strip('\n')
        file_lines.pop(i)
        edit_file_line(delete_drink,file_lines,'drink_list.txt','deleted')

def add_ingredient(width):  #subfunction for adding new ingredients to list of ingredients
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('ADD INGREDIENT TO LIST APPLICATION', width - 1))
    while True:
        print('Add new ingredient or type \'help\' for further actions:\n')
        new_ing = in_method_control('noint','Enter ingredient.\nFor multiple word ingredient use \'_\' instead of '
                    'space. No semicolons. No commas.\nEnter any character to quit this application\n',width)
        if new_ing == None:
            continue

        if len(new_ing) < 2:
            break

        forb = ' ;,'
        if len(set(new_ing) & set(forb)) > 0:
            print('Forbidden symbols were used.\n',end='')
            continue

        new_ing = new_ing.lower()
        ing_list = read_ingredient_file()
        if new_ing in ing_list.keys():
            print('\nIngredient {0} already exists.\n\n'.format(new_ing),end='')
            continue
        similar_ings = set()
        for ing_part in new_ing.split('_'):
            for ing in ing_list.keys():
                if ing_part in ing:
                    similar_ings.add(ing)
        if len(similar_ings) > 0:
            print('\nSimilar ingredients already exist:\n{0}\n\nEnter \'N\' to cancel adding this '
                  'ingredient'.format(', '.join(similar_ings)),end='')
            if input().lower() == 'n':
                continue
        new_line = new_ing + ',' + str(max(ing_list.values())+1)
        add_line_to_file(new_line,'ingredients.txt','igredients')

def edit_ingredient(width): #subfunction for editing ingredients in list of ingredients
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('EDIT INGREDIENT APPLICATION', width - 1))
    while True:
        print('Enter old ingredient, then new one or type \'help\' for further actions:\n')
        edit_ing1 = in_method_control('noint','Enter ingredient to be replaced, then its replacement.\nFor multiple '
                    'word ingredient use \'_\' instead of '
                    'space. No semicolons. No commas.\nEnter any character to quit this application\n',width)
        if edit_ing1 == None:
            continue

        if len(edit_ing1) < 2:
            break

        forb = ' ;,'
        if len(set(edit_ing1) & set(forb)) > 0:
            print('Forbidden symbols were used.\n',end='')
            continue

        edit_ing1 = edit_ing1.lower()
        ing_list = read_ingredient_file()
        file_lines = read_file_lines('ingredients.txt')
        i = 0
        for line in file_lines:
            if edit_ing1 == line[:line.index(',')]:
                break
            i += 1
        if edit_ing1 not in ing_list.keys():
            print('\nIngredient {0} doesn\'t exist.\n\n'.format(edit_ing1),end='')
            continue
        edit_ing2 = input('...will be replaced with:\n').lower()
        if len(set(edit_ing2) & set(forb)) > 0:
            print('Forbidden symbols were used.\n',end='')
            continue
        if file_lines[i] != file_lines[-1]:
            file_lines[i] = edit_ing2 + ',' + str(ing_list[edit_ing1]) + '\n'
        else:
            file_lines[i] = edit_ing2 + ',' + str(ing_list[edit_ing1])
        edit_file_line(edit_ing1+' to '+edit_ing2, file_lines, 'ingredients.txt','edited')

def delete_ingredient(width):   #subfunction for removing ingredients in list of ingredients
    print('\n\n{0}\n'.format((width - 1) * '.'), end='')
    print('{0:^{1}}\n'.format('DELETE INGREDIENT APPLICATION', width - 1))
    while True:
        print('Enter ingredient to delete or type \'help\' for further actions:\n')
        delete_ing = in_method_control('noint','Enter ingredient name to delete\n'
                'Enter any character to quit this application\n',width)
        if delete_ing == None:
            continue

        if len(delete_ing) < 2:
            break

        file_lines = read_file_lines('ingredients.txt')
        i = 0
        for line in file_lines:
            if delete_ing == line[:line.index(',')]:
                break
            i += 1
        if i == len(file_lines):
            print('\nNo such ingredient in drink list. Use search app to find out precise name of drink.\n')
            continue
        drinks = read_drink_file()
        met_drinks = set()
        print('\n{0} is present in following drinks:\n'.format(delete_ing), end='')
        for name, value in drinks.items():
            for var in value:
                if delete_ing in var[1]:
                    met_drinks.add(name)
                    continue
        for drink in met_drinks:
            print('{0}\n'.format(drink),end='')
        if len(met_drinks) != 0:
            print('\nCan\'t delete {0} until it\'s not present in any drink.\n\n'.format(delete_ing), end='')
            continue
        else:
            print('None\n', end='')
        if file_lines[i] == file_lines[-1]:
            file_lines[i-1] = file_lines[i-1].strip('\n')
        file_lines.pop(i)
        edit_file_line(delete_ing,file_lines,'ingredients.txt','deleted')

def drink_table(width,drinks):    #prints list of drinks
    if drinks == {}:
        drinks = read_drink_file()
    title_len = max([len(name) for name in drinks.keys()])
    var_len = max([len(var[0]) for drink in drinks.values() for var in drink])
    #ing_len = max([len(', '.join(ing[1][0])) for ing in drinks.values()])
    title = ['DRINK','VARIATION','INGREDIENTS']
    mcs = 5 #minimal space between columns
    print('\n\n{1:*<{0}}\n'.format(width-1,''),end='')
    print("{1:^{0}}\n\n".format(width - 1, 'DRINK LIST'), end='')
    print("{3:<{0}}{4:<{1}}{5:<{2}}\n\n".format(title_len+mcs,var_len+mcs, width-1-title_len-var_len,
                                            title[0],title[1],title[2]),end='')
    for drink, rest in sorted(drinks.items()):
        print("{1:<{0}}".format(title_len+mcs, drink), end='')
        for var in rest:
            ing_lines = []
            ing_line = ''
            ing_list = list(var[1])
            for ing in ing_list:
                if len(ing_line + ', ' + ing) > width - 2 - title_len - var_len - 2 * mcs:
                    ing_lines.append(ing_line[:-1])
                    ing_line = ''
                if ing == ing_list[-1]:
                    ing_line += ing
                    ing_lines.append(ing_line)
                    break
                ing_line += ing + ', '
            print("{1:<{0}}".format(var_len + mcs, var[0]), end='')
            for line in ing_lines:
                print("{0:<}\n".format(line), end='')
                if line != ing_lines[-1]:
                    print("{1:<{0}}".format(var_len + 2 * mcs + title_len, ''), end='')
            if var != rest[-1]:
                print("\n{1:<{0}}".format(title_len+mcs,''), end='')
            else:
                print('\n',end='')
        print('\n', end='')
    print('{1:*<{0}}\n'.format(width-1,''),end='')

def ingredient_table(width,ings):   #prints list of ingredients
    if ings == {}:
        ings = read_ingredient_file()
    ing_len = max([len(name) for name in ings.keys()])
    #num_len = max([len(str(num)) for num in ings.values()])
    mcs = 2 #minimal space between columns
    print('\n\n{1:*<{0}}\n'.format(width-1,''),end='')
    print("{1:^{0}}\n\n".format(width - 1, 'LIST OF INGREDIENTS'), end='')
    cols = (width-1)//(ing_len+mcs)
    i = 1
    for ing in sorted(ings.keys()):
        print("{1:<{0}}".format(ing_len+mcs,ing),end='')
        if i % cols == 0:
            print("{1:<{0}}\n\n".format(width-1-cols*ing_len,''),end='')
        i += 1
    print('\n\n{1:*<{0}}\n'.format(width-1,''),end='')

def met_drinks_by_ings(search, index, missing): #finds drinks by entry ingredients and returns dict of those drinks
    drinks = read_drink_file()
    met_drinks = {}
    for name, vars in drinks.items():
        value = []
        for var in vars:
            ing_list = [search,var[1]]
            if len(ing_list[0] & ing_list[1]) >= len(ing_list[index]) - missing:
                value.append(var)
        if value != []:
            met_drinks.update({name: value})
    return met_drinks

def read_drink_file():  #reads drink file and returns dictionary of drinks
    drink_list = read_file_lines('drink_list.txt')
    drinks = {}
    for drink in drink_list:
        drink = drink.replace('\n', '')
        variations1 = read_drink_row(drink)
        drinks.update({variations1[0]: [[var[0], set(convert_ing([int(j) for j in var[1:-1]])),
                                         var[-1]] for var in variations1[1:]]})
    return drinks

def read_drink_row(drink):  #reads one row of entered or file related drink and returns list format for one drink
    drink = drink.split(';')
    variations = []
    for var in drink:
        if var == drink[0]:
            var = var.split(',')
            variations.append(var[0])
            variations.append(var[1:])
            continue
        variations.append(var.split(','))
    return variations

def print_titles(width, titles, symbol):    #prints rows with methods and corresponding numbers (entries)
    for title in titles:
        print('{1:^{0}}'.format(width // len(titles) - 1, title),end='')
        if title != titles[-1]:
            print(symbol,end='')
    print('\n',end='')

def create_drink_line(old_drink,drink): #creates lines to be inserted into file from list of elements defining drink
    if old_drink == '':
        drink_line = drink[0] + ','
    else:
        drink_line = old_drink.strip('\n') + ';'
    i = 1
    for ings in [ing[1:-1] for ing in drink[1:]]:
        conv_ings = convert_ing(ings)
        if conv_ings == None:
            break
        drink_line += drink[i][0] + ',' + ','.join(str(num) for num in conv_ings) + ',' + drink[i][-1]
        if i < len(drink[1:]):
            drink_line += ';'
        else:
            return drink_line
        i += 1

def in_method_control(list_of_int,clause,width): #checks if entry is integer from interval of possible entries or help, drinkl, ingl
    while True:
        try:
            value = input()
            if value in ('help','ingl','drinkl'):
                if value == 'help':
                    print('{0}'.format(clause), end='')
                    print_help()
                elif value == 'drinkl':
                    drink_table(width, {})
                elif value == 'ingl':
                    ingredient_table(width,{})
                return None
            if list_of_int == 'noint':
                break
            value = int(value)
            if value in list_of_int:
                break
            else:
                print('Enter {0} or {1}.'.format(', '.join(str(i) for i in list_of_int[:-1]),list_of_int[-1]))
        except ValueError:
            print('Enter integers only.')
            return None
    return value

def convert_ing(conv_list):  #converts between numbers and ingredients according to ing list
    ingredients = read_ingredient_file()
    ing_list = []
    if type(conv_list[0]) == type(1):
        for num in conv_list:
            ing_list.append(list(ingredients.keys())[list(ingredients.values()).index(num)])
    elif type(conv_list[0]) == type('1'):
        missing = [miss for miss in conv_list if ingredients.get(miss) == None]
        if len(missing) > 0:
            print('List of ingredients does not contain {0}.\nEither adjust the format of ingredient(s) or '
                  'add ingredient(s) to the list of ingredients.\n'.format(', '.join(missing)), end='')
            return
        for ing in conv_list:
            ing_list.append(ingredients.get(ing))
    return ing_list

def read_ingredient_file():  #returns dictionary of igredients
    ing_list = read_file_lines('ingredients.txt')
    ingredients = {}
    for ing in ing_list:
        ing = ing.replace('\n', '')
        ing = ing.split(',')
        ingredients.update({ing[0]:int(ing[1])})
    return ingredients

def add_line_to_file(line,path,item):   #adds new line to any file
    with open(path,'a') as f:
        f.write('\n{0}'.format(line))
    f.close()
    print('\n{0} was added to list of {1}.\n\n'.format(line.split(',')[0],item),end='')

def edit_file_line(drink_ing,lines,path,action):   #edits any line in file
    with open(path,'w') as f:
        f.writelines(lines)
    f.close()
    print('\n{0} was {1}.\n\n'.format(drink_ing,action),end='')

def read_file_lines(path):  #reads file and returns list of lines
    with open(path,'r',encoding='utf8') as f:
        lines = f.readlines()
    return lines

def print_help():   #prints help clause common for all methods
    print('To see list of all drinks, type \'drinkl\'\nTo see list of all ingredients that can be used, type \'ingl\''
          '\n\n', end='')

main()