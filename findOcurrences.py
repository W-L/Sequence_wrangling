
# weird sorting strategy to find the positions of all occurrences of 
# some set of elements. This is quite fast, except that it needs to
# sort the array each time it finds the indices - so O(n)

    sortIndex = np.squeeze(np.argsort(targetCoverage.view('i8,i8,i8,i8,i8'),
     order=['f0', 'f1', 'f2', 'f3', 'f4'], axis=0))
    targetCov_sorted = targetCoverage[sortIndex]

    unPatterns, unfirst, unindex, uncount = np.unique(targetCov_sorted, return_index=True, return_counts=True, return_inverse=True, axis=0)
    
    # targetPatterns = [i.tostring() for i in unPatterns]
    # nPatterns = len(targetPatterns)    
    # # sets of indices
    res = np.split(sortIndex, unfirst[1:])
    # # filter to size, keep only items occurring more than once
    # # rPatterns = unPatterns[uncount >= 1]
    res = list(filter(lambda x: x.size >= 1, res))