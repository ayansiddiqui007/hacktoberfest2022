def merge(A,B):
    (m,n)=(len(A),len(B))
    (C,i,j)=([],0,0)
    
    while i<m and j<n:
        if A[i] <= B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    while i < m:
        C.append(A[i])
        i+=1
    while j<n:
        C.append(B[j])
        j+=1
    return C
def merge_sort(L):
    n=len(L)
    if n<=1:
        return (L)
    
    left_half=merge_sort(L[:n//2])
    right_half=merge_sort(L[n//2:])
    sorted_merged_list=merge(left_half,right_half)
    return(sorted_merged_list)    
L=[4,2,7,6,8,3,5,1]
print(merge_sort(L))
