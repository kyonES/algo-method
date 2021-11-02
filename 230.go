//文字列の全探索4
//https://algo-method.com/tasks/230
package main

import "fmt"

func main() {
	var n int
	var s, t string
	var ans int
	fmt.Scan(&n, &s, &t)
	for i := range make([]int, n) {
		if s[i] != t[i] {
			ans++
		}
	}
	fmt.Println(ans)
}
