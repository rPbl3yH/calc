def quicksort(nums):
    if len(nums) <= 1:
        return(nums)
    else:
        q = nums[len(nums)//2]
        r_nums = []
        b_nums = []
        m_nums = []
        for n in nums:
            if n > q:
                b_nums.append(n)
            elif n < q:
                m_nums.append(n)
            else:
                r_nums.append(n)
            return quicksort(m_nums) + r_nums + quicksort(b_nums)
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
quicksort(a)
print(a)
