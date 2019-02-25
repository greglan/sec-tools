def find_armv7a_vector_tables():
    """
    Find consecutives B/LDR PC instructions
    """
    find_armv7a_vector_tables_by_ldr()
    find_armv7a_vector_tables_by_branches()


def find_armv7a_vector_tables_by_ldr():
    """
    Find consecutives LDR PC instructions
    """
    pass


def find_armv7a_vector_tables_by_branches():
    """
    Find consecutives B instructions
    """
    pass
