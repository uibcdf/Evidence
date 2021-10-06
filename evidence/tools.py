from .evidence import Evidence
from .refs import dict_ref

def is_reference(reference):

    output = False

    if type(reference) is dict:

        if ('database' in reference) and ('id' in reference):
            output = True
        elif ('authors' in reference) and ('journal' in reference):
            output = True

    else:

        if reference.__class__.__name__ in dict_ref:
            output = True

    return output

def reference(reference):

    output = None

    if is_reference(reference):

        if type(reference) is not dict:

            output = reference.__deepcopy__()

        else:

            if 'database' in reference:
                database = reference.pop('database')
                output = dict_ref[database](**reference)

            elif ('authors' in reference) and ('jounal' in reference):
                output = dict_ref['JournalArticle'](**reference)

            else:
                raise ValueError('The input argument is not valid as reference')

    else:
        raise ValueError('The input argument is not valid as reference')

    return output

def identity(evidence_A, evidence_B):

    output = False

    if evidence_A.value==evidence_B.value:

        references_A = [ref() for ref in evidence_A.references]
        references_B = [ref() for ref in evidence_B.references]

        if len(references_A)==len(references_B):

            for reference_A in references_A:
                for ii in range(len(references_B)):
                    if reference_A==references_B[ii]:
                        _ = references_B.pop(ii)
                        break

            if len(references_B)==0:
                output = True

    return output


def is_subset(evidence_A, evidence_B):

    output = False

    if evidence_A.value==evidence_B.value:

        references_A = [ref() for ref in evidence_A.references]
        references_B = [ref() for ref in evidence_B.references]

        for reference_B in references_B:
            for ii in range(len(references_A)):
                if reference_B==references_A[ii]:
                    _ = references_A.pop(ii)
                    break

        if len(references_A)==0:
            output = True

    return output

def same_value(evidences):

    if not type(evidences) in [list, tuple]:
        evidences = [evidences]

    value = evidences[0].value

    output = True

    for aux in evidences:
        if aux.value!=value:
            output = False
            break

    return output


def join(evidences):

    if not type(evidences) in [list, tuple]:
        evidences = [evidences]

    if not same_value(evidences):
        return None

    evidence = Evidence()

    evidence.value = evidences[0].value

    for aux in evidences:
        for reference in aux.references:
            evidence.add_reference(reference())

    return evidence


