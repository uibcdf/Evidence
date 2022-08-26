from .evidence import Evidence

def is_reference(reference):

    from .reference import _dict_class

    output = False

    if type(reference) is dict:
        if ('database' in reference) and ('id' in reference):
            output = True
        elif ('authors' in reference) and ('journal' in reference):
            output = True
    else:
        if reference.__class__.__module__.startswith('evidence.reference.'):
            output = True

    return output

def is_eco(eco):

    output = False

    if isinstance(eco, str):

        if len(eco)==7:
            output = True

    else:

        if eco.__class__.__name__ == 'ECO':
            output = True

    return output

def is_evidence(evidence):

    output = False

    if evidence.__class__.__name__ == 'Evidence':
        output = True

    return output


def compare(evidence_A, evidence_B, rule='A_eq_B'):

    # rule in ['A_eq_B', 'A_neq_B', 'A_in_B', 'B_in_A']

    output = False

    if rule == 'A_eq_B':

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

                    ecos_A = [eco() for eco in evidence_A.ecos]
                    ecos_B = [eco() for eco in evidence_B.ecos]


                    if len(ecos_A)==len(ecos_B):

                        for eco_A in ecos_A:
                            for ii in range(len(ecos_B)):
                                if eco_A==eco_B[ii]:
                                    _ = ecos_B.pop(ii)
                                    break

                        if len(ecos_B)==0:

                            output = True

    elif rule == 'A_neq_B':

        output = True

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

                    ecos_A = [eco() for eco in evidence_A.ecos]
                    ecos_B = [eco() for eco in evidence_B.ecos]


                    if len(ecos_A)==len(ecos_B):

                        for eco_A in ecos_A:
                            for ii in range(len(ecos_B)):
                                if eco_A==eco_B[ii]:
                                    _ = ecos_B.pop(ii)
                                    break

                        if len(ecos_B)==0:

                            output = False

    elif rule == 'A_in_B':

        if evidence_A.value==evidence_B.value:

            references_A = [ref() for ref in evidence_A.references]
            references_B = [ref() for ref in evidence_B.references]

            for reference_B in references_B:
                for ii in range(len(references_A)):
                    if reference_B==references_A[ii]:
                        _ = references_A.pop(ii)
                        break

            if len(references_A)==0:

                ecos_A = [eco() for eco in evidence_A.ecos]
                ecos_B = [eco() for eco in evidence_B.ecos]

                for eco_B in ecos_B:
                    for ii in range(len(ecos_A)):
                        if eco_B==ecos_A[ii]:
                            _ = ecos_A.pop(ii)
                            break

                if len(ecos_A)==0:

                    output = True

    elif rule == 'B_in_A':

        if evidence_A.value==evidence_B.value:

            references_A = [ref() for ref in evidence_A.references]
            references_B = [ref() for ref in evidence_B.references]

            for reference_A in references_A:
                for ii in range(len(references_B)):
                    if reference_A==references_B[ii]:
                        _ = references_B.pop(ii)
                        break

            if len(references_B)==0:

                ecos_A = [eco() for eco in evidence_A.ecos]
                ecos_B = [eco() for eco in evidence_B.ecos]

                for eco_A in ecos_A:
                    for ii in range(len(ecos_B)):
                        if eco_A==ecos_B[ii]:
                            _ = ecos_B.pop(ii)
                            break

                if len(ecos_B)==0:

                    output = True

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

