def Convert_lstodic(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct