impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut cnt:i32 =0;
        let mut ans:i32 =0;
        for number in nums {
            println!("{:?}", number);
            if number == 1{
                cnt+=1;
                if cnt > ans {
                    ans = cnt
    
                } 
            } else{
                cnt =0
            }
        }
    ans    
    }
}