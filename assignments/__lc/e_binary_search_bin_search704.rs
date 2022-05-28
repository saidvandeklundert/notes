impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let len_n: usize = nums.len();
        let mut lo: isize = 0;
        let mut hi: isize = len_n as isize - 1;
        while lo <= hi {
            let mid = lo + (hi - lo) / 2;
            if nums[mid as usize] == target {
                return mid as i32;
            }
            if nums[mid as usize] > target {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        -1
    }
}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let len_n: usize = nums.len();
        let mut low:isize=0;
        let mut high: isize = len_n as isize -1;
        let mut middle: isize = 0;
        middle = (low + high) /2 ;
        println!("low {:?} high {:?} middle {:?}", low, high, middle);
        
        while low <= high{
            middle = (low + high) /2 ;  
            if nums[middle as usize] == target{
                return middle as i32
            } else if nums[middle as usize] > target{
                high = middle -1
            } else{
                low = middle +1
            }
        }
    -1
    }
}