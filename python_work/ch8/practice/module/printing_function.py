
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
        

