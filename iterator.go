/*
The Problem:

Create a iterator that takes two arrays of values and returns the next value
from each in a round robin manner.

Example Input:
[1,3,5,7,9], [2,4,6,8,10]

Example Output:
1
2
3
4
5
6
7
8
9
10
*/
package main

import (
	"fmt"
)

type MyIterator struct {
	a [][]int
	c int
}

func (m *MyIterator) Next() int {

	v := m.a[m.c][0]
	m.a[m.c] = m.a[m.c][1:]

	if m.c+1 == len(m.a) {
		m.c = 0
	} else {
		m.c++
	}

	return v
}

func (m *MyIterator) HasNext() bool {

	for i := range m.a {
		if len(m.a[i]) > 0 {
			return true
		}
	}
	return false
}

func GetIterator(a [][]int) MyIterator {
	newIterator := MyIterator{a, 0}
	return newIterator
}

func main() {

	a := [][]int{[]int{1, 3, 5, 7, 9}, []int{2, 4, 6, 8, 10}}

	i := GetIterator(a)

	for {
		if i.HasNext() == true {
			fmt.Println(i.Next())
		} else {
			break
		}
	}

}
