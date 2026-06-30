class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        k1, k2 = (n1+n2+1)//2, (n1+n2+2)//2
        median1 = self.get_kth(nums1,n1,nums2,n2,k1)
        median2 = self.get_kth(nums1,n1,nums2,n2,k2)
        return (median1 + median2) / 2.0

    def get_kth(self,a,m,b,n,k,a_start=0,b_start=0):
        if m >  n: return self.get_kth(b,n,a,m,k,b_start,a_start)
        if m == 0: return b[b_start+k-1]
        if k == 1: return min(a[a_start], b[b_start])

        i = min(m, k//2)
        j = min(n, k//2)

        if a[a_start+i-1] > b[b_start+j-1]:
            return self.get_kth(a,m,b,n-j,k-j,a_start,b_start+j)
        else:
            return self.get_kth(a,m-i,b,n,k-i,a_start+i,b_start)