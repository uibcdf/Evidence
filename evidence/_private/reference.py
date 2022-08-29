def digest_reference(reference):

    from evidence.main import is_reference
    from evidence.reference import _dict_class, _dict_keyname

    if is_reference(reference):
 
        if isinstance(reference, dict):
 
            if 'database' in reference:
                database = reference.pop('database')
                keyname = _dict_keyname[database]
                reference = _dict_class[keyname](**reference)
 
            elif ('authors' in reference) and ('journal' in reference):

                reference = _dict_class['journal article'](**reference)
  
            elif ('web' in reference) and ('name' in reference):

                reference = _dict_class['web'](**reference)

            else:

                raise ValueError('The input argument is not valid as reference')

        return reference
 
    else:

        raise ValueError('The input argument is not valid as reference')

