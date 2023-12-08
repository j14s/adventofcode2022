package days

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"

	"github.com/j14s/adventofcode/2023/go/utils"
)

func DayOne(part string) {

	lines, err := utils.ReadLines("inputs/1.input")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	wnums := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	var inputTot int

	for _, line := range lines {
		fmt.Println(line)
		var firstNum int = 0
		var lastNum int = 0
		for _, singleChar := range strings.Split(line, "") {
			if c, err := strconv.Atoi(singleChar); err == nil {
				if firstNum == 0 {
					firstNum = c
					lastNum = c
				} else {
					lastNum = c
				}
			}
		}

		if part == "2" {
			regexdigit := regexp.MustCompile("[0-9]")
			numslice := []string(regexdigit.Split(line, -1))
			fwni := len(numslice[0])
			lwni := -1

			for wnum, dnum := range wnums {

				pattern := regexp.MustCompile(wnum)

				prefoundindex := pattern.FindStringIndex(numslice[0])
				if len(prefoundindex) > 0 {
					if prefoundindex[0] < fwni {
						fwni = prefoundindex[0]
						firstNum = dnum
					}
				}
				postfoundindex := pattern.FindStringIndex(numslice[len(numslice)-1])
				if len(postfoundindex) > 0 {
					if postfoundindex[0] > lwni {
						lwni = postfoundindex[0]
						lastNum = dnum
					}
				}
			}
		}

		fmt.Printf("first: %d\n", firstNum)
		fmt.Printf("last: %d\n", lastNum)
		lineTot := firstNum*10 + lastNum
		fmt.Printf("Line Total: %d\n", lineTot)
		inputTot = inputTot + lineTot
		fmt.Printf("Cur Input Total: %d\n", inputTot)
	}

	fmt.Printf("Input Total: %d\n", inputTot)
}
