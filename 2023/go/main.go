package main

import (
	"flag"
	"fmt"
	"regexp"
	"slices"
	"strings"

	"github.com/j14s/adventofcode/2023/go/days"
)

func main() {

	day := flag.String("day", "0.0", "command options")
	flag.Parse()

	digmatch := regexp.MustCompile("\\d+\\.\\d+")

	if *day == "0.0" {
		fmt.Printf("some help goes here(got 0.0)\n")
	} else if 3 <= len(*day) && len(*day) <= 4 && digmatch.MatchString(*day) {
		ddigits := strings.Split(*day, ".")
		ddig, dstep := ddigits[0], ddigits[1]
		fmt.Printf("Received Day: %s Part: %s\n", ddig, dstep)
		if ddig == "1" && slices.Contains([]string{"1", "2"}, dstep) {
			days.DayOne(dstep)
		} else {
			fmt.Printf("Day and Part did not match current capabilities. Exiting.\n")
		}
	} else {
		fmt.Printf("some help goes here(fell through)\n")
	}
}
