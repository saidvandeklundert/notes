
fn bin_search(nums: Vec<i32>, target: i32) -> i32 {
    let mut low:i32 = 0;
    let mut high:i32 = (nums.len()-1) as i32;
    let mut middle:i32 ;
    while low <=high{
        middle = low + (high-low)/2;
        // middle = (low+high)>>1; We can also right-shift by one
        
        if nums[middle as usize]==target{
            return middle;
        } else if nums[middle as usize] > target{
            high = middle-1;
        } else{
            low = middle +1;
        }
    }
    return -1                
}

fn main(){
    let nums = vec![-1,0,3,5,9,12];
    let x = bin_search(nums,9);
    println!("{:?}", x);
}