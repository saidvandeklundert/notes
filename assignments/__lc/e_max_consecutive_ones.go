func findMaxConsecutiveOnes(nums []int) int {
    var cnt int = 0
    var ans int = 0
    for _, value := range nums {
	    fmt.Println(value)
        if value == 1 {
            cnt +=1
            if cnt > ans {
                ans = cnt

            }             
        } else {
            cnt =0

        }
    }    
    return ans   
}