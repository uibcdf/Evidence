def digest_reference(reference):

    from evidence.reference import is_reference

    if is_reference(reference):
 
        if isinstance(reference, dict):
 
            if 'database' in reference:

                database = reference.pop('database')
                reference = refs.dict_ref[database](**reference)
 
            elif ('authors' in reference) and ('journal' in reference):

                reference = refs.dict_ref['JournalArticle'](**reference)
 
            else:

                raise ValueError('The input argument is not valid as reference')

        return reference
 
    else:

        raise ValueError('The input argument is not valid as reference')

