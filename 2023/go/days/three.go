package days

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"strings"

	"github.com/j14s/adventofcode/2023/go/utils"
)

func DayThree(part string) {
	lines, linesCount, err := utils.ReadLinesAndCount("inputs/3.input")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var prevLine = [141]string{}
	var curLine = [141]string{}
	var nextLine = [141]string{}

	for _, line := range lines {
		re := regexp.MustCompile(`[^a-zA-Z\.0-9]`)
		simplifiedLine := re.ReplaceAllString(line, "x")
		//fmt.Println(simplifiedLine)

		prevLine = curLine
		curLine = nextLine
		//nextLine = simplifiedLine

		if len(curLine) == 0 {
			fmt.Println("CurLine is empty")
			continue
		}

		r := bufio.NewReader(strings.NewReader(simplifiedLine))
		for {
			arrayPosition := 0
			if char, size, err := r.ReadRune(); err != nil {
				if err == io.EOF {
					break
				} else {
					log.Fatal(err)
				}
			} else {
				nextLine[arrayPosition] = string(char)
				_ = size
				//fmt.Printf("%q [%d]\n", string(char), size)
			}
		}

		fmt.Fprintf(os.Stderr, "prevLine: %v\n", prevLine)
		fmt.Fprintf(os.Stderr, "curLine: %v\n", curLine)
		fmt.Fprintf(os.Stderr, "nextLine: %v\n", nextLine)
	}

	fmt.Printf("Line Count: %d\n", linesCount)

}
