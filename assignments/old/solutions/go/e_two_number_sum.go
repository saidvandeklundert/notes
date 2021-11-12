package main

// O(n*n) time
func TwoNumberSum(array []int, target int) []int {
	for index, nr := range array {
		for index_2, nr_2 := range array {
			if index != index_2 {
				if target-(nr+nr_2) == 0 {
					return []int{nr, nr_2}
				}
			}
		}
	}
	return []int{}
}
