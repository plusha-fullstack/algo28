def SynchronizingTables(N, ids, salary):
    ids_sorted = ids.copy()
    salary_sorted = salary.copy()
    ids_sorted = sorted(ids_sorted)
    salary_sorted = sorted(salary_sorted)
    for i in range(N):
        for j in range(N):
            if ids[i]==ids_sorted[j]:
                salary[i] = salary_sorted[j]
    
    return salary
