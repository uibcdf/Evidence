def digest_eco(eco):

    from evidence.main import is_eco
    from evidence.eco import ECO

    if is_eco(eco):
 
        if isinstance(eco, str):
            eco = ECO(eco) 

        return eco
 
    else:

        raise ValueError('The input argument is not valid as ECO')

