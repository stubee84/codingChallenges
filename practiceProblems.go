package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func addItUp(number int) int {
	sum := 0
	for i := 1; i <= number; i++ {
		sum += i
	}
	return sum
}

func ceasarCipher(msg string, shift int) string {
	alphabet := map[rune]int{
		'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
		'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
	}
	runeMsg := []rune(msg)
	resultStr := ""
	newIndex := 0
	for _, char := range runeMsg {
		if index, ok := alphabet[char]; ok {
			if index+shift > 26 {
				newIndex = shift - (26 - index)
			} else {
				newIndex = index + shift
			}
			for key, value := range alphabet {
				if value == newIndex {
					resultStr += string(key)
				}
			}
			continue
		}
		resultStr += string(char)
	}
	return resultStr
}

func acmTeam(topic []string) []int32 {
	maxValue := 0
	teamCount := 0
	for _, list := range topic {
		for _, item := range topic[1:] {
			value := 0
			for i := range []int32(list) {
				if (int32(list[i]) | int32(item[i])) == 49 {
					value++
				}
			}
			if maxValue < value {
				maxValue = value
				teamCount = 1
			} else if maxValue == value {
				teamCount++
			}
		}
		topic = topic[1:]
	}
	return []int32{int32(maxValue), int32(teamCount)}
}

func nonDivisibleSubset(k int32, s []int32) int32 {
	// Write your code here
	sets := []map[int32]struct{}{}

	var checkNum func(int32, map[int32]struct{}) bool = func(num int32, numbers map[int32]struct{}) bool {
		for key := range numbers {
			if (num+key)%k == 0 {
				return false
			}
		}
		return true
	}

	var max int32 = 0
	for _, num := range s {
		nonDivisible := make(map[int32]struct{})
		s = s[1:]
		nonDivisible[num] = struct{}{}

		for _, item := range s {
			if (num+item)%k != 0 {
				if checkNum(item, nonDivisible) {
					nonDivisible[item] = struct{}{}
				}
			}
		}
		s = append(s, num)

		length := int32(len(nonDivisible))
		if length > max {
			max = length
		}
		sets = append(sets, nonDivisible)
	}

	return max
}

func taumBday(b int32, w int32, bc int32, wc int32, z int32) int64 {
	// Write your code here
	var total int64 = 0
	if bc > (z + wc) {
		total = int64(b) * int64((wc + z))
		total += int64(wc) * int64(w)
	} else if wc > (z + bc) {
		total = int64(w) * int64(bc+z)
		total += int64(bc) * int64(b)
	} else {
		total = int64(b)*int64(bc) + int64(w)*int64(wc)
	}

	return total
}

// Complete the countSort function below.
func countSort(arr [][]string) {
	mid := len(arr) / 2

	output := ""
	for i := 1; i < len(arr); i++ {
		key := arr[i]
		j := i - 1

		if j <= mid {
			arr[j][1] = "-"
		}

		for j > 0 && key[0] < arr[j][0] {
			arr[j+1] = arr[j]
			j--
		}

		if i < mid {
			key[1] = "-"
		}

		// if j < 0 {
		// 	fmt.Println(j)
		// }

		if arr[j][0] == key[0] {
			arr[j] = append(arr[j], key[1])
			left := arr[:j+1]
			right := arr[j+2:]

			arr = left
			arr = append(arr, right...)
			i--
			mid--
		} else {
			arr[j+1] = key
		}
	}

	for i := range arr {
		for j := 1; j < len(arr[i]); j++ {
			output = fmt.Sprintf("%s%s ", output, arr[i][j])
		}
	}
	fmt.Println(output)
}

func readFileIntoMemory(name string) [][]string {
	results := [][]string{}

	text, _ := os.Open(name)
	defer text.Close()

	reader := bufio.NewScanner(text)

	i := 0
	for reader.Scan() {
		line := reader.Text()

		results = append(results, []string{})
		for _, split := range strings.Split(line, " ") {
			results[i] = append(results[i], split)
		}
		i++
	}
	return results
}

func main() {
	// fmt.Println(addItUp(10))
	// fmt.Println(ceasarCipher("abcd xyz", 4))
	// fmt.Println(acmTeam([]string{`10101`, "11110", "00010"}))

	// fmt.Println(nonDivisibleSubset(4, []int32{19, 10, 12, 24, 25, 22}))

	// fmt.Println(taumBday(27984, 1402, 619246, 615589, 247954))

	// countSort([][]string{{"0", "e"}, {"2", "a"}, {"1", "b"}, {"3", "a"}, {"4", "f"}, {"1", "f"}, {"2", "a"}, {"1", "e"}, {"1", "b"}, {"1", "c"}})
	// countSort([][]string{{"0", "ab"}, {"6", "cd"}, {"0", "ef"}, {"6", "gh"}, {"4", "ij"}, {"0", "ab"}, {"6", "cd"}, {"0", "ef"}, {"6", "gh"}, {"0", "ij"},
	// 	{"4", "that"}, {"3", "be"}, {"0", "to"}, {"1", "be"}, {"5", "question"}, {"1", "or"}, {"2", "not"}, {"4", "is"}, {"2", "to"}, {"4", "the"}})
	countSort(readFileIntoMemory("countingsort.txt"))
}
