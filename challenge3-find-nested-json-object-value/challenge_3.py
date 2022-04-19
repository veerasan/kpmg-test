

def get_value(dc_ob,l_key):
    return dc_ob[l_key]

def find_key_value(dict_ob,list_keys):
    temp_dc = dict_ob
    li_keys = list_keys

    try:
        for l_key in li_keys.split("/"):
            if isinstance(temp_dc,dict):
                temp_dc = get_value(temp_dc,l_key)
        if isinstance(temp_dc,str):
             output_val = temp_dc
        else:
            output_val = None
    except KeyError:
        output_val = 'Key Not Found'

    return output_val




