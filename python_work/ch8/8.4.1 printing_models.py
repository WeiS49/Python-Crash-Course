
def print_models(unprinted_designs, completed_models):
    """
    simulation every printing design, until no unprinted_designs
    every design which printed will be pass to the list 'complete_models'
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model {current_design.title()}")
        completed_models.append(current_design)
        

def show_completed_models(completed_models):
    """ Print completed models."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"\t{model.title()}")
        
unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
unprinted_models2 = unprinted_models    # 使用浅拷贝传入, 指向同一地址, 两个结果都会被修改
completed_models = []

# 传入切边可以保证原列表不会被修改(传入副本)‘
# 但同时也会降低效率(大量数据时尤其如此)
print_models(unprinted_models[:], completed_models) 
show_completed_models(completed_models)
show_completed_models(unprinted_models)



