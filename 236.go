//二重ループの全探索4
//https://algo-method.com/tasks/236

package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	count := 0
	for c := 'a'; c <= 'z'; c++ {
		found := false
		for _, c2 := range s {
			if c2 == c {
				found = true
			}
		}
		if found {
			count++
		}
	}
	fmt.Println(count)
}
