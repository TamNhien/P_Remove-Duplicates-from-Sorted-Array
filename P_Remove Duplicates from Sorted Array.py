def remove_duplicates(nums):
    if not nums:
        return 0 # Trả về 0 nếu mảng rỗng
    
    unique_index = 0 # Khởi tạo con trỏ chỉ vị trí của phần tử duy nhất
    
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i] # Ghi đè lên vị trí i hiện tại
            
    return unique_index + 1, nums[:unique_index + 1]  # Trả về kích thước của mảng và mảng sau khi loại bỏ các phần tử dư thừa

# Test
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums1))  # Output: 2, nums1 = [1, 2]
print(remove_duplicates(nums2))  # Output: 5, nums2 = [0, 1, 2, 3, 4]
        