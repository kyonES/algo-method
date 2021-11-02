//二重ループの全探索3
//https://algo-method.com/tasks/238
package main

import "fmt"
import "strconv"

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
	var l, r int
	ans := 0
	fmt.Scan(&l, &r)
	for i := l; i <= r; i++ {
		if isPalindromic(strconv.Itoa(i)) {
			ans++
		}
	}
	fmt.Println(ans)
}
