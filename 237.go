//二重ループの全探索5
//https://algo-method.com/tasks/237
package main

import "fmt"

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
func isPalindromic(s string) bool {
	return s == Reverse(s)
}
func main() {
	var n int
	fmt.Scan(&n)
	ss := []string{}
	count := 0
	for _ = range make([]int, n) {
		var s string
		fmt.Scan(&s)
		ss = append(ss, s)
	}
	for _, s := range ss {
		if isPalindromic(s) {
			count++
		}
	}
	fmt.Println(count)
}
