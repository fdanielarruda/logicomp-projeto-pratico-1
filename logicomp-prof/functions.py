"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """

from formula import *

def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1

def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).

def atoms(formula):
    """Returns the set of all atoms occurring in a formula."""
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return atoms(formula.left).union(atoms(formula.right))

def remove_atoms(atom, list_atoms):
    """ Removes an Atom from list_atoms """
    for index in list_atoms:
        if index == atom:
            list_atoms.remove(index)
            break

def number_of_atoms(formula):
    """Returns the number of atoms occurring in a formula."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_atoms(formula.left) + (number_of_atoms(formula.right))

def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return number_of_connectives(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1


def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_literal(formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_clause(formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""

    """ Preciso verificar se a negação só é aplicada apenas nas atómicas e os únicos outros operadores booleanos permitidos são a conjunção ( E ) e disjunção ( OU )."""
            
    if isinstance(formula, Atom):
        return True
    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return True
        else:
            return False
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        if isinstance(formula, Implies):
            return False
        else:
            if is_negation_normal_form(formula.left) == True and is_negation_normal_form(formula.right) == True:
                return True
            else:
                return False


def is_cnf(formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========

def separate_pathologies(archive_data, cols_data, pathologies, no_pathologies):
    count_data = 0

    for data in archive_data:
        if(count_data == 0):
            for col in data:
                if(len(cols_data) < len(data) - 1):
                    cols_data.append(col)
        else:
            if(data[len(data) - 1] == 0):
                no_pathologies.append(data)
            elif(data[len(data) - 1] == 1):
                pathologies.append(data)
        count_data += 1

def set_up_rules():
    pass

dados = []
dados.append(["PI <= 42.09", "LA <= 39.63", "GS <= 37.89", "P"])
dados.append([0,1,1,1])
dados.append([0,0,0,1])
dados.append([1,1,1,0])
dados.append([0,0,1,0])

cols_data = []
pathologies = []
no_pathologies = []
separate_pathologies(dados, cols_data, pathologies, no_pathologies)
# print(cols_data)
